# Problem B — Quarantine Logistics

Time limit: 2 s   Memory limit: 256 MB

## Description
An interstellar trading conglomerate operates across $n$ planetary markets. Commerce flows between these markets through $m$ established hyperspace routes. Each route connects two specific markets and allows unrestricted two-way cargo transport.

Recently, a highly infectious agricultural blight was detected on planet $s$. To prevent the blight from reaching the conglomerate's primary agricultural hub on planet $t$, you must sever all possible supply chains between the two planets. Cargo can hop through any number of intermediate markets, so you must ensure that absolutely no sequence of active routes allows travel between $s$ and $t$, in either direction. 

You can permanently shut down routes to achieve this quarantine. A shut down route permits no cargo transport whatsoever. Shutting down the route between market $u$ and market $v$ incurs a financial penalty of $w$ credits. You have an emergency fund of $B$ credits; the sum of penalties for all shut down routes cannot exceed this fund.

The exact fate of the other $n-2$ markets—whether they remain connected to $s$, to $t$, or to neither—is entirely irrelevant to your success. The only metric that matters is that $s$ and $t$ share no chain of active routes, and that the total shutdown penalty is within your $B$ credit fund. 

Find a valid set of routes to shut down that meets these conditions, or determine that the emergency fund is insufficient. (Note: Do not overcomplicate the logistics. You are only required to segregate two specific planets, not partition the entire conglomerate into multiple isolated zones. Complex maneuvers designed for generalized multi-way segregation will do unnecessary work here.)

## Input
The first line provides five integers: $n$, $m$, $s$, $t$, and $B$.
The following $m$ lines each contain three integers $u$, $v$, and $w$, describing an established route between market $u$ and market $v$ that costs $w$ credits to shut down.

## Output
If a valid quarantine plan exists within the budget, print `YES` on the first line. On the second line, print the number of routes to be shut down, $c$. This must be followed by $c$ lines, each containing two integers $u$ and $v$ representing a shut down route. 
If no such plan is possible within the budget, print `NO`.

## Example

### Input
```text
4 5 1 4 10
1 2 4
1 3 5
2 4 6
3 4 3
2 3 2
```

### Output
```text
YES
2
1 2
1 3
```
