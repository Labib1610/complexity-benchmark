# Problem A — Cohesive Enclaves

Time limit: 5 s
Memory limit: 256 MB

## Description

You are configuring a network of **n** microservices, identified by integers from 1 to **n**. You can provision data bridges between specific pairs of microservices. There are **m** possible bridges available. Provisioning a bridge between microservice **u** and microservice **v** incurs a one-time licensing cost of **w**. Bridges operate symmetrically.

A subset of microservices **S** is defined as a *cohesive enclave* if it cannot be split into two isolated halves. Formally, for every possible way to partition **S** into two non-empty disjoint sets **X** and **Y** (such that **X** ∪ **Y** = **S**), there must be at least one provisioned bridge that connects a microservice in **X** to a microservice in **Y**.

A new compliance framework requires that a designated group of **t** *audit-critical* microservices must all reside within the same cohesive enclave.

You may include any number of other non-critical microservices in this enclave if provisioning bridges to them helps reduce the overall cost. Your task is to select a set of bridges to provision such that there exists at least one cohesive enclave containing all **t** audit-critical microservices, while keeping the total licensing cost of the provisioned bridges to the absolute minimum.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).  
The second line lists **t** distinct integers representing the identifiers of the audit-critical microservices.  
Following this, there are **m** lines. Each line provides three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), indicating that a bridge can be provisioned between microservice **u** and microservice **v** for a licensing cost of **w**.  
It is guaranteed that the available bridges provide at least one valid way to form a cohesive enclave containing all audit-critical microservices.

## Output

Output a single integer representing the minimum possible total licensing cost required to satisfy the compliance framework.

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

In Example 1, provisioning the bridges between microservice 4 and microservices 1, 2, and 3 requires a total cost of 1 + 1 + 1 = 3. The subset **S** = {1, 2, 3, 4} forms a cohesive enclave. For instance, if we partition **S** into **X** = {1, 2} and **Y** = {3, 4}, the provisioned bridge between 2 and 4 connects **X** and **Y**. Any valid partition of **S** will have at least one provisioned bridge crossing between its two sets. This enclave successfully contains the critical microservices 1, 2, and 3. Utilizing microservice 4 in the enclave is more cost-effective than provisioning bridges exclusively among the critical microservices, which would incur a cost of at least 4.

In Example 3, only one microservice is designated as audit-critical. A subset consisting of just this single microservice (**S** = {1}) vacuously satisfies the condition for a cohesive enclave, because it is impossible to partition a one-element set into two non-empty sets. Thus, zero bridges need to be provisioned, resulting in a cost of 0.