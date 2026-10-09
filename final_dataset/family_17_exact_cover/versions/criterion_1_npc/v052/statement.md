# Problem A — Curating the Antiquities Exhibition

Time limit: 5 s   Memory limit: 256 MB

## Description
The national museum is planning a new gallery to showcase $3q$ newly restored relics. The relics are tagged with unique integer codes from $1$ to $3q$. The gallery will be organized into exactly $q$ distinct installations.

To ensure historical accuracy, the design of each installation must be governed by an archival blueprint. The museum's archives contain $t$ such blueprints. A blueprint dictates that a specific combination of exactly three relics must be displayed together. 

The gallery must be planned by adhering to the following operational rules:
- You must select exactly $q$ blueprints from the archives.
- Each selected blueprint is used to construct one of the $q$ installations, meaning the three relics specified by the blueprint are placed there.
- Every single relic from the $3q$ tagged items must be placed into an installation.
- Because a relic is a single physical object, it cannot be placed in more than one installation.

Determine if there is a way to select the blueprints to satisfy all these requirements. If successful, output the plan. If the collection cannot be fully exhibited under these strict historical constraints, report that it is impossible.

## Input
The first line provides two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $q$ is the number of installations and $t$ is the number of archival blueprints available.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the relic codes required by one archival blueprint.

## Output
If a valid exhibition layout exists, print `YES` on a single line, followed by $q$ lines each containing the three relic codes of a selected blueprint.
Otherwise, print `NO`.

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
