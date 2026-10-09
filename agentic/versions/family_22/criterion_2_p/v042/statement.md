# Establishing the Chronology

Time limit: 2 s   Memory limit: 256 MB

## Description
A research team has uncovered a series of distinct historical incidents. To publish their findings, they must arrange these incidents into a single, continuous chronological timeline from earliest to latest.

While the exact dates are lost, translators have recovered several ancient texts. Each text provides a relative clue by confirming that one specific incident took place before another. The timeline must be a single list containing all the discovered incidents exactly once. The exact duration, geographical location, and severity of the incidents are irrelevant. The only constraints on your timeline are the relative chronological clues provided by the texts. To be considered historically valid, the published timeline must not contradict any of the recovered clues. That is, whenever a text indicates that an incident happened earlier than another, the former must be placed closer to the beginning of the timeline than the latter.

Your task is to determine whether a timeline can be formed that satisfies every translated clue simultaneously. If the clues are fundamentally inconsistent—for example, if they create a paradox where a chain of clues implies an incident precedes itself—you must declare the chronological reconstruction impossible. Otherwise, provide any one timeline that fully aligns with all the clues.

## Input
The first line contains two integers $n$ and $m$, representing the number of historical incidents (numbered $1$ through $n$) and the number of recovered clues.  
Each of the following $m$ lines contains two integers $a$ and $b$, meaning a clue states that incident $a$ occurred before incident $b$.

## Output
If a valid timeline can be established, print `YES` on the first line, followed by a second line containing a sequence of the $n$ integers separated by spaces, representing the incidents in chronological order. If multiple valid timelines exist, any sequence that respects all clues is acceptable.  
If no such timeline is possible, print `NO`.

## Example

### Input
```
4 4
1 2
1 3
2 4
3 4
```

### Output
```
YES
1 2 3 4
```
