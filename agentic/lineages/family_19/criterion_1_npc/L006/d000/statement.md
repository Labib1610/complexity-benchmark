# Problem A — Crowd Routing for Stadium Security

Time limit: 5 s   Memory limit: 256 MB

## Description
A large entertainment complex is divided into secure zones connected by one-way turnstile banks. Each turnstile bank has a strict mechanical limit on the total number of attendees that can pass through it during the entry phase. This limit applies to the combined footfall across all attendees, regardless of their ticket type.

There are several distinct fan groups entering the complex. Each group has a specific gathering zone where they start, a specific seating zone they must reach, and an exact number of members. All groups are moving through the complex simultaneously. A turnstile bank's limit restricts the combined number of people from all groups that use it, meaning groups compete for shared turnstile access even though they are otherwise independent. People cannot be divided, so the number of individuals from any group passing through a given bank is a non-negative whole number.

Attendees must keep moving without getting lost in the complex. For any zone that is neither a group's gathering zone nor its seating zone, the number of members of that group entering the zone must exactly equal the number of members of that group leaving it. At a group's gathering zone, the number of its members leaving minus the number entering must equal the total size of the group. At their seating zone, the number of its members entering minus the number leaving must equal the group's size. 

Determine a movement plan that guides every group's entire membership to their respective seating zones without exceeding the limit of any turnstile bank. If it is impossible to route all groups together under these shared limits, you must report this.

## Input
The first line contains three integers: $n$ (number of secure zones), $m$ (number of turnstile banks), and $k$ (number of fan groups).
The next $k$ lines each contain three integers: $s_i$ (gathering zone for group $i$), $t_i$ (seating zone for group $i$), and $d_i$ (number of members in group $i$).
The next $m$ lines each contain three integers: $u$, $v$, and $cap$, representing a one-way turnstile bank from zone $u$ to zone $v$ that allows at most $cap$ people to pass in total.

## Output
If a valid movement plan exists, print `YES` on the first line. Then, print $k$ lines, each containing $m$ integers. The $j$-th integer on the $i$-th line must be the number of members from fan group $i$ passing through turnstile bank $j$ (where banks are indexed 1 to $m$ in the order they appear in the input). 
If no such movement plan is possible, print `NO`.

## Example

**Input:**
```
4 5 2
1 4 10
2 3 5
1 2 10
2 4 10
1 3 10
3 4 10
2 3 5
```

**Output:**
```
YES
5 5 5 5 0
0 0 0 0 5
```
