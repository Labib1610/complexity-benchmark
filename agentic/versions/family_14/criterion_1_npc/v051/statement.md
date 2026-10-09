# Problem A — Universal Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description

The galactic council is attempting to establish a unified diplomatic channel among a specific group of **t** foundational civilizations. In total, there are **n** known civilizations in the galaxy (numbered 1 through **n**). 

Communication between different civilizations is difficult. However, there are known translation interfaces between certain pairs of civilizations. Activating a translation interface requires a specific computational cost. Once an interface is activated, messages can be seamlessly translated back and forth between those two civilizations. Furthermore, these translations can be chained: if interfaces are active between A and B, and between B and C, then A and C can communicate.

The council's goal is strictly to ensure that all **t** foundational civilizations can understand each other. They do not care whether the remaining civilizations are integrated, but they are perfectly willing to route communications through them if activating their translation interfaces results in a lower overall computational cost. An activated interface can handle unlimited messages, so an intermediate civilization can serve as a translation hub for multiple foundational civilizations simultaneously without incurring any additional cost beyond the initial activation of its interfaces.

Determine the absolute minimum total computational cost required to activate a set of translation interfaces such that every foundational civilization can communicate with all other foundational civilizations.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).
The second line contains **t** distinct integers: the identifiers of the foundational civilizations.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), representing a translation interface between civilization **u** and civilization **v** with an activation cost of **w**.
It is guaranteed that the provided interfaces are sufficient to connect all foundational civilizations.

## Output

Print a single integer: the minimum total cost to ensure all foundational civilizations can communicate.

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

In Example 1, routing the translations through civilization 4 (which costs 1+1+1 = 3) is cheaper than integrating the three foundational civilizations using only their direct interfaces (which would cost 4). In Example 3, there is only one foundational civilization, so no interfaces need to be activated.
