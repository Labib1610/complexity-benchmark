# Problem A — Database Flag Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

You are managing a legacy database system containing **n** configuration flags. All flags are initially set to `FALSE`.

You can purchase synchronization scripts to manipulate these flags. Each script is hardwired to exactly two distinct flags, $u$ and $v$. When executed, the script simultaneously toggles the boolean state of both flag $u$ and flag $v$ (changing `FALSE` to `TRUE`, or `TRUE` to `FALSE`). 

Once a script is purchased, it is permanently unlocked. You may execute your purchased scripts in any order, and you may execute the same script multiple times. 

A specific subset of **t** flags are designated as *critical*. Your task is to purchase a subset of available scripts such that the following condition is satisfied: 
For *every* pair of distinct critical flags $i$ and $j$, there must exist some sequence of executions of your purchased scripts that transitions the database from its initial state (all flags `FALSE`) to a target state where exactly flag $i$ and flag $j$ are `TRUE`, and all other $n-2$ flags are `FALSE`. 

The specific sequence of executions may be different for each pair of critical flags, but every sequence may only use scripts from the subset you purchased.

You are given a list of **m** available scripts, each with a one-time purchase cost **w**. Determine the minimum total cost of a subset of scripts that satisfies this requirement.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line lists **t** distinct integers representing the indices of the critical flags (1-indexed).
The following **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1,000,000). These represent an available script wired to flags **u** and **v** that can be purchased for a cost of **w**. (Note that the order of $u$ and $v$ does not matter, as the script toggles both simultaneously).
It is guaranteed that it is possible to satisfy the requirement using the available scripts.

## Output

Output a single integer representing the minimum total cost of a subset of scripts that allows reaching the required target states for all pairs of critical flags.

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

In Example 1, the critical flags are 1, 2, and 3. We must be able to reach three target states:
- Exactly 1 and 2 are `TRUE`
- Exactly 2 and 3 are `TRUE`
- Exactly 1 and 3 are `TRUE`

By purchasing the three scripts wired to (1, 4), (2, 4), and (3, 4) for a total cost of 1+1+1 = 3, we can satisfy the requirement. For instance, to reach the state where exactly 1 and 2 are `TRUE`, we can execute the script (1, 4) and then the script (2, 4). Flag 4 is toggled twice (returning to `FALSE`), while flags 1 and 2 are each toggled once (becoming `TRUE`). This is cheaper than purchasing the scripts (1, 2) and (2, 3) directly, which would cost 2+2=4.

In Example 3, there is only one critical flag. Because there are no pairs of distinct critical flags, the requirement is vacuously satisfied. No scripts need to be purchased, resulting in a cost of 0.