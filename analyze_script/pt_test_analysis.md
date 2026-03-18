# Trace Mapping and Bank Interleaving Analysis

## 1. Configuration (設定摘要)
- **Trace File**: `traces/PT_test/pt_test.trace`
- **Mapping Config**: `configs/mapping_2ch.json`
- **Queue Depth**: `128`
- **Queue Chunk Size**: `256` Bytes

## 2. Overall Statistics (整體統計)
- **Total Queue Chunks**: `56000`
- **Total Consecutive Bank Switches (連續 Bank 切換次數)**: `13999`
- **Average Unique Banks per Window (平均 Queue Bank 數量)**: `9.55`
- **Max Unique Banks (最大 Bank 數量)**: `16`
- **Min Unique Banks (最小 Bank 數量)**: `8`

## 3. Sliding Window Log (視窗滑動歷程)
*(Showing first 50 steps, peak interleaving steps, and last 50 steps to avoid massive file size)*

### Initial Steps (初始階段)
- **Step 0**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 1**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 2**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 3**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 4**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 5**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 6**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 7**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 8**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 9**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 10**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 11**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 12**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 13**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 14**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 15**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 16**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 17**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 18**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 19**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 20**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 21**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 22**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 23**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 24**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 25**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 26**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 27**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 28**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 29**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 30**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 31**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 32**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 33**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 34**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 35**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 36**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 37**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 38**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 39**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 40**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 41**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 42**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 43**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 44**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 45**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 46**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 47**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 48**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`
- **Step 49**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:16, CH0_R0_B4:16, CH0_R1_B0:16, CH0_R1_B4:16, CH1_R0_B0:16, CH1_R0_B4:16, CH1_R1_B0:16, CH1_R1_B4:16]`

...

### Peak Interleaving Steps (最大交錯階段)
- **Step 413**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:12, CH0_R0_B5:4, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:12, CH1_R0_B5:4, CH1_R1_B0:15, CH1_R1_B1:1, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 414**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:12, CH0_R0_B5:4, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:12, CH1_R0_B5:4, CH1_R1_B0:14, CH1_R1_B1:2, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 415**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:12, CH0_R0_B5:4, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:12, CH1_R0_B5:4, CH1_R1_B0:13, CH1_R1_B1:3, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 416**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:12, CH0_R0_B5:4, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:12, CH1_R0_B5:4, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 417**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:11, CH0_R0_B5:5, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:12, CH1_R0_B5:4, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 418**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:10, CH0_R0_B5:6, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:12, CH1_R0_B5:4, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 419**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:9, CH0_R0_B5:7, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:12, CH1_R0_B5:4, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 420**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:12, CH1_R0_B5:4, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 421**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:11, CH1_R0_B5:5, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 422**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:10, CH1_R0_B5:6, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 423**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:9, CH1_R0_B5:7, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 424**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:12, CH0_R1_B5:4, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:8, CH1_R0_B5:8, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 425**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:11, CH0_R1_B5:5, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:8, CH1_R0_B5:8, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 426**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:10, CH0_R1_B5:6, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:8, CH1_R0_B5:8, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 427**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:9, CH0_R1_B5:7, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:8, CH1_R0_B5:8, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 428**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:8, CH0_R1_B5:8, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:8, CH1_R0_B5:8, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:12, CH1_R1_B5:4]`
- **Step 429**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:8, CH0_R1_B5:8, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:8, CH1_R0_B5:8, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:11, CH1_R1_B5:5]`
- **Step 430**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:8, CH0_R1_B5:8, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:8, CH1_R0_B5:8, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:10, CH1_R1_B5:6]`
- **Step 431**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:8, CH0_R1_B5:8, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:8, CH1_R0_B5:8, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:9, CH1_R1_B5:7]`
- **Step 432**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:12, CH0_R0_B1:4, CH0_R0_B4:8, CH0_R0_B5:8, CH0_R1_B0:12, CH0_R1_B1:4, CH0_R1_B4:8, CH0_R1_B5:8, CH1_R0_B0:12, CH1_R0_B1:4, CH1_R0_B4:8, CH1_R0_B5:8, CH1_R1_B0:12, CH1_R1_B1:4, CH1_R1_B4:8, CH1_R1_B5:8]`

...

### Final Steps (最終階段)
- **Step 55823**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55824**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55825**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55826**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55827**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55828**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55829**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55830**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55831**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55832**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55833**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55834**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55835**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55836**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55837**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55838**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55839**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55840**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55841**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55842**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55843**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55844**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55845**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55846**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55847**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55848**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55849**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55850**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55851**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55852**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55853**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55854**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55855**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55856**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55857**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55858**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55859**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55860**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55861**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55862**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55863**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55864**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55865**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55866**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55867**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55868**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55869**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55870**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55871**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
- **Step 55872**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:16, CH0_R0_B5:16, CH0_R1_B1:16, CH0_R1_B5:16, CH1_R0_B1:16, CH1_R0_B5:16, CH1_R1_B1:16, CH1_R1_B5:16]`
