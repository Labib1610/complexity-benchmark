# Problem A — Deduplication Backup

Time limit: 5 s   Memory limit: 256 MB

## Description

You are managing a storage system containing **n** document files.
To save space, the system uses data deduplication. There are **m** shared data blocks in the system. Each of these data blocks is referenced by exactly two distinct document files.

For any document, its *reference count* is the number of shared data blocks it references.

When a set of documents is selected for an archive, the system calculates two metrics:
1. The *Total Reference Count*: the sum of the reference counts of all documents in the set.
2. The *Boundary Size*: the total number of shared data blocks that are referenced by **exactly one** document in the set.

Your task is to select exactly **k** document files from the **n** available files such that the *Boundary Size* is exactly equal to the *Total Reference Count*.

Notice how each shared data block contributes to these two metrics for a given selection:
- If a block is referenced by exactly one selected file, it adds 1 to the Boundary Size and 1 to the Total Reference Count.
- If it is referenced by two selected files, it adds 0 to the Boundary Size but 2 to the Total Reference Count.
- If it is referenced by zero selected files, it adds 0 to both metrics.

Therefore, the equality holds if and only if no shared data block has both of its referencing documents selected.

If such a selection exists, report it by listing the 1-based indices of the selected files.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 46, 0 ≤ **m** ≤ **n**·(**n**−1)/2, 1 ≤ **k** ≤ **n**).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), indicating that a shared data block is referenced by document **u** and document **v**. The input will never list the same pair of documents more than once.

## Output

If a valid selection exists, print `YES` on the first line, then on the second line print the **k** distinct indices of the selected documents, separated by spaces. If multiple valid selections exist, any valid selection is accepted. Print only the **k** selected indices.

If no such selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```

## Note

In Example 2, if we select documents 1, 3, and 5:
- Document 1 references one shared block (shared with 2). Its reference count is 1.
- Document 3 references one shared block (shared with 4). Its reference count is 1.
- Document 5 references zero shared blocks. Its reference count is 0.
The Total Reference Count is 1 + 1 + 0 = 2.
The shared blocks in the system are (1, 2) and (3, 4).
- Block (1, 2) is referenced by exactly one selected document (document 1).
- Block (3, 4) is referenced by exactly one selected document (document 3).
The Boundary Size is 2.
Since the Boundary Size equals the Total Reference Count (2 = 2), this selection is valid.

In Example 1, consider selecting exactly 3 documents, for instance, 1, 2, and 4:
The Total Reference Count for 1, 2, and 4 is 2 + 2 + 1 = 5.
The blocks referenced by exactly one selected document are (1, 3), (2, 3), and (3, 4). Thus, the Boundary Size is 3.
Since 5 ≠ 3, this selection is invalid. In fact, no selection of exactly 3 documents will satisfy the required equality.