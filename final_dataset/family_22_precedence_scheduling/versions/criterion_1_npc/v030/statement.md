# Problem A — Arranging the Tasting Experience

Time limit: 5 s   Memory limit: 256 MB

## Description
A culinary team is designing a tasting experience featuring $n$ distinct dishes, numbered $1$ to $n$. The event is partitioned into a sequence of $T$ consecutive stages. During any given stage, guests are presented with a selection of dishes to sample. To ensure the kitchen staff can maintain quality, no single stage may include more than $M$ dishes. Every dish must be featured in exactly one stage.

The chefs have established a set of $m$ flavor progression dictates. Rather than providing a holistic map of the menu, these are given as individual rules where a specific dish prepares the palate for another. If a dictate states that dish $a$ prepares the palate for dish $b$, dish $a$ must be assigned to a stage with a strictly smaller index than the stage for dish $b$. Serving them in the same stage is not permitted, as the palate requires the transition between stages to fully reset.

A small per-stage capacity often pulls against long chains of progression dictates, so an arrangement that satisfies all flavor rules might still overflow the capacity of individual stages, and vice versa. Determine if all $n$ dishes can be assigned to the $T$ stages such that no stage exceeds the limit of $M$ dishes and every progression dictate is respected.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$. 
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that dish $a$ must be assigned to a strictly earlier stage than dish $b$.

## Output
If a valid arrangement is possible, print `YES` followed by a space-separated sequence of $n$ integers, where the $i$-th integer represents the stage (from $1$ to $T$) assigned to dish $i$. Otherwise, print `NO`.

## Example

### Input
```text
5 2 3 4
1 3
2 3
3 4
3 5
```

### Output
```text
YES
1 1 2 3 3
```
