# Phase Alignment in Asymmetric Data Fabrics

Time limit: 2 s   Memory limit: 256 MB

## Description
A communication system consists of a set of Primary modules and a set of Secondary modules. Data links are established such that every link bridges exactly one Primary module and one Secondary module. There are no links between two Primary modules, nor between two Secondary modules.

To prevent interference, each link must be assigned a transmission phase, represented by a positive integer. If multiple links connect to the same module (whether Primary or Secondary), they must all operate on strictly different phases.

The system's *peak concentration* is defined as the largest number of links connected to any single module across the entire system. Because this most heavily loaded module must distinctively phase all of its links, the system inherently requires at least that many phases.

Your task is to assign a phase to each link such that no module has two of its links on the same phase, and the total number of distinct phases used does not exceed the peak concentration. Due to the structural division between Primary and Secondary modules, it is a guaranteed property of the system that such an assignment is always possible without needing any extra phases beyond the peak concentration.

## Input
The first line contains three integers $n_P$, $n_S$, and $m$ ($1 \le n_P, n_S \le 100000$, $0 \le m \le 400000$), representing the number of Primary modules, the number of Secondary modules, and the number of data links, respectively. Primary modules are indexed from $1$ to $n_P$, and Secondary modules from $1$ to $n_S$.

The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_P$, $1 \le v \le n_S$), indicating a data link between Primary module $u$ and Secondary module $v$.

## Output
First, print `YES`.
On the next line, print $m$ integers separated by spaces. The $i$-th integer (in the order the links are given in the input) must be the phase assigned to the $i$-th link. Each phase must be an integer between $1$ and the peak concentration, inclusive. If multiple valid assignments exist, you may output any of them.

## Example

**Input**
```text
2 2 3
1 1
1 2
2 1
```

**Output**
```text
YES
1 2 2
```
