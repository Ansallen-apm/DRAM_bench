from src.main import TraceReader
from src.mapper import AddressMapper
import json

with open("configs/mapping_2ch.json", "r") as f:
    config = json.load(f)

mapper = AddressMapper(config)
reader = TraceReader("traces/PT_test/pt_test.trace", mapper)
trace_iter = iter(reader)

for i in range(16):
    req = next(trace_iter)
    print(f"Req {i+1}: Addr: {hex(req['address'])}, Size: {req['size']}, Beats: {req['beats']}")
