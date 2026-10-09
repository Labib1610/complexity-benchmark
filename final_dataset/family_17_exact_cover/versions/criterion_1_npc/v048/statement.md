# Problem A — Phase 3: Mobilization Assignment

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate strictly follows a five-phase protocol for its annual readiness drill. 

- **Phase 1: Roster Compilation.** Exactly $3q$ active personnel are selected and assigned sequential tracking numbers from $1$ to $3q$. 
- **Phase 2: Synergy Testing.** Various three-person groups are put through a communication simulator. Any group that successfully completes the simulation is logged in the clearance database. 
- **Phase 3: Mobilization Assignment.** A subset of the logged groups from Phase 2 must be selected. To satisfy the drill's strict requirements, every single person from Phase 1 must be assigned to exactly one selected group. This ensures no one is left idle and no one is scheduled twice. 
- **Phase 4: Field Deployment.** The selected groups are dispatched to their respective zones.
- **Phase 5: Debrief.** Post-drill performance analysis.

Your software is responsible for executing Phase 3. You must determine if a valid mobilization assignment exists based on the Phase 2 logs, and if so, output the specific groups to pass to Phase 4.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $q$ is the target number of groups to select, and $t$ is the number of groups logged during Phase 2.

Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the tracking numbers of three personnel who formed a successful group in Phase 2.

## Output
If a valid assignment can be formed for Phase 3, print `YES` on the first line. Following that, print $q$ lines, each containing the three tracking numbers of a selected group. 
If no such assignment is possible, print `NO`.

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
