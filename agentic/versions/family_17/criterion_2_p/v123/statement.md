# Problem B — Synchronized Fleet Activation

Time limit: 2 s   Memory limit: 256 MB

## Description
During a routine drill, the directorate must deploy a fleet of $2q$ remote assets. These assets are assigned identification numbers from $1$ to $2q$. The deployment strategy relies on establishing secure communication links between specific assets. A link can only be established if it is explicitly listed in the pre-approved registry. 

Every entry in the registry specifies a potential link between a lower-indexed asset (with an ID from $1$ to $q$) and a higher-indexed asset (with an ID from $q+1$ to $2q$). The registry contains $t$ such potential links, and some assets may appear in multiple different entries. Due to the generation protocol, the registry is mathematically guaranteed to satisfy two structural properties:
1. The total number of times assets from the range $1$ to $q$ appear across all registry entries is exactly equal to the total number of times assets from the range $q+1$ to $2q$ appear.
2. For every potential link between asset $a$ and asset $b$, the sum of their identification numbers, $a + b$, is strictly greater than $q$ and does not exceed $3q$.

To achieve full operational capacity, the planners must activate a specific configuration of these registry entries. A configuration of active links is considered valid if and only if it satisfies all of the following strict requirements:
- Every single one of the $2q$ assets is involved in at least one active link.
- No asset is involved in more than one active link.
- The configuration consists of exactly $q$ active links.
- The sum of the identification numbers of the lower-indexed assets across all active links is exactly $q(q+1)/2$.

Determine if there is a valid configuration that fully deploys the fleet. If such a configuration exists, provide the list of active links. Otherwise, report that full deployment is impossible under the current registry.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), where $2q$ is the total number of assets and $t$ is the number of potential links in the registry.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a pre-approved link between asset $a$ and asset $b$.

## Output
If a valid configuration exists, output `YES` on the first line, followed by $q$ lines each containing the two integers of an activated link. If no such configuration is possible, output `NO`.

## Example

**Input**
```
3 4
1 4
2 5
3 5
3 6
```

**Output**
```
YES
1 4
2 5
3 6
```
