# Problem A — Ministry Workflow: Dispatch Generation

Time limit: 5 s   Memory limit: 256 MB

## Description
The Ministry of Administration operates a complex daily workflow. The process is divided into three distinct phases: Intake, Dispatch, and Audit. Your task is to implement the central component: the Dispatch phase.

During the **Intake phase**, citizen petitions are sorted into $k$ distinct classifications. For each classification, the Intake system outputs a specific origin office, a destination office where the cases are archived, and the exact quantity of dossiers that must be resolved today. 

Your program handles the **Dispatch phase**. The Ministry consists of $n$ offices connected by $m$ one-way courier routes. Because the couriers have limited carrying capacity, each route has a strict daily limit on the total number of dossiers it can transport. This limit applies to the combined sum of all classifications using that route. 

Dossiers are physical, indivisible folders. Your Dispatch module must generate a routing schedule that satisfies the strict chain of custody for each classification independently:
- For a given classification, its origin office must dispatch exactly its required quantity of dossiers more than it receives.
- For a given classification, its destination office must receive exactly its required quantity of dossiers more than it dispatches.
- For a given classification, every other office must dispatch exactly the same number of dossiers as it receives.

Different classifications are moved concurrently and share the same courier routes, competing for the limited daily capacities. 

Once your program generates the schedule, it is passed to the **Audit phase**. The Audit system will verify that all dossiers reach their destinations, that no route exceeds its daily limit, and that the number of dossiers of each classification on any route is a non-negative integer. You must determine if a valid Dispatch schedule exists and, if so, provide the exact routing details required by the Audit system.

## Input
The first line of the input provided by the Intake phase contains three integers $n$, $m$, and $k$.
The following $k$ lines detail the classifications. Each line contains three integers $s_i$, $t_i$, and $d_i$, representing the origin office, the destination office, and the required quantity of dossiers for classification $i$.
The final $m$ lines describe the Ministry's infrastructure. Each line contains three integers $u$, $v$, and $cap$, representing a one-way courier route from office $u$ to office $v$ with a daily capacity limit of $cap$ dossiers.

## Output
If the Dispatch phase can successfully route all dossiers without exceeding any courier route limits, print `YES` on the first line. 
Following this, output $k$ lines to be read by the Audit system. The $i$-th of these lines must contain exactly $m$ integers, where the $j$-th integer defines the number of dossiers of classification $i$ assigned to the $j$-th courier route (routes are indexed in the exact order they appear in the input).
If no such schedule is possible, print `NO`.

## Example

**Input:**
```text
4 5 2
1 4 2
2 3 1
1 2 2
2 4 1
1 3 1
3 4 2
2 3 1
```

**Output:**
```text
YES
1 1 1 1 0
0 0 0 0 1
```
