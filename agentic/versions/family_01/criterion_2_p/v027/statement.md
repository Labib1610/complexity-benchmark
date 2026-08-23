# Problem B — Harmonic Calibration

Time limit: 1 s   Memory limit: 256 MB

A research facility contains $n$ experimental modules, indexed from 1 to $n$. Over the course of preliminary testing, engineers have identified $m$ pairs of modules that exhibit harmonic resonance. 

Each module must be permanently calibrated to operate in one of two phase states, designated as state 1 and state 2. A calibration plan is represented as a sequence of $n$ integers, where the $i$-th integer corresponds to the phase state of module $i$. Because of the physical risks involved, a calibration plan is strictly required to be stable. Stability means that for every identified pair of modules exhibiting harmonic resonance, the two modules in the pair must be assigned distinct phase states.

Your objective is to process the list of resonating pairs and determine if at least one stable calibration plan exists for the $n$ modules. If such a plan is possible, you must find the stable calibration plan that is lexicographically smallest. If no stable calibration plan can be achieved, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$, representing a pair of modules that exhibit harmonic resonance.

## Output
If no stable calibration plan exists, print a single line containing the word NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each either 1 or 2), representing the lexicographically smallest stable calibration plan.

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
