# Problem A — Backbone Trenching for the Control Vault

Time limit: 5 s   Memory limit: 256 MB

## Description
A new control vault is being commissioned. Its $n$ modules must be installed along a single straight equipment trench. The trench is divided into $n$ consecutive mounting bays, numbered $1$ through $n$. Each module must be placed in exactly one bay, and each bay must hold exactly one module.

The modules exchange signals over point-to-point harnesses. There are $m$ such harnesses required. Whenever two modules must exchange signals, a harness is run between their bays. The physical length of a harness is determined solely by how many bay positions separate the two modules it connects. For example, modules in adjacent bays require one unit of harness; modules separated by one bay require two units, and so on.

Procurement has fixed a total harness budget $B$ for the job.

To pass the vault inspection, your installation plan must satisfy all of the following compliance directives:
1. Every module must be assigned a distinct bay number from $1$ to $n$.
2. The sum of the bay positions assigned to all $n$ modules must be exactly $n(n+1)/2$.
3. For every individual harness, its physical length (the absolute difference between the bay numbers of the two connected modules) must be strictly less than $n$.
4. The sum of the lengths of all $m$ harnesses must not exceed $B$.

Decide whether the modules can be placed to satisfy all inspection directives, and if so, output a valid placement. Otherwise, report that no such placement exists.

## Input
The first line contains three integers $n$, $m$, and $B$, representing the number of modules (and bays), the number of required harnesses, and the maximum total harness budget, respectively.
The next $m$ lines each contain two integers $u$ and $v$, indicating that a harness must connect module $u$ and module $v$.

## Output
If a compliant installation plan exists, print `YES` on the first line. On the second line, print $n$ integers representing the bay positions assigned to modules $1, 2, \dots, n$ respectively.
If no such plan is possible, print `NO`.

## Example

### Input
```
4 3 4
1 2
2 3
3 4
```

### Output
```
YES
1 2 3 4
```
