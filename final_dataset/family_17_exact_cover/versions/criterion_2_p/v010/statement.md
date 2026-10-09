# Problem B — Full-Coverage Asset Commitment

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate's remote segment must be fully committed for the upcoming drill. The deployment consists of $2q$ distinct assets in total. Assets with identifiers from $1$ to $q$ are designated as controllers, while those with identifiers from $q+1$ to $2q$ are designated as platforms. 

Command requires a comprehensive operational plan. You are provided with a catalog of verified operational ties. Each tie specifies a stable link between one specific controller and one specific platform. Unverified links are strictly forbidden, regardless of operational convenience. The catalog may contain many overlapping ties, providing multiple options for how assets might be linked.

An acceptable operational plan is a selection of these verified ties such that every single asset (all controllers and all platforms, from $1$ to $2q$) is utilized exactly once. No asset may be left out of the plan, and no asset may be involved in more than one selected tie. 

Determine if there is a valid plan that fully commits all $2q$ assets without any overlap. If such a plan can be formed from the verified ties, output it. Otherwise, indicate that a complete commitment is impossible.

## Input
First line: two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
Next $t$ lines: two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a verified operational tie between asset $a$ and asset $b$.

## Output
If a complete plan is possible, print `YES` followed by $q$ lines, each containing the two asset identifiers of a selected tie. If no such plan exists, print `NO`.

## Example

**Input:**
```
3 4
1 4
2 5
3 5
2 6
```

**Output:**
```
YES
1 4
3 5
2 6
```
