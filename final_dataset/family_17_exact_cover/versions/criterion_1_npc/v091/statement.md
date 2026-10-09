# Curatorial Display Configuration

Time limit: 5 s   Memory limit: 256 MB

## Description
A prestigious museum is preparing a new gallery to exhibit its latest collection. The collection consists of distinct historical artifacts, cataloged with ID numbers from $1$ up to $3q$.

The gallery will feature custom-built display pedestals, each designed to hold exactly three items. To ensure the exhibition tells a coherent historical story, the lead curators have evaluated all possible combinations and approved a strict list of thematic groupings, known as "narrative triads." Each triad consists of exactly three specific artifacts that complement one another. Ad-hoc or unapproved groupings are strictly prohibited.

The exhibition must adhere to two absolute physical and curatorial requirements. First, every single artifact in the collection must be placed on display; none can remain in the archives. Second, an artifact cannot be physically present in more than one pedestal. Therefore, you must select a set of approved narrative triads such that every artifact from $1$ to $3q$ is included in exactly one chosen triad.

Your task is to determine if it is possible to configure the gallery using only the approved triads. If a valid configuration exists, you must also provide the selected groupings.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The value $q$ specifies that there are $3q$ artifacts in total, and $t$ represents the number of approved narrative triads.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), denoting the ID numbers of the artifacts that make up one approved triad.

## Output
If a valid exhibition layout can be formed, print `YES` on the first line. Then, output $q$ lines, each containing the three artifact ID numbers for one selected triad. If no such layout is possible, print `NO`.

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
