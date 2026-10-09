# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate requires a full-commitment deployment plan for the upcoming drill. You are provided with a registry of $t$ certified configurations. Your objective is to explore the combinatorial space of all possible subsets of the $t$ provided configurations to find a valid deployment plan.

A deployment plan is valid if and only if every single asset in the remote segment is committed exactly once. The chosen subset of configurations must perfectly partition the entire set of assets, leaving no asset unused and assigning no asset to more than one configuration. Because the registry can contain up to 400,000 configurations, the number of possible subsets to consider is up to $2^{400000}$. You must determine if this massive search space contains at least one valid subset that achieves this complete commitment.

The remote segment consists of $2q$ distinct assets. Assets $1$ through $q$ are designated as controllers, while assets $q+1$ through $2q$ are designated as platforms. Every certified configuration in the registry happens to consist of exactly two assets: one controller and one platform.

If a valid subset of configurations exists, you must output it. If multiple valid subsets exist, any one is acceptable. Otherwise, report that no valid plan can be formed.

## Input
First line: two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
Next $t$ lines: two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a certified configuration that includes asset $a$ and asset $b$.

## Output
If a valid deployment plan is possible, print `YES` on the first line, followed by $q$ lines, each containing the two assets of one selected configuration.
If no valid plan is possible, print `NO`.

## Example

**Input**
```text
3 4
1 4
2 5
3 6
1 5
```

**Output**
```text
YES
1 4
2 5
3 6
```
