# Problem A — Component Fabrication Sequence

Time limit: 5 s   Memory limit: 256 MB

## Description
When a new product design arrives, an automated breakdown process splits it into $n$ indivisible fabrication steps. It also identifies which steps rely on the physical output of others.

Your system is responsible for the intermediate planning phase: assigning each of the $n$ steps to a specific activation cycle. The facility draws from a localized power grid capable of operating exactly $M$ identical fabrication units simultaneously. Each step occupies a single unit for exactly one full cycle. 

When a step provides material for another step, the extraction and cooling mechanism means the output is only viable for use in subsequent cycles. Thus, a dependent step cannot occur concurrently with or prior to the step it relies on. 

Furthermore, the raw materials are prepared at the beginning of cycle 1. They contain a stabilizing agent that remains effective for exactly $T$ cycles before degrading. Any step taking place after this lifespan will result in a defective product.

Once a valid assignment of steps to cycles is generated, the plan is passed to the floor control system for physical assembly. Your task is to determine if a valid assignment exists and, if so, to output the cycle number for each step.

## Input
The first line contains four integers: $n$ (the number of steps), $M$ (the number of fabrication units available), $T$ (the lifespan of the stabilizing agent in cycles), and $m$ (the number of material dependencies). 
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that step $a$ produces an output required by step $b$. Steps are numbered from $1$ to $n$.

## Output
If all steps can be safely assigned to cycles without violating unit capacity, material lifespans, or dependency requirements, print `YES`. On the next line, print $n$ integers, where the $i$-th integer is the activation cycle assigned to step $i$. 
If no such assignment is possible, print `NO`.

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
