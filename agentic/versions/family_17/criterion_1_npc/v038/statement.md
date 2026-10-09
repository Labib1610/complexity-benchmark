# Problem A — Module Synchronization Schedule

Time limit: 5 s
Memory limit: 256 MB

## Description
A software architecture consists of a set of modules numbered sequentially from $1$ to $3q$. To ensure stable deployment, all modules must be synchronized. 

Synchronization is executed by activating predefined integration scripts. Each script strictly coordinates a specific combination of three modules. The vendor provides a catalog of $t$ tested scripts. You may only use scripts from this catalog. 

Your objective is to activate a subset of the available scripts such that every module in the system is synchronized exactly once. If a module is synchronized more than once, it will cause state corruption. If a module is never synchronized, the system remains unstable. 

Thus, you must choose a subset of the tested scripts such that their module lists collectively include every integer from $1$ to $3q$ exactly once. As an inherent property of the system's numbering scheme, the sum of the module numbers in any single tested script is strictly less than $9q$.

If such an activation plan is possible, you must output `YES` followed by the chosen scripts. If no such plan can be formed from the catalog, output `NO`.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the following $t$ lines describes one available script by listing its three module numbers, $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$).

## Output
If a valid selection exists, print `YES` on the first line. Then, print $q$ lines, each containing the three module numbers of a chosen script. 
If no valid selection exists, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
