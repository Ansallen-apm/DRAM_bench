from src.mapper import AddressMapper
import json

with open("configs/mapping_2ch.json", "r") as f:
    config = json.load(f)

mapper = AddressMapper(config)
addr = 0x20000
print(f"Current Addr: {hex(addr)}")
print(f"Next Boundary: {hex(mapper.get_next_boundary(addr))}")
addr = 0x203FE
print(f"Current Addr: {hex(addr)}")
print(f"Next Boundary: {hex(mapper.get_next_boundary(addr))}")
