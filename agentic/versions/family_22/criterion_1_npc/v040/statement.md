# Problem A — Component Fabrication Sequence

Time limit: 5 s   Memory limit: 256 MB

## Description
When a new product design arrives, it first undergoes an automated breakdown process that splits the design into $n$ indivisible fabrication steps and identifies which steps rely on the physical output of others. 

Your system is responsible for the intermediate planning phase. You must allocate each of the $n$ steps to a specific activation cycle. The facility is equipped with a bank of $M$ identical fabrication units. During any single activation cycle, the facility can execute at most $M$ steps in total, as each unit handles at most one step per cycle. Every step requires exactly one full cycle to complete. When a step relies on the output of another step, the dependent step must be allocated to an activation cycle strictly greater than the cycle of the step it relies on; they cannot occur in the same cycle because the output is only available after the cycle concludes.

The raw materials will degrade if the process takes too long, so all steps must be allocated to an activation cycle between $1$ and $T$, inclusive.

Once a valid cycle allocation is generated, the plan is passed to the floor control system which handles the final phase: routing materials to specific units and monitoring the physical assembly. Your task is only to determine if a valid cycle allocation exists and, if so, to output the cycle number for each step.

## Input
The first line contains four integers: $n$ (the number of steps), $M$ (the number of units available per cycle), $T$ (the maximum allowed cycles), and $m$ (the number of dependency relations). 
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that step $a$ produces an output required by step $b$ (meaning step $a$'s cycle must be strictly less than step $b$'s cycle). Steps are numbered from $1$ to $n$.

## Output
If all steps can be allocated to cycles $1$ through $T$ without exceeding the $M$ steps per cycle limit and while respecting all dependencies, print `YES`. On the next line, print $n$ integers, where the $i$-th integer is the activation cycle allocated to step $i$. 
If no such allocation is possible, print `NO`.

## Example

**Input:**
```
5 2 3 4
1 3
2 3
3 4
3 5
```

**Output:**
```
YES
1 1 2 3 3
```
