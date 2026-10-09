# Salvage Excavation

Time limit: 5 s   Memory limit: 256 MB

## Description
A valley is slated to be flooded, leaving a strict limit on the number of excavation campaigns to recover historical artifacts. The site is divided into $n$ distinct sectors. Every sector requires exactly one full campaign to clear.

The expedition is constrained by its workforce: during any single campaign, the available teams can clear a maximum of $M$ sectors in total. 

Furthermore, the physical layout of the ruins dictates the progression of the dig. Certain sectors structurally cover or block access to others. If sector $b$ is buried under sector $a$, then sector $a$ must be cleared in a strictly earlier campaign than sector $b$. It is physically impossible for a deeper sector and the sector covering it to be cleared during the same campaign.

The flood waters will arrive after exactly $T$ campaigns. Determine if it is possible to arrange the clearing of all $n$ sectors within this timeframe (using campaigns $1$ through $T$) such that no campaign exceeds the team capacity and all structural restrictions are respected. If a valid arrangement exists, provide the campaign assignment for each sector.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$.
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that sector $a$ must be cleared in a campaign strictly prior to the campaign in which sector $b$ is cleared. Sectors are identified by integers from $1$ to $n$.

## Output
If a valid arrangement exists, print `YES` followed by $n$ integers, where the $i$-th integer represents the campaign (from $1$ to $T$) assigned to sector $i$. If no such arrangement can be formed, print `NO`.

## Example
**Input**
```text
5 2 3 4
1 3
2 3
3 4
3 5
```

**Output**
```text
YES
1 1 2 3 3
```
