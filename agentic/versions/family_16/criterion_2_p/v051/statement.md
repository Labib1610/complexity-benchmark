# Problem B — Archive Decoding

Time limit: 1 s   Memory limit: 256 MB

## Description

An archaeological team has recovered **j** ancient scrolls. To fully decode a scroll, it must undergo a two-stage process: first, it must be transcribed by the team's sole linguist, and then it must be analyzed by the team's sole historian. 

All scrolls are available to the linguist at time 0. For each scroll, you are provided with the time required for transcription and the time required for analysis. The decoding process is subject to the following organizational rules:

- Each expert can only work on one scroll at a time.
- The historian cannot begin analyzing a scroll until the linguist has completely finished transcribing it.
- You must establish a single processing sequence for the scrolls. To maintain a strict chain of custody, the historian must analyze the scrolls in the exact same order that the linguist transcribes them.
- An expert will never remain idle if there is a scroll ready for their stage according to the sequence.

Your task is to arrange the initial sequence of the scrolls to minimize the time at which the historian finishes analyzing the final scroll. Output this minimum possible completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000), representing the number of scrolls.
Each of the following **j** lines contains two integers **t_transcribe** and **t_analyze** (1 ≤ t_transcribe, t_analyze ≤ 1000000), representing the duration of transcription and the duration of analysis for that scroll.

## Output

Print a single integer: the earliest possible time at which all scrolls are completely analyzed by the historian.

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

In Example 2, the single scroll takes 5 time units to transcribe and then 3 time units to analyze, completing the entire process at time 8.
