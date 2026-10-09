# Cargo Routing Logistics

Time limit: 2 s   Memory limit: 256 MB

## Description

You are managing the logistics for $n$ distinct cargo shipments. Each shipment must be directed through exactly one of two available transit corridors: the Northern route (represented by 1) or the Southern route (represented by 0).

To comply with international trade regulations, your routing plan must adhere to a set of $m$ customs mandates. Every mandate provides a list of three acceptable routing decisions. As long as your overall plan includes at least one of the three decisions listed in a mandate, that mandate is considered cleared. 

A routing decision is encoded as a non-zero integer $d$:
- A positive value of $d$ means shipment $d$ goes via the Northern route (1).
- A negative value of $d$ means shipment $|d|$ goes via the Southern route (0).

You must establish a comprehensive routing plan for all $n$ shipments that clears all $m$ customs mandates simultaneously. If the mandates contradict each other such that no comprehensive plan is possible, you must reject the batch.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$), the number of shipments and the number of customs mandates.
Each of the next $m$ lines contains three non-zero integers $p_1, p_2, p_3$ ($|p_i| \le n$), representing the three acceptable routing decisions for that mandate. A single mandate might list the same shipment more than once.

## Output
If no valid routing plan can clear all mandates, output a single line with the word `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer is 1 if shipment $i$ takes the Northern route, and 0 if it takes the Southern route. Any fully compliant plan is acceptable.

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
