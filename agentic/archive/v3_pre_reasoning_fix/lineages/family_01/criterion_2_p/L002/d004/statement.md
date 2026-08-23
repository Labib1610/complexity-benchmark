# Deep-Space Array

Time limit: 1 s
Memory limit: 256 MB

An array of $n$ deep-space transceivers must be calibrated. Each transceiver must be assigned a polarity index, which can be either 1 or 2.

The array relies on $m$ continuous data links. Each link directly connects a specific pair of transceivers, allowing them to exchange telemetry. To maintain stable telemetry across a link, the two connected transceivers must achieve phase equilibrium. Specifically, for any link connecting transceiver $u$ and transceiver $v$, the sum of their assigned polarity indices must be exactly 3. If the sum deviates from 3 for any link, the connection will fail and the entire array will go offline.

You must determine a valid polarity assignment for all $n$ transceivers that ensures full functionality. When multiple valid assignments exist, the automated calibration system defaults to the lexicographically smallest sequence (meaning the sequence of indices $b_1, b_2, \dots, b_n$ should be as small as possible when evaluated element by element from the first transceiver to the last).

## Input
The first line provides the number of transceivers $n$ and the number of data links $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$, representing a data link connecting transceiver $u$ and transceiver $v$.

## Output
If it is impossible to assign the polarity indices without the array failing, output a single line with `NO`.
If a viable assignment exists, output `YES` on the first line. On the second line, output $n$ integers $b_1, \dots, b_n$ (where each is 1 or 2), representing the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```