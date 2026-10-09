# Problem B — Void Channeling

Time limit: 1 s
Memory limit: 256 MB

## Description

A coven of warlocks is preparing $j$ magical rituals. Each ritual requires two consecutive phases to be executed: inscribing a runic circle, and subsequently channeling void energy. 

The coven possesses one dedicated Inscriber and one dedicated Channeler. Before beginning, they must establish a single, strict sequence in which all $j$ rituals will be performed. Both members will adhere strictly to this sequence.

The mechanics of the ritual execution are as follows:
- The Inscriber processes the rituals back-to-back in the chosen sequence, working on one circle at a time.
- The Channeler also processes the rituals in the exact same chosen sequence, working on one channeling phase at a time.
- For any given ritual, the Channeler can only commence channeling once two conditions are met: the Channeler has finished the channeling phase for the preceding ritual in the sequence (if it is not the first ritual), AND the Inscriber has completely finished inscribing the circle for this current ritual.
- Once either member begins a phase for a ritual, they work continuously until that phase is completed.

For each ritual, you are provided the duration it takes to inscribe its circle, and the duration it takes to channel its void energy.

You must determine the optimal sequence in which to perform the rituals. Your objective is to find the sequence that minimizes the total time elapsed from the moment the Inscriber begins the first circle until the moment the Channeler completes the final channeling phase, and report this minimum possible total time.

## Input

The first line contains a single integer $j$ ($1 \le j \le 200000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the time required to inscribe the circle and the time required to channel the void energy for that ritual, respectively.

## Output

Print a single integer: the smallest possible time at which all rituals can be completely finished.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 1, if the given rituals (1-indexed) are ordered 3, then 2, then 1:
- **Ritual 3**: The Inscriber works from time 0 to 1. The Channeler works from 1 to 4.
- **Ritual 2**: The Inscriber works from 1 to 3. The Channeler waits until time 4, then works from 4 to 8.
- **Ritual 1**: The Inscriber works from 3 to 6. The Channeler waits until time 8, then works from 8 to 10.

The final completion time is 10. No other sequence results in a smaller total time.
