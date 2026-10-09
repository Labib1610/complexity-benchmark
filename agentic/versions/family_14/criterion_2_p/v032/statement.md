# Problem B — Critical Module Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description

A distributed system consists of **n** processing modules, numbered 1 to **n**. You are provided a list of **m** bidirectional synchronization links that can be activated. Each link joins two specific modules and requires a certain amount of energy to remain active.

Among the **n** modules, a specific subset of **t** modules are designated as *critical*. You must choose a subset of the **m** links to activate such that every critical module can communicate with every other critical module. Two modules can communicate if they are joined by an active link, or if they can relay through a sequence of active links (which may pass through critical or non-critical modules).

Because each link can independently be toggled active or inactive, there are $2^m$ possible activation states for the network. The search space of possible configurations grows rapidly as the number of links increases. Your objective is to find a valid activation state that minimizes the sum of the energy costs of the active links.

The system's hardware is wired such that there are exactly **m = n - 1** total links available to choose from. Furthermore, the wiring ensures that if all **m** links were activated, there would be exactly one sequence of distinct links connecting any given pair of modules in the system.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the critical modules.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): indicating that a link exists between module **u** and module **v**, and it costs **w** energy to activate.

## Output

Print a single integer: the minimum total energy cost of an activation state that allows all critical modules to communicate.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```
