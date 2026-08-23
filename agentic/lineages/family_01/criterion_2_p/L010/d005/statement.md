# Gyroscopic Centrifuge Calibration

Time limit: 1 s   Memory limit: 256 MB

A laboratory is configuring a high-speed centrifuge with $n$ sample slots, numbered 1 through $n$. Each slot must be equipped with exactly one counterweight. There are two available counterweight models: Type 1 (which has a mass of 100 grams) and Type 2 (which has a mass of 200 grams).

The centrifuge is highly sensitive to harmonic vibrations. The manufacturer has provided a list of $m$ critical slot pairs. For each critical pair of slots, the combined mass of their installed counterweights must be exactly 300 grams to cancel out rotational resonance. 

You need to determine if there is a valid configuration of counterweights for all $n$ slots that satisfies every critical pair requirement.

If a valid configuration exists, you must provide it. To minimize the overall rotational inertia of the system, the configuration software prioritizes the lighter Type 1 counterweights. Specifically, it requires the configuration that is lexicographically smallest when represented as a sequence of counterweight types (1s and 2s). A sequence $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if, at the first slot index $i$ where they differ, $s_i < t_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of sample slots and the number of critical slot pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — a critical pair of slots whose combined counterweight mass must be exactly 300 grams.

## Output
If there is no way to configure the centrifuge without violating the resonance constraints, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each either 1 or 2), representing the lexicographically smallest valid counterweight configuration.

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