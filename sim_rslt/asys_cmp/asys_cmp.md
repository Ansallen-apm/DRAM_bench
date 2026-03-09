# Comparison of main.py vs asys_parall.py (basic100, QD=64)

This report compares the original sequential `main.py` against the new parallelized `asys_parall.py` on the `basic100` trace set.

| Trace File | Total Bytes | Hits/Misses | main Cycles | asys Cycles | main BW | asys BW | main Util | asys Util |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rand_read_128B.trace | 12800 | 0/30 | 1359 | 1359 | 30.14 | 30.14 | 58.87% | 58.87% |
| rand_read_256B.trace | 25600 | 0/30 | 2070 | 2152 | 39.57 | 38.07 | 77.29% | 74.35% |
| rand_read_512B.trace | 51200 | 0/29 | 3648 | 3640 | 44.91 | 45.01 | 87.72% | 87.91% |
| rand_write_128B.trace | 12800 | 0/31 | 1653 | 1653 | 24.78 | 24.78 | 48.40% | 48.40% |
| rand_write_256B.trace | 25600 | 0/32 | 1980 | 2025 | 41.37 | 40.45 | 80.81% | 79.01% |
| rand_write_512B.trace | 51200 | 0/29 | 3600 | 3548 | 45.51 | 46.18 | 88.89% | 90.19% |
| sample.trace | 320 | 3/1 | 190 | 190 | 5.39 | 5.39 | 21.05% | 21.05% |
| seq_read_128B.trace | 12800 | 96/4 | 952 | 952 | 43.03 | 43.03 | 84.03% | 84.03% |
| seq_read_256B.trace | 25600 | 96/4 | 1784 | 1784 | 45.92 | 45.92 | 89.69% | 89.69% |
| seq_read_512B.trace | 51200 | 92/8 | 3320 | 3320 | 49.35 | 49.35 | 96.39% | 96.39% |
| seq_read_64B.trace | 6400 | 96/4 | 624 | 624 | 32.82 | 32.82 | 64.10% | 64.10% |
| seq_write_128B.trace | 12800 | 96/4 | 948 | 948 | 43.21 | 43.21 | 84.39% | 84.39% |
| seq_write_256B.trace | 25600 | 96/4 | 1780 | 1780 | 46.02 | 46.02 | 89.89% | 89.89% |
| seq_write_512B.trace | 51200 | 92/8 | 3316 | 3316 | 49.41 | 49.41 | 96.50% | 96.50% |
| seq_write_64B.trace | 6400 | 96/4 | 620 | 620 | 33.03 | 33.03 | 64.52% | 64.52% |

## 分析與結論 (Analysis & Conclusion)
- **正確性 (Correctness)**：總位元組數 (Total Bytes) 與 Page 命中/未命中 (Hits/Misses) 在兩種執行方式下完全相同，證實位址映射與請求處理邏輯維持一致。
- **效能差異 (Performance Difference)**：
  - 在大部分序列存取 (seq) 中，兩者的週期數幾乎完全相同。這是因為在單純的循序存取下，幾乎沒有因為 Channel 之間的指令互相干擾而造成的阻塞。
  - 在隨機存取 (rand) 中，`asys_parall.py` 與 `main.py` 會出現些微的週期差異（例如 `rand_read_256B.trace` asys 稍慢，但 `rand_read_512B.trace` asys 稍快）。這是因為：
    1. `main.py` 是將所有 Channel 的請求放入一個共享的 Queue (QD=64)，而 `asys_parall.py` 是各 Channel 擁有獨立的 Queue (QD=64)。這會改變指令在 Queue 中排隊的順序與可視範圍，進而影響了排程器的決策與記憶體狀態的交錯執行。
    2. 當 Trace 中的指令集中在某個 Channel 時，`main.py` 可能會被塞滿單一 Channel 的指令，導致另一個 Channel 的指令進不去；而 `asys_parall.py` 完全解除了這種互相阻塞。相反地，拆分 Queue 也可能導致某些原先在 Global Queue 裡能利用總線空隙穿插的排程被改變。
  - 總結來說，`asys_parall.py` 提供了一個各通道完全非同步且更貼近實體硬體獨立 Channel 行為的模擬模式，這點微小的差距是合理且符合預期的。
