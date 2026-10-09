# Problem B — Ritual of Severance

Time limit: 2 s   Memory limit: 256 MB

## Description
In the Grand Archive, there are $n$ enchanted pedestals, indexed from $1$ to $n$. Certain pairs of pedestals are connected by ethereal threads, which allow magical energy to flow between them in either direction. Each thread requires a specific amount of mental focus to temporarily dissipate. Once a thread is dissipated, it can no longer transmit energy.

The Archive contains two highly volatile artifacts placed on pedestals $s$ and $t$. If any chain of active ethereal threads connects pedestal $s$ to pedestal $t$, their combined resonance will shatter the Archive. You must dissipate a chosen set of threads such that it is impossible for energy to travel, through any sequence of active threads, from $s$ to $t$. 

The pedestals other than $s$ and $t$ are stable; it does not matter which artifacts they remain connected to, or how they are grouped, as long as the primary connection between $s$ and $t$ is absolutely broken. What is measured is solely the total mental focus required, which is the sum of the focus costs of the threads actually dissipated.

You have a maximum mental focus capacity of $B$. Choose a set of threads to dissipate whose total focus cost is at most $B$ and whose removal leaves the two volatile artifacts completely isolated from one another, or report that no such intervention is possible within your capacity.

## Input
The first line contains five integers $n$, $m$, $s$, $t$, and $B$. 
The next $m$ lines each contain three integers $u$, $v$, and $w$, representing an ethereal thread between pedestal $u$ and pedestal $v$ that requires $w$ mental focus to dissipate.

## Output
If it is impossible to secure the Archive within the focus limit $B$, output `NO`. 
Otherwise, output `YES`. On the next line, output an integer $c$, the number of threads you have chosen to dissipate. Then, output $c$ lines, each containing two integers $u$ and $v$ representing a dissipated thread. (If there are multiple valid sets of threads that require $\le B$ focus, any one will be accepted).

## Example

### Input
4 5 1 4 15
1 2 4
1 3 7
2 3 2
2 4 6
3 4 5

### Output
YES
2
2 4
3 4
