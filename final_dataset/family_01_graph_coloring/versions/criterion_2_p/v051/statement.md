# Tracking Frequencies

Time limit: 1 s   Memory limit: 256 MB

Wildlife researchers are deploying tracking collars on $n$ animals. Each collar must be programmed to transmit on one of two available radio frequencies, designated as 1 and 2. 

Based on observational data, the team has identified $m$ specific pairs of animals that frequently forage together. If two animals in one of these pairs are assigned the exact same transmission frequency, their tracking signals will interfere with each other when they are in close proximity. To guarantee reliable data collection, any two animals that are part of a known foraging pair must be programmed with different frequencies.

Your task is to determine whether it is possible to assign a frequency to every collar without any signal interference. If a valid configuration exists, the tracking system requires a specific allocation format. The resulting sequence of $n$ frequency assignments must be lexicographically smallest, meaning that the system prefers using frequency 1 over frequency 2, prioritizing the animal with the lowest ID, then the second lowest, and so forth.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of collared animals and the number of foraging pairs.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that animal $u$ and animal $v$ forage together and thus risk signal interference.

## Output
If there is no way to assign the frequencies without interference, output a single line containing `NO`.
If a valid assignment exists, output `YES` on the first line. On the second line, output $n$ space-separated integers, where the $i$-th integer (either 1 or 2) represents the frequency assigned to animal $i$. This sequence must be the lexicographically smallest valid assignment.

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
