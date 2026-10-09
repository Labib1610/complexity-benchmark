# Problem A — Curating the Antiquities Exhibition

Time limit: 5 s   Memory limit: 256 MB

## Description
A national museum is organizing an exhibition for a collection of $3q$ artifacts, labeled with integer IDs from $1$ through $3q$. The exhibition hall is equipped with $q$ available display cases.

To ensure historical accuracy, the museum's curator has developed a catalog of $t$ approved installation blueprints. Every blueprint designates exactly three artifact IDs that are permitted to share a single display case. A display case can only be assembled by strictly following one of these blueprints.

Your objective is to finalize the exhibition by executing exactly $q$ blueprints from the catalog. The donors stipulate that the entire collection must be shown, meaning every artifact from $1$ to $3q$ must be placed in a display case. Because each artifact is a unique physical item, it cannot be subjected to more than one blueprint.

Determine whether it is possible to populate the $q$ display cases under these conditions. If a valid configuration exists, output one such configuration. Otherwise, indicate that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), representing the number of display cases and the number of approved blueprints, respectively.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), detailing the artifact IDs required for that specific blueprint.

## Output
If the exhibition can be fully realized, print `YES` on the first line. Following this, print $q$ lines, each listing the three artifact IDs for one of the chosen blueprints.
If the collection cannot be completely exhibited according to the rules, print `NO`.

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
