# Problem A — Emergency Relief Dispatch over Shared Airlift Corridors

Time limit: 5 s   Memory limit: 256 MB

## Description
A disaster response agency manages a set of response camps linked by directional airlift corridors. Each corridor has a hard threshold on the total number of crates it can handle per day. This threshold restricts the combined volume of all crates transported through it, regardless of their contents, and cannot be breached.

Today, there are several distinct aid types that need to be moved. Each aid type has a specific dispatch camp, a specific target camp, and a strict quota of crates that must be completely transferred today. Because all aid types rely on the same infrastructure, they share the daily flight allowances: the sum of crates across all aid types sent through a corridor cannot exceed that corridor's threshold. The number of crates of any aid type on any corridor must be a non-negative whole number.

Crates cannot be stored or consumed at any camp other than their designated dispatch and target camps. For any given aid type, the number of crates of that type arriving at any intermediate camp must exactly equal the number of crates of that same type departing from it. At the dispatch camp for a specific aid type, the number of crates of that type leaving minus the number arriving must equal its strict quota. At its target camp, the number arriving minus the number leaving must equal that quota. Transit times and distances are irrelevant; only the corridor thresholds, the exact transfer of each aid type without intermediate loss or storage, and the required quotas matter.

Determine a daily flight schedule that fulfills the quota for every aid type while respecting the threshold of every corridor, or state that it is impossible to handle all aid types in a single day.

## Input
Line 1: Three integers $n$ (camps), $m$ (corridors), and $k$ (aid types).
Next $k$ lines: Three integers $s_i$ (dispatch camp), $t_i$ (target camp), and $d_i$ (strict quota) for aid type $i$.
Next $m$ lines: Three integers $u$, $v$, and $cap$ representing a directional corridor from camp $u$ to camp $v$ with a daily threshold of $cap$ crates.

## Output
Output `YES` followed by $k$ lines, each containing $m$ integers — the number of crates of aid type $i$ sent through corridor $j$ (in the exact order corridors were given in the input). If a valid schedule is impossible, output `NO`.

## Example

**Input:**
```
4 5 2
1 4 10
2 3 5
1 2 10
2 4 10
1 3 5
3 4 5
2 3 5
```

**Output:**
```
YES
5 5 5 5 0
0 0 0 0 5
```
