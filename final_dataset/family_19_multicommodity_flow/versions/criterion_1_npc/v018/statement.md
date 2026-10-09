# Problem A — Concurrent Freight Dispatch over a Shared Corridor Grid

Time limit: 5 s
Memory limit: 256 MB

## Description
A national distributor maintains $m$ one-way haulage lanes connecting $n$ hubs. Every lane is assigned a strict maximum container load per dispatch cycle due to rolling stock availability.

During operations, discrete containers of various products move through this network. The movement of these containers is subject to strict continuity: for any specific product, the number of its containers arriving at an intermediate hub must perfectly match the number of its containers departing from that hub. Furthermore, containers are indivisible units, meaning the transport of any product along a lane must consist of a non-negative whole number of containers.

Crucially, all products share the infrastructure. If multiple different products are routed through the same lane, their combined container count must not exceed the lane's maximum load.

In the upcoming dispatch cycle, there are $k$ distinct products that require transportation. Each product has a designated starting facility, a receiving facility, and a firm quantity of containers that must be delivered in full. At a product's starting facility, the net outflow (containers departing minus containers arriving) of that product must exactly equal its required quantity. At its receiving facility, the net inflow (containers arriving minus containers departing) must equal this same quantity. 

Your task is to provide a comprehensive dispatch plan that delivers every product's full quantity while strictly observing the shared lane loads, or to determine that the network cannot support all products concurrently in one cycle.

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of hubs, haulage lanes, and distinct products.
The next $k$ lines specify the products. The $i$-th of these lines contains three integers $s_i$, $t_i$, and $d_i$, which are the starting facility, the receiving facility, and the required container quantity for product $i$.
The final $m$ lines describe the haulage lanes. The $j$-th of these lines contains three integers $u_j$, $v_j$, and $c_j$, indicating a one-way lane from hub $u_j$ to hub $v_j$ with a maximum container load of $c_j$.
Hubs are numbered from 1 to $n$.

## Output
If a valid dispatch plan exists, print `YES` on the first line. Then, print $k$ lines. The $i$-th line should contain $m$ space-separated integers, where the $j$-th integer represents the number of containers of product $i$ routed over the $j$-th haulage lane (in the order the lanes were given in the input).
If no such plan is possible, print `NO`.

## Example
### Input
```text
4 3 2
1 4 1
2 4 1
1 3 1
2 3 1
3 4 2
```
### Output
```text
YES
1 0 1
0 1 1
```
