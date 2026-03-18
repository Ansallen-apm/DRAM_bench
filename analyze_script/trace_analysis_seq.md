# Trace Mapping and Bank Interleaving Analysis

## 1. Configuration (設定摘要)
- **Trace File**: `traces/basic100/seq_read_512B.trace`
- **Mapping Config**: `configs/mapping_2ch.json`
- **Queue Depth**: `16`
- **Queue Chunk Size**: `256` Bytes

## 2. Overall Statistics (整體統計)
- **Total Queue Chunks**: `200`
- **Total Consecutive Bank Switches (連續 Bank 切換次數)**: `49`
- **Average Unique Banks per Window (平均 Queue Bank 數量)**: `4.06`
- **Max Unique Banks (最大 Bank 數量)**: `5`
- **Min Unique Banks (最小 Bank 數量)**: `4`

## 3. Sliding Window Log (視窗滑動歷程)
*(Showing first 50 steps, peak interleaving steps, and last 50 steps to avoid massive file size)*

### Initial Steps (初始階段)
- **Step 0**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 1**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 2**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 3**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 4**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 5**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 6**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 7**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 8**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 9**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 10**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 11**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 12**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 13**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 14**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 15**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 16**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 17**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 18**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 19**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 20**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 21**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 22**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 23**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 24**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 25**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 26**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 27**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 28**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 29**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 30**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 31**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 32**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 33**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 34**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 35**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 36**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 37**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 38**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 39**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 40**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 41**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 42**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 43**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 44**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 45**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 46**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 47**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 48**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 49**: Unique Banks: `4` | Distribution: `[CH0_R0_B0:4, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`

...

### Peak Interleaving Steps (最大交錯階段)
- **Step 113**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:3, CH0_R0_B1:1, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 114**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:2, CH0_R0_B1:2, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 115**: Unique Banks: `5` | Distribution: `[CH0_R0_B0:1, CH0_R0_B1:3, CH0_R1_B0:4, CH1_R0_B0:4, CH1_R1_B0:4]`
- **Step 117**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B0:4, CH1_R0_B0:3, CH1_R0_B1:1, CH1_R1_B0:4]`
- **Step 118**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B0:4, CH1_R0_B0:2, CH1_R0_B1:2, CH1_R1_B0:4]`
- **Step 119**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B0:4, CH1_R0_B0:1, CH1_R0_B1:3, CH1_R1_B0:4]`
- **Step 121**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B0:3, CH0_R1_B1:1, CH1_R0_B1:4, CH1_R1_B0:4]`
- **Step 122**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B0:2, CH0_R1_B1:2, CH1_R0_B1:4, CH1_R1_B0:4]`
- **Step 123**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B0:1, CH0_R1_B1:3, CH1_R0_B1:4, CH1_R1_B0:4]`
- **Step 125**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B0:3, CH1_R1_B1:1]`
- **Step 126**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B0:2, CH1_R1_B1:2]`
- **Step 127**: Unique Banks: `5` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B0:1, CH1_R1_B1:3]`

...

### Final Steps (最終階段)
- **Step 135**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 136**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 137**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 138**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 139**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 140**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 141**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 142**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 143**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 144**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 145**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 146**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 147**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 148**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 149**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 150**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 151**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 152**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 153**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 154**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 155**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 156**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 157**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 158**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 159**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 160**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 161**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 162**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 163**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 164**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 165**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 166**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 167**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 168**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 169**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 170**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 171**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 172**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 173**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 174**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 175**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 176**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 177**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 178**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 179**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 180**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 181**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 182**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 183**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
- **Step 184**: Unique Banks: `4` | Distribution: `[CH0_R0_B1:4, CH0_R1_B1:4, CH1_R0_B1:4, CH1_R1_B1:4]`
