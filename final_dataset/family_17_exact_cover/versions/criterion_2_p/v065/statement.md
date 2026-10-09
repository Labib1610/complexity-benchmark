# Problem B — Secure Data Link Configuration

Time limit: 2 s
Memory limit: 256 MB

## Description
A communication array consists of two equal-sized sets of nodes: transmitters and receivers. Transmitters are assigned consecutive integer identifiers starting from 1 up to $q$. Receivers are assigned consecutive identifiers immediately following the transmitters, from $q+1$ up to $2q$.

You are provided with a list of potential data links, each specifying one transmitter and one receiver that can be synchronized. Due to hardware limitations, not all pairs can be synchronized; only the links explicitly listed are available.

Your task is to select a subset of these potential data links to form a complete network configuration. A configuration is considered valid if and only if it simultaneously satisfies all of the following strict criteria:
- Exactly $q$ data links are selected from the provided list.
- Every single transmitter and every single receiver is utilized in exactly one selected data link.
- Every selected link pairs one identifier from the range $[1, q]$ with one from the range $[q+1, 2q]$.
- For every selected link, the sum of its two node identifiers is strictly between $q+1$ and $3q+1$.
- The grand sum of all $2q$ node identifiers involved in the selected links is exactly $q(2q+1)$.

Determine if such a valid configuration exists. If it does, output one such configuration. If no configuration can satisfy all of these criteria simultaneously, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of transmitters (which is also the number of receivers) and the number of potential data links, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that transmitter $a$ and receiver $b$ can be synchronized.

## Output
If a valid configuration exists, print `YES` on the first line, followed by $q$ lines each containing the two node identifiers of a selected data link. If multiple valid configurations exist, you may output any of them.
If no valid configuration is possible, print `NO`.

## Example
### Input
```
3 4
1 4
2 5
2 6
3 5
```
### Output
```
YES
1 4
2 6
3 5
```
