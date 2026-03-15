# Trace Mapping and Bank Interleaving Analysis

## 1. Configuration (設定摘要)
- **Trace File**: `traces/PT_test/pt_test.trace`
- **Mapping Config**: `configs/mapping_2ch.json`
- **Queue Depth**: `64`
- **Queue Chunk Size**: `256` Bytes

## 2. Overall Statistics (整體統計)
- **Total Queue Chunks**: `56000`
- **Total Consecutive Bank Switches (連續 Bank 切換次數)**: `13999`
- **Average Unique Banks per Window (平均 Queue Bank 數量)**: `8.55`
- **Max Unique Banks (最大 Bank 數量)**: `16`
- **Min Unique Banks (最小 Bank 數量)**: `8`

## 3. Sliding Window Log (視窗滑動歷程)
*(Showing first 50 steps, peak interleaving steps, and last 50 steps to avoid massive file size)*

### Initial Steps (初始階段)
- **Step 0**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 1**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 2**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 3**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 4**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 5**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 6**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 7**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 8**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 9**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 10**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 11**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 12**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 13**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 14**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 15**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 16**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 17**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 18**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 19**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 20**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 21**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 22**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 23**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 24**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 25**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 26**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 27**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 28**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 29**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 30**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 31**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 32**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 33**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 34**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 35**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 36**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 37**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 38**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 39**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 40**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 41**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 42**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 43**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 44**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 45**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 46**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 47**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 48**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`
- **Step 49**: Unique Banks: `8` | Distribution: `[CH0_R0_B0:8, CH0_R0_B4:8, CH0_R1_B0:8, CH0_R1_B4:8, CH1_R0_B0:8, CH1_R0_B4:8, CH1_R1_B0:8, CH1_R1_B4:8]`

...

### Peak Interleaving Steps (最大交錯階段)
- **Step 477**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:4, CH0_R0_B1:4, CH0_R0_B4:4, CH0_R0_B5:4, CH0_R1_B0:4, CH0_R1_B1:4, CH0_R1_B4:4, CH0_R1_B5:4, CH1_R0_B0:4, CH1_R0_B1:4, CH1_R0_B4:4, CH1_R0_B5:4, CH1_R1_B0:7, CH1_R1_B1:1, CH1_R1_B4:4, CH1_R1_B5:4]`
- **Step 478**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:4, CH0_R0_B1:4, CH0_R0_B4:4, CH0_R0_B5:4, CH0_R1_B0:4, CH0_R1_B1:4, CH0_R1_B4:4, CH0_R1_B5:4, CH1_R0_B0:4, CH1_R0_B1:4, CH1_R0_B4:4, CH1_R0_B5:4, CH1_R1_B0:6, CH1_R1_B1:2, CH1_R1_B4:4, CH1_R1_B5:4]`
- **Step 479**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:4, CH0_R0_B1:4, CH0_R0_B4:4, CH0_R0_B5:4, CH0_R1_B0:4, CH0_R1_B1:4, CH0_R1_B4:4, CH0_R1_B5:4, CH1_R0_B0:4, CH1_R0_B1:4, CH1_R0_B4:4, CH1_R0_B5:4, CH1_R1_B0:5, CH1_R1_B1:3, CH1_R1_B4:4, CH1_R1_B5:4]`
- **Step 480**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:4, CH0_R0_B1:4, CH0_R0_B4:4, CH0_R0_B5:4, CH0_R1_B0:4, CH0_R1_B1:4, CH0_R1_B4:4, CH0_R1_B5:4, CH1_R0_B0:4, CH1_R0_B1:4, CH1_R0_B4:4, CH1_R0_B5:4, CH1_R1_B0:4, CH1_R1_B1:4, CH1_R1_B4:4, CH1_R1_B5:4]`
- **Step 481**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:4, CH0_R0_B1:4, CH0_R0_B4:3, CH0_R0_B5:5, CH0_R1_B0:4, CH0_R1_B1:4, CH0_R1_B4:4, CH0_R1_B5:4, CH1_R0_B0:4, CH1_R0_B1:4, CH1_R0_B4:4, CH1_R0_B5:4, CH1_R1_B0:4, CH1_R1_B1:4, CH1_R1_B4:4, CH1_R1_B5:4]`
- **Step 482**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:4, CH0_R0_B1:4, CH0_R0_B4:2, CH0_R0_B5:6, CH0_R1_B0:4, CH0_R1_B1:4, CH0_R1_B4:4, CH0_R1_B5:4, CH1_R0_B0:4, CH1_R0_B1:4, CH1_R0_B4:4, CH1_R0_B5:4, CH1_R1_B0:4, CH1_R1_B1:4, CH1_R1_B4:4, CH1_R1_B5:4]`
- **Step 483**: Unique Banks: `16` | Distribution: `[CH0_R0_B0:4, CH0_R0_B1:4, CH0_R0_B4:1, CH0_R0_B5:7, CH0_R1_B0:4, CH0_R1_B1:4, CH0_R1_B4:4, CH0_R1_B5:4, CH1_R0_B0:4, CH1_R0_B1:4, CH1_R0_B4:4, CH1_R0_B5:4, CH1_R1_B0:4, CH1_R1_B1:4, CH1_R1_B4:4, CH1_R1_B5:4]`
- **Step 989**: Unique Banks: `16` | Distribution: `[CH0_R0_B1:4, CH0_R0_B2:4, CH0_R0_B5:4, CH0_R0_B6:4, CH0_R1_B1:4, CH0_R1_B2:4, CH0_R1_B5:4, CH0_R1_B6:4, CH1_R0_B1:4, CH1_R0_B2:4, CH1_R0_B5:4, CH1_R0_B6:4, CH1_R1_B1:7, CH1_R1_B2:1, CH1_R1_B5:4, CH1_R1_B6:4]`
- **Step 990**: Unique Banks: `16` | Distribution: `[CH0_R0_B1:4, CH0_R0_B2:4, CH0_R0_B5:4, CH0_R0_B6:4, CH0_R1_B1:4, CH0_R1_B2:4, CH0_R1_B5:4, CH0_R1_B6:4, CH1_R0_B1:4, CH1_R0_B2:4, CH1_R0_B5:4, CH1_R0_B6:4, CH1_R1_B1:6, CH1_R1_B2:2, CH1_R1_B5:4, CH1_R1_B6:4]`
- **Step 991**: Unique Banks: `16` | Distribution: `[CH0_R0_B1:4, CH0_R0_B2:4, CH0_R0_B5:4, CH0_R0_B6:4, CH0_R1_B1:4, CH0_R1_B2:4, CH0_R1_B5:4, CH0_R1_B6:4, CH1_R0_B1:4, CH1_R0_B2:4, CH1_R0_B5:4, CH1_R0_B6:4, CH1_R1_B1:5, CH1_R1_B2:3, CH1_R1_B5:4, CH1_R1_B6:4]`
- **Step 992**: Unique Banks: `16` | Distribution: `[CH0_R0_B1:4, CH0_R0_B2:4, CH0_R0_B5:4, CH0_R0_B6:4, CH0_R1_B1:4, CH0_R1_B2:4, CH0_R1_B5:4, CH0_R1_B6:4, CH1_R0_B1:4, CH1_R0_B2:4, CH1_R0_B5:4, CH1_R0_B6:4, CH1_R1_B1:4, CH1_R1_B2:4, CH1_R1_B5:4, CH1_R1_B6:4]`
- **Step 993**: Unique Banks: `16` | Distribution: `[CH0_R0_B1:4, CH0_R0_B2:4, CH0_R0_B5:3, CH0_R0_B6:5, CH0_R1_B1:4, CH0_R1_B2:4, CH0_R1_B5:4, CH0_R1_B6:4, CH1_R0_B1:4, CH1_R0_B2:4, CH1_R0_B5:4, CH1_R0_B6:4, CH1_R1_B1:4, CH1_R1_B2:4, CH1_R1_B5:4, CH1_R1_B6:4]`
- **Step 994**: Unique Banks: `16` | Distribution: `[CH0_R0_B1:4, CH0_R0_B2:4, CH0_R0_B5:2, CH0_R0_B6:6, CH0_R1_B1:4, CH0_R1_B2:4, CH0_R1_B5:4, CH0_R1_B6:4, CH1_R0_B1:4, CH1_R0_B2:4, CH1_R0_B5:4, CH1_R0_B6:4, CH1_R1_B1:4, CH1_R1_B2:4, CH1_R1_B5:4, CH1_R1_B6:4]`
- **Step 995**: Unique Banks: `16` | Distribution: `[CH0_R0_B1:4, CH0_R0_B2:4, CH0_R0_B5:1, CH0_R0_B6:7, CH0_R1_B1:4, CH0_R1_B2:4, CH0_R1_B5:4, CH0_R1_B6:4, CH1_R0_B1:4, CH1_R0_B2:4, CH1_R0_B5:4, CH1_R0_B6:4, CH1_R1_B1:4, CH1_R1_B2:4, CH1_R1_B5:4, CH1_R1_B6:4]`
- **Step 1501**: Unique Banks: `16` | Distribution: `[CH0_R0_B2:4, CH0_R0_B3:4, CH0_R0_B6:4, CH0_R0_B7:4, CH0_R1_B2:4, CH0_R1_B3:4, CH0_R1_B6:4, CH0_R1_B7:4, CH1_R0_B2:4, CH1_R0_B3:4, CH1_R0_B6:4, CH1_R0_B7:4, CH1_R1_B2:7, CH1_R1_B3:1, CH1_R1_B6:4, CH1_R1_B7:4]`
- **Step 1502**: Unique Banks: `16` | Distribution: `[CH0_R0_B2:4, CH0_R0_B3:4, CH0_R0_B6:4, CH0_R0_B7:4, CH0_R1_B2:4, CH0_R1_B3:4, CH0_R1_B6:4, CH0_R1_B7:4, CH1_R0_B2:4, CH1_R0_B3:4, CH1_R0_B6:4, CH1_R0_B7:4, CH1_R1_B2:6, CH1_R1_B3:2, CH1_R1_B6:4, CH1_R1_B7:4]`
- **Step 1503**: Unique Banks: `16` | Distribution: `[CH0_R0_B2:4, CH0_R0_B3:4, CH0_R0_B6:4, CH0_R0_B7:4, CH0_R1_B2:4, CH0_R1_B3:4, CH0_R1_B6:4, CH0_R1_B7:4, CH1_R0_B2:4, CH1_R0_B3:4, CH1_R0_B6:4, CH1_R0_B7:4, CH1_R1_B2:5, CH1_R1_B3:3, CH1_R1_B6:4, CH1_R1_B7:4]`
- **Step 1504**: Unique Banks: `16` | Distribution: `[CH0_R0_B2:4, CH0_R0_B3:4, CH0_R0_B6:4, CH0_R0_B7:4, CH0_R1_B2:4, CH0_R1_B3:4, CH0_R1_B6:4, CH0_R1_B7:4, CH1_R0_B2:4, CH1_R0_B3:4, CH1_R0_B6:4, CH1_R0_B7:4, CH1_R1_B2:4, CH1_R1_B3:4, CH1_R1_B6:4, CH1_R1_B7:4]`
- **Step 1505**: Unique Banks: `16` | Distribution: `[CH0_R0_B2:4, CH0_R0_B3:4, CH0_R0_B6:3, CH0_R0_B7:5, CH0_R1_B2:4, CH0_R1_B3:4, CH0_R1_B6:4, CH0_R1_B7:4, CH1_R0_B2:4, CH1_R0_B3:4, CH1_R0_B6:4, CH1_R0_B7:4, CH1_R1_B2:4, CH1_R1_B3:4, CH1_R1_B6:4, CH1_R1_B7:4]`
- **Step 1506**: Unique Banks: `16` | Distribution: `[CH0_R0_B2:4, CH0_R0_B3:4, CH0_R0_B6:2, CH0_R0_B7:6, CH0_R1_B2:4, CH0_R1_B3:4, CH0_R1_B6:4, CH0_R1_B7:4, CH1_R0_B2:4, CH1_R0_B3:4, CH1_R0_B6:4, CH1_R0_B7:4, CH1_R1_B2:4, CH1_R1_B3:4, CH1_R1_B6:4, CH1_R1_B7:4]`

...

### Final Steps (最終階段)
- **Step 55887**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55888**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55889**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55890**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55891**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55892**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55893**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55894**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55895**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55896**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55897**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55898**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55899**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55900**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55901**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55902**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55903**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55904**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55905**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55906**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55907**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55908**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55909**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55910**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55911**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55912**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55913**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55914**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55915**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55916**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55917**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55918**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55919**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55920**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55921**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55922**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55923**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55924**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55925**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55926**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55927**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55928**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55929**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55930**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55931**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55932**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55933**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55934**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55935**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
- **Step 55936**: Unique Banks: `8` | Distribution: `[CH0_R0_B1:8, CH0_R0_B5:8, CH0_R1_B1:8, CH0_R1_B5:8, CH1_R0_B1:8, CH1_R0_B5:8, CH1_R1_B1:8, CH1_R1_B5:8]`
