# Problem B — Production Line Configuration

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing facility runs $n$ distinct machines. Each machine must be securely locked into one of two modes: mode 0 or mode 1. 
For the purpose of system evaluation, we define the *active polarity* of machine $i$ as $p_i = 2 s_i - 1$, where $s_i \in \{0, 1\}$ is the assigned mode of machine $i$. Thus, mode 1 gives a polarity of $1$, and mode 0 gives a polarity of $-1$.

The facility's power grid is safeguarded by $m$ safety interlocks. Each interlock receives two signal feeds from the machines. A signal feed is defined by a non-zero integer $c$. The feed's source machine is given by the absolute value $|c|$, and its signed value $c$ acts as its calibration factor.

An interlock remains stable if and only if the sum of the products of each feed's calibration factor and its corresponding machine's active polarity is strictly greater than the negative sum of the feeds' absolute values. 
Mathematically, for an interlock with feeds $c_1$ and $c_2$, the stability condition is:
$$c_1 \cdot p_{|c_1|} + c_2 \cdot p_{|c_2|} > -(|c_1| + |c_2|)$$

If this inequality is not met, a catastrophic shutdown is triggered. To keep the facility running, you must determine a facility-wide configuration (assigning mode 0 or mode 1 to each machine) such that all $m$ interlocks remain stable.

Determine if a safe configuration exists, and if so, output the required mode for each machine.

## Input
The first line of the input provides two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of machines and the number of safety interlocks, respectively.

The next $m$ lines each contain two non-zero integers $c_1$ and $c_2$ ($|c_i| \le n$), detailing the two signal feeds for that interlock. 

## Output
If it is impossible to configure all $n$ machines without causing a shutdown, output a single line with the word `NO`.

If a safe configuration is possible, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) to specify the chosen mode for each machine from 1 to $n$.

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
There might be several safe configurations; outputting any valid one is correct. A single machine can provide signal feeds to multiple interlocks.