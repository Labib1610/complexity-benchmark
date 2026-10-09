# Problem B — Pressurizing the Habitat

Time limit: 2 s
Memory limit: 256 MB

## Description

A deep-space habitat consists of a collection of modules. To ensure structural integrity without redundancy, the modules are linked by transit tubes such that there is exactly one sequence of tubes connecting any two modules.

A subset of these modules are designated as command centers. You must select a set of tubes to pressurize so that all command centers can communicate with each other exclusively through the pressurized tubes (either directly or via intermediate modules). 

Pressurizing a tube requires a certain amount of energy. Your goal is to determine the minimum total energy required to pressurize a valid set of tubes. 

The habitat's design imposes several physical and operational limits:
- The total number of modules, $n$, is at least one and cannot exceed the habitat's maximum architectural capacity of two hundred thousand.
- The number of command centers, $t$, is at least one and can scale up to include all $n$ modules.
- The total number of transit tubes, $m$, is always exactly one less than the number of modules.
- The energy $w$ required to pressurize any single tube is a positive integer, limited by the local generator's maximum output of one million units.

## Input

The first line contains three integers $n$, $m$, and $t$, representing the number of modules, the number of transit tubes, and the number of command centers, respectively. 

The second line contains $t$ distinct integers representing the identifiers of the command centers. Modules are identified by integers starting from one up to $n$.

Each of the following $m$ lines contains three integers $u$, $v$, and $w$. These indicate a transit tube connecting module $u$ and module $v$ ($u \neq v$), requiring $w$ units of energy to pressurize. The tube layout adheres to the unique-path property described above.

## Output

Print a single integer: the minimum total energy required to pressurize a set of tubes that connects all command centers.

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
