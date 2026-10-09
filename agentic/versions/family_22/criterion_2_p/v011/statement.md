# Crucible of the Elements

Time limit: 2 s
Memory limit: 256 MB

## Description
A grand artificer is forging a legendary artifact by fusing $n$ distinct elemental cores. The fusion process takes place in a single crucible, meaning the cores must be dropped into the mixture one at a time until all $n$ have been added.

The elemental cores are highly reactive. Through trial and error, past artificers have documented $m$ strict stability laws. Each law specifies that a certain core must already be stabilizing in the crucible before another specific core can be safely introduced. If a core is dropped into the crucible before one of its required predecessors is present, the reaction will fail catastrophically. 

Your task is to determine a complete, linear sequence for adding all $n$ cores that respects every single documented stability law. The physical properties of the cores and the time it takes them to melt are irrelevant; the only constraints on the order of additions are these stability laws. If the laws contradict each other—for example, if a sequence of laws creates an impossible loop of requirements—you must declare the artifact impossible to forge. Any sequence that includes all $n$ cores exactly once and satisfies all $m$ laws is considered a valid fusion process.

## Input
The first line contains two integers $n$ and $m$, representing the number of elemental cores and the number of stability laws, respectively. The cores are numbered from $1$ to $n$.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that core $a$ must be added to the crucible at some point before core $b$ is added.

## Output
If a safe fusion sequence exists, print `YES` followed by a valid sequence of the $n$ cores (a permutation of the integers $1$ through $n$, separated by spaces). If there are multiple valid sequences, any of them will be accepted. If no such sequence is possible, print `NO`.

## Examples

**Input 1**
```
5 5
1 2
1 3
2 4
3 4
4 5
```

**Output 1**
```
YES
1 3 2 4 5
```
*(Note: `1 2 3 4 5` would also be accepted as a valid sequence.)*

**Input 2**
```
3 3
1 2
2 3
3 1
```

**Output 2**
```
NO
```
