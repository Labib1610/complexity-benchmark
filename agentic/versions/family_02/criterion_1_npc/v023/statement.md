# Problem A — Warehouse Climate Control

Time limit: 2 s   Memory limit: 256 MB

## Description

A logistics company operates a warehouse with **n** distinct storage zones. The facility manager must assign a permanent temperature setting to each zone before the upcoming season. Every zone must be explicitly configured to either Ambient (represented by 0) or Refrigerated (represented by 1). No zone can be left unconfigured, and there are no intermediate temperature states.

The warehouse is scheduled to receive **m** cargo batches. Quality assurance audits have produced a strict set of safety rules for these batches. Each rule corresponds to a specific batch and lists exactly three acceptable configuration conditions. A condition specifies a zone and the required temperature setting for that zone. For a batch to be stored safely, **at least one** of its three listed conditions must be satisfied by the warehouse's global configuration. A rule is considered met if one, two, or all three of its conditions are satisfied; it imposes no further restrictions. A rule is violated only if none of its three conditions are met.

The same storage zone may be referenced across multiple rules. Different batches might demand conflicting settings for the same zone, and the rules may overlap significantly. Your task is to determine whether there exists a single, comprehensive configuration of all **n** zones that simultaneously satisfies the safety rules for all **m** batches. If such a configuration exists, you must provide it. If it is impossible to satisfy all rules concurrently, the requirements are over-constrained.

## Input

The first line of the input contains two integers **n** and **m**.
A warehouse must have at least one storage zone. The facility's maximum capacity is limited by its blueprint, which allocates exactly one zone for every two-digit positive integer in base 10, thus implicitly setting the upper bound for **n**.
The batch processing system has a memory limit of exactly 20 pages, where each page holds exactly 20 batch records. The number of batches **m** is non-negative and is at most the total batch capacity of this memory.

Each of the following **m** lines corresponds to a cargo batch and contains three non-zero signed integers $l_1$, $l_2$, and $l_3$. Each integer $l_i$ represents a condition:
- The absolute value $|l_i|$ indicates the storage zone index, which is guaranteed to be a valid zone number from the first zone up to zone **n**.
- A positive value means the condition is satisfied if the corresponding zone is configured as Refrigerated (1).
- A negative value means the condition is satisfied if the corresponding zone is configured as Ambient (0).

At least one of the three conditions on each line must hold for the configuration to be valid.

## Output

If no valid configuration exists that satisfies all **m** batches simultaneously, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print **n** space-separated integers $s_1, s_2, \dots, s_n$ (each being either `0` or `1`), where $s_i$ is the configuration of storage zone $i$ (0 for Ambient, 1 for Refrigerated). If multiple valid configurations exist, any of them will be accepted.

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
Each safety rule specifies exactly three conditions. The same storage zone index may appear more than once within the same rule.
