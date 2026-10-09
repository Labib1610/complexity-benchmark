# Problem B — Border Checkpoint Queue

Time limit: 1 s   Memory limit: 256 MB

## Description

A border crossing has a single lane dedicated to commercial transport trucks. Processing each truck requires two consecutive security checks. First, the truck's manifest is reviewed by the manifest officer. Second, the truck's cargo is scanned by the X-ray gantry.

Because the checkpoint consists of a single narrow lane with concrete barriers, trucks cannot pass one another. They must proceed through the X-ray gantry in the exact same sequence they were reviewed by the manifest officer.

The manifest officer can only review one truck at a time. Similarly, the X-ray gantry can only scan one truck at a time. A truck can enter the X-ray gantry immediately after its manifest review is completely finished. If the gantry is currently scanning another truck, the next truck must wait.

You are the yard manager, and you can arrange the initial queue of trucks before the checkpoint opens. Your objective is to determine the earliest possible time the final truck can exit the X-ray gantry, assuming you arrange the queue optimally.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000), representing the number of trucks.
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the time required for the manifest review and the time required for the X-ray scan for that specific truck, respectively.

## Output

Print a single integer: the earliest possible time at which all trucks have completed both security checks.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single truck takes 5 units of time for the manifest review and then 3 units of time for the X-ray scan, finishing at time 8.
