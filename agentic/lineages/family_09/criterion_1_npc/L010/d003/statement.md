# Problem A — Module Configuration Constraints

Time limit: 5 s   Memory limit: 256 MB

## Description

A software system consists of **n** modules (labeled 1 to **n**). You need to configure a deployment by turning on exactly **k** of these modules.

The architecture includes **m** exclusive hardware locks. Each lock monitors a specific pair of modules. During system startup, the diagnostic routine verifies every lock. If a lock registers that both of its monitored modules are active, it trips a collision fault. The configuration is safe if the diagnostic routine finishes with zero collision faults.

Determine whether you can turn on exactly **k** modules to achieve a safe configuration. If so, output one valid set of modules.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 46, 0 ≤ **m** ≤ **n**·(**n**−1)/2, 1 ≤ **k** ≤ **n**).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), specifying the two modules monitored by a hardware lock. No pair of modules is monitored by more than one lock.

## Output

If a safe configuration of exactly **k** modules is possible, print `YES` on the first line. On the second line, print the **k** distinct module labels that form this configuration, separated by spaces. If multiple safe configurations exist, you may print any one of them (in any order).

If no such configuration is possible, print `NO`.

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

In Example 2, turning on modules 1, 3, and 5 is safe because for the lock monitoring (1, 2), only module 1 is active, and for the lock monitoring (3, 4), only module 3 is active. No lock detects both of its monitored modules as being active. In Example 1, any combination of three modules will cause at least one lock to register both of its monitored modules as active, tripping a fault.