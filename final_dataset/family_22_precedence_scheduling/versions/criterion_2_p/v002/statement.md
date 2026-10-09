# Problem B — Reconstructing the Timeline

Time limit: 2 s   Memory limit: 256 MB

## Description
A single historian must work through a batch of distinct historical events, one after another, until the whole timeline is reconstructed. Some events produce outcomes that other events react to, which imposes chronological requirements: whenever one event must occur before another can happen, the first event has to appear earlier in the timeline's sequence than the second. Because there is only one timeline, exactly one event takes place at any moment and the chronology is simply a linear order of all the events.

Exact dates, event significance, durations, and the physical nature of the evidence are all irrelevant to acceptance; the only thing that constrains the order is the collection of "occurred-before" requirements between pairs of events. A valid answer is any complete ordering of every event in the batch that honours all of these requirements at once.

Produce such an ordering, or report that the requirements are mutually contradictory — for instance if a cycle of deductions makes it impossible to place every event after all the events it depends on. (With several regions and a specific timeframe this kind of reconstruction becomes genuinely hard; on a single timeline with no specific timeframe, honouring the occurred-before requirements is all that is asked, and any order that respects them is acceptable.)

## Input
First line: two integers $n$, $m$. Each of the next $m$ lines: two integers $a$ $b$ — event $a$ happened before event $b$.

## Output
Print `YES` then a permutation of 1..$n$ (a valid chronological order); otherwise `NO`.

## Example

### Input
3 2
1 2
2 3

### Output
YES
1 2 3
