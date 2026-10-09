# Cargo Dispatch Plan

Time limit: 2 s   Memory limit: 256 MB

## Description
A logistics company must coordinate the movement of a specific volume of cargo through a system of transfer yards joined by one-way tracks. Each track has a firm daily limit on the number of cargo units it can handle, due to operational constraints that cannot be exceeded.

You are given a target volume, $d$, representing the exact number of cargo units that must be successfully transported from a designated starting yard to a final receiving yard over the course of a single day. All cargo is counted in whole units.

The routing plan must satisfy the following operational rules:
- The number of units assigned to any track must be a non-negative integer that does not exceed the track's daily limit.
- Any yard that is neither the starting yard nor the final receiving yard lacks overnight storage. Therefore, the total count of cargo units arriving at such a yard must perfectly match the total count of units departing from it.
- The net volume of cargo leaving the starting yard (total departing minus total arriving) must be exactly $d$. 
- The net volume of cargo arriving at the final receiving yard (total arriving minus total departing) must be exactly $d$.
- Empty repositioning, transit times, track distances, and the order in which units move are outside the scope of this plan and must be ignored.

Determine an assignment of cargo units to tracks that meets all conditions, or report that the required volume cannot be transported in a single day.

## Input
The first line contains three integers: $n$ (the number of transfer yards), $m$ (the number of one-way tracks), and the number $1$.
The second line contains three integers: $s$ (the starting yard), $t$ (the final receiving yard), and $d$ (the required volume).
Each of the following $m$ lines contains three integers: $u$ (the yard where the track begins), $v$ (the yard where the track ends), and $cap$ (the daily limit for this track).

## Output
If a valid assignment exists, output `YES` on the first line. On the second line, output $m$ integers representing the number of cargo units assigned to each track, in the exact order the tracks were provided in the input. 
If no such assignment is possible, output `NO`.

## Example

### Input
```
4 5 1
1 4 3
1 2 2
1 3 2
2 3 1
2 4 1
3 4 2
```

### Output
```
YES
2 1 1 1 2
```
