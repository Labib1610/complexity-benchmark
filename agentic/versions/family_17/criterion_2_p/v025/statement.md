# Thermal Equilibrium Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description
A quantum computing cluster requires precise thermal management. The system contains $q$ heat-producing logic cores, indexed sequentially from $1$ to $q$. It also contains an equal number of cryogenic dissipators, indexed sequentially from $q+1$ to $2q$.

To achieve thermal equilibrium, every single logic core must be exclusively linked to exactly one cryogenic dissipator, and every dissipator must be assigned to exactly one core. No core or dissipator may be left unlinked, nor can they be shared.

Because of quantum interference, a core can only be linked to a dissipator if that specific core-dissipator pair has been physically calibrated. You are provided with the list of $t$ calibrated pairs.

To prevent cascade failures and ensure physical viability, the cluster's engineering specifications guarantee the following structural properties for all provided calibrated pairs $(a, b)$ where $a$ is the core and $b$ is the dissipator:
- The spatial distance metric, defined as $D(a, b) = a + b$, will never exceed $3q$.
- The thermal flow gradient, defined as $G(a, b) = b - a$, is strictly positive.
- The total number of active components (cores and dissipators combined) is bounded by $200,000$.

Determine if there is a valid configuration that assigns every core to a distinct dissipator using only calibrated pairs. If such a configuration exists, you must provide it. Otherwise, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100,000$, $0 \le t \le 400,000$), representing the number of logic cores (which is also the number of dissipators) and the total number of calibrated pairs, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a calibrated pair between core $a$ and dissipator $b$.

## Output
If a full assignment is possible, print `YES`. Then, print $q$ lines, each containing the two integers $a$ and $b$ of a chosen pair in the assignment. If multiple valid assignments exist, you may output any of them.
If no such full assignment is possible, print `NO`.

## Example 1
### Input
```
3 4
1 4
2 5
3 6
2 4
```
### Output
```
YES
1 4
2 5
3 6
```

## Example 2
### Input
```
2 2
1 3
2 3
```
### Output
```
NO
```
