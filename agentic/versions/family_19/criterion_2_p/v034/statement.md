# Problem B — Pallet Transfer Assignment

Time limit: 2 s
Memory limit: 256 MB

## Description
A logistics operator needs to transfer a specific quota of standardized pallets across a network of facilities connected by one-way transit corridors. Each corridor has a strict structural limit on the number of pallets it can accommodate during a single operational shift. The operator must move the exact target quota of pallets from a specified starting facility to a designated ending facility in one shift.

Each transit corridor is a one-way physical conveyor, meaning it cannot process a negative number of pallets. Moreover, the number of pallets routed through a corridor must not exceed its structural limit. Pallets are indivisible units. At any facility other than the start and the end, the total count of arriving pallets and the total count of departing pallets must be identical, ensuring no pallets are stored or lost. The starting facility must send out exactly the target quota more than it receives, and the ending facility must receive exactly the target quota more than it sends out.

Factors such as pallet loading times, corridor lengths, or the specific sequence of movements do not affect the assignment—only the structural limits, the strict in-out matching at intermediate facilities, and the overall quota strictly constrain the valid assignments.

You need to determine an assignment of pallets to each corridor that successfully moves the target quota from the start to the end without violating any corridor's limit. If it is impossible to move the full quota in a single shift, you must report this.

## Input
The first line contains three values: the number of facilities $n$, the number of corridors $m$, and the number of pallet types (which is always 1).
The second line contains three values: the starting facility ID $s$, the ending facility ID $t$, and the target quota $d$.
The next $m$ lines each describe a corridor with three values: the facility it originates from, the facility it goes to, and its structural limit.

## Output
If an assignment is possible, print `YES` on the first line. On the second line, output $m$ integers representing the number of pallets assigned to each corridor, in the exact order the corridors were provided in the input.
If it is impossible, print `NO`.

## Example
### Input
```text
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```
### Output
```text
YES
5 5 0 5 5
```
