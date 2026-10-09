# Problem B — Cargo Inspection

Time limit: 1 s   Memory limit: 256 MB

## Description

A port authority manages a fleet of **j** vessels arriving for cargo inspection. You must arrange the fleet into a single line. Two inspectors, a Local officer and a Federal officer, will walk down this line from the first vessel to the last. You are given the duration the Local officer spends on each vessel, followed by the duration the Federal officer spends on it.

The operational rules are:
- You must decide the initial sequence of vessels in the line. Both officers will visit the vessels in this exact same chosen order.
- An officer boards and inspects exactly one vessel at a time.
- The Local officer moves to the next vessel in the sequence as soon as they finish the current one.
- The Federal officer can only begin inspecting a vessel after the Local officer has completely finished their inspection of that specific vessel.
- The Federal officer must strictly follow the sequence. If they finish a vessel but the Local officer is still on the next vessel in the sequence, the Federal officer must wait outside.

You must decide the initial sequence of vessels in the line. Choose the sequence that minimizes the time at which the final vessel finishes its Federal inspection. Output this minimum possible finish time. If multiple sequences achieve this optimum, you still output only the minimum final completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the duration required for the Local officer and the Federal officer to inspect a vessel, respectively.

## Output

Print a single integer: the smallest possible time at which all vessels have completely finished the Federal inspection.

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

In Example 2, the single vessel takes 5 for the Local officer and then 3 for the Federal officer, finishing at time 8.