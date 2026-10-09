# Freight Routing Operation

Time limit: 2 s
Memory limit: 256 MB

## Description

A logistics company operates a maritime shipping network connecting $n$ seaports via $m$ one-way shipping routes. 

During a shipping season, the network must obey strict intermediate handling rules. For any port—with the exception of a designated origin port and a designated destination port—the total number of containers arriving from incoming routes must perfectly match the total number of containers departing on outgoing routes. No containers may be temporarily held over, destroyed, or created at these intermediate locations.

Furthermore, the physical capacity of the routes is restricted by the fleet size. The network manifest specifies a certain number of cargo vessels allocated to each route. During the season, each vessel is capable of making exactly one voyage and transporting at most one container. Consequently, the total number of containers dispatched along any given route must be a non-negative integer that cannot be greater than the number of vessels assigned to it.

A special contract has been requested. It requires a net outbound shipment of exactly $d$ containers from the origin port $s$, and a net inbound shipment of exactly $d$ containers to the destination port $t$. 

Determine if there is a valid routing plan that fulfills the contract without violating the fleet limitations or the port storage restrictions. If such a plan exists, specify how many containers should be assigned to each route.

## Input

The first line contains three integers: $n$, $m$, and $1$ (indicating a single container type).
The second line contains three integers: $s$ (the origin port), $t$ (the destination port), and $d$ (the required number of containers).
The following $m$ lines each contain three integers $u$, $v$, and $cap$. These values indicate a one-way shipping route from port $u$ to port $v$ that has an allocated fleet of $cap$ vessels.

## Output

If the contract can be fulfilled, print `YES` on the first line. On the second line, output $m$ space-separated integers representing the number of containers transported on each route, in the identical order the routes were provided in the input.
If it is impossible to fulfill the contract under the given restrictions, print `NO`.

## Example

**Input:**
```
4 5 1
1 4 10
1 2 5
1 3 10
2 4 10
3 4 5
3 2 5
```

**Output:**
```
YES
5 5 5 5 0
```
