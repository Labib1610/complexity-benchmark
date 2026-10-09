# Problem A — Simulation Roster Allocation

Time limit: 5 s   Memory limit: 256 MB

## Description
A regional crisis agency is scheduling personnel for an upcoming field simulation. The agency employs a staff whose total size is a multiple of the standard team capacity. Specifically, there are $3q$ staff members, identified by integer IDs ranging from $1$ up to $3q$.

During the simulation, personnel are deployed in field teams. Strict operational protocols dictate that a field team can only be formed if its members have previously completed a joint synchronization course. The agency maintains a historical catalog of all such synchronized combinations. Each combination invariably consists of three specific staff members.

The simulation coordinator must authorize a selection of combinations from the catalog so that the entire roster is mobilized. Agency rules dictate a strict allocation: every staff member must participate in the simulation, and no staff member may be assigned to more than one authorized combination.

Your objective is to determine if the coordinator can successfully schedule all personnel under these constraints. If a valid schedule is possible, you must provide one. If the historical catalog does not permit an allocation where everyone is assigned exactly once, you must report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the subsequent $t$ lines provides three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the IDs of the staff members in one synchronized combination from the catalog.

## Output
If a valid schedule can be formed, print `YES` on the first line. Following this, print $q$ lines, each containing the three staff IDs of an authorized combination.
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
