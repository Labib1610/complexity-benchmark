# Problem A — Magical Ley Lines

Time limit: 5 s   Memory limit: 256 MB

## Description
An ancient grid consists of runestones connected by one-way magical conduits. The grid must simultaneously channel several distinct frequencies of magic. 

For each frequency, pulses of magic are manifested at a specific origin runestone and must be guided to a specific destination runestone. The destination has a certain number of glyphs that must be illuminated. Illuminating a single glyph requires exactly one discrete pulse of that frequency to successfully arrive from the origin. 

Runestones themselves cannot hold magic. For any specific frequency, the number of pulses arriving at a runestone must exactly equal the number of pulses departing from it, with two exceptions: at the frequency's origin runestone, the number of departing pulses must exceed the arriving pulses by exactly the number of glyphs to illuminate; at the destination runestone, the number of arriving pulses must exceed the departing pulses by exactly the number of glyphs to illuminate. Pulses are discrete and indivisible, meaning all counts must be non-negative whole numbers.

The conduits are volatile and must be actively managed by acolytes. Each conduit has a specific headcount of acolytes stationed along it. Guiding a single pulse—regardless of its frequency—occupies exactly one acolyte. Consequently, the total count of pulses (summing across all frequencies) directed through any single conduit cannot exceed the number of acolytes stationed on that conduit. All frequencies share the same conduits, meaning they compete for the attention of the same acolytes.

Determine if it is possible to illuminate all glyphs for all frequencies simultaneously without overwhelming the acolytes on any conduit. If it is possible, provide the exact number of pulses of each frequency to send down each conduit.

## Input
The first line contains three integers: $n$ (runestones), $m$ (conduits), and $k$ (frequencies).
The next $k$ lines describe the frequencies. Each line contains three integers: $s_i$ (origin runestone), $t_i$ (destination runestone), and $d_i$ (the number of glyphs to illuminate).
The next $m$ lines describe the conduits. Each line contains three integers: $u$, $v$, and $c$, representing a one-way conduit from runestone $u$ to runestone $v$ with a headcount of $c$ acolytes.

## Output
If a valid configuration exists, print `YES` on the first line. Following this, print $k$ lines (one for each frequency, in input order). Each line must contain $m$ integers representing the number of pulses of that frequency assigned to each of the $m$ conduits (in input order).
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
