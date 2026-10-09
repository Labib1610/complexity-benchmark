# Phase-Locked Signal Alignment

Time limit: 2 s   Memory limit: 256 MB

## Description
A communications grid consists of $2q$ relay nodes, assigned sequential identification numbers from $1$ up to $2q$. 

To establish a stable network protocol, nodes must be locked together in pairs. However, the hardware enforces a strict polarity rule: a valid lock can only be formed between a low-band node (those with identification numbers from $1$ to $q$) and a high-band node (those with identification numbers from $q+1$ to $2q$). 

You are provided with a diagnostic log of $t$ pre-tested locks that successfully bridge a low-band node and a high-band node.

The grid reaches full-spectrum integration only if a subset of these pre-tested locks is activated such that every single relay node (from $1$ to $2q$) is incorporated into exactly one active lock. No node may be excluded, and no node may be assigned to multiple locks.

Evaluate the diagnostic log to determine whether full-spectrum integration is possible. If it can be achieved, output a valid configuration; otherwise, declare it impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a pre-tested lock between low-band node $a$ and high-band node $b$.

## Output
If full-spectrum integration is possible, print `YES` on the first line, followed by $q$ lines each containing the two node identification numbers of an activated lock. If it is not possible, print `NO`.

## Example
**Input**
```
3 4
1 4
2 5
3 6
2 6
```

**Output**
```
YES
1 4
2 5
3 6
```
