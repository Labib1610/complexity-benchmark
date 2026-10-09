# Problem A — Faction Isolation in the Lower Depths

Time limit: 5 s
Memory limit: 256 MB

## Description
Deep below the surface, a sprawling network comprises $n$ cavernous zones. These zones are joined together by $m$ bidirectional transit corridors. 

Among these zones, $k$ are designated as primary habitats, each occupied by a distinct and highly aggressive faction. To maintain order and prevent catastrophic conflicts, the facility administrators have mandated a strict quarantine: no faction may have access to the habitat of another. 

Factions can traverse any corridor that remains open, passing through any number of neutral zones along the way. Your task is to strategically deploy heavy bulkheads to close off certain corridors. When a bulkhead is activated in a corridor, it becomes permanently impassable in both directions. Each corridor has a specific energy cost associated with deploying its bulkhead.

You have a total energy allowance of $B$. You must select a set of corridors to close such that no open route exists connecting any pair of primary habitats. The sum of the energy costs for all deployed bulkheads must not exceed your allowance $B$. Find whether it is possible to achieve this absolute separation. If it is, you must output the specific corridors to close. If no such configuration is possible within the limit $B$, indicate that it cannot be done.

## Input
Line 1: four integers $n$, $m$, $k$, and $B$, representing the number of zones, corridors, primary habitats, and the energy allowance.
Line 2: $k$ distinct integers, the IDs of the zones designated as primary habitats.
Next $m$ lines: three integers $u$, $v$, and $w$ per line, indicating a corridor linking zone $u$ and zone $v$ with a sealing cost of $w$.

## Output
If the habitats can be isolated within the energy allowance $B$, print `YES` on the first line. On the second line, print an integer $c$, the number of corridors you chose to seal. On each of the next $c$ lines, print two integers $u$ and $v$ representing a sealed corridor. (If there are multiple valid sets of corridors within the allowance, any of them will be accepted).

If it is impossible to isolate the habitats within the allowance, print `NO`.

## Example 1

**Input**
```text
4 4 3 20
1 2 3
1 4 3
2 4 4
3 4 5
1 2 10
```

**Output**
```text
YES
3
1 4
2 4
1 2
```
