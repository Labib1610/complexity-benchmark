# Problem B — Restoring Mine Circulation

Time limit: 2 s   Memory limit: 256 MB

## Description

A massive underground mine consists of $n$ caverns (numbered sequentially starting from 1). The total number of caverns $n$ is at least one, limited by the mine's structural maximum of two hundred thousand caverns. 

There are $m$ ventilation shafts. The total count of shafts $m$ is exactly one fewer than the number of caverns. Each shaft connects two distinct caverns. The shafts are laid out so that air can travel between any two caverns, and there are no alternative routes—exactly one sequence of shafts links any given pair of caverns.

An incident has occurred, and miners are trapped in $t$ specific caverns. There is at least one such cavern, and there could be up to $n$ of them.

You must restore air circulation among the trapped miners. To do this, you will clear blockages in a selected set of shafts so that all $t$ caverns containing trapped miners end up connected to one another (either directly or through intermediate caverns) using only the cleared shafts. 

Clearing a shaft requires a certain amount of energy $w$. The energy $w$ for any single shaft is a minimum of one joule and caps at a maximum of one million joules. You need to determine the minimum total energy required to clear a set of shafts that successfully links all caverns with trapped miners.

## Input

The first line contains three integers $n$, $m$, and $t$, obeying the physical limits described above.
The second line contains $t$ distinct integers: the identifiers of the caverns with trapped miners.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$, describing a shaft between cavern $u$ and cavern $v$ (where $u$ and $v$ are distinct valid cavern identifiers) that requires $w$ joules to clear.

## Output

Print a single integer: the minimum total energy required to clear a set of shafts that connects all caverns with trapped miners.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```
