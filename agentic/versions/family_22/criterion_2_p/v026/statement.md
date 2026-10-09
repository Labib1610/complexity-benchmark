# Phase II: Synthesis Sequencer

Time limit: 2 s   Memory limit: 256 MB

## Description
You are developing the control software for an automated chemical synthesis pipeline. The pipeline's complete operation is strictly divided into three phases:

1. **Preparation:** Raw materials are purified, measured, and loaded into the rotary dispenser.
2. **Sequencing (Your Task):** The system must determine a linear execution order for $n$ discrete chemical reactions. Because the machine has only one mixing chamber, it can only perform one reaction at a time. Furthermore, certain reactions require intermediate compounds produced by others. You are provided with a list of constraints, each dictating that a specific reaction must be completely finished before another can be started. You must order all $n$ reactions such that every constraint is satisfied.
3. **Execution & Finalization:** The generated sequence is transmitted to the robotic controller, which executes the reactions in the exact order provided, followed by a final crystallization procedure.

You only need to implement the software for the Sequencing phase. Given the number of reactions and the dependencies between them, produce a valid sequence. If the dependencies are logically contradictory (meaning no such sequence can possibly exist), you must report that the sequence cannot be formed.

## Input
The first line contains two integers $n$ and $m$, representing the number of reactions and the number of constraints, respectively. The reactions are numbered from $1$ to $n$.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that reaction $a$ must be performed before reaction $b$.

## Output
If a valid sequence exists, print `YES` on the first line, and on the second line print a sequence of all integers from $1$ to $n$ separated by spaces, representing the execution order. If there are multiple valid sequences, any of them will be accepted.
If no valid sequence can be formed, print `NO` on a single line.

## Example 1
**Input**
```
4 4
1 2
2 3
1 4
4 3
```
**Output**
```
YES
1 4 2 3
```

## Example 2
**Input**
```
3 3
1 2
2 3
3 1
```
**Output**
```
NO
```
