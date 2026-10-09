# Problem A — Valve Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

A fluid control network contains **n** valves. Prior to operation, every valve must be assigned a fixed operational state of exactly `1` or `0`; no intermediate or floating states are permitted.

During commissioning, the engineering team recorded **m** safety checks. Each check consists of three target specifications for specific valves. A safety check fails exclusively when all three of its specifications differ from the actual valve states. If the system configuration matches the target state for any of the specifications within the check, the check passes silently.

The same valve can be referenced by multiple checks, potentially with conflicting target states across different checks. Your task is to determine if there exists a single, comprehensive configuration for all **n** valves that passes every safety check simultaneously.

## Input

The first line provides two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
The following m lines detail the safety checks. Each line contains three non-zero integers l1, l2, and l3, where |li| ≤ n. The absolute value of an integer refers to the valve index (from 1 to n). A positive integer represents a target state of `1` for that valve, while a negative integer represents a target state of `0`.

## Output

If there is no configuration that passes all checks, output a single line containing NO.
Otherwise, output YES on the first line. On the second line, output n integers s1, s2, …, sn (each being 0 or 1) separated by spaces, where si represents the assigned state of valve i. Any configuration that passes all checks is acceptable.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each safety check lists exactly three target specifications. The same valve index may appear more than once within a single check.
