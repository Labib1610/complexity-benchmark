# Problem B — Component Activation

Time limit: 2 s
Memory limit: 256 MB

## Description

You are in charge of bringing a distributed sensor array online. The array contains **n** modules, indexed from 1 to **n**. The system requires exactly **k** modules to be powered on to reach its operational threshold.

Some modules cannot be active at the same time due to destructive resonance. You have a diagnostic report detailing **m** pairs of modules that will resonate destructively if both are powered on. An acceptable configuration must strictly avoid activating any two modules that appear together in this report.

The physical architecture of the array divides all modules into several containment zones. Destructive resonance can occur both between modules in different zones and between modules located in the same zone. However, the system guarantees a global structural property regarding these resonances: any sequence of resonance links that forms a simple cycle (a closed loop that starts and ends at the same module without revisiting any other module) will always contain an even number of links.

You must establish whether a safe configuration of exactly **k** modules exists and, if so, identify one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n), representing the number of modules, the number of resonance links, and the target number of modules to power on.

Each of the following **m** lines provides two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), meaning that module **u** and module **v** will resonate destructively. No pair is repeated. All resonance links strictly comply with the structural property described above.

## Output

If a safe configuration of exactly **k** modules is possible, print `YES` on the first line. On the second line, print **k** distinct integers separated by spaces, denoting the modules to power on. If multiple such configurations exist, you may output any single one.

If no such configuration is possible, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```