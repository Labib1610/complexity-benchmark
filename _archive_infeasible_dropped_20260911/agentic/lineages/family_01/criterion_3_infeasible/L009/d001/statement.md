# Problem C — Triple-Core Resonance

Time limit: 2 s
Memory limit: 256 MB

An experimental reactor contains $n$ magnetic coils, numbered $1$ to $n$. The engineers have tested various pairs of coils and recorded $m$ combinations that exhibit direct magnetic resonance.

To achieve sustained fusion, the reactor requires a "triple-core" configuration. This configuration is formed by isolating exactly three distinct coils. For the configuration to function, energy must flow seamlessly among all its components. Specifically, every coil in the chosen group of three must have a confirmed, direct resonance with both of the other two coils in that same group.

It is guaranteed that the recorded data contains at least one such configuration. Your task is to identify it.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the subsequent $m$ lines provides two integers $u$ and $v$, indicating that coil $u$ and coil $v$ have a confirmed resonance. The records are symmetric (order does not matter), and no combination is listed more than once.
It is guaranteed that at least one valid triple-core configuration exists.

## Output
Print three integers $x$, $y$, and $z$ on a single line, separated by spaces, such that $x < y < z$. These represent the identifiers of the three coils in your chosen configuration. If multiple valid groups of three exist, you must output the one that minimizes the value of $x$. If there are still multiple options, minimize $y$, and finally minimize $z$ to break any remaining ties.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```