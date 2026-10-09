# Problem B — Directorate Drill Allocation

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate is planning a system-wide drill that requires locking hardware assets into synchronized pairs. The inventory consists of $2q$ assets, badged sequentially from $1$ to $2q$. The linkage protocol enforces a strict division: a valid synchronized pair must always bridge one asset from the lower badge tier ($1$ through $q$) and one asset from the upper badge tier ($q+1$ through $2q$). 

Due to firmware constraints, only specific combinations of lower-tier and upper-tier assets can successfully synchronize. You will receive the complete registry of these certified combinations. 

The mission objective is a full-capacity deployment. You must select a set of certified combinations to activate such that every single asset—across both badge tiers—is incorporated into exactly one active pair. No asset can be left idle, nor can any asset be assigned to more than one pair. Determine whether the registry allows for a selection of pairs that incorporates all $2q$ assets exactly once, and if so, output the configuration. Otherwise, report that a full-capacity deployment is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a certified combination between lower-tier asset $a$ and upper-tier asset $b$.

## Output
If a full-capacity deployment is possible, print `YES` on the first line, followed by $q$ lines that each list the two asset badges of a selected pair. If no such deployment is possible, print `NO`.

## Example
### Input
```
3 5
1 4
1 5
2 4
2 6
3 5
```

### Output
```
YES
1 4
2 6
3 5
```
