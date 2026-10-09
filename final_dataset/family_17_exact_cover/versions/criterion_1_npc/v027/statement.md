# Problem A — Chamber Stabilization Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description
The Harmonic Resonance Chamber currently sustains a series of standing waves. The total number of waves is a multiple of three, denoted as **3q**, and they are indexed sequentially by integers from 1 up to **3q**.

To stabilize the chamber, the system can project acoustic dampening chords. A single dampening chord targets exactly three specific frequencies simultaneously, neutralizing them permanently. The system is restricted to a pre-compiled database of **t** calibrated chords; no other combinations can be projected. Each calibrated chord in the database specifies exactly three distinct frequencies.

When a chord is projected, its three target frequencies must still be actively oscillating in the chamber. If any of the three frequencies has already been neutralized by a previous chord, the projection will fail and trigger a cascade resonance. Consequently, no frequency can be targeted more than once. At the same time, any frequency left active will eventually destabilize the chamber, meaning no frequency can be left out.

Your objective is to determine whether it is possible to select exactly **q** chords from the database that successfully neutralize all **3q** standing waves. If such a selection exists, you must identify one acceptable set of chords. If the database does not contain a combination of chords that satisfies all operational constraints, you must report this failure.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the next **t** lines contains three integers **a**, **b**, and **c** (1 ≤ a < b < c ≤ 3q), representing the frequencies of one calibrated chord.

## Output
If a valid selection exists, print `YES`, followed by **q** lines each containing the three frequencies of one selected chord.
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
