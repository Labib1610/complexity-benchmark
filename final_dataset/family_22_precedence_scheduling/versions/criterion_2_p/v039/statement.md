# Problem B — Sequencing the Welds on One Robotic Arm

Time limit: 2 s   Memory limit: 256 MB

## Description
A single robotic arm must execute a batch of unit-time welding tasks, one after another, until the whole batch is done. Certain tasks fuse metal brackets that other tasks must attach components to, which imposes precedence requirements: whenever one weld must cool before another can be applied, the first weld has to appear earlier in the arm's processing order than the second. Because there is only one robotic arm, exactly one weld is in progress at any moment and the schedule is simply a linear order of all the tasks.

Setup times, weld priorities, and the physical shape of the brackets are all irrelevant to acceptance; the only thing that constrains the schedule is the collection of "cool-before-weld" requirements between pairs of tasks. A valid answer is any complete ordering of every weld in the batch that honours all of these requirements at once.

Produce such an ordering, or report that the requirements are mutually contradictory — for instance if a cycle of cooling dependencies makes it impossible to place every weld after all the welds it depends on. (With several arms this kind of planning becomes genuinely hard; on a single arm with no deadline, honouring the cool-before-weld requirements is all that is asked, and any order that respects them is acceptable.)

## Input
First line: two integers n, m. Each of the next m lines: two integers a b — weld a before weld b.

## Output
Print `YES` then a permutation of 1..n (a valid processing order); otherwise `NO`.

## Example

### Input
4 4
1 2
1 3
2 4
3 4

### Output
YES
1 2 3 4
