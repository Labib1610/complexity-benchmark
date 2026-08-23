# Deep-Space Array

Time limit: 1 s
Memory limit: 256 MB

An array of $n$ deep-space transceivers must be calibrated. Each transceiver must be tuned to one of two frequency bands, denoted as band 1 and band 2.

The array relies on $m$ continuous data links. Each link directly connects a specific pair of transceivers, allowing them to exchange telemetry. However, the links pass through an atmospheric anomaly that causes frequency inversion. 
Specifically, a signal transmitted on band 1 by a transceiver undergoes inversion in the link and arrives as a band 2 signal, requiring the receiving transceiver to be tuned to band 2 to detect it. Conversely, a signal transmitted on band 2 undergoes inversion and arrives as a band 1 signal, requiring the receiver to be tuned to band 1.

For the array to function, every data link must support two-way communication. This means each transceiver's single assigned band must allow it to successfully detect the incoming inverted signals from all of its connected partners. If any transceiver cannot detect the incoming signals from a link, the entire array will fail.

You must determine a valid band assignment for all $n$ transceivers that ensures full functionality. When multiple valid assignments exist, the automated calibration system defaults to the lexicographically smallest sequence (meaning the sequence of bands $b_1, b_2, \dots, b_n$ should be as small as possible when evaluated element by element from the first transceiver to the last).

## Input
The first line provides the number of transceivers $n$ and the number of data links $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$, representing a data link connecting transceiver $u$ and transceiver $v$.

## Output
If it is impossible to assign the frequency bands without the array failing, output a single line with `NO`.
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