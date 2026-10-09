# Establishing the Narrative

Time limit: 2 s   Memory limit: 256 MB

## Description
A high-profile public inquiry is scheduled to hear testimonies from a specific headcount of witnesses. The presiding commissioner will hear from exactly one witness at a time, and every witness must take the stand exactly once until the inquiry concludes. 

To ensure the narrative makes sense, the investigative team has identified several foundational dependencies. Each dependency specifies that a particular piece of context must be established before another can be introduced. Consequently, the witness providing the foundational context must take the stand at some point before the witness who builds upon it. 

The inquiry's schedule is simply a complete sequence of all the witnesses. Your task is to organize this sequence. Setup times, witness priorities, and the specific contents of the testimonies are irrelevant; any sequence is acceptable as long as it respects every single foundational dependency at once. 

Produce such a sequence, or report that the dependencies contradict one another—for example, if a chain of context requirements loops back on itself, making it impossible to schedule everyone. (With multiple commissioners this kind of planning becomes highly demanding; with a single commissioner, honoring the foundational dependencies is all that is asked, and any valid sequence is acceptable.)

## Input
The first line contains two integers $n$ and $m$: the total headcount of witnesses, and the tally of foundational dependencies. 
Each of the next $m$ lines details a single dependency using two badge numbers. Every witness is issued a unique integer badge; these badges form a continuous range where the lowest is exactly one, and the highest corresponds exactly to $n$. Two badges $x$ and $y$ on a line indicate that the witness holding badge $x$ must testify before the witness holding badge $y$.

## Output
Print `YES` then the badge numbers of all witnesses in a valid sequence, separated by spaces. If no such sequence is possible due to contradictions, print `NO`.

## Example 1
### Input
4 4
1 2
1 3
2 4
3 4
### Output
YES
1 2 3 4

## Example 2
### Input
3 3
1 2
2 3
3 1
### Output
NO
