# Phase 2: Critical Vault Integration

Time limit: 2 s   Memory limit: 256 MB

## Description

A cybersecurity firm is isolating a facility's hardware. This project is divided into three distinct phases:

**Phase 1: Facility Survey.** Engineers map out $S$ available bidirectional access tunnels between $R$ server vaults (numbered 1 to $R$). The engineers verify that these mapped tunnels connect all $R$ vaults with exactly zero redundancy: between any two vaults, there is exactly one valid sequence of tunnels that routes between them.

**Phase 2: Quarantine Planning.** You are responsible for this phase. The client has detected security anomalies in $P$ specific vaults, designating them as compromised. These $P$ compromised vaults must all be able to exchange diagnostic data with one another, either directly or by relaying data through a sequence of intermediate (uncompromised) vaults. You are given the activation cost for each mapped tunnel. You must choose a subset of the available tunnels to activate such that the compromised vaults are all interconnected. Calculate the minimum possible total activation cost to achieve this requirement.

**Phase 3: Procurement.** The finance department takes your calculated minimum cost, adds a 20% markup for price fluctuations, and approves the final budget.

Your task is to write a program that executes Phase 2. Given the survey data from Phase 1 and the list of compromised vaults, output the exact minimum cost before any Phase 3 markups are applied.

## Input

The first line contains three integers $R$, $S$, and $P$ ($1 \le P \le R \le 200000$). The number of tunnels $S$ is always exactly $R - 1$.
The second line contains $P$ distinct integers: the identifiers of the compromised vaults.
Each of the next $S$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le R$, $u \neq v$, $1 \le w \le 1000000$): a tunnel joining vault $u$ and vault $v$ with an activation cost of $w$. 
The tunnels provided in the input are guaranteed to connect all $R$ vaults such that for every pair of vaults, there is exactly one unique sequence of tunnels connecting them.

## Output

Print a single integer: the minimum total activation cost calculated in Phase 2.

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