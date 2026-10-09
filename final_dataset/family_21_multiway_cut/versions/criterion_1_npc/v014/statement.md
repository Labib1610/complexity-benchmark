# Problem A — Securing the Subterranean Archive

Time limit: 5 s   Memory limit: 256 MB

## Description
A subterranean archive is divided into chambers connected by tunnels. Each tunnel requires a specific quantity of sealant to block completely. Certain chambers are designated as quarantine zones, holding artifacts that will react catastrophically if exposed to one another. The maintenance crew must deploy sealant to block a selection of tunnels. Once a tunnel is blocked, nothing can pass through it in either direction.

After deployment, the quarantine zones must be strictly segregated: it must be impossible to travel between any two quarantine zones using unblocked tunnels. Chambers that are not quarantine zones can end up connected to at most one quarantine zone (or none at all) — their final arrangement does not matter. The total amount of sealant used is simply the sum of the sealant required for each blocked tunnel.

The crew has a fixed allocation of sealant. Determine a selection of tunnels to block such that the total sealant used is no more than this allocation, and every quarantine zone is segregated from all others. If the allocation is insufficient to achieve complete segregation, report this. (Isolating a single pair of zones might require little sealant; the allocation must be enough to separate all zones from each other simultaneously.)

## Input
The first line provides four integers: the total number of chambers ($n$), the total number of tunnels ($m$), the number of quarantine zones ($k$), and the sealant allocation ($B$).
The second line contains $k$ integers representing the identifiers of the quarantine zones.
The following $m$ lines each describe a tunnel with three integers $u$, $v$, and $w$, indicating a tunnel between chamber $u$ and chamber $v$ that requires $w$ units of sealant to block.

## Output
If segregation is possible within the allocation, print `YES` on the first line. On the second line, print the number of blocked tunnels, $c$. Then print $c$ lines, each containing the two chambers connected by a blocked tunnel (in the format $u$ $v$).
If it is not possible to segregate all quarantine zones within the allocation, print `NO`.

## Example

**Input:**
```text
4 3 3 8
1 2 3
1 4 2
2 4 4
3 4 3
```

**Output:**
```text
YES
2
1 4
3 4
```
