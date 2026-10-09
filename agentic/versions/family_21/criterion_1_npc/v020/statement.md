# Die-Level Interference Mitigation

Time limit: 5 s   Memory limit: 256 MB

## Description
A prototype integrated circuit consists of $n$ junctions connected by $m$ micro-traces. The circuit contains $k$ primary oscillators. Each oscillator generates a signal at a unique, highly sensitive frequency. If a signal from one oscillator reaches another oscillator through any sequence of intact micro-traces, the resulting interference causes a critical failure.

To salvage the prototype, a focused ion beam can be used to ablate (permanently sever) certain micro-traces. Ablating a micro-trace prevents any signal transmission between its two endpoints in either direction. Because the traces vary in thickness and depth, ablating a specific trace requires a known amount of beam energy.

The goal is to select a set of micro-traces to ablate such that no two oscillators remain connected by any path of intact traces. In other words, every oscillator must end up in its own completely separate conductive region. Junctions that are not oscillators serve merely as routing points and may end up in whichever region the ablation produces; their placement is unconstrained and irrelevant to acceptance. What is measured is solely the total ablation energy, the sum of the energies required for the traces actually severed.

There is a fixed beam energy budget $B$. Choose a set of micro-traces to ablate whose total required energy does not exceed the budget and whose removal leaves every pair of oscillators disconnected, or report that no ablation within budget can isolate all oscillators simultaneously. (Isolating any one pair may be cheap; the budget must cover separating all oscillators from one another at once.)

## Input
Line 1: four integers $n$, $m$, $k$, and $B$.
Line 2: $k$ integers representing the junction IDs of the oscillators.
Next $m$ lines: three integers $u$, $v$, and $w$ — a micro-trace connecting junction $u$ and junction $v$ that requires $w$ beam energy to ablate.

## Output
If it is possible to isolate all oscillators without exceeding the energy budget, print `YES` on the first line. On the second line, print the number $c$ of ablated micro-traces. On the following $c$ lines, print the endpoints $u$ and $v$ of each ablated micro-trace. If it is impossible, print `NO`.

## Example
**Input**
```text
5 4 3 10
1 2 3
1 4 5
2 4 5
3 4 5
4 5 1
```

**Output**
```text
YES
2
1 4
2 4
```
