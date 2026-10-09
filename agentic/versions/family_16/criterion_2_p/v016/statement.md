# Problem B — Data Pipeline Optimization

Time limit: 1 s   Memory limit: 256 MB

## Description

A computing cluster is tasked with processing $j$ continuous data streams using exactly two specialized nodes: the Extractor and the Analyzer. 

The pipeline must operate under the following conditions:
- Every data stream must be processed first by the Extractor, and then by the Analyzer.
- A stream can only begin processing on the Analyzer after its processing on the Extractor has completely finished.
- The Extractor and the Analyzer can each handle only a single stream at a time.
- A single, universal processing sequence must be chosen. The Extractor will process the streams in this chosen sequence, and the Analyzer will process the streams in the exact same chosen sequence.
- The absolute difference in processing times between the Extractor and the Analyzer for any given stream is guaranteed to be at most 999,999.
- The combined processing time of any single stream across both nodes will never exceed 2,000,000.

Your objective is to determine a processing sequence that minimizes the total elapsed time from the start of the first extraction to the completion of the final analysis. Output this minimum possible completion time.

## Input

The first line provides a single integer $j$ ($1 \le j \le 200,000$), representing the number of data streams.
The following $j$ lines each contain two integers $e$ and $a$ ($1 \le e, a \le 1,000,000$), denoting the processing times required for the stream on the Extractor and the Analyzer, respectively.

## Output

Output a single integer representing the earliest possible time at which the Analyzer can finish processing all streams.

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
