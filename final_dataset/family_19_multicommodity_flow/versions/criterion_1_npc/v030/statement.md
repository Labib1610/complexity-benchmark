# Problem A — Concurrent Freight Dispatch

Time limit: 5 s   Memory limit: 256 MB

## Description
A logistics operator manages $n$ facilities and $m$ one-way transport connections between specific pairs of facilities. Each connection has a strict upper limit on the total number of pallets it can carry during a shift, dictated by available vehicle space. 

During a shift, $k$ client requests must be fulfilled. Each request mandates moving a precise number of intact pallets from a designated starting facility to a designated ending facility. 

The movement of pallets must strictly adhere to the following operational rules:
- Pallets are indivisible. The number of pallets assigned to any connection for any request must be a non-negative integer.
- All requests share the same transport connections. For any single connection, the sum of pallets across all requests utilizing it cannot exceed that connection's upper limit.
- For any facility that is neither the starting nor ending point for a specific request, the total number of pallets for that request arriving at the facility must exactly equal the total number departing from it.
- At the starting facility for a request, the number of departing pallets minus the number of arriving pallets for that request must exactly equal the requested quantity.
- At the ending facility for a request, the number of arriving pallets minus the number of departing pallets for that request must exactly equal the requested quantity.

Determine a valid assignment of pallets to connections that fulfills all $k$ requests simultaneously without exceeding any connection's limit, or determine that it is impossible to fulfill all requests in a single shift.

## Input
The first line contains three integers $n$, $m$, and $k$: the number of facilities, the number of transport connections, and the number of client requests.
The following $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the starting facility, the ending facility, and the required number of pallets for the $i$-th request.
The next $m$ lines each contain three integers $u$, $v$, and $c$, indicating a one-way transport connection from facility $u$ to facility $v$ with a maximum limit of $c$ pallets.

## Output
If it is possible to fulfill all requests, output `YES` on the first line. Then, output $k$ lines. The $i$-th of these lines should contain $m$ integers, representing the number of pallets for the $i$-th request assigned to each of the $m$ connections, in the exact order the connections were given in the input.
If it is impossible, output `NO`.

## Example

### Input
```text
4 5 2
1 4 2
2 3 1
1 2 2
2 3 2
3 4 2
1 3 1
2 4 1
```

### Output
```text
YES
1 0 1 1 1
0 1 0 0 0
```
