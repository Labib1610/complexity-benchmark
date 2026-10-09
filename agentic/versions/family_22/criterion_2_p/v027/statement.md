# Problem B — Fresco Restoration Sequence

Time limit: 2 s   Memory limit: 256 MB

## Description
During the restoration of a delicate fresco, $n$ distinct chemical treatments (numbered 1 through $n$) must be applied. Extensive laboratory testing has established $m$ safety protocols regarding their use. Each protocol consists of a pair of treatments, $a$ and $b$, and mandates that treatment $a$ must be entirely completed before treatment $b$ can be initiated. Violating any of these protocols will cause an irreversible reaction that destroys the pigments.

Because the restoration is performed inside a single climate-controlled isolation chamber, the application process is strictly sequential. At any given moment, exactly one treatment is being administered, and no treatment can be split into parts.

Your task is to evaluate the provided safety protocols and determine whether they are logically consistent. If the protocols do not inherently contradict one another, you must generate a comprehensive schedule. This schedule must be a single sequence of all $n$ treatments that satisfies every safety protocol simultaneously. If multiple valid sequences exist, any sequence that meets all requirements is acceptable.

## Input
The first line contains two integers $n$ and $m$. 
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that treatment $a$ must be completed before treatment $b$.

## Output
Print `YES` then a space-separated permutation of 1 to $n$ (a valid application order); otherwise print `NO`.

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
