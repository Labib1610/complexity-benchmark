# Problem B — Full-Capacity Observatory Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description
The summit telescope captures images using an array of $q$ wave-collectors and $q$ signal-processors. Collectors are assigned identification numbers from $1$ to $q$, while processors receive numbers from $q+1$ to $2q$. 

During a calibration run, fiber-optic connections between specific collectors and processors are tested for integrity. The diagnostic system outputs a log of $t$ functioning connections, each identifying one collector and one processor that can successfully transmit data. 

To achieve maximum observation resolution, the telescope must be configured to use all hardware simultaneously. A valid configuration consists of a chosen set of functioning connections. In this configuration, every single collector must transmit to exactly one processor, and every single processor must receive from exactly one collector. 

Determine whether a valid configuration can be formed from the logged connections, and if so, provide the exact connections to use.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).  
Each of the next $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a functioning connection between collector $a$ and processor $b$.

## Output
If a valid configuration can be formed, print `YES` on the first line. Following this, print $q$ lines, each containing the two identification numbers of a chosen connection. If no such configuration is possible, print `NO`.

## Example

**Input:**
```
3 4
1 4
1 5
2 5
3 6
```

**Output:**
```
YES
1 4
2 5
3 6
```
