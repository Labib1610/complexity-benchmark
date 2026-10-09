# Datacenter Activation

Time limit: 2 s   Memory limit: 256 MB

## Description

A computing facility houses $n$ server racks, indexed from 1 to $n$. The facility is equipped with $m = n - 1$ pre-wired bidirectional fiber-optic links. The infrastructure is fully interconnected, meaning that despite having only $n - 1$ links, every single rack in the facility can reach any other rack through a sequence of connections. Because the physical layout provides this full reachability with the minimum possible number of links, there is exactly one unique communication route between any given pair of racks.

A customer has rented a specific group of $t$ racks. Each fiber-optic link has a specific activation expense to power on. Your objective is to determine the minimum total activation expense of a subset of links that must be powered on so that every rented rack can exchange data with every other rented rack. Data can be routed through intermediate racks that the customer has not rented. Any link that is not required to maintain this mutual connectivity among the $t$ rented racks can be left powered off.

## Input

The first line provides three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line provides $t$ distinct integers, representing the indices of the rented racks.
The next $m$ lines each contain three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), indicating a pre-wired bidirectional link between rack $u$ and rack $v$ with an activation expense of $w$.

## Output

Output a single integer: the minimum total activation expense of the links that must be powered on to ensure all rented racks can communicate with each other.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```