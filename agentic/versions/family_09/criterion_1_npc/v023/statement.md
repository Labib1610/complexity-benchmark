# Problem A — Multiplexer Calibration

Time limit: 5 s   Memory limit: 256 MB

## Description

A telecommunications operator is setting up a new base station capable of utilizing $n$ distinct frequency bands, which are identified by integers from 1 to $n$. The hardware requires at least one band to be active. The regulatory body limits the maximum number of bands an operator can license to exactly 46.

Certain pairs of frequency bands experience harmonic interference when used simultaneously. A survey has identified $m$ such interfering pairs. The number of interfering pairs ranges from zero (a perfectly clear spectrum) up to the theoretical maximum where every distinct pair among the $n$ licensed bands interferes.

The operator needs to configure a multiplexer that must operate using exactly $k$ distinct frequency bands. The multiplexer must be assigned at least one band, and naturally cannot be assigned more than the $n$ licensed bands. To ensure strict signal integrity, no two bands assigned to the multiplexer can be an interfering pair.

Determine if it is possible to select exactly $k$ bands that are mutually free of harmonic interference. If such a configuration exists, report one valid selection.

## Input

The first line contains three integers $n$, $m$, and $k$. Their valid ranges are determined by the physical, regulatory, and theoretical limits described above.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a pair of frequency bands that cause harmonic interference. No interfering pair is listed more than once.

## Output

If a valid configuration of exactly $k$ bands exists, print `YES` on the first line. On the second line, print the $k$ distinct band identifiers forming this configuration, separated by spaces. Any valid selection of exactly $k$ mutually non-interfering bands is accepted.

If no such configuration is possible, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```
