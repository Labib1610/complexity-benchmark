# Problem A — Standardized Cargo Logistics

Time limit: 5 s   Memory limit: 256 MB

## Description
You are organizing the logistics for transporting a batch of $n$ standardized shipping crates. The transport schedule consists of a maximum of $T$ consecutive daily cargo flights. Because all crates are perfectly standardized to the same dimensions, they are entirely interchangeable from the perspective of the aircraft. Every crate occupies exactly one cargo bay, and every single daily flight has a uniform capacity of exactly $M$ identical cargo bays. There are no varying transit times, no specialized handling requirements, and no priority tiers. 

The only restrictions come from the assembly sequence at the destination. Certain crates contain components that must be unpacked and prepared before other specific crates arrive. You are given $m$ such rules. If crate $a$ must arrive before crate $b$, then crate $a$ must be assigned to a strictly earlier day than crate $b$. 

Given the perfect uniformity of the crates and the consistent daily capacity, your task is simply to assign each of the $n$ crates to a specific day such that no day exceeds the $M$-crate capacity, all destination assembly rules are respected, and the entire batch is shipped within the $T$-day deadline. You do not need to worry about packing different sizes or minimizing costs—any valid sequence of days that respects the prerequisites and fits within the uniform daily limit is perfectly acceptable.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$. 
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that crate $a$ must be shipped on a strictly earlier day than crate $b$.

## Output
If a valid schedule exists, print `YES` followed by $n$ space-separated integers representing the assigned day (from 1 to $T$) for crates 1 through $n$ respectively. If no such schedule is possible, print `NO`.

## Example

**Input**
```text
4 2 2 3
1 3
1 4
2 4
```

**Output**
```text
YES
1 1 2 2
```
