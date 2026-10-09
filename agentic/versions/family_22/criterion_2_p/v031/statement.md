# Problem B — Sequencing the Roster on One Stage

Time limit: 2 s   Memory limit: 256 MB

## Description
A single stage must host a roster of guest speakers, one after another, until the whole event is done. Some speakers introduce core concepts that other speakers rely on, which imposes ordering requirements: whenever one speaker must present before another can begin, the first speaker has to appear earlier in the stage's schedule than the second. Because there is only one stage, exactly one speaker is presenting at any moment and the schedule is simply a linear order of all the speakers.

Transition times, speaker priorities, time slots, and the specific topics of the concepts are all irrelevant to acceptance; the only thing that constrains the order is the collection of "present-before-start" requirements between pairs of speakers. A valid answer is any complete ordering of every speaker on the roster that honours all of these requirements at once.

Produce such an ordering, or report that the requirements are mutually contradictory — for instance if a cycle of dependencies makes it impossible to place every speaker after all the speakers they depend on. (With several stages and a deadline this kind of planning becomes genuinely hard; on a single stage with no deadline, honouring the present-before-start requirements is all that is asked, and any order that respects them is acceptable.)

## Input
First line: two integers n, m. Each of the next m lines: two integers a b — speaker a before speaker b.

## Output
Print `YES` then a permutation of 1..n (a valid schedule order); otherwise `NO`.

## Example

### Input
```
3 2
1 2
2 3
```

### Output
```
YES
1 2 3
```
