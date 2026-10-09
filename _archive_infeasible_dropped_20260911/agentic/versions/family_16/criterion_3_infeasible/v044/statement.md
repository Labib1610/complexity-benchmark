# Two-Phase Synthesis Verification

Time limit: 2 s   Memory limit: 256 MB

## Description

A manufacturing facility must process $j$ distinct components. Each component requires sequential processing through two specialized stations: the Primary Assembler and the Secondary Finisher. The process is strictly ordered; a component must completely finish its primary assembly before it can be transferred to the secondary finisher. Each station can process only one component at a time. For each component, you are provided the exact time it requires at the Primary Assembler and the Secondary Finisher.

The facility operates under a strict continuous uptime mandate of exactly $T$ milliseconds. All $j$ components must be completely processed through both stations within this timeframe. To determine if this is achievable, one must typically simulate the pipeline and evaluate the $j!$ possible processing sequences to discover if any permutation allows all components to finish before the $T$ millisecond threshold. The search space grows factorially, making sequence evaluation heavily resource-intensive.

However, the configurations provided in this verification dataset are structurally deficient, meaning no sequence among the $j!$ possibilities can ever satisfy the timeframe. Rather than searching for a valid sequence, your task is to output a specific diagnostic code proving why the components cannot be scheduled. You are guaranteed that exactly one of the following two structural deficiencies will be present in any given input, and you must print the one that holds:

- **Individual Component Exhaustion:** A single component requires so much time that, even if processed entirely in isolation, its sequential processing through both stations exceeds $T$.
  Print: `JOB i` — where $i$ (1-based) is the index of such a component.

- **Station Saturation:** Because a station processes components one at a time, it must remain active for the sum of the processing times of all components assigned to it. If the total processing time across all components for a single station exceeds $T$, the deadline cannot be met.
  Print: `LOAD c` — where $c$ is the station number (1 for Primary Assembler, 2 for Secondary Finisher) whose total load exceeds $T$.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
The following $j$ lines each contain two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the processing times for a component at the Primary Assembler and the Secondary Finisher, respectively.

## Output

Print a single line: `JOB i` (if a component $i$'s combined processing time exceeds $T$) or `LOAD c` (if a station $c$'s total processing time exceeds $T$).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, component 1 requires $70 + 60 = 130 > 100$ milliseconds in sequence, so `JOB 1` proves the timeframe is impossible. In Example 2, no single component exceeds 150 milliseconds, but the Primary Assembler must process $50+50+50+50 = 200 > 150$ milliseconds of work in total, so `LOAD 1` is the diagnostic code.
