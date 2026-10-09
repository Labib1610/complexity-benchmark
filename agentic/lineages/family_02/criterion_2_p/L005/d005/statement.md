# Problem B — Quantum Array Calibration

Time limit: 1 s   Memory limit: 256 MB

## Description
You are tasked with finding a valid operating state for a quantum computing array consisting of $n$ qubits, numbered 1 to $n$. A global calibration assigns a spin $x_i \in \{-1, 1\}$ to each qubit $i$.

The system's error-correction protocol monitors a rigid set of $m$ entanglement routes. Each route imposes a structural restriction on the spins. 

A route is defined by two non-zero signed integers $l_1$ and $l_2$. The resonance score of the route under a given calibration is calculated as:
$R = l_1 \cdot x_{|l_1|} + l_2 \cdot x_{|l_2|}$
where $|l|$ denotes the absolute value of $l$.

A critical fault occurs on a route if its resonance score reaches its theoretical minimum possible limit. Since $x_i \in \{-1, 1\}$, the score $R$ can never be strictly less than $-(|l_1| + |l_2|)$. A route triggers a critical fault if and only if $R = -(|l_1| + |l_2|)$.

The array is considered stable if no route triggers a critical fault. Write a program to determine if a stable global calibration exists, and if so, output one.

Because the hardware interface expects binary states, your output must map each spin $x_i$ to a binary value $s_i \in \{0, 1\}$ using the transformation $s_i = \frac{x_i + 1}{2}$. (Thus, a spin of $-1$ becomes $0$, and a spin of $1$ becomes $1$).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines describes a route using two non-zero signed integers $l_1$ and $l_2$, where $|l_1|, |l_2| \le n$. 

## Output
If no valid calibration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each either 0 or 1) representing the binary state of each qubit in a valid calibration.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid calibrations may exist; any one is accepted. The same qubit may appear in multiple routes.