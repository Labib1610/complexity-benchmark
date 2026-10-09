# Debate Teams

Time limit: 1 s
Memory limit: 256 MB

You are organizing a large-scale debate tournament involving $n$ speakers, indexed 1 through $n$. Each speaker must be assigned to one of two sides:
* Affirmative (represented by the identifier 1)
* Negative (represented by the identifier 2)

You are provided with $m$ historical dispute records. Each record indicates a pair of speakers who cannot be assigned to the same side.

To ensure the tournament meets the venue's regulations, your assignment must satisfy the following conditions:
1. Dispute Avoidance: No two speakers who have a historical dispute may be assigned to the same side.
2. Capacity Conservation: Every speaker must be assigned to exactly one side, such that the total number of speakers on the Affirmative side plus the total number of speakers on the Negative side is exactly $n$.
3. Identifier Bounds: The sum of the assigned side identifiers across all $n$ speakers, denoted as $S$, must strictly satisfy $n - 1 < S < 2n + 1$.

Additionally, you are guaranteed that the input data satisfies the following structural properties:
* The sum, over all $n$ speakers, of the number of times each speaker appears in the dispute records will never exceed $400,000$.
* No individual speaker appears in the dispute records more than $400,000$ times.

If there is no way to assign the speakers while satisfying all conditions, you must announce this by printing `NO`.
If a valid assignment exists, print `YES`. On the next line, print the valid assignment as a sequence of $n$ integers (each 1 or 2). If there are multiple valid assignments, you must output the one that is lexicographically smallest.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the number of speakers and the number of dispute records, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a dispute between speaker $u$ and speaker $v$.

## Output
If no valid assignment is possible, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1, s_2, \dots, s_n$ where $s_i \in \{1, 2\}$, representing the lexicographically smallest valid assignment.

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
