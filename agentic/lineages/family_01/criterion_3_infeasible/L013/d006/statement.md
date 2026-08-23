# Problem C — Weekend Deployment Veto

Time limit: 2 s   Memory limit: 256 MB

During a system upgrade, a tech firm needs to transition $n$ legacy microservices (numbered 1 to $n$). The engineering team has identified $m$ pairs of these microservices that share temporary database tables. To prevent data corruption, any two microservices sharing a table cannot be processed in the same deployment batch.

Leadership wants the transition finished in a single weekend using exactly two deployment batches. However, the engineering lead realizes this schedule is unachievable. The shared-table records confirm the presence of an unresolvable core: a specific set of three microservices that demand three separate deployment batches. This situation arises because the shared-table records include every possible two-microservice combination that can be drawn from this set of three.

To justify adding a third deployment batch to the schedule, you must extract the IDs of three microservices that form such an unresolvable core.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating a pair of microservices that share temporary tables. No pair is repeated.
It is guaranteed that at least one such set of three microservices exists.

## Output
Output three space-separated integers $a$, $b$, and $c$, which are the IDs of the three microservices in the core, sorted in ascending order ($a < b < c$).
If more than one valid set exists, output the one that is lexicographically smallest (first minimize $a$, then minimize $b$ in case of a tie, and finally minimize $c$).

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