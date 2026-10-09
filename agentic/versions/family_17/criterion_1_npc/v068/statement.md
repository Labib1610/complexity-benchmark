# Problem A — Relief Pallet Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description
A logistics center must pack exactly $q$ relief pallets. There are $3q$ distinct crates of supplies on the dock, uniquely numbered from 1 to $3q$. The center possesses exactly one of each numbered crate.

Each pallet must be loaded with exactly three crates. Once a crate is loaded onto a pallet, it is shipped and unavailable for any other pallet. 

To ensure the pallets are balanced for transport, crates can only be grouped according to an approved safety manifest. The manifest contains $t$ approved groupings, each specifying three particular crates that can safely be loaded together onto a single pallet. Loading any unlisted grouping, or a grouping with a different number of crates, is prohibited.

Determine if it is possible to pack the required $q$ pallets using the approved groupings.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), representing the number of pallets to pack and the number of approved groupings in the manifest, respectively.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), detailing the crate numbers for that approved grouping.

## Output
If the required pallets can be packed, print `YES` on the first line. Then, output $q$ lines, each containing the three crate numbers of a grouping used in the packing plan.
If it is not possible, print `NO`.

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
