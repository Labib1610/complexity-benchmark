# Problem A — Composite Synthesis

Time limit: 5 s   Memory limit: 256 MB

## Description
In a specialized manufacturing facility, the inventory consists of a set of distinct raw materials, indexed sequentially from $1$ to $3q$. The facility contains exactly one unit of each indexed material. Operations are governed by a technical manual that catalogs $t$ validated fusion procedures. A single procedure dictates a strict combination of exactly three distinct raw materials that are compatible for reaction.

Whenever a procedure is carried out, the three specified materials undergo an irreversible reaction. As a result, those specific units are entirely depleted. Due to the strict limitation of having only one unit of each material in stock, no raw material index can be involved in more than one carried-out procedure.

A new work order demands the production of exactly $q$ composite units. Since each carried-out procedure yields a single composite unit, the task requires selecting a subset of the validated procedures. Determine whether it is possible to fulfill the work order under the inventory limitations. If a valid operational plan exists, specify the procedures that comprise it.

## Input
The first line provides two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), representing the work order requirement (number of composite units) and the number of validated procedures in the manual, respectively.

Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing a validated procedure that reacts materials $a$, $b$, and $c$ together.

## Output
If the work order can be fulfilled, output `YES` on the first line. On each of the subsequent $q$ lines, output the three material indices for one of the procedures you have chosen to carry out. If there is no valid selection of procedures that meets the requirement, output `NO`.

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
