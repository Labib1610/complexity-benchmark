# Problem B — Network Activation Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description
A network upgrade involves $2q$ stations, numbered sequentially from $1$ to $2q$. The upgrade protocol requires establishing dedicated communication channels. A valid channel always connects a low-band station (which has an ID from $1$ to $q$) to a high-band station (which has an ID from $q+1$ to $2q$).

You are provided with a catalog of $t$ potential channels that have been verified as stable by the engineering team. Your objective is to activate a subset of these verified channels such that every single station in the network (all $2q$ of them) is actively communicating on exactly one activated channel. No station may be left isolated, and no station may participate in more than one channel. Redundancies in the verified list are irrelevant; you only need to find one valid configuration.

Determine if such a comprehensive network activation is possible. If it is, output the specific channels to activate. Otherwise, report that it cannot be done.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing half the total number of stations and the number of verified channels, respectively.
Each of the following $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), denoting a verified channel between station $a$ and station $b$.

## Output
If a comprehensive activation is possible, print `YES` on the first line, followed by $q$ lines each containing the two station IDs of an activated channel. If it is not possible, print `NO`.

## Example

### Input
```
2 3
1 3
1 4
2 3
```

### Output
```
YES
1 4
2 3
```
