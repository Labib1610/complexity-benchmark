# Phase 2: High-Priority Routing

Time limit: 2 s   Memory limit: 256 MB

## Description

A cybersecurity firm is upgrading a facility's hardware. This project is divided into three distinct phases:

**Phase 1: Facility Survey.** Engineers map out the available conduit segments between $n$ equipment rooms (numbered 1 to $n$). To minimize drilling, they identify exactly $n-1$ conduit segments such that there is exactly one continuous route of segments between any two rooms. 

**Phase 2: Cable Planning.** You are responsible for this phase. The client has designated $t$ specific rooms as high-priority. These high-priority rooms must all be able to exchange data with one another, either directly or by passing data through intermediate rooms. You are given the cost of installing fiber optic cable in each conduit segment. You must calculate the minimum possible total installation cost to achieve this connectivity.

**Phase 3: Procurement.** The finance department takes your calculated minimum cost, adds a 20% markup for price fluctuations, and approves the final budget.

Your task is to write a program that executes Phase 2. Given the network topology from Phase 1 and the list of high-priority rooms, output the exact minimum cost before any Phase 3 markups are applied.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line contains $t$ distinct integers: the identifiers of the high-priority rooms.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$): a conduit segment joining room $u$ and room $v$ at an installation cost of $w$. 
The segments provided in the input are guaranteed to satisfy the property established in Phase 1.

## Output

Print a single integer: the minimum total cost calculated in Phase 2.

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
