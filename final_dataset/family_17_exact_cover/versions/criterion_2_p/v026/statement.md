# Phase II: Synthesis Alignment

Time limit: 2 s   Memory limit: 256 MB

## Description
The automated pharmaceutical pipeline operates in three distinct phases. Your software module is responsible strictly for Phase II.

In Phase I, the synthesizer generates exactly $q$ acidic precursors (assigned consecutive identifiers from $1$ to $q$) and exactly $q$ alkaline precursors (assigned identifiers from $q+1$ to $2q$). The Phase I environmental sensor then tests all precursors in a rapid spectroscopic scan and outputs a discrete list of viable covalent links. A viable link always connects one acidic precursor to one alkaline precursor.

Your module executes Phase II. It must process the list of viable links from Phase I and determine if it is possible to achieve total batch crystallization. Total crystallization occurs if and only if every single precursor (both acidic and alkaline) is utilized in exactly one link, with no precursors left unlinked and no precursor participating in more than one link. You are restricted to using only the links validated by the Phase I scan.

If you determine that total crystallization is possible, you must output the exact set of links to be utilized. This output is immediately passed to Phase III, which physically induces the links. If your module determines that no such configuration exists, it must output a specific rejection signal so the pipeline can flush the batch and abort Phase III altogether. 

## Input
The first line of the input contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of acidic precursors (which is also the number of alkaline precursors) and the total number of viable links identified by Phase I.
This is followed by $t$ lines, each containing two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that the Phase I sensor has validated a link between precursor $a$ and precursor $b$.

## Output
If Phase III can proceed with total crystallization, print `YES` followed by $q$ lines, each containing the two precursor identifiers of one chosen link.
If total crystallization is impossible from the given viable links, print `NO`.

## Example 1
### Input
```text
3 4
1 4
2 4
2 5
3 6
```
### Output
```text
YES
1 4
2 5
3 6
```

## Example 2
### Input
```text
2 2
1 3
2 3
```
### Output
```text
NO
```
