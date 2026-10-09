# Problem A — Containment Vessel Acoustic Nullification

Time limit: 5 s   Memory limit: 256 MB

## Description
The facility's primary containment vessel is currently experiencing a resonance event consisting of **3q** distinct standing waves. These waves are identified by integer channels from 1 to **3q**. Operating procedures require the complete elimination of all standing waves to prevent structural failure.

To achieve this, the control system can emit acoustic cancellation pulses. Due to hardware limitations, the system can only emit pulses from a pre-loaded registry of **t** validated configurations. Each validated configuration is hardwired to emit exactly three specific cancellation frequencies simultaneously. When a pulse is emitted, it permanently nullifies its three corresponding standing waves.

Emitting a cancellation frequency for a wave that has already been nullified will cause an interference feedback loop, immediately breaching containment. Therefore, no channel can be targeted by more than one pulse. Furthermore, any channel left un-targeted will continue to resonate and eventually cause a breach.

Your task is to determine if the operator can authorize a selection of exactly **q** pulses from the registry that safely nullifies all **3q** standing waves. If a safe authorization exists, you must provide one valid selection. If the registry lacks a combination that satisfies all operational constraints, you must report the failure.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the next **t** lines contains three integers **a**, **b**, and **c** (1 ≤ a < b < c ≤ 3q), representing the three frequencies emitted by one validated pulse configuration.

## Output
If a valid selection exists, output `YES`, followed by **q** lines each containing the three frequencies of one selected pulse configuration.
Otherwise, output `NO`.

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
