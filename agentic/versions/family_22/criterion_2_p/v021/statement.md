# Linear Gallery Curation

Time limit: 2 s   Memory limit: 256 MB

## Description
An art gallery is setting up a new exhibition in a long, narrow corridor. The exhibition will feature $n$ distinct art installations, labeled 1 to $n$. Visitors will walk down the corridor in a single direction, passing each installation exactly once in a linear sequence.

The physical dimensions of the artwork, the artists' identities, and the lighting requirements are all irrelevant to the layout. The only constraints on the arrangement are $m$ thematic guidelines established by the curator. Each guideline specifies a pair of installations, $a$ and $b$, and mandates that installation $a$ must appear earlier in the sequence than installation $b$. This ensures visitors experience the thematic progression as intended.

You must determine if it is possible to arrange all $n$ installations in the corridor such that all $m$ guidelines are simultaneously respected. A valid arrangement is any complete linear sequence of the $n$ installations from the entrance to the exit that honors every guideline.

Produce such an arrangement, or report that the guidelines are mutually contradictory — for instance, if a chain of thematic rules makes it impossible to place every installation earlier than the ones it is supposed to precede.

## Input
First line: two integers $n$, $m$. 
Each of the next $m$ lines: two integers $a$ and $b$ — installation $a$ must appear earlier than installation $b$.

## Output
Print `YES` then a permutation of 1..n (a valid sequence of the installations from first to last); otherwise `NO`.

## Example 1
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

## Example 2
### Input
```
3 3
1 2
2 3
3 1
```
### Output
```
NO
```
