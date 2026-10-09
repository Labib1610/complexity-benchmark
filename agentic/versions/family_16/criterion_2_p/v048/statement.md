# Problem B — Data Migration Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

A central data warehouse handles daily migration batches containing **j** distinct records. The migration lifecycle consists of three distinct phases:

1. **Validation**: The batch is scanned and metadata is generated. This phase is already complete before you intervene.
2. **Transformation**: This is the core bottleneck. Every record must first run through the extraction service, and then it must run through the encoding service.
3. **Archiving**: Once the entire batch of records has fully cleared the transformation phase, the batch is pushed to long-term cold storage.

You are responsible for optimizing the Transformation phase. The infrastructure enforces strict concurrency rules:
- The extraction service and the encoding service can each process only a single record at a time.
- A record cannot be fed into the encoding service until its extraction is strictly finished.
- If the encoding service is currently occupied, any record that has finished extraction will sit idle in a queue.
- To maintain consistency for the Archiving phase, the batch coordinator requires you to choose a single global ordering of the records. The extraction service will process the records exactly in this order, and the encoding service will also process the records exactly in this same order.

The metadata from the Validation phase provides the exact time required to extract and encode each record. Your objective is to determine a global ordering that minimizes the total duration of the Transformation phase—measured from the instant the first record enters extraction until the final record finishes encoding—so that the Archiving phase can begin as early as possible.

## Input

The first line provides a single integer **j** (1 ≤ **j** ≤ 200000), representing the number of records in the daily batch.
The following **j** lines each contain two integers, **p1** and **p2** (1 ≤ **p1**, **p2** ≤ 1000000). These represent the durations required for a record in the extraction service and the encoding service, respectively.

## Output

Output a single integer: the earliest possible time the Archiving phase can begin (which is strictly the minimum possible total duration of the Transformation phase).

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single record takes 5 time units in the extraction service and then 3 time units in the encoding service, letting the Archiving phase begin at time 8.
