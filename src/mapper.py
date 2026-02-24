class AddressMapper:
    def __init__(self, mapping_config):
        self.mapping = mapping_config

    def _extract_bits(self, addr, msb, lsb):
        mask = (1 << (msb - lsb + 1)) - 1
        return (addr >> lsb) & mask

    def map_address(self, phys_addr):
        """
        Maps a physical address to (channel, rank, bank, row, column).
        Returns a dictionary.
        """
        result = {}
        # Order of keys usually matters for printing but dictionary is fine.
        # Required keys: Channel, Rank, Bank, Row, Column
        for key in ["Channel", "Rank", "Bank", "Row", "Column"]:
            ranges = self.mapping.get(key, [])
            value = 0
            # Calculate total width to shift appropriately?
            # Or construct value range by range.
            # Assuming first range in list is MSB.
            # Example: [[16, 14], [5, 4]]
            # Range 0: 3 bits (val1)
            # Range 1: 2 bits (val2)
            # Total = (val1 << 2) | val2

            # We need to know the width of subsequent ranges to shift the current one.
            # Alternatively, iterate from last range (LSB) to first (MSB).

            current_shift = 0
            temp_value = 0

            # Iterate in reverse order (LSB first)
            for r in reversed(ranges):
                msb, lsb = r
                width = msb - lsb + 1
                part = self._extract_bits(phys_addr, msb, lsb)
                temp_value |= (part << current_shift)
                current_shift += width

            result[key] = temp_value

        return result
