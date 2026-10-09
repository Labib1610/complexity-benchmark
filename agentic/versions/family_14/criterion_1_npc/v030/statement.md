# Problem A — Ledger Reconciliation

Time limit: 5 s   Memory limit: 256 MB

## Description

A financial system consists of **n** separate ledgers (numbered 1 to **n**). You can contract auditors to reconcile specific pairs of ledgers. Executing a contract to reconcile a pair incurs a specific fee.

When two ledgers are reconciled, they share all their entries. This sharing propagates transitively: any two ledgers will share all their entries if there exists a sequence of ledgers starting at the first and ending at the second, where every adjacent pair in the sequence has been reconciled.

A specific subset of **t** ledgers are designated as **mandated**. You must choose a set of auditor contracts to execute so that every mandated ledger shares all its entries with every other mandated ledger. You may execute contracts involving non-mandated ledgers if it allows you to achieve this requirement for a lower total fee.

Determine the minimum total fee required to execute a valid set of auditor contracts.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the mandated ledgers.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): an available contract that reconciles ledger **u** and ledger **v** for a fee of **w**.
The available contracts are guaranteed to be sufficient to satisfy the requirement.

## Output

Print a single integer: the minimum total fee to execute a set of auditor contracts satisfying the requirement.

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

In Example 1, reconciling mandated ledgers 1, 2, and 3 with the non-mandated ledger 4 (fees 1+1+1 = 3) is cheaper than executing contracts to reconcile the three mandated ledgers directly with each other (which would incur a fee of 4). In Example 3, there is only one mandated ledger, so no contracts need to be executed.
