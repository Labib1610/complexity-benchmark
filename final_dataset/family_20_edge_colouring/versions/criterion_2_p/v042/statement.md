# Problem B — Signal Calibration in a Two-Sided Array

Time limit: 2 s   Memory limit: 256 MB

## Description
A testing facility needs to calibrate a communications array consisting of a bank of transmitters and a bank of receivers. The calibration process requires running a series of signal tests. Each test establishes a dedicated link between exactly one transmitter and exactly one receiver. The hardware architecture is strictly two-sided: tests only ever occur across the two banks, never between two devices of the same type.

To run a test, the facility must assign it a specific frequency channel (numbered 1, 2, 3, and so on). A strict hardware limitation dictates that no single device—whether a transmitter or a receiver—can process multiple tests on the same frequency channel. Consequently, if any device is involved in multiple tests, every single one of those tests must be assigned a distinctly different channel. Other factors like signal strength, device model, and which side of the array a device sits on do not matter; the only rule is avoiding channel interference on shared devices.

Some devices are involved in more tests than others. The device with the absolute highest number of assigned tests (let this maximum workload be $\Delta$) dictates the theoretical minimum number of channels the facility must allocate. Your objective is to achieve optimal spectral efficiency by configuring all tests using **no more** than this unavoidable minimum. You must assign a channel to each test such that no device experiences channel interference, ensuring the total number of distinct channels used is exactly $\Delta$. (Because the array is strictly two-sided, this optimal configuration is always achievable; no channel beyond the busiest-device count is ever required.)

## Input
First line: three integers nL, nR, m (1 ≤ nL, nR ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nL, 1 ≤ v ≤ nR): a test between transmitter u and receiver v.

## Output
Print `YES`, then a line with m integers in 1..Δ — the channel of test i in input order (tests involving any common device must differ).

## Example
### Input
```
3 3 4
1 1
2 1
2 2
3 3
```

### Output
```
YES
1 2 1 1
```
