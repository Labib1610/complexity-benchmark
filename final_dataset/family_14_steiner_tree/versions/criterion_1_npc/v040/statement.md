# Problem A — Infrastructure Synchronization Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description

Phase 1 of the campus expansion has concluded with the architectural committee finalizing the locations of **n** key landmarks. Following this, the board of trustees mandated that a specific group of **t** of these landmarks must be equipped with interactive kiosks that share a synchronized database.

You are responsible for Phase 2: designing the physical data pathways. You are provided with a list of **m** feasible underground conduits between pairs of landmarks. Each conduit has an associated excavation and material expense. You must select a subset of these conduits to activate so that a continuous data route exists between every pair of the **t** kiosk-hosting landmarks. You may route these paths through any of the remaining landmarks if doing so minimizes the total expense.

Upon completion of your task, Phase 3 will commence: contractors will begin trenching along your selected conduits, and the software teams will deploy the synchronization protocol across the newly established network.

Determine the minimum total expense required for Phase 2 to ensure all kiosk-hosting landmarks are mutually reachable through the activated conduits.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the kiosk-hosting landmarks (landmarks are numbered 1 to **n**).
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a conduit can be activated between landmark **u** and landmark **v** at an expense of **w**.
It is guaranteed that the available conduits are sufficient to establish the required routes.

## Output

Print a single integer: the minimum total expense to ensure all kiosk-hosting landmarks share a continuous data route.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, routing the data through landmark 4 (which does not host a kiosk) incurs an expense of 1+1+1 = 3. This is cheaper than establishing conduits directly between the three kiosk-hosting landmarks, which would cost at least 4. In Example 3, there is only one kiosk-hosting landmark, so no conduits need to be activated.
