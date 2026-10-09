# Problem B — Chemical Demonstration

Time limit: 2 s   Memory limit: 256 MB

## Description
A laboratory must demonstrate a set of $n$ chemical reactions. The reactions are assigned unique identifiers from 1 to $n$. They must be conducted one at a time in a single primary vessel, with the vessel fully cleaned between each demonstration. You must arrange the entire set of $n$ reactions into a single sequential timeline.

The laboratory has compiled a list of $m$ safety protocols. Each protocol specifies two reactions, $a$ and $b$, and dictates that reaction $a$ must be demonstrated at some earlier point in the timeline than reaction $b$. 

You may assume that for every safety protocol provided, the absolute difference between the identifiers of the two reactions is strictly less than $n$. Furthermore, the sum of their identifiers will never exceed $2n$.

Your task is to determine a complete timeline that accommodates all $n$ reactions while satisfying every safety protocol concurrently. If the protocols logically contradict one another such that no such timeline can be formed, you must report this.

## Input
The first line contains two integers $n$ and $m$. 
Each of the next $m$ lines contains two integers $a$ and $b$, indicating a safety protocol where reaction $a$ must be demonstrated before reaction $b$.

## Output
If a valid timeline is possible, print `YES` followed by a space-separated sequence of $n$ integers (containing each identifier from 1 to $n$ exactly once) representing the order of reactions. Otherwise, print `NO`.

## Example 1

**Input:**
```text
3 2
1 2
2 3
```

**Output:**
```text
YES
1 2 3
```

## Example 2

**Input:**
```text
3 3
1 2
2 3
3 1
```

**Output:**
```text
NO
```
