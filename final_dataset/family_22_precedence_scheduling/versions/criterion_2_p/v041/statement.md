# Problem B — Reconstructing the Narrative

Time limit: 2 s   Memory limit: 256 MB

## Description
A historian is compiling a comprehensive narrative from a batch of distinct historical fragments. The fragments must be arranged one after another into a single uninterrupted sequence until the entire collection is processed. 

Certain fragments establish context that other fragments rely upon. Whenever fragment $a$ provides context for fragment $b$, the historian must position fragment $a$ earlier in the sequence than fragment $b$. The narrative structure is strict: exactly one fragment occupies each position in the sequence, and all fragments from the batch must be included.

Exact dates, event significance, and physical evidence are irrelevant. The only restriction on the arrangement is the set of contextual dependencies between specific pairs of fragments. Any complete arrangement of the fragments that satisfies every dependency simultaneously is considered valid.

Provide a valid sequence, or determine if the dependencies inherently contradict one another—for example, if a chain of context references eventually requires a fragment to precede itself, making it impossible to finalize the arrangement.

## Input
The first line contains two integers $n$ and $m$, representing the number of fragments and the number of contextual dependencies, respectively. Fragments are identified by integers from 1 to $n$.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that fragment $a$ provides context for fragment $b$ (and therefore must appear earlier in the sequence).

## Output
If a valid sequence exists, print `YES` on the first line, followed by a space-separated list of the $n$ fragment identifiers in an acceptable order on the second line. If no such arrangement is possible, print `NO`.

## Example

### Input
3 2
1 2
2 3

### Output
YES
1 2 3
