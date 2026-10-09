# Problem B — Array Fabrication Pipeline

Time limit: 5 s
Memory limit: 256 MB

## Description
The production of a localized sensor array follows a strict three-stage protocol. 

**Stage 1 (Specification):** The centralized controller ingests the array's communication blueprint. The blueprint defines $n$ distinct modules and $m$ communication links. The links are structured such that every module, except one, relays data directly to exactly one superior module, ensuring all modules are interconnected without any redundant pathways. The controller also reads the maximum total wire allowance $B$.

**Stage 2 (Bay Assignment):** The system must determine a one-to-one mapping of the $n$ modules into $n$ physical bays arranged in a single straight row, numbered $1$ to $n$. When two modules are linked by the blueprint, a wire is run between their bays. A wire's length is precisely the absolute difference between the bay numbers of the two modules it connects. All wires share a common trench. The system must find an assignment where the sum of the lengths of all necessary wires does not exceed the allowance $B$.

**Stage 3 (Fabrication):** If Stage 2 produces a valid mapping, robotic assemblers populate the bays and lay the wires. If no such mapping exists, the blueprint is rejected.

Your software is responsible only for Stage 2. Given the output of Stage 1, you must either provide the required mapping for Stage 3, or signal that fabrication should be aborted.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$, representing a communication link between module $u$ and module $v$.

## Output
If Stage 3 can proceed, print `YES` on the first line. On the second line, print $n$ space-separated integers, where the $i$-th integer is the bay number (from $1$ to $n$) assigned to module $i$. Every bay from $1$ to $n$ must be assigned exactly once.
If Stage 3 cannot proceed because no assignment meets the wire allowance, print `NO`.

## Example

**Input:**
```
5 4 6
1 2
1 3
3 4
3 5
```

**Output:**
```
YES
3 2 4 1 5
```
