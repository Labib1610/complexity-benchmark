# Problem B — Live Sync Scheduling

Time limit: 2 s   Memory limit: 256 MB

## Description
A localization agency pairs translators with proofreaders to finalize documents. Each document requires a live sync session involving exactly one specific translator and one specific proofreader, and no document is ever handled by two people of the same role. The agency's workflow dictates that some individuals are assigned more documents than others; the person assigned the highest number of documents determines the length of the scheduling cycle. Let this maximum number of documents for a single individual be $K$.

Routine finalization requires scheduling each document's live sync for exactly one hour slot. During any single hour slot, a translator can only participate in the sync of a single document. Similarly, a proofreader can only participate in the sync of a single document. Consequently, two documents involving the same individual—whether a translator or a proofreader—cannot be scheduled in the same hour slot. 

Since the busiest person is assigned $K$ documents, and none of their sessions can share an hour slot, the scheduling cycle requires at least $K$ hour slots. Your task is to generate a schedule that uses exactly $K$ hour slots. You must assign every document to an hour slot from $1$ to $K$ such that no person is involved in more than one sync session per slot.

## Input
First line: three integers $n_T$, $n_P$, $m$ ($1 \le n_T, n_P \le 100000$, $0 \le m \le 400000$), representing the number of translators, the number of proofreaders, and the number of documents.
Next $m$ lines: two integers $u$ $v$ ($1 \le u \le n_T$, $1 \le v \le n_P$) representing a document assigned to translator $u$ and proofreader $v$.

## Output
Print `YES`, then a line with $m$ integers in $1 \dots K$ — the hour slot assigned to document $i$ in input order (documents sharing any person must be assigned different hour slots).

## Example

### Input
```text
3 3 4
1 1
1 2
2 2
3 3
```

### Output
```text
YES
1 2 1 1
```
