# Problem A — Thermal Resonance Tuning

Time limit: 2 s   Memory limit: 256 MB

A reactor core contains $n$ thermal modules. To maintain stability, each module must be assigned a resonance state $s_i \in \{1, 2, 3\}$.

The diagnostic system has identified $m$ critical interactions between specific pairs of modules. The stability of the core is determined by its total system energy $W$, which consists solely of coupling energies between interacting modules.

For each critical interaction between module $u$ and module $v$, their coupling energy is given by the following resonance formula:
$C_{u,v} = s_u^5 + s_v^5 - 3 s_u^4 s_v - 3 s_u s_v^4 + 2 s_u^3 s_v^2 + 2 s_u^2 s_v^3 - 5 s_u^3 - 5 s_v^3 + 5 s_u^2 s_v + 5 s_u s_v^2 + 4 s_u + 4 s_v$

The total system energy $W$ is the sum of all coupling energies for the critical interactions:
$W = \sum_{j=1}^m C_{u_j, v_j}$

To prevent core failure, the configuration must achieve a state of perfect resonance, which requires the total system energy to be exactly $0$. (That is, $W = 0$).

Your task is to determine whether there exists a valid state assignment for all modules $1 \dots n$ such that the total system energy is exactly $0$. If such an assignment exists, you must provide one.

## Input
The first line contains two integers $n$ and $m$ — the number of thermal modules and the number of critical interactions ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a critical interaction between module $u$ and module $v$. Each interaction is listed at most once.

## Output
If it is impossible to calibrate the modules to the required energy state, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), with $s_i$ representing the resonance state assigned to module $i$. Any valid assignment is accepted.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```
*Explanation for Example 1:*
Assigning states 1, 2, 3, 3 yields the following coupling energies:
- Interaction (1, 2) with states 1 and 2: $C_{1,2} = 1 + 32 - 6 - 48 + 8 + 16 - 5 - 40 + 10 + 20 + 4 + 8 = 0$.
- Interaction (1, 3) with states 1 and 3: $C_{1,3} = 1 + 243 - 9 - 243 + 18 + 54 - 5 - 135 + 15 + 45 + 4 + 12 = 0$.
- Interaction (2, 3) with states 2 and 3: $C_{2,3} = 32 + 243 - 144 - 486 + 144 + 216 - 40 - 135 + 60 + 90 + 8 + 12 = 0$.
- Interaction (1, 4) with states 1 and 3: $C_{1,4} = 0$.
- Interaction (2, 4) with states 2 and 3: $C_{2,4} = 0$.

The total system energy $W$ is $0 + 0 + 0 + 0 + 0 = 0$. The configuration achieves the target energy, so it is stable.

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```