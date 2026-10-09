# Problem B — Sequencing the Batch on One Station

Time limit: 2 s
Memory limit: 256 MB

## Description
A single manufacturing workstation must complete a batch of distinct operations. The workstation performs exactly one operation at a time until the entire batch is finished.

Some operations generate specific components that are strictly required by other operations. If operation $a$ generates a component needed by operation $b$, the workstation must perform operation $a$ at some point before it starts operation $b$. You are given the total number of operations in the batch and a list of these component relationships. 

Your goal is to arrange all the operations into a single continuous sequence that ensures every operation has its required components ready when its turn arrives. If the relationships contradict each other (for example, if a chain of requirements eventually requires an operation to be completed before itself), it is impossible to process the batch. In this case, you must report the failure.

## Input
The first line contains two integers $n$ and $m$, representing the total number of operations in the batch and the number of supplier-consumer relationships, respectively. Operations are identified by integers from $1$ to $n$.

Each of the next $m$ lines contains two integers $a$ and $b$, indicating that operation $a$ generates a component required by operation $b$.

## Output
If a valid sequence exists, print `YES` followed by all $n$ operation identifiers separated by spaces, in the order they should be performed. If no such sequence is possible, print `NO`.

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
