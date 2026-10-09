# Problem A — Network Redundancy Stability

Time limit: 5 s   Memory limit: 256 MB

## Description

A software system consists of **n** modules (labeled 1 to **n**). You need to configure a deployment by upgrading exactly **k** of these modules. Modules that are not upgraded remain in their standard state.

The system architecture includes **m** critical links. Each link connects a specific pair of modules. 
For any module, its *link capacity* is a fixed value defined as the total number of critical links connected to it in the architecture.

To ensure system stability, the configuration must satisfy a strict structural equation focused on the non-upgraded modules: the number of critical links connecting two standard modules must be exactly equal to the sum of the link capacities of all standard modules, minus the total number of critical links in the entire system (**m**).

Determine whether you can upgrade exactly **k** modules to achieve a stable configuration. If so, output one valid set of upgraded modules.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 46, 0 ≤ **m** ≤ **n**·(**n**−1)/2, 1 ≤ **k** ≤ **n**).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), specifying the two modules connected by a critical link. No pair of modules is connected by more than one link.

## Output

If a stable configuration of exactly **k** modules is possible, print `YES` on the first line. On the second line, print the **k** distinct module labels that form this configuration, separated by spaces. If multiple stable configurations exist, you may print any one of them (in any order).

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

In Example 2, upgrading modules 1, 3, and 5 yields a stable configuration, leaving modules 2 and 4 in their standard state. The standard modules have link capacities of 1 and 1 respectively, summing to 2. The total number of critical links in the system is 2. The number of critical links connecting two standard modules is 0 (since 2 and 4 are not connected). The stability equation holds because 0 equals 2 minus 2.

In Example 1, any combination of three upgraded modules leaves exactly one module in its standard state. Since it is impossible for a single module to have a link connecting to another standard module, the left side of the equation is always 0. However, the link capacity of any single module is at most 3. Subtracting the total number of critical links (4) yields a strictly negative number, failing the stability condition.