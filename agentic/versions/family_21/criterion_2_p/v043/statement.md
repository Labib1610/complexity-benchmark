# Problem B — Ritual of Severance

Time limit: 2 s   Memory limit: 256 MB

## Description
Within the Grand Archive lie $n$ enchanted pedestals, numbered $1$ through $n$. Pairs of pedestals may be linked by ethereal threads, which can carry energy in either direction. These threads facilitate the transmission of magical resonance according to the following principles:
- The volatile artifact on pedestal $s$ constantly brims with resonance.
- Whenever a pedestal is infused with resonance, the resonance automatically cascades across all intact ethereal threads connected to it, infusing the pedestals on their other ends.
- This cascading effect continues indefinitely, infusing further pedestals as long as intact threads allow.

A second volatile artifact rests on pedestal $t$. Should resonance ever cascade to pedestal $t$, the resulting reaction will shatter the Archive. To prevent this, you can permanently dissipate certain ethereal threads. Dissipating the thread between pedestal $u$ and pedestal $v$ requires a specific expenditure of mental focus. Once dissipated, a thread is no longer intact and cannot carry resonance.

You are capable of exerting at most $B$ total mental focus. Determine a set of threads to dissipate such that their combined focus cost does not exceed $B$, and the resonance originating at $s$ is entirely prevented from cascading to $t$. Other pedestals may safely become infused, provided $t$ remains completely isolated from the resonance. 

## Input
The first line contains five integers $n$, $m$, $s$, $t$, and $B$. 
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating an ethereal thread linking pedestal $u$ and pedestal $v$ that requires $w$ mental focus to dissipate.

## Output
If it is impossible to prevent the resonance from reaching $t$ using at most $B$ focus, output `NO`. 
Otherwise, output `YES`. On the following line, output an integer $c$, representing the number of threads you chose to dissipate. Then, provide $c$ lines, each containing two integers $u$ and $v$ to identify a dissipated thread. (If multiple valid sets of threads require $\le B$ focus, any one is acceptable).

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
