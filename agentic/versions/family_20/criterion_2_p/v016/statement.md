# Frequency Allocation on a Two-Tier Terminal Grid

Time limit: 2 s   Memory limit: 256 MB

## Description
A communication grid consists of a set of Source terminals and a set of Destination terminals. Each active data stream connects exactly one Source terminal to exactly one Destination terminal. The architecture is strictly two-tier: no stream ever connects two Source terminals or two Destination terminals together. 

The peak load of the grid, denoted as $D$, is defined as the maximum number of streams connected to any single terminal (either Source or Destination). 

To prevent signal collision, each stream must be assigned a frequency channel (numbered 1, 2, 3, …). The collision rule dictates that if two streams share any terminal (either originating at the same Source or arriving at the same Destination), they must be assigned different channels. 

Because the busiest terminal has $D$ streams, at least $D$ channels are strictly necessary. Your objective is to allocate channels using exactly this theoretical minimum. You must assign every stream a channel from the range $1$ to $D$ such that no collision rule is violated. The two-tier architecture mathematically guarantees that such an allocation is always possible.

Additionally, the hardware controller guarantees two universal system limits for any valid grid:
1. The combined total of Source and Destination terminals ($S + T$) is at most 200,000.
2. The grid's peak load $D$ is at most the total number of active streams $m$.

## Input
The first line contains three integers $S$, $T$, and $m$ ($1 \le S, T \le 100000$, $0 \le m \le 400000$), representing the number of Source terminals, Destination terminals, and data streams, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le S$, $1 \le v \le T$), indicating a data stream from Source terminal $u$ to Destination terminal $v$.

## Output
First, print `YES`.
On the next line, print $m$ integers representing the frequency channels assigned to the data streams, in the exact order they appear in the input. Each channel must be an integer between $1$ and $D$ inclusive. If multiple valid channel assignments exist, you may output any of them.

## Example
**Input:**
```
4 4 6
1 1
1 2
2 2
3 3
3 4
4 4
```

**Output:**
```
YES
1 2 1 1 2 1
```
