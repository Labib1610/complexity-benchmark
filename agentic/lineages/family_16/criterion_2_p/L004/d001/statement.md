# Problem B — Void Channeling

Time limit: 1 s
Memory limit: 256 MB

## Description

A coven of warlocks is preparing $j$ magical rituals to form a unified void channel. Each ritual possesses two properties: an inscription duration and a channeling duration. 

Before the alignment begins, the coven must establish a single, strict sequence in which all $j$ rituals will be arranged. 

Once the sequence is established, the chaotic nature of the void will test the arrangement by forming a "focal point" at exactly one of the rituals. If the $k$-th ritual in the chosen sequence becomes the focal point, the overall strain on the channel is defined as the sum of two components:
- The sum of the inscription durations of all rituals from the first position up to, and including, the $k$-th position.
- The sum of the channeling durations of all rituals from the $k$-th position up to, and including, the final position.

The void will always naturally settle its focal point on the ritual that results in the highest possible overall strain. 

To maintain control over the channel, the coven must determine the optimal sequence in which to arrange the rituals. Your objective is to find the sequence that minimizes this highest possible overall strain, and report this minimum possible value.

## Input

The first line contains a single integer $j$ ($1 \le j \le 200000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the inscription duration and the channeling duration for that ritual, respectively.

## Output

Print a single integer: the smallest possible maximum strain the coven can achieve.

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

In Example 1, if the given rituals (1-indexed) are arranged in the order 3, then 2, then 1:
The sequence of (inscription, channeling) durations is: (1, 3), (2, 4), and (3, 2).
- If the focal point is at the 1st ritual, the strain is $1 + (3 + 4 + 2) = 10$.
- If the focal point is at the 2nd ritual, the strain is $(1 + 2) + (4 + 2) = 9$.
- If the focal point is at the 3rd ritual, the strain is $(1 + 2 + 3) + 2 = 8$.

The void will choose the focal point that maximizes the strain, which is 10. No other sequence results in a smaller maximum strain.