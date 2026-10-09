# Establishing the Narrative

Time limit: 2 s   Memory limit: 256 MB

## Description
An investigative tribunal is organizing a series of testimonies. The presiding official will listen to exactly one individual at a time. The proceedings will conclude only after every summoned individual has spoken exactly once.

To ensure the events recounted make logical sense, the legal team has established a set of procedural rules. Each rule mandates that a specific piece of context must be introduced before another related topic can be discussed. As a result, the individual providing the earlier context must take the stand at some moment prior to the individual whose testimony relies on it.

The schedule for the tribunal is a complete ordering of all the individuals. Your objective is to formulate this ordering. Factors such as preparation time or specific testimony content do not matter; any ordering is valid provided it simultaneously satisfies every single procedural rule.

Determine such an ordering, or determine if the rules contradict each other—for instance, if a chain of requirements loops back on itself, making it impossible to formulate a schedule.

## Input
The first line contains two integers: the total headcount of individuals summoned, and the total count of procedural rules. 

Each of the subsequent lines describes a single rule using two ID tags. Individuals are identified by sequential ID tags. The initial tag is numbered one, and each subsequent tag increases by exactly one until every individual has received a tag (meaning the maximum tag number corresponds exactly to the headcount). Two tags $x$ and $y$ on a line mean the individual holding tag $x$ must testify before the individual holding tag $y$.

## Output
Print `YES` then the ID tags of all individuals in a valid sequence, separated by spaces. If no such sequence can be formed due to contradictions, print `NO`.

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
