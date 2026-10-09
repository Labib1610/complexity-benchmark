# Problem A — Manufacturing Lifecycle Simulation

Time limit: 5 s   Memory limit: 256 MB

## Description

The lifecycle of a custom manufacturing order consists of three distinct phases: blueprint generation, physical fabrication, and logistics dispatch.

During blueprint generation, an automated system analyzes client requests and translates them into a set of **j** components. Each component is broken down into an ordered series of physical tasks. Every task is assigned to one of the **m** specialized workstations on the factory floor, along with a precise time duration.

Your software module is responsible for analyzing the physical fabrication phase. In this phase, the factory must execute the generated blueprints under strict physical limitations:
- A component's tasks must be executed sequentially, exactly in the order specified by its blueprint (a task can only begin after the component's previous task is completely finished).
- A workstation can handle only one task at any given moment.
- Once a workstation starts a task, it must run it continuously until the specified duration elapses.

The physical fabrication phase is considered complete only when the final task of the last remaining component finishes.

The third phase, logistics dispatch, cannot begin until the physical fabrication phase is entirely complete. Given the blueprints from the first phase, your goal is to determine the absolute earliest time the logistics dispatch phase can commence.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of components and workstations, respectively.
The next **j** lines provide the output from the blueprint generation phase. Each line corresponds to one component and begins with an integer **o** (the number of tasks for this component). This is followed by **o** pairs of integers, each formatted as `workstation duration` (1 ≤ workstation ≤ m, 1 ≤ duration ≤ 1000). These pairs describe the tasks in the mandatory sequence they must be executed.
The total number of tasks across all components is at most 50.

## Output

Print a single integer: the earliest possible time the logistics dispatch phase can begin.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical components require workstations 1, 2, and 3 in sequence (2 time units each). The second component follows the first through the workstations, completing its fabrication phase at time 8. In Example 3, the two components require different workstations and are fabricated simultaneously, allowing logistics dispatch to begin at time 4.
