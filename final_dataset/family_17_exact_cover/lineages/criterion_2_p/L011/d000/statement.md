# Problem B — Fleet Deployment Roster

Time limit: 2 s   Memory limit: 256 MB

## Description
The logistics division must deploy a fleet of transport vehicles and their assigned operators for an upcoming supply run. The available personnel and equipment are divided into two equal-sized groups: a set of operators, assigned ID numbers consecutively starting from 1, and an equal-sized set of transport vehicles, assigned ID numbers in the block immediately following the operators. Every operator and every vehicle is a distinct resource, and the supply run requires that **all** of them be deployed simultaneously in a single fleet assignment.

An operator may be assigned to a vehicle only when that exact operator–vehicle combination appears on the safety certification list; uncertified pairings are strictly forbidden by regulations. An operator is typically certified on several vehicles, and a vehicle may be operated by several certified personnel. The provided certification list contains all legally permitted pairings.

An acceptable deployment roster selects certified pairings such that **every** operator and **every** vehicle is committed in **exactly one** selected pairing: each resource is used exactly once, none are omitted, and none are shared between two pairings. Decide whether the certification list admits such a complete one-to-one assignment of all resources, and if so output one; otherwise, report that the certified pairings cannot simultaneously deploy every resource.

## Input
First line: two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of operators (which is also the number of vehicles) and the number of certified pairings, respectively.
Next $t$ lines: two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a certified pairing between operator $a$ and vehicle $b$.

## Output
If a complete deployment roster is possible, print `YES` followed by $q$ lines, each containing the two ID numbers of one selected pairing from the roster. Otherwise, print `NO`.

## Example

**Input:**
```
3 5
1 4
1 5
2 4
2 6
3 5
```

**Output:**
```
YES
1 4
3 5
2 6
```
