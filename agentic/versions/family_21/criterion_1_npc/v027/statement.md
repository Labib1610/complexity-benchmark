# Problem A — Suppressing Neural Feedback

Time limit: 5 s   Memory limit: 256 MB

## Description
An experimental neural culture contains $n$ neuron clusters. These clusters interact via $m$ bidirectional synaptic pathways. Administering a specific chemical inhibitor to a pathway permanently blocks it, stopping all signal transmission between its two endpoints. Each pathway requires a specific dosage of the inhibitor to be successfully blocked.

Within this culture, exactly $k$ clusters are identified as primary sensory anchors. To prevent feedback loops during the experiment, the pathways must be manipulated so that no signal can travel between any two different sensory anchors. A signal can propagate through any sequence of unblocked pathways. Consequently, there must be no intact route remaining between any pair of these $k$ anchors. The remaining $n - k$ clusters do not have strict placement rules; their final connectivity is irrelevant as long as the primary sensory anchors are completely separated from one another.

The culture can withstand a maximum total inhibitor dosage of $B$. You must decide which synaptic pathways to block. Your goal is to find a set of pathways whose combined dosage requirement is less than or equal to $B$, leaving all $k$ sensory anchors completely isolated from each other in terms of signal propagation. If such a configuration is possible, you must output the chosen pathways; otherwise, you must declare it impossible.

## Input
The first line contains four integers $n$, $m$, $k$, and $B$.
The second line contains $k$ integers representing the identifiers of the primary sensory anchors.
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating a synaptic pathway between cluster $u$ and cluster $v$ requiring an inhibitor dosage of $w$.

## Output
If it is possible to satisfy the conditions without exceeding the dosage limit $B$, print `YES` on the first line. On the second line, print an integer $c$ representing the number of blocked pathways. Then, output $c$ lines, each containing two integers $u$ and $v$, representing the endpoints of a blocked pathway.
If it is not possible, print `NO` on a single line.

## Example

### Input
```
4 3 3 10
1 2 3
1 4 3
2 4 4
3 4 5
```

### Output
```
YES
2
1 4
2 4
```
