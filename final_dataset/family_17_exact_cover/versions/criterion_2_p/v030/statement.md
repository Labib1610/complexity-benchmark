# Orbital Asset Integration

Time limit: 2 s   Memory limit: 256 MB

## Description
The fleet needs to execute a fleet-wide deployment using $2q$ distinct orbital assets. These assets are uniquely identified by integers from 1 to $2q$.

A deployment consists of establishing secure linkages between assets. Each linkage integrates exactly two assets. However, assets cannot be linked arbitrarily. A linkage is only viable if it appears in the telemetry clearance registry, which specifies $t$ cleared configurations. A strict hardware standard ensures that every cleared configuration in this registry pairs an asset whose identifier is at most $q$ with an asset whose identifier is strictly greater than $q$.

The strategic command mandates a comprehensive deployment. This means you must select a set of viable linkages such that every single asset from 1 to $2q$ is incorporated into exactly one selected linkage. No asset can be left dormant, and no asset can be assigned to multiple linkages.

Determine whether it is possible to achieve this comprehensive deployment using only the cleared configurations. If it is possible, provide the selected linkages; otherwise, indicate that it cannot be done.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing half the total number of assets and the number of cleared configurations, respectively.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a cleared configuration between asset $a$ and asset $b$.

## Output
If a comprehensive deployment is possible, print `YES` on the first line. Then, print $q$ lines, each containing the two asset identifiers of a selected linkage. If it is not possible, print `NO`.

## Example

**Input**
```text
3 5
1 4
1 5
2 5
3 5
3 6
```

**Output**
```text
YES
1 4
2 5
3 6
```
