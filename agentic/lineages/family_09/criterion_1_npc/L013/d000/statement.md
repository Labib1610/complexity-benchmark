# Problem A — Stable Payload Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description

A software system contains **n** available modules, numbered 1 through **n**. Through automated integration testing, the system has identified **m** pairs of modules that exhibit a resource collision when loaded into the same environment.

Your objective is to assemble a stable deployment payload consisting of exactly **k** distinct modules. The system architecture guarantees that collisions are strictly pairwise; there are no complex, higher-order dependencies between three or more modules. Therefore, a payload is considered stable if and only if no two modules selected for the payload form one of the **m** identified colliding pairs.

Given the exact configuration of the **n** modules and the **m** colliding pairs, determine whether a stable payload of exactly **k** modules can be successfully assembled. If such a payload can be formed, you must also provide one valid selection of modules.

## Input

The first line of the input contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 46, 0 ≤ **m** ≤ **n**·(**n**−1)/2, 1 ≤ **k** ≤ **n**).
The next **m** lines each contain two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing a pair of modules that experience a resource collision.
The collision relationships are symmetric, and no colliding pair is listed more than once.

## Output

If a stable deployment payload of exactly **k** modules can be assembled, print `YES` on the first line. On the second line, print **k** distinct integers representing the module numbers in the payload, separated by spaces. If there are multiple valid payloads, any one will be accepted.

If no such payload can be assembled, print `NO`.

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
