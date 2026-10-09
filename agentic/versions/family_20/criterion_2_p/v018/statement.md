# Problem B — Service Windows on a Two-Sided Exchange Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description
An exchange fabric consists of two distinct banks of hardware: a left-side bank of ports and a right-side bank of ports. The fabric is wired with a number of cables. Each cable connects exactly one port from the left bank to exactly one port from the right bank. There are never any cables connecting two ports within the same bank. The number of cables attached to a given port determines its load.

Routine maintenance requires taking individual cables offline during designated service windows, which are numbered sequentially starting from 1. A strict safety protocol dictates that if two or more cables terminate at the same port (whether on the left or the right bank), they must be taken offline in strictly different service windows. A port cannot safely handle the simultaneous offline status of multiple attached cables. 

Your objective is to generate a valid maintenance schedule. First, determine the maximum load across all ports in the entire fabric; this value represents the unavoidable minimum number of service windows required. You must assign every cable a service window such that the total number of distinct windows used does not exceed this maximum load. The structural guarantees of the two-sided wiring ensure that such a schedule is always possible.

## Input
The first line contains three integers $n_L$, $n_R$, and $m$ ($1 \le n_L, n_R \le 100000$, $0 \le m \le 400000$), representing the number of left-side ports, the number of right-side ports, and the total number of cables, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_L$, $1 \le v \le n_R$), indicating a cable connecting left port $u$ to right port $v$.

## Output
On the first line, print `YES`.
On the second line, print $m$ space-separated integers. The $i$-th integer must represent the service window (a value between $1$ and the maximum port load, inclusive) assigned to the $i$-th cable from the input. If multiple valid schedules exist, you may output any of them.

## Example

### Input
```text
3 3 4
1 1
1 2
2 2
3 3
```

### Output
```text
YES
1 2 1 1
```
