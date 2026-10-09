# Problem A — Curating the Antiquities Exhibition

Time limit: 5 s   Memory limit: 256 MB

## Description
The national museum is preparing a new gallery to display a collection of $3q$ newly restored relics, tagged with unique integer codes from $1$ to $3q$. The gallery floorplan is already divided into $q$ distinct installations. The total capacity of these installations is exactly $3q$, meaning each installation will house exactly three relics.

To streamline the curation process, the museum's archiving system has pre-compiled a list of $t$ valid configuration blueprints. Each blueprint specifies a triplet of relics that are historically compatible and can be grouped together in a single installation.

Your objective is to find a perfect allocation of relics to installations. Because the total supply of relics perfectly matches the total capacity of the installations, you only need to ensure that the collection is conserved without duplication or omission:
- Select a subset of exactly $q$ blueprints from the archives.
- Apply each selected blueprint to one of the $q$ installations.
- Ensure every relic from $1$ to $3q$ is included in exactly one of the selected blueprints.

Determine if the archives contain a subset of blueprints that perfectly allocates the collection. If so, output the successful plan. If no such allocation is possible under the given blueprints, report that it is impossible.

## Input
The first line provides two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $q$ is the number of installations and $t$ is the number of pre-compiled blueprints.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the relic codes of a single blueprint.

## Output
If a perfect allocation can be formed, print `YES` on a single line, followed by $q$ lines each containing the three relic codes of a selected blueprint.
If no such allocation is possible, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
