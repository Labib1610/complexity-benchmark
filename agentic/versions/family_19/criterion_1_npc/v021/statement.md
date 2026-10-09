# Harmonic Resonance Tuning

Time limit: 5 s
Memory limit: 256 MB

## Description
An ancient arcane apparatus consists of $n$ focal crystals, numbered $1$ to $n$. These crystals are interlinked by $m$ one-way resonance beams. Each beam originates at one crystal and terminates at another. Because of the physical properties of the crystals, each beam has a strict structural threshold: it can carry at most a certain total number of energetic pulses simultaneously.

You must calibrate the apparatus to transmit $k$ distinct harmonic signatures. Each harmonic signature must be injected at a specific originating crystal and extracted at a specific terminating crystal. Furthermore, each signature requires exactly a certain number of pulses to be successfully transmitted.

Pulses are indivisible. The number of pulses of any given signature assigned to any beam must be a non-negative integer. All pulses of all signatures share the same resonance beams. The structural threshold of a beam applies to the sum of the pulses of all signatures currently traversing it.

The crystals themselves cannot store or alter the signatures. For any given harmonic signature, the following rules apply:
- If a crystal is neither its originating nor its terminating crystal, the total number of incoming pulses of that signature must exactly equal the total number of outgoing pulses of that signature.
- At the originating crystal, the total outgoing pulses of that signature minus the total incoming pulses of that signature must exactly equal its required pulse count.
- At the terminating crystal, the total incoming pulses of that signature minus the total outgoing pulses of that signature must exactly equal its required pulse count.

Determine if there is a valid assignment of pulses for each signature across the resonance beams that fulfills all requirements without exceeding the structural threshold of any beam. If it is possible, output the exact number of pulses for each signature on each beam.

## Input
Line 1: Three integers $n$, $m$, and $k$ — the number of crystals, beams, and harmonic signatures.
Next $k$ lines: Three integers $s_i$, $t_i$, and $d_i$, specifying the originating crystal, terminating crystal, and required number of pulses for harmonic signature $i$.
Next $m$ lines: Three integers $u$, $v$, and $cap$, specifying a one-way resonance beam from crystal $u$ to crystal $v$ with a structural threshold of $cap$ total pulses.

## Output
If a valid configuration exists, print `YES` on the first line. Then print $k$ lines. The $i$-th line should contain $m$ integers, where the $j$-th integer is the number of pulses of harmonic signature $i$ assigned to the $j$-th resonance beam (in the order the beams are listed in the input).
If no such configuration is possible, print `NO`.

## Example

**Input**
```text
4 4 2
1 4 1
1 4 1
1 2 1
1 3 1
2 4 1
3 4 1
```

**Output**
```text
YES
1 0 1 0
0 1 0 1
```
