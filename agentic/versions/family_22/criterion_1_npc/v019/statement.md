# Problem A — Culinary Event Sequencing

Time limit: 5 s   Memory limit: 256 MB

## Description
You are designing a tasting menu for a high-profile banquet. There are $n$ distinct culinary creations to be served, numbered 1 to $n$. The banquet is structured as a sequence of distinct servings, numbered starting from 1. Each creation is presented exactly once, occupying exactly one serving.

In any single serving, the kitchen staff can prepare and present at most $M$ creations simultaneously. There is no benefit to leaving kitchen capacity unused, but there is also no penalty as long as the event finishes on time. The entire event must conclude within a maximum of $T$ servings.

To ensure the appropriate progression of flavors, certain creations must be experienced before others. You are given $m$ progression rules. For each rule indicating that creation $a$ must precede creation $b$, creation $a$ must be assigned to a strictly earlier serving number than creation $b$. Presenting them in the same serving is not permitted, as the palate must reset between them. 

Assign each of the $n$ creations to a serving number (from 1 to $T$) such that all progression rules are strictly respected and no serving contains more than $M$ creations, or report that such a menu cannot be designed. (With a small capacity $M$, the per-serving limit and the progression chains pull against each other, so a menu that respects the progression rules may still overflow the serving capacity, and vice versa.)

## Input
The first line contains four integers $n$, $M$, $T$, and $m$.
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that creation $a$ must be presented in a strictly earlier serving than creation $b$.

## Output
Print `YES` then $n$ integers (the serving number of each creation, in $1 \dots T$); otherwise print `NO`.

## Example

### Input
```
5 2 3 4
1 3
2 3
3 4
3 5
```

### Output
```
YES
1 1 2 3 3
```
