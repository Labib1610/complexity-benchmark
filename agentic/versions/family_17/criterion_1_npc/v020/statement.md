# Problem A — Curating the Antiquities Exhibition

Time limit: 5 s   Memory limit: 256 MB

## Description
A national museum is preparing a grand exhibition of newly excavated antiquities. The collection consists of exactly $3q$ unique artifacts, cataloged with sequential ID numbers from $1$ up to $3q$. The entire collection must be displayed; leaving any artifact in storage is strictly prohibited by the donors' agreement.

The main hall features $q$ custom-built triangular display pedestals. To maintain visual balance, each pedestal must hold exactly three artifacts. Furthermore, the museum's chief curator insists that artifacts cannot be grouped arbitrarily. The curator has provided a comprehensive ledger of $t$ historically harmonious triads—specific sets of three artifacts that are known to have been used together in antiquity. A pedestal may only be populated using one of these exact pre-approved triads.

Your task is to design a complete exhibition layout. You must select a set of triads from the curator's ledger such that every single artifact in the collection is displayed exactly once. No artifact may be omitted, and since each artifact is a unique physical object, it cannot be placed on more than one pedestal.

Determine if the curator's ledger allows for a perfect arrangement of the entire collection. If it does, provide one valid assignment of artifacts to pedestals. If the collection cannot be fully exhibited under these strict historical constraints, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $q$ is the number of display pedestals and $t$ is the number of historically harmonious triads in the ledger.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the catalog IDs of three artifacts that form an approved triad.

## Output
If a valid exhibition layout exists, print `YES` on a single line, followed by $q$ lines each containing the three artifact IDs of a selected triad.
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
