# Problem A — Compliance Audit Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

You are managing a network of **n** financial ledgers. Before any compliance check, all ledgers are cleared and have exactly zero audit marks.

You can purchase automated reconcilement procedures. Each procedure is hardwired to exactly two distinct ledgers, $u$ and $v$. When executed, the procedure simultaneously adds exactly one audit mark to ledger $u$ and one audit mark to ledger $v$. 

Once a procedure is purchased, it is permanently unlocked. You may execute your purchased procedures in any order, and you may execute the same procedure multiple times. 

A specific subset of **t** ledgers are designated as *regulated*. Your task is to purchase a subset of available procedures such that the following condition is satisfied: 
For *every* pair of distinct regulated ledgers $i$ and $j$, there must exist some sequence of executions of your purchased procedures that transitions the network from its cleared state (zero audit marks on all ledgers) to a target state where exactly ledger $i$ and ledger $j$ have an **odd** number of audit marks, and all other $n-2$ ledgers have an **even** number of audit marks. 

The specific sequence of executions may be different for each pair of regulated ledgers, but every sequence may only use procedures from the subset you purchased.

You are given a list of **m** available procedures, each with a one-time purchase cost **w**. Determine the minimum total cost of a subset of procedures that satisfies this requirement.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line lists **t** distinct integers representing the indices of the regulated ledgers (1-indexed).
The following **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1,000,000). These represent an available procedure wired to ledgers **u** and **v** that can be purchased for a cost of **w**. (Note that the order of $u$ and $v$ does not matter, as the procedure adds a mark to both simultaneously).
It is guaranteed that it is possible to satisfy the requirement using the available procedures.

## Output

Output a single integer representing the minimum total cost of a subset of procedures that allows reaching the required target states for all pairs of regulated ledgers.

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

In Example 1, the regulated ledgers are 1, 2, and 3. We must be able to reach three target states from the cleared state:
- Exactly ledgers 1 and 2 have an odd number of marks.
- Exactly ledgers 2 and 3 have an odd number of marks.
- Exactly ledgers 1 and 3 have an odd number of marks.

By purchasing the three procedures wired to (1, 4), (2, 4), and (3, 4) for a total cost of 1+1+1 = 3, we can satisfy the requirement. For instance, to reach the state where exactly 1 and 2 have an odd number of marks, we can execute the procedure (1, 4) and then the procedure (2, 4). Ledger 4 receives two marks (an even number), while ledgers 1 and 2 each receive one mark (an odd number). This is cheaper than purchasing the procedures (1, 2) and (2, 3) directly, which would cost 2+2=4.

In Example 3, there is only one regulated ledger. Because there are no pairs of distinct regulated ledgers, the requirement is vacuously satisfied. No procedures need to be purchased, resulting in a cost of 0.