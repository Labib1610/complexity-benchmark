# Fault-Tolerant Flag Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

A server cluster relies on **n** configuration flags. Each flag must be explicitly initialized to either 1 or 0; there are no floating states. 

During deployment, the system's integrity is verified by **m** independent validation modules. Each module is designed with triple redundancy: it monitors exactly three flag conditions. A condition specifies a required state (1 or 0) for a specific flag. 

To ensure high availability, a module will pass its check if **at least one** of its three monitored conditions evaluates to true. The states of the other two flags in the module's scope are ignored once a single condition is met. A module only fails if all three of its conditions are simultaneously violated. Because satisfying any individual module is trivial—requiring only one correct flag out of three—the system's constraints are extremely flexible at a local level. 

However, flags are shared across modules, sometimes with conflicting required states (e.g., demanded to be 1 by one module and 0 by another). Your task is to determine whether this localized flexibility extends globally. Decide if there is a single, system-wide assignment of all **n** flags that allows **every** validation module to pass simultaneously. If such an assignment exists, output it. 

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the following m lines describes a validation module and contains three non-zero signed integers l₁, l₂, l₃, with |lᵢ| ≤ n. 
The absolute value |lᵢ| represents the flag index (from 1 to n). If lᵢ is positive, the condition is satisfied when flag |lᵢ| is set to 1. If lᵢ is negative, the condition is satisfied when flag |lᵢ| is set to 0.

## Output
If there is no way to set the flags to make all modules pass, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print n integers s₁ s₂ … sₙ (where each sᵢ ∈ {0, 1}), representing the state of each flag from 1 to n. Any valid assignment is accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each validation module specifies exactly three conditions. It is possible for the same flag index to be specified more than once within the same module's conditions.
