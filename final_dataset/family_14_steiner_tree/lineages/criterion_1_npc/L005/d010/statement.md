# Problem A — Oscillator Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

You are configuring a system of $n$ oscillators. 

Each oscillator $i$ operates at a continuous frequency $F_i$. 

You can purchase phase-lock links. Each available link connects two distinct oscillators, $u$ and $v$, and physically constrains them to operate at the exact same frequency ($F_u = F_v$). 

A global operating state of the system is defined as *stable* if it satisfies the constraints of every purchased link.

A specific subset of $t$ oscillators are designated as *critical*. Your task is to purchase a subset of available links such that the following condition is satisfied:
In EVERY stable operating state, the $t$ critical oscillators are mathematically guaranteed to operate at the exact same frequency as each other. 
(If $t \le 1$, this condition is vacuously satisfied without purchasing any links).

You are given a list of $m$ available links, each with a one-time purchase cost $w$. Determine the minimum total cost of a subset of links that satisfies this requirement.

## Input

The first line provides three integers $n$, $m$, and $t$ ($1 \le t \le 10$, $1 \le n \le 100$, $0 \le m \le n(n-1)/2$).
The second line lists $t$ distinct integers representing the indices of the critical oscillators (1-indexed).
The following $m$ lines each contain three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$). These represent an available phase-lock link between oscillator $u$ and oscillator $v$ that can be purchased for a cost of $w$.
It is guaranteed that it is possible to satisfy the requirement using the available links.

## Output

Output a single integer representing the minimum total cost of a subset of links that satisfies the condition.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, the critical oscillators are 1, 2, and 3. By purchasing the links (1, 4), (2, 4), and (3, 4) for a total cost of 1+1+1=3, any stable state must satisfy $F_1 = F_4$, $F_2 = F_4$, and $F_3 = F_4$. This mathematically forces $F_1, F_2$, and $F_3$ to all equal each other. If we had only purchased (1, 2), a stable state could have $F_1 = F_2 = 50$ and $F_3 = 60$, which violates the requirement since the critical oscillators do not share the same frequency. 

In Example 2, by purchasing links (1, 2) and (2, 3) for a cost of 1+1=2, any stable state must have $F_1 = F_2 = F_3$. Oscillator 4 can operate at any independent frequency, which is perfectly valid since it is not a critical oscillator.

In Example 3, there is only one critical oscillator. In any operating state, this single oscillator operates at the same frequency as itself. Thus, the requirement is vacuously satisfied without purchasing any links, resulting in a cost of 0.