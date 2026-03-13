class AddressMapper:
    def __init__(self, mapping_config):
        self.mapping = mapping_config

    def _extract_bits(self, addr, msb, lsb):
        """
        Extracts bits from address within range [msb, lsb] (inclusive).
        從位址中擷取 [msb, lsb] (包含) 範圍內的位元。
        """
        mask = (1 << (msb - lsb + 1)) - 1
        return (addr >> lsb) & mask

    def map_address(self, phys_addr):
        """
        Maps a physical address to (channel, rank, bank, row, column).
        將實體位址映射為 (channel, rank, bank, row, column)。

        Returns a dictionary.
        回傳一個字典。
        """
        result = {}
        # Required keys: Channel, Rank, Bank, Row, Column
        # 必要鍵值：Channel, Rank, Bank, Row, Column
        for key in ["Channel", "Rank", "Bank", "Row", "Column"]:
            ranges = self.mapping.get(key, [])
            value = 0

            # Example: [[16, 14], [5, 4]]
            # Range 0 (MSB part): [16, 14] -> 3 bits
            # Range 1 (LSB part): [5, 4] -> 2 bits
            # Result = (Range0_Value << 2) | Range1_Value
            # 範例：[[16, 14], [5, 4]]
            # 區段 0 (高位部分): [16, 14] -> 3 bits
            # 區段 1 (低位部分): [5, 4] -> 2 bits
            # 結果 = (區段0_數值 << 2) | 區段1_數值

            current_shift = 0
            temp_value = 0

            # Iterate in reverse order (LSB first) to construct the value
            # 以反向順序 (從低位區段開始) 迭代以建構數值
            for r in reversed(ranges):
                msb, lsb = r
                width = msb - lsb + 1
                part = self._extract_bits(phys_addr, msb, lsb)
                temp_value |= (part << current_shift)
                current_shift += width

            result[key] = temp_value

        return result

    def get_next_boundary(self, phys_addr):
        """
        Calculates the next physical address boundary that causes a change in
        Channel, Rank, Bank, or Row. This is essential for splitting large AXI
        bursts into smaller hardware-aligned transactions.
        計算下一個會導致 Channel, Rank, Bank 或 Row 改變的實體位址邊界。
        這對於將大型 AXI burst 切割成硬體對齊的較小傳輸非常重要。
        """
        # We only care about bits that determine Channel, Rank, Bank, and Row.
        # Column bits represent addresses within the same page/bank, so they don't break hardware parallelism boundaries.
        # 我們只關心決定 Channel, Rank, Bank 和 Row 的位元。
        # Column 位元代表同一 page/bank 內的位址，因此不會跨越硬體平行處理的邊界。

        lowest_critical_lsb = 64 # Start with an arbitrarily high bit

        for key in ["Channel", "Rank", "Bank", "Row"]:
            ranges = self.mapping.get(key, [])
            for r in ranges:
                # The lowest LSB among all critical fields dictates the finest interleaving granularity
                # 所有關鍵欄位中最低的 LSB 決定了最細的交錯粒度
                msb, lsb = r
                if lsb < lowest_critical_lsb:
                    lowest_critical_lsb = lsb

        # If no critical fields are found (e.g. invalid config), fallback to 1KB (bit 10)
        # 如果沒有找到關鍵欄位（如無效設定），預設為 1KB (bit 10)
        if lowest_critical_lsb == 64:
            lowest_critical_lsb = 10

        boundary_size = 1 << lowest_critical_lsb

        # Calculate next boundary by clearing lower bits and adding boundary_size
        # 透過清除低位元並加上邊界大小來計算下一個邊界
        next_boundary = (phys_addr & ~(boundary_size - 1)) + boundary_size
        return next_boundary
