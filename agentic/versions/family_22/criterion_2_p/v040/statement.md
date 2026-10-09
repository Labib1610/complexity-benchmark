# Problem B — Motion Sequence Compiler

Time limit: 2 s   Memory limit: 256 MB

## Description
The automated trajectory planner has just finished its phase of computation. It has output a manifest of $n$ discrete micro-motions for a single robotic arm, along with $m$ ordering rules. Your software module must now process this manifest before the results can be sent downstream. 

Because the robotic arm operates a single end-effector, your module must arrange all $n$ micro-motions into a single, flat sequence. Each ordering rule from the planner specifies that a particular micro-motion must be fully executed prior to another specific micro-motion. This occurs when the later motion relies on the physical configuration established by the earlier one. 

Your task is to compile a comprehensive sequence that includes every micro-motion exactly once. In this sequence, for every rule provided, the relied-upon motion must appear earlier than the motion that relies on it. 

Once you produce this sequence, it is passed to the hardware controller to physically drive the servos. Occasionally, the trajectory planner produces rules that logically contradict each other, making it impossible to arrange the motions without violating at least one rule. If no valid sequence can be formed, you must reject the planner's output so it can recalculate.

## Input
The first line contains two integers $n$ and $m$. 
Each of the subsequent $m$ lines contains two integers $a$ and $b$, indicating that micro-motion $a$ must be executed prior to micro-motion $b$. Micro-motions are identified by integers from $1$ to $n$.

## Output
If a valid sequence can be formed, print `YES` on the first line, followed by a sequence of the integers $1$ to $n$ (separated by spaces) representing a valid execution order. If multiple valid sequences exist, any one is acceptable. If no such sequence is possible, print `NO`.

## Example 1
**Input:**
```
4 5
1 2
1 3
2 4
3 4
3 2
```
**Output:**
```
YES
1 3 2 4
```

## Example 2
**Input:**
```
3 3
1 2
2 3
3 1
```
**Output:**
```
NO
```
