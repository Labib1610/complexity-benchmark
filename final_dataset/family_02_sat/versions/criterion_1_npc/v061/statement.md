# Problem A — Fleet Routing and Promotions

Time limit: 2 s   Memory limit: 256 MB

## Description

A logistics company manages a fleet of $n$ delivery trucks. For the upcoming shift, the dispatcher must route each truck to either the upper corridor (represented by 1) or the lower corridor (represented by 0). Every truck must be assigned to exactly one of these two corridors.

The company has hired $m$ freelance photographers to gather promotional material. Each photographer is given a contract based on an itinerary of exactly three planned shots. A planned shot specifies a particular truck and the specific corridor it must be on.

To determine if a photographer's contract is honored, the company's automated auditing system evaluates the itinerary using the following procedure:
1. The system checks the first planned shot. If the specified truck is routed to the specified corridor, the contract is immediately marked as honored, and the system stops evaluating this photographer's itinerary.
2. If the first shot does not match the routing, the system checks the second planned shot. If this truck is on the specified corridor, the contract is marked as honored, and the system stops.
3. If the second shot also does not match, the system checks the third planned shot. If this truck is on the specified corridor, the contract is marked as honored.
4. If the system evaluates all three planned shots and none of them match the actual routing, the contract is considered breached.

A single truck may appear in the itineraries of multiple photographers, and different shots might require the same truck to be on different corridors. It is also possible for the same truck to appear more than once in a single itinerary.

You must determine whether there is a single, fleet-wide routing plan that ensures no contracts are breached. If such a routing exists, you must provide one valid plan.

## Input

The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines describes a photographer's itinerary using three non-zero signed integers $l_1$, $l_2$, $l_3$, with $|l_i| \le n$. 
The absolute value $|l_i|$ represents the truck's ID for that planned shot. A positive integer means the shot requires that truck to be routed to the upper corridor. A negative integer means the shot requires that truck to be routed to the lower corridor.

## Output

If no routing plan can honor all contracts, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being $0$ or $1$), where $s_i$ is the corridor assigned to truck $i$. If multiple valid routing plans exist, any of them will be accepted.

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
