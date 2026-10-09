# Project: Equilibrium

Time limit: 2 s   Memory limit: 256 MB

## Description

You are evaluating a communication network consisting of $R$ outposts. The network is built using $S$ bidirectional transmission links, each connecting a specific pair of outposts. The infrastructure is fully integrated: a message can be routed between any two outposts using a sequence of links, and the total number of links $S$ is exactly $R - 1$.

A new security protocol requires you to upgrade a subset of the outposts. You must upgrade a specific roster of $P$ mandated outposts, and you have the discretion to upgrade any additional outposts.

The subset of upgraded outposts must satisfy a strict structural invariant known as the *Redundancy Index*. The Index is calculated as follows: count the total number of upgraded outposts, and then subtract the number of *internal links*. An internal link is defined as any transmission link where **both** of its endpoint outposts are upgraded. For the protocol to be satisfied, the Redundancy Index of your chosen subset must be exactly 1.

Upgrading outposts incurs costs based on the internal links. Each transmission link has a characteristic penalty $w$. If a link becomes an internal link (because both its endpoints are upgraded), its penalty $w$ is added to your total upgrade cost. Links where one or neither endpoint is upgraded remain dormant and contribute 0 to the cost.

Your objective is to determine the minimum possible total upgrade cost of the internal links such that all $P$ mandated outposts are upgraded and the Redundancy Index of the upgraded subset is exactly 1.

## Input

The first line contains three integers $R$, $S$, and $P$. 
The total number of outposts $R$ satisfies $1 \le R \le 200000$. 
The number of transmission links $S$ is always exactly $R - 1$. 
The number of mandated outposts $P$ satisfies $1 \le P \le R$.

The second line contains $P$ distinct integers representing the identifiers of the mandated outposts.

Each of the following $S$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le R$, $u \neq v$). This specifies a transmission link between outpost $u$ and outpost $v$ with a characteristic penalty of $w$ ($1 \le w \le 1000000$). 

## Output

Output a single integer representing the minimum possible total upgrade cost of the internal links under the given conditions.

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