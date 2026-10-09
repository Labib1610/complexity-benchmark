# Assembly Track Layout

Time limit: 5 s   Memory limit: 256 MB

## Description
The engineering team has designed a production process that requires $n$ processing stations. These stations must exchange materials according to a strict transport specification. The specification demands exactly $m = n - 1$ direct conveyor links between specific pairs of stations. This setup guarantees that every station can reach every other station, either directly or through intermediate stops, with no redundant links.

To bring this design to life, a factory manager must install the $n$ stations onto exactly $n$ consecutive mounting pads. The pads are arranged in a straight line and numbered $1$ through $n$. Each pad can accommodate exactly one station. 

When a conveyor link is required between a station placed on pad $x$ and a station placed on pad $y$, the physical belt length is exactly $|x - y|$ meters. Because the belts are suspended overhead, they never interfere with one another or the stations below. The manager has a strict infrastructure allowance of $B$ meters of total conveyor belting. The objective is to assign each station to a unique pad such that the sum of all installed belt lengths is at most $B$.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a required conveyor link between station $u$ and station $v$.

## Output
If a valid placement exists, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $i$-th integer is the pad number (from $1$ to $n$) assigned to station $i$. (These $n$ integers must form a permutation of the numbers from $1$ to $n$). 
If the allowance cannot be met, print `NO`.

## Example
**Input:**
```
5 4 6
1 2
1 3
1 4
1 5
```

**Output:**
```
YES
3 1 2 4 5
```
