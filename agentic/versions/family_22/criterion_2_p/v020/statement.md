# Reagent Sequencing

Time limit: 2 s
Memory limit: 256 MB

## Description
A new synthetic material requires exactly $n$ distinct liquid reagents, numbered 1 through $n$, to be poured into a central vat. The reagents must be added strictly one at a time. The final properties of the material are not affected by the exact timing of the additions, only by the relative order in which the chemicals are introduced.

However, certain reactions are highly volatile. To prevent an uncontrolled reaction, the laboratory has established a set of strict safety guidelines. Each guideline mandates that a specific reagent must already be present in the vat before another specific reagent can be added. If a guideline states that reagent $a$ must precede reagent $b$, then $a$ must be poured into the vat at some point before $b$ is poured (not necessarily immediately before).

Your task is to determine a complete sequence for adding all $n$ reagents such that every safety guideline is satisfied. If the guidelines form a logical contradiction (meaning no safe sequence exists), you must report this. Any sequence that includes all $n$ reagents exactly once and satisfies all guidelines is acceptable.

## Input
The first line contains two integers $n$ and $m$, representing the number of reagents and the number of safety guidelines, respectively. 
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that reagent $a$ must be added to the vat before reagent $b$.

## Output
If a safe sequence exists, print `YES` on the first line, and on the second line print a sequence of the integers from 1 to $n$ separated by spaces, representing a valid addition order. If there are multiple valid orders, any of them will be accepted. 
If no safe sequence is possible, print `NO`.

## Example 1
**Input:**
```
4 4
1 2
2 3
1 4
4 3
```
**Output:**
```
YES
1 2 4 3
```

## Example 2
**Input:**
```
3 3
1 2
2 3
3 1
```
**Output:**
```
NO
```
