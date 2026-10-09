# Phase II: Diagnostic Constraint Resolution

Time limit: 1 s   Memory limit: 256 MB

## Description
The automated maintenance protocol consists of three phases. 

In **Phase I**, the telemetry module assesses the health of `n` independent hardware components. Each component (indexed 1 to `n`) must be locked into exactly one of two operating modes: active (1) or standby (0). Based on thermal and electrical limits, Phase I generates a list of `m` critical stability requirements that must be upheld during the switchover.

You are responsible for **Phase II: Constraint Resolution**. The input to your module is the raw requirement list from Phase I. Every requirement specifies exactly two potential component states. A positive integer `x` indicates that component `|x|` is in active mode, while a negative integer `-x` indicates that component `|x|` is in standby mode. To prevent a system fault, every requirement must have at least one of its two stated conditions met by the final configuration. Your task is to process this list and determine if a global mode assignment exists for all `n` components that satisfies all `m` requirements simultaneously.

If your module successfully finds a valid assignment, **Phase III** will take over, using your output to physically actuate the relays. If the requirements are mutually exclusive and no such assignment exists, your module must abort the sequence.

## Input
The first line provides two integers `n` and `m` (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5), representing the number of components from Phase I and the number of stability requirements.
The following `m` lines each contain two non-zero signed integers `l1` and `l2` (|l1|, |l2| ≤ n). These represent the two potential component states for that requirement. At least one of these two states must be adopted in the final configuration.

## Output
If the requirements cannot be satisfied, output a single line with the word `NO` to trigger the abort sequence.
Otherwise, output `YES` on the first line. On the second line, output `n` space-separated integers `s1, s2, ..., sn`, where each `si` is either 1 (active) or 0 (standby), representing a valid assignment for components 1 through `n`. If multiple valid configurations exist, Phase III will accept any of them.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```
