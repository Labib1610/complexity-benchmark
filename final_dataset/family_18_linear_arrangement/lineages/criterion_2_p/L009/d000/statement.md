# Assembly Track Layout

Time limit: 5 s   Memory limit: 256 MB

## Description
A manufacturing facility needs to install $n$ different processing modules into $n$ sequential bays along a single assembly track. Each bay can hold exactly one module, and the bays are numbered $1$ to $n$ in physical order.

There are $m$ physical conveyor belts that must be installed to transport materials between specific pairs of modules. The length of a conveyor belt connecting a module placed in bay $x$ and a module placed in bay $y$ is exactly $|x - y|$. The belts can overlap and bypass other modules without interference.

The facility has a maximum total belt allowance of $B$. You must assign each module to exactly one bay such that the sum of the lengths of all $m$ conveyor belts is at most $B$. 

The conveyor blueprint is guaranteed to be a minimally fully integrated design: there are exactly $m = n - 1$ belts, and it is possible for material to flow between any two modules (possibly passing through intermediate modules along consecutive belts) without any redundant alternative routes.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a conveyor belt required between module $u$ and module $v$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $i$-th integer is the bay number (from $1$ to $n$) assigned to module $i$. (These $n$ integers must form a permutation of the numbers from $1$ to $n$). 
If the budget cannot be met, print `NO`.

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
