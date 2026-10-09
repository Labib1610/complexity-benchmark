# Problem A — System Upgrade Isolation

Time limit: 5 s   Memory limit: 256 MB

## Description

A server cluster is undergoing a major infrastructure upgrade. The cluster's architecture consists of exactly **k** input streams, **k** computational units, and **k** storage modules, each indexed from 1 to **k**.

An automated diagnostic tool has evaluated the cluster and generated a log of operational links. Each operational link in the log connects exactly one input stream, one computational unit, and one storage module that can safely operate together without interference.

During the upgrade, the network controller must physically isolate the hardware using a subset of these logged links. To ensure system stability, the isolation phase must follow strict rules: every single input stream, computational unit, and storage module must be assigned to exactly one operational link. Consequently, no hardware piece can be left unassigned, and no piece can be shared across multiple links. A configuration that satisfies all these rules is known as a full allocation scheme.

Your task is to process the diagnostic log and determine if a full allocation scheme exists. If one can be formed, you must output the exactly **k** operational links that make up the scheme so the controller can proceed. If the hardware cannot be isolated according to the rules using the provided log, the upgrade must be aborted.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of components of each type and the total number of operational links in the diagnostic log.

Each of the next **t** lines contains three integers **s**, **c**, and **m** (1 ≤ s, c, m ≤ k), representing an operational link connecting input stream **s**, computational unit **c**, and storage module **m**. No link is listed more than once in the log.

## Output

If a full allocation scheme can be formed, print `YES` on the first line. Then, print **k** lines, each containing the three integers `s c m` corresponding to one of the operational links in your scheme. The links may be printed in any order. Any valid scheme that meets the isolation rules is accepted.

If no such scheme is possible, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both operational links require computational unit 1, meaning computational unit 2 would be left unassigned, which violates the isolation rules.
