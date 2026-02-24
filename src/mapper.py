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
