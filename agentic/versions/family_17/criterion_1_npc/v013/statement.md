# Problem A — Full-Coverage Cell Deployment for the Regional Drill

Time limit: 5 s
Memory limit: 256 MB

## Description
The regional emergency directorate is preparing a full-scale readiness drill. The active roster contains exactly $3q$ certified operators, numbered consecutively from 1 to $3q$. 

Command requires a highly structured deployment. Every operating cell must consist of exactly three members. Because the roster size is a perfect multiple of three, the arithmetic guarantees that exactly $q$ cells are needed to deploy the entire roster. Leadership has mandated that every single operator must be assigned to exactly one cell. No operator may be left out, and no operator may be assigned to multiple cells simultaneously.

Over the years, specific three-person combinations have trained together and received joint clearance. The directorate's database provides a list of $t$ such pre-cleared trios. Command policy strictly limits the drill to these pre-cleared trios. 

Because the total number of operators ($3q$) perfectly matches the capacity of $q$ cells, finding a valid schedule is simply a matter of identifying $q$ mutually exclusive trios from the list. Every time you confirm a trio for the schedule, you cleanly reduce the remaining unassigned operators by exactly three. By systematically filtering the $t$ candidate trios and resolving overlaps, you must isolate exactly $q$ independent trios that perfectly partition the roster. If the historical data does not contain a set of trios that achieves this exact balance, report that no acceptable plan exists.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The total number of operators on the roster is $3q$.
Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing one pre-cleared trio.

## Output
If a perfect deployment schedule can be extracted, print `YES` on the first line. Then, print $q$ lines, each containing the three operators of one chosen trio.
If no such schedule can be formed, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
