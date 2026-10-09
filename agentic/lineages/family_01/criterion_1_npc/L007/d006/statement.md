# Problem A — Thermal Resonance Tuning

Time limit: 2 s   Memory limit: 256 MB

A reactor core contains $n$ thermal modules. To maintain stability, each module must be assigned a resonance state $s_i \in \{1, 2, 3\}$.

The diagnostic system has identified $m$ critical interactions between specific pairs of modules. The stability of the core is determined by its total system energy $W$, which consists of intrinsic energies and coupling energies.

For each module $i$, let $d_i$ be the number of critical interactions involving module $i$. The intrinsic energy of module $i$ is given by:
$E_i = d_i (s_i^4 - 5s_i^2)$

For each critical interaction between module $u$ and module $v$, their coupling energy is given by:
$C_{u,v} = 2 s_u s_v (3 s_u s_v + 5 - 2 s_u^2 - 2 s_v^2)$

The total system energy $W$ is the sum of all intrinsic energies and all coupling energies:
$W = \sum_{i=1}^n E_i + \sum_{j=1}^m C_{u_j, v_j}$

To prevent core failure, the configuration must achieve the theoretical minimum energy state, which requires that $W = -4m$.

Your task is to determine whether there exists a valid state assignment for all modules $1 \dots n$ such that the total system energy is exactly $-4m$. If such an assignment exists, you must provide one.

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
Assigning states 1, 2, 3, 3 yields the following:
- Module 1 is involved in 3 interactions ($d_1 = 3$). Its intrinsic energy is $E_1 = 3(1^4 - 5(1^2)) = -12$.
- Module 2 has $d_2 = 3$, $s_2 = 2$. $E_2 = 3(2^4 - 5(2^2)) = 3(16 - 20) = -12$.
- Module 3 has $d_3 = 2$, $s_3 = 3$. $E_3 = 2(3^4 - 5(3^2)) = 2(81 - 45) = 72$.
- Module 4 has $d_4 = 2$, $s_4 = 3$. $E_4 = 2(81 - 45) = 72$.
The sum of intrinsic energies is $120$.

The coupling energies are:
- (1, 2) with states 1 and 2: $C_{1,2} = 2(2)(6 + 5 - 2 - 8) = 4$.
- (1, 3) with states 1 and 3: $C_{1,3} = 2(3)(9 + 5 - 2 - 18) = -36$.
- (2, 3) with states 2 and 3: $C_{2,3} = 2(6)(18 + 5 - 8 - 18) = -36$.
- (1, 4) with states 1 and 3: $C_{1,4} = -36$.
- (2, 4) with states 2 and 3: $C_{2,4} = -36$.
The sum of coupling energies is $-140$.

Total system energy $W = 120 - 140 = -20$. Since $m = 5$, the target energy is $-4 \times 5 = -20$. The configuration achieves this, so it is stable.

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