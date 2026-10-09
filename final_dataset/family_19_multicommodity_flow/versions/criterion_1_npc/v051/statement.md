# Problem A — Bureaucratic Bottlenecks

Time limit: 5 s   Memory limit: 256 MB

## Description
A massive government complex consists of various offices connected by a system of one-way pneumatic tubes. The administration needs to process several distinct contract types before the day ends.

For each contract type, a specific number of physical files must be dispatched from a drafting office and delivered to an archival office. Offices act merely as transfer hubs and cannot permanently store files. For any given contract type, the number of files of that type arriving at an office must exactly equal the number of files of that type departing from it. The only exceptions are:
- At the contract type's drafting office, the number of departing files must exceed the arriving files by exactly the number of files required for that contract.
- At the contract type's archival office, the number of arriving files must exceed the departing files by exactly the number of files required for that contract.

Since files are physical documents, all counts must be non-negative whole numbers.

The pneumatic tubes are aging and have strict limits. Each tube is equipped with a specific number of pneumatic carriers. Transmitting a single file—regardless of its contract type—occupies exactly one carrier. Consequently, the total number of files (summing across all contract types) sent through any single tube cannot exceed the number of carriers available in that tube. All contract types share the same system, meaning they compete for the same carriers.

Determine if it is possible to deliver all required files for all contract types simultaneously without exceeding the carrier limit on any tube. If it is possible, provide the exact number of files of each contract type to send down each tube.

## Input
The first line contains three integers: $n$ (offices), $m$ (tubes), and $k$ (contract types).
The next $k$ lines describe the contract types. Each line contains three integers: $s_i$ (drafting office), $t_i$ (archival office), and $d_i$ (the number of files to deliver).
The next $m$ lines describe the tubes. Each line contains three integers: $u$, $v$, and $c$, representing a one-way tube from office $u$ to office $v$ with $c$ available carriers.

## Output
If a valid delivery configuration exists, print `YES` on the first line. Following this, print $k$ lines (one for each contract type, in input order). Each line must contain $m$ integers representing the number of files of that contract type assigned to each of the $m$ tubes (in input order).
If no such configuration is possible, print `NO`.

## Example

### Input
```text
4 5 2
1 4 2
2 3 1
1 2 2
2 4 1
1 3 1
3 4 2
2 3 1
```

### Output
```text
YES
1 1 1 1 0
0 0 0 0 1
```
