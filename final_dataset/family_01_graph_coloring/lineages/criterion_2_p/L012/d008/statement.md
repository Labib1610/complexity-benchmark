# Problem B — Linkage Configuration

Time limit: 1 s   Memory limit: 256 MB

You are designing a mechanical linkage with $n$ vertical sliders, identified by integers from 1 to $n$. Each slider $i$ is fixed at a horizontal coordinate $x = i$. Your task is to lock each slider at a vertical height $h_i$, which must be exactly 1 or 2.

The linkage contains $m$ rigid struts. Each strut is installed between a starting slider $u$ and a receiving slider $v$, strictly in the order they are listed in the blueprint. 

To prevent the mechanism from jamming, every strut must pass a digital checksum calibration based on the assigned heights of its two endpoints. The calibration follows this exact three-step procedure:
1. The base value $C$ of the strut is initialized to the starting height $h_u$ plus 4.
2. The value $C$ is then modified based on the receiving height $h_v$:
   - If $h_v = 1$, $C$ is multiplied by 2, and then 1 is subtracted from it.
   - If $h_v = 2$, $C$ has 3 added to it.
3. Finally, the bitwise XOR of $C$ and the starting height $h_u$ is calculated. For the assembly to pass inspection, this final result must be exactly 9.

(If a slider is not connected to any struts, its height does not affect the assembly of other components).

Your task is to determine whether all sliders can be locked at valid heights such that every strut passes the checksum calibration. If a valid configuration exists, you must provide the sequence of heights $h_1, h_2, \dots, h_n$ (where each $h_i \in \{1, 2\}$). If multiple valid sequences exist, you must output the one that produces the smallest possible decimal value when the sequence of digits $h_1 h_2 \dots h_n$ is evaluated as a single $n$-digit number in base 3.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a strut installed from starting slider $u$ to receiving slider $v$.

## Output
If there is no way to assign the heights without violating the calibration requirement, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print $n$ space-separated integers $h_1, h_2, \dots, h_n$ (each either 1 or 2), representing the valid configuration sequence that minimizes the required base-3 value.

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