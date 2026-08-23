# Concurrency Configuration

Time limit: 1 s
Memory limit: 256 MB

You are optimizing a software engine that executes $n$ background tasks. Each task requires a binary configuration flag, which must be calibrated to either 1 or 2.

To prevent race conditions, the engine has identified $m$ resource contentions. Each contention involves a specific pair of tasks that interact over a shared memory address. To guarantee memory safety, for every pair of tasks linked by a resource contention, their configuration flags must strictly not equal each other.

Your task is to determine a valid configuration array for all $n$ tasks, or report if it is impossible to satisfy all contention rules. If multiple valid arrays exist, you must choose the one that yields the minimum deterministic state hash. The state hash is computed sequentially: start with an initial hash $H_0 = 0$. For each task $i$ from 1 to $n$ in increasing order, the hash is updated as $H_i = 2 \cdot H_{i-1} + t_i - 1$, where $t_i \in \{1, 2\}$ is the flag assigned to task $i$. The final state hash evaluated is $H_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of background tasks and the number of resource contentions.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a resource contention between task $u$ and task $v$.

## Output
If there is no valid configuration array, output a single line containing `NO`.
If a valid array exists, output `YES` on the first line. On the next line, output $n$ space-separated integers $t_1, \ldots, t_n$ ($t_i \in \{1, 2\}$), representing the flag assignments that minimize the final state hash.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```