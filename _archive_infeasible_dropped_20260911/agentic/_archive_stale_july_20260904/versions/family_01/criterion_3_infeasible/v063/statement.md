# Problem C — Phase 2: Cascade Isolation

Time limit: 2 s
Memory limit: 256 MB

The Automated Stability Protocol is responsible for maintaining the integrity of volatile compound batches. The protocol operates in three sequential phases.

Phase 1 has already concluded. During this phase, $n$ chemical compounds were screened pairwise to determine which specific combinations exhibit mutual reactivity. The system has generated a log of these bidirectional reactions.

Your objective is to execute Phase 2. Safety regulations dictate that a batch is unstable if a closed three-step reaction sequence can occur. You must find a group of three distinct compounds—let us call them $X$, $Y$, and $Z$—that satisfy the following operational rules:
- A recorded reaction exists between $X$ and $Y$.
- A recorded reaction exists between $Y$ and $Z$.
- A recorded reaction exists between $Z$ and $X$.

It is chemically guaranteed that the current batch contains at least one such group of three compounds. Your task is to process the logs and identify one such group to initiate emergency neutralization.

Phase 3 will deploy neutralizers based on your output. To ensure deterministic deployment, you must list the identifiers of the three compounds in the chosen group in ascending order. If more than one valid group of three compounds exists, you must choose the group whose lowest identifier is as small as possible. In the event of a tie, minimize the second-lowest identifier, and if a tie still remains, minimize the highest identifier.

## Input
The first line of the Phase 1 log contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the total number of compounds (numbered $1$ to $n$) and the number of mutual reactions observed.

Following this are $m$ lines, each containing two integers $u$ and $v$, indicating that compound $u$ and compound $v$ react with one another. 
It is guaranteed that the log contains at least one group of three compounds satisfying the reaction sequence rules.

## Output
Output a single line with three integers $a$, $b$, and $c$ representing the identifiers of the compounds in the chosen group. The identifiers must be sorted in ascending order ($a < b < c$). Apply the exact tie-breaking criteria as specified for Phase 3.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
