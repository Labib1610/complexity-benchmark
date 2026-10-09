# Problem B — Cloud Resource Allocation

Time limit: 2 s   Memory limit: 256 MB

## Description

A cloud computing platform is managing **k** user accounts, **k** virtual machines (VMs), and **k** physical servers. The accounts are labeled 1 to **k**, the VMs 1 to **k**, and the servers 1 to **k**.

Each user account is permanently bound to exactly one unique VM, and no two accounts share the same VM. The platform has generated a list of acceptable deployment configurations. Each configuration specifies a user account, its bound VM, and a physical server where it can be hosted.

The platform must activate exactly **k** of these configurations. A valid activation must deploy every user account, every VM, and every physical server exactly once. 

To ensure system stability, the load balancer guarantees two structural properties about the provided list of configurations:
1. No single physical server is listed in more than **k** configurations.
2. The aggregate sum of the physical server IDs across all provided configurations will never exceed **k³**.

Determine whether a valid activation of **k** configurations is possible, and if so, report one such valid set of configurations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of user accounts (which also equals the number of VMs and physical servers) and the number of acceptable configurations.

Each of the next **t** lines contains three integers **a**, **v**, **s** (1 ≤ a, v, s ≤ k), representing an acceptable configuration of an account, a VM, and a server. No configuration is listed more than once. Because each account is strictly bound to one unique VM, every configuration involving a given account will always list the same VM, and different accounts will always be listed with different VMs.

## Output

If a valid activation of **k** configurations exists, print `YES` on the first line, then print **k** lines, each containing the three integers `a v s` of one chosen configuration (in any order). Any valid activation is accepted.

If no valid activation exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```
