# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
During a comprehensive drill, the directorate must deploy its entire remote segment. The assets are divided into two identically sized fleets: controllers and platforms. Controllers are assigned consecutive badge numbers starting from one. Platforms are assigned consecutive badge numbers starting immediately after the highest-numbered controller.

To ensure safe operation, a controller may only operate a platform if their specific combination has been explicitly verified and recorded in the certification log. The certification log may contain many overlapping entries, but only these verified pairings are permitted.

Your task is to formulate a complete deployment roster. A valid roster must activate a set of verified pairings such that every single controller and every single platform is deployed exactly once. No asset may be left idle, and no asset may participate in more than one pairing. If such a comprehensive one-to-one deployment is possible, you must provide it. Otherwise, you must indicate that a full deployment cannot be achieved.

## Input
The first line contains two integers $q$ and $t$, representing the controller fleet size and the length of the certification log, respectively. The controller fleet size is at least one, but never exceeds the regulatory cap of one hundred thousand. The log may be empty, but is restricted by the testing facility's storage limit of four hundred thousand records.

The next $t$ lines each contain two integers $a$ and $b$, denoting a verified pairing. The value $a$ is a valid controller badge (ranging from one up to the controller fleet size), and $b$ is a valid platform badge (ranging from one strictly greater than the controller fleet size, up to exactly twice the controller fleet size).

## Output
If a complete deployment roster is possible, print `YES` followed by $q$ lines, each containing the two badge numbers of an activated pairing. If no such roster exists, print `NO`.

## Example

**Input**
```text
3 4
1 4
2 5
3 6
2 6
```

**Output**
```text
YES
1 4
2 5
3 6
```
