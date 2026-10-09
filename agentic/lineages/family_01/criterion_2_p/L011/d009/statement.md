# Solvent Allocation

Time limit: 1 s
Memory limit: 256 MB

A chemical plant operates a network of $n$ reactors. To maintain stable reactions, every reactor $i$ ($1 \le i \le n$) must be filled with exactly one of two standard solvent mixtures:
- Mixture 1: 1 liter of Alpha and 2 liters of Beta.
- Mixture 2: 2 liters of Alpha and 1 liter of Beta.

The plant's layout includes $m$ balancing requirements. Each requirement specifies two reactors $u$ and $v$. To prevent pressure imbalances, the sum of the contents of reactor $u$ and reactor $v$ must yield exactly 3 liters of Alpha and 3 liters of Beta. A configuration of the plant is only valid if this condition holds for all $m$ requirements simultaneously.

Your objective is to determine if a viable assignment of mixtures to the $n$ reactors exists. Among all valid assignments, you must output the one that yields the lexicographically smallest sequence of Alpha volumes across the reactors.

For a chosen mixture, the Alpha volume is either 1 or 2. Thus, you will output a sequence of $n$ integers, each being either 1 or 2. (A sequence $X$ is lexicographically smaller than sequence $Y$ if, at the first index where they differ, $X$ has a smaller value than $Y$. This prioritization applies globally across the entire sequence of $n$ reactors.)

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 200,000$, $0 \le m \le 200,000$), representing the number of reactors and the number of balancing requirements, respectively.

Each of the next $m$ lines provides two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that the balancing requirement must hold for the sum of the contents of reactor $u$ and reactor $v$.

## Output
If it is impossible to find a viable assignment of mixtures, output `NO` on a single line.
If a viable assignment exists, output `YES` on the first line. On the second line, output $n$ space-separated integers representing the sequence of Alpha volumes (either 1 or 2) for reactors $1, 2, \dots, n$. This sequence must be the lexicographically smallest valid sequence.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```