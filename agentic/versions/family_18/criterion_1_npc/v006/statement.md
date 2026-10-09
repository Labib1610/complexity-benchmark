# Backbone Trenching for the Control Vault

Time limit: 5 s
Memory limit: 256 MB

## Description
A control vault requires $n$ modules to be installed along a single straight equipment trench. The trench contains exactly $n$ consecutive mounting bays, numbered $1$ to $n$. Each module must be assigned to exactly one bay, such that every bay contains exactly one module.

The modules exchange signals over $m$ point-to-point harnesses. Whenever two modules must exchange signals, a harness is run between their bays through the trench's cable tray. The length of each harness is exactly the absolute difference between the bay position numbers of the two modules it connects.

Procurement has fixed a total harness budget of $B$. The sum of the lengths of all $m$ required harnesses must not exceed this budget.

Determine if the modules can be assigned to the bays so that the total harness length stays within the budget. If possible, output a valid assignment; otherwise, report that no such assignment exists.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a harness must connect module $u$ and module $v$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ space-separated integers representing the bay positions (from $1$ to $n$) assigned to modules $1, 2, \dots, n$ respectively.
If no valid assignment exists, print `NO`.

## Example 1

### Input
```
4 3 4
1 2
2 3
3 4
```

### Output
```
YES
1 2 3 4
```

## Example 2

### Input
```
3 3 3
1 2
2 3
1 3
```

### Output
```
NO
```
