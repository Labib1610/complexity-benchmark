# Preventative Valve Actuation

Time limit: 5 s   Memory limit: 256 MB

## Description
A chemical processing plant operates a network of storage vats connected by bidirectional fluid pipes. Each pipe is equipped with a failsafe valve. Activating a valve permanently halts all fluid transfer through that specific pipe, but doing so incurs a mechanical adjustment cost.

Several specific vats in the network are classified as primary injectors, each holding a distinct, highly reactive catalyst. If the catalysts from any two different primary injectors ever come into contact, it will trigger a catastrophic failure. Plant engineers must actuate a subset of the valves to guarantee that no sequence of open pipes exists between any two primary injectors. Vats that are not primary injectors are considered inert; they may end up connected to other inert vats or to a single primary injector, provided the primary injectors themselves remain strictly separated from one another.

The facility has a fixed maintenance budget for this operation. You must identify a set of valves to actuate such that every primary injector is isolated from all others, and the total adjustment cost does not exceed the budget. If it is impossible to achieve this separation within the given budget, you must report that it cannot be done. (Note that while separating a single pair of injectors might be inexpensive, the budget must be sufficient to mutually separate all primary injectors simultaneously).

## Input
The first line contains four integers: the total number of vats, the total number of pipes, the number of primary injectors, and the maximum allowed maintenance budget.
The second line contains a sequence of integers identifying the vats that act as primary injectors.
Each of the subsequent lines describes a single pipe using three integers: the IDs of the two vats it connects, followed by the cost to actuate its valve.

## Output
If a valid set of valves can be actuated within the budget, output `YES` on the first line. On the second line, output the number of actuated valves, $c$. Then, output $c$ lines, each containing the two vat IDs connected by an actuated valve. 
If it is impossible to separate all primary injectors within the budget, output `NO`.

## Example 1

### Input
```
4 3 3 5
1 2 3
1 4 2
2 4 3
3 4 4
```

### Output
```
YES
2
1 4
2 4
```

## Example 2

### Input
```
4 3 3 4
1 2 3
1 4 2
2 4 3
3 4 4
```

### Output
```
NO
```
