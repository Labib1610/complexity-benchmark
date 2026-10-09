# Problem A — Regional Readiness Drill Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate relies on a registry of pre-approved operational protocols. Each protocol in this registry strictly specifies a trio of personnel using their ID codes. The current workforce consists of individuals whose total count is scaled by a factor $q$, meaning there are $3q$ personnel on duty. They are assigned consecutive ID codes from 1 to $3q$.

Every individual in the workforce is issued exactly one clearance chip at the start of a shift. When command activates a protocol from the registry, it simultaneously consumes the chips of the three personnel specified in that particular protocol. A protocol can only be activated if all three required individuals still possess their unconsumed chips. Protocols cannot be modified or generated on the fly; only the exact trios listed in the registry may be used.

A full-scale readiness drill requires that the workforce's entire chip pool is completely exhausted, ensuring no individual is left idle and no one is assigned to conflicting duties. Your task is to determine whether it is possible to designate a selection of the registered protocols that meets this requirement. If such a selection exists, you must also output the chosen protocols. Otherwise, indicate that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the ID codes in a pre-approved protocol from the registry.

## Output
If a valid selection exists, print `YES`, followed by $q$ lines, each containing the three ID codes of one activated protocol.
Otherwise, print `NO`.

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
