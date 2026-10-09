# Problem B — Migration Window Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description
A software team's database architecture consists of a set of distinct migrations. These migrations are bound by a strict dependency hierarchy. Specifically, there is exactly one foundational migration, and every subsequent migration is linked directly to exactly one other migration. These links unify all migrations into a single connected framework with no closed loops.

To implement the architecture, the team has allotted a sequence of consecutive maintenance windows. The windows are numbered starting from 1 and incrementing by one, up to the exact total number of migrations. The deployment protocol requires that every migration is assigned to exactly one maintenance window, and every window must host exactly one migration.

Whenever two migrations are linked in the hierarchy, executing them in different windows incurs a wait time. This wait time is calculated as the absolute difference between the window numbers assigned to the two linked migrations. The direction of the link does not dictate which migration must happen earlier; the wait time only depends on the gap between their scheduled windows. The cumulative wait time for the deployment is the sum of the wait times across every link in the framework.

The team operates under a strict deployment budget. Your task is to determine a valid assignment of migrations to maintenance windows such that the cumulative wait time does not exceed this budget, or to report that no such schedule is possible.

## Input
The first line contains three integers $n$, $m$, and $B$, representing the number of migrations, the number of links, and the wait time budget, respectively. 
Each of the next $m$ lines contains two integers $u$ and $v$, indicating a link between migration $u$ and migration $v$. 
(The hierarchy ensures $m$ is exactly one less than $n$.)

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers, where the $i$-th integer represents the maintenance window assigned to migration $i$. If no assignment can satisfy the budget, print `NO`.

## Example

**Input:**
4 3 4
1 2
1 3
1 4

**Output:**
YES
2 1 3 4
