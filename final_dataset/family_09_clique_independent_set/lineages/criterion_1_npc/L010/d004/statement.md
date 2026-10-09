# Problem A — Network Asymmetry Stability

Time limit: 5 s   Memory limit: 256 MB

## Description

A software system consists of **n** modules (labeled 1 to **n**). You need to configure a deployment by upgrading exactly **k** of these modules. Modules that are not upgraded remain in their standard state.

The system architecture includes **m** critical links. Each link connects a specific pair of modules. 
For any module, its *link capacity* is a fixed value defined as the total number of critical links connected to it in the architecture.

When a link connects one upgraded module and one standard module, it operates in an *asymmetric* state. Links connecting two upgraded modules, or two standard modules, operate in a *symmetric* state.

To ensure system stability, the configuration must satisfy a strict load-balancing equation: the total number of links operating in an asymmetric state must be exactly equal to the sum of the link capacities of all upgraded modules.

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

In Example 2, upgrading modules 1, 3, and 5 yields a stable configuration. The upgraded modules have link capacities of 1, 1, and 0 respectively, summing to 2. The link between 1 and 2 is asymmetric (module 1 is upgraded, 2 is standard), and the link between 3 and 4 is asymmetric (module 3 is upgraded, 4 is standard). The total number of asymmetric links is 2, which exactly matches the sum of the capacities. 

In Example 1, any combination of three modules will result in a total number of asymmetric links strictly less than the sum of the link capacities of the chosen modules, failing the stability condition.