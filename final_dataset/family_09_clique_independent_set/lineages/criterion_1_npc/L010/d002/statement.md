# Problem A — Module Configuration Constraints

Time limit: 5 s   Memory limit: 256 MB

## Description

A software system consists of **n** modules (labeled 1 to **n**). You are evaluating the system for a specific deployment that requires activating exactly **k** modules.

The modules share various exclusive hardware resources. You are given a list of **m** resource-sharing constraints. Each constraint identifies two distinct modules that require the same exclusive resource.

A deployment is considered safe if it avoids all resource collisions. This means that for every one of the **m** constraints, your chosen set of **k** modules must include at most one of the two modules identified by that constraint (it is also acceptable if neither module is included).

Determine if there is a safe deployment of exactly **k** modules. If such a deployment is possible, you must identify one valid set of modules to activate.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 46, 0 ≤ **m** ≤ **n**·(**n**−1)/2, 1 ≤ **k** ≤ **n**).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing a resource-sharing constraint between module **u** and module **v**. No constraint is listed more than once.

## Output

If a safe deployment of exactly **k** modules can be formed, output `YES` on the first line. On the second line, output the **k** distinct module labels that make up this deployment, separated by spaces. If multiple valid deployments exist, print any one of them (in any order).

If no such deployment can be formed, output `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```

## Note

In Example 2, checking the constraints shows that a deployment of modules 1, 3, and 5 includes at most one module from the constraint (1, 2) and at most one from (3, 4). Thus, it is safe. In Example 1, any selection of three modules will include both modules from at least one constraint, so no safe deployment of size 3 exists.