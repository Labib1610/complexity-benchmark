# Problem B — Fleet Deployment Roster

Time limit: 2 s   Memory limit: 256 MB

## Description
The central logistics division must organize a comprehensive fleet dispatch for an upcoming supply run. They have a roster of operators and an identical count of transport vehicles. Operators are assigned sequential identification badges starting at 1. Vehicles receive sequential identification numbers in the block immediately following the operators.

A strict safety protocol dictates that an operator may only pilot a vehicle if their specific combination is listed in the approved certification registry. An operator might be cleared for multiple vehicles, and a vehicle might be accessible to multiple operators.

The supply run requires that every single operator and every single vehicle be deployed simultaneously. A valid dispatch plan pairs each operator with exactly one vehicle they are certified for, ensuring no resource is left idle, none are omitted, and no vehicle is shared between multiple operators. You must determine if such a complete, one-to-one dispatch plan can be formed from the approved combinations, and if so, provide it. Otherwise, indicate that the requirements cannot be met.

The logistics hub operates with a minimum of 1 and a maximum capacity of 100000 operators per dispatch. The certification registry can store any non-negative number of approved pairings, up to a system limit of 400000 records.

## Input
First line: two integers $q$ and $t$, representing the total count of operators (which is also the number of vehicles) and the number of approved pairings, respectively. The valid ranges for $q$ and $t$ correspond exactly to the minimums and maximum capacities of the logistics hub and registry described previously.
Next $t$ lines: two integers $a$ and $b$, representing an approved pairing. The integer $a$ is guaranteed to be a valid operator badge number, and $b$ is guaranteed to be a valid vehicle identification number.

## Output
If a complete dispatch plan is possible, print `YES` followed by $q$ lines, each containing the two ID numbers of one selected pairing from the plan. Otherwise, print `NO`.

## Example

**Input:**
```
3 5
1 4
1 5
2 4
2 6
3 5
```

**Output:**
```
YES
1 4
3 5
2 6
```
