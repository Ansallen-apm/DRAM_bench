# Trace Mapping and Bank Interleaving Analysis

## 1. Configuration (設定摘要)
- **Trace File**: `traces/PT_test/pt_test.trace`
- **Mapping Config**: `configs/mapping_2ch.json`
- **Queue Depth**: `16`
- **Queue Chunk Size**: `256` Bytes

## 2. Overall Statistics (整體統計)
- **Total Queue Chunks**: `56000`
- **Total Consecutive Bank Switches (連續 Bank 切換次數)**: `13999`
- **Average Unique Banks per Window (平均 Queue Bank 數量)**: `4.75`
- **Max Unique Banks (最大 Bank 數量)**: `5`
- **Min Unique Banks (最小 Bank 數量)**: `4`

## 3. Sliding Window Log (視窗滑動歷程)
*(Showing first 50 steps, peak interleaving steps, and last 50 steps to avoid massive file size)*

### Initial Steps (初始階段)
- **Step 0**: Unique Banks: `4` | Distribution: `[CH0_R0_B4:4, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 1**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:1, CH0_R0_B4:3, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 2**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:2, CH0_R0_B4:2, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 3**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:3, CH0_R0_B4:1, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 4**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 5**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B0:1, CH1_R0_B4:3, CH1_R1_B4:4]`
- **Step 6**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B0:2, CH1_R0_B4:2, CH1_R1_B4:4]`
- **Step 7**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B0:3, CH1_R0_B4:1, CH1_R1_B4:4]`
- **Step 8**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 9**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:1, CH0_R1_B4:3, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 10**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:2, CH0_R1_B4:2, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 11**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:3, CH0_R1_B4:1, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 12**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 13**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:1, CH1_R1_B4:3]`
- **Step 14**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:2, CH1_R1_B4:2]`
- **Step 15**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:3, CH1_R1_B4:1]`
- **Step 16**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 17**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:3, CH0_R0_B4:1, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 18**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:2, CH0_R0_B4:2, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 19**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:1, CH0_R0_B4:3, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 20**: Unique Banks: `4` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 21**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:4, CH1_R0_B0:3, CH1_R0_B4:1, CH1_R1_B0:4]`
- **Step 22**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:4, CH1_R0_B0:2, CH1_R0_B4:2, CH1_R1_B0:4]`
- **Step 23**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:4, CH1_R0_B0:1, CH1_R0_B4:3, CH1_R1_B0:4]`
- **Step 24**: Unique Banks: `4` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:4, CH1_R0_B4:4, CH1_R1_B0:4]`
- **Step 25**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:3, CH0_R1_B4:1, CH1_R0_B4:4, CH1_R1_B0:4]`
- **Step 26**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:2, CH0_R1_B4:2, CH1_R0_B4:4, CH1_R1_B0:4]`
- **Step 27**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:1, CH0_R1_B4:3, CH1_R0_B4:4, CH1_R1_B0:4]`
- **Step 28**: Unique Banks: `4` | Distribution: `[CH0_R0_B4:4, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B0:4]`
- **Step 29**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B0:3, CH1_R1_B4:1]`
- **Step 30**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B0:2, CH1_R1_B4:2]`
- **Step 31**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B0:1, CH1_R1_B4:3]`
- **Step 32**: Unique Banks: `4` | Distribution: `[CH0_R0_B4:4, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 33**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:1, CH0_R0_B4:3, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 34**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:2, CH0_R0_B4:2, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 35**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:3, CH0_R0_B4:1, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 36**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 37**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B0:1, CH1_R0_B4:3, CH1_R1_B4:4]`
- **Step 38**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B0:2, CH1_R0_B4:2, CH1_R1_B4:4]`
- **Step 39**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B0:3, CH1_R0_B4:1, CH1_R1_B4:4]`
- **Step 40**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 41**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:1, CH0_R1_B4:3, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 42**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:2, CH0_R1_B4:2, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 43**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:3, CH0_R1_B4:1, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 44**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 45**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:1, CH1_R1_B4:3]`
- **Step 46**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:2, CH1_R1_B4:2]`
- **Step 47**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:3, CH1_R1_B4:1]`
- **Step 48**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 49**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:3, CH0_R0_B4:1, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`

...

### Peak Interleaving Steps (最大交錯階段)
- **Step 1**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:1, CH0_R0_B4:3, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 2**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:2, CH0_R0_B4:2, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 3**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:3, CH0_R0_B4:1, CH0_R1_B4:4, CH1_R0_B4:4, CH1_R1_B4:4]`
- **Step 5**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B0:1, CH1_R0_B4:3, CH1_R1_B4:4]`
- **Step 6**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B0:2, CH1_R0_B4:2, CH1_R1_B4:4]`
- **Step 7**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B4:4, CH1_R0_B0:3, CH1_R0_B4:1, CH1_R1_B4:4]`
- **Step 9**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:1, CH0_R1_B4:3, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 10**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:2, CH0_R1_B4:2, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 11**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:3, CH0_R1_B4:1, CH1_R0_B0:4, CH1_R1_B4:4]`
- **Step 13**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:1, CH1_R1_B4:3]`
- **Step 14**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:2, CH1_R1_B4:2]`
- **Step 15**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:3, CH1_R1_B4:1]`
- **Step 17**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:3, CH0_R0_B4:1, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 18**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:2, CH0_R0_B4:2, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 19**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:1, CH0_R0_B4:3, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 21**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:4, CH1_R0_B0:3, CH1_R0_B4:1, CH1_R1_B0:4]`
- **Step 22**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:4, CH1_R0_B0:2, CH1_R0_B4:2, CH1_R1_B0:4]`
- **Step 23**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:4, CH1_R0_B0:1, CH1_R0_B4:3, CH1_R1_B0:4]`
- **Step 25**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:3, CH0_R1_B4:1, CH1_R0_B4:4, CH1_R1_B0:4]`
- **Step 26**: Unique Banks: `5` | Distribution: `[CH0_R0_B4:4, CH0_R1_B0:2, CH0_R1_B4:2, CH1_R0_B4:4, CH1_R1_B0:4]`

...

### Final Steps (最終階段)
- **Step 55935**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:3, CH1_R1_B5:1]`
- **Step 55936**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 55937**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:3, CH0_R0_B5:1, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 55938**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:2, CH0_R0_B5:2, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 55939**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:1, CH0_R0_B5:3, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 55940**: Unique Banks: `4` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 55941**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:4, CH1_R0_B1:3, CH1_R0_B5:1, CH1_R1_B1:4]`
- **Step 55942**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:4, CH1_R0_B1:2, CH1_R0_B5:2, CH1_R1_B1:4]`
- **Step 55943**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:4, CH1_R0_B1:1, CH1_R0_B5:3, CH1_R1_B1:4]`
- **Step 55944**: Unique Banks: `4` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:4, CH1_R0_B5:4, CH1_R1_B1:4]`
- **Step 55945**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:3, CH0_R1_B5:1, CH1_R0_B5:4, CH1_R1_B1:4]`
- **Step 55946**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:2, CH0_R1_B5:2, CH1_R0_B5:4, CH1_R1_B1:4]`
- **Step 55947**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:1, CH0_R1_B5:3, CH1_R0_B5:4, CH1_R1_B1:4]`
- **Step 55948**: Unique Banks: `4` | Distribution: `[CH0_R0_B5:4, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B1:4]`
- **Step 55949**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B1:3, CH1_R1_B5:1]`
- **Step 55950**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B1:2, CH1_R1_B5:2]`
- **Step 55951**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B1:1, CH1_R1_B5:3]`
- **Step 55952**: Unique Banks: `4` | Distribution: `[CH0_R0_B5:4, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B5:4]`
- **Step 55953**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:1, CH0_R0_B5:3, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B5:4]`
- **Step 55954**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:2, CH0_R0_B5:2, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B5:4]`
- **Step 55955**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:3, CH0_R0_B5:1, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B5:4]`
- **Step 55956**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B5:4]`
- **Step 55957**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B5:4, CH1_R0_B1:1, CH1_R0_B5:3, CH1_R1_B5:4]`
- **Step 55958**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B5:4, CH1_R0_B1:2, CH1_R0_B5:2, CH1_R1_B5:4]`
- **Step 55959**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B5:4, CH1_R0_B1:3, CH1_R0_B5:1, CH1_R1_B5:4]`
- **Step 55960**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B5:4, CH1_R0_B1:4, CH1_R1_B5:4]`
- **Step 55961**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:1, CH0_R1_B5:3, CH1_R0_B1:4, CH1_R1_B5:4]`
- **Step 55962**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:2, CH0_R1_B5:2, CH1_R0_B1:4, CH1_R1_B5:4]`
- **Step 55963**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:3, CH0_R1_B5:1, CH1_R0_B1:4, CH1_R1_B5:4]`
- **Step 55964**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B5:4]`
- **Step 55965**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:1, CH1_R1_B5:3]`
- **Step 55966**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:2, CH1_R1_B5:2]`
- **Step 55967**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:3, CH1_R1_B5:1]`
- **Step 55968**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 55969**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:3, CH0_R0_B5:1, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 55970**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:2, CH0_R0_B5:2, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 55971**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:1, CH0_R0_B5:3, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 55972**: Unique Banks: `4` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 55973**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:4, CH1_R0_B1:3, CH1_R0_B5:1, CH1_R1_B1:4]`
- **Step 55974**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:4, CH1_R0_B1:2, CH1_R0_B5:2, CH1_R1_B1:4]`
- **Step 55975**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:4, CH1_R0_B1:1, CH1_R0_B5:3, CH1_R1_B1:4]`
- **Step 55976**: Unique Banks: `4` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:4, CH1_R0_B5:4, CH1_R1_B1:4]`
- **Step 55977**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:3, CH0_R1_B5:1, CH1_R0_B5:4, CH1_R1_B1:4]`
- **Step 55978**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:2, CH0_R1_B5:2, CH1_R0_B5:4, CH1_R1_B1:4]`
- **Step 55979**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B1:1, CH0_R1_B5:3, CH1_R0_B5:4, CH1_R1_B1:4]`
- **Step 55980**: Unique Banks: `4` | Distribution: `[CH0_R0_B5:4, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B1:4]`
- **Step 55981**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B1:3, CH1_R1_B5:1]`
- **Step 55982**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B1:2, CH1_R1_B5:2]`
- **Step 55983**: Unique Banks: `5` | Distribution: `[CH0_R0_B5:4, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B1:1, CH1_R1_B5:3]`
- **Step 55984**: Unique Banks: `4` | Distribution: `[CH0_R0_B5:4, CH0_R1_B5:4, CH1_R0_B5:4, CH1_R1_B5:4]`
