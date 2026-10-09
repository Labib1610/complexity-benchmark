# Problem B — Pipeline Optimization

Time limit: 1 s   Memory limit: 256 MB

## Description

You are optimizing a data pipeline that processes a batch of **j** datasets. Each dataset requires two consecutive stages: Extraction and Transformation. You must arrange the datasets into a single processing sequence.

The pipeline follows these operational rules:
- The Extraction stage processes datasets one by one in your chosen sequence. It begins the first dataset at time 0 and operates continuously, starting each subsequent dataset the instant the previous one finishes.
- The Transformation stage processes datasets one by one in the exact same sequence you chose.
- A dataset can only begin its Transformation stage after its Extraction stage is completely finished.
- The Transformation stage processes only one dataset at a time. For the first dataset, Transformation begins exactly when its Extraction finishes. For all subsequent datasets, Transformation begins exactly when its Extraction finishes, or exactly when the previous dataset's Transformation finishes, whichever is later.

For each dataset, you are given the time **p1** it requires for Extraction, and the time **p2** it requires for Transformation.

Determine the optimal sequence of datasets to minimize the time at which the Transformation stage completes the final dataset. Output this minimum possible time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the time required for a dataset in the Extraction stage and the Transformation stage, respectively.

## Output

Print a single integer: the smallest possible time at which the final dataset finishes its Transformation.

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

In Example 1, one optimal sequence is to process the 3rd dataset, then the 2nd, then the 1st.
- **3rd dataset:** Extraction takes 1 (finishes at 1). Transformation starts at 1 and takes 3 (finishes at 4).
- **2nd dataset:** Extraction takes 2 (finishes at 1 + 2 = 3). Transformation must wait for the previous dataset to finish at 4. It starts at 4 and takes 4 (finishes at 8).
- **1st dataset:** Extraction takes 3 (finishes at 3 + 3 = 6). Transformation must wait for the previous dataset to finish at 8. It starts at 8 and takes 2 (finishes at 10).
The final dataset finishes Transformation at time 10.

In Example 2, the single dataset takes 5 for Extraction and 3 for Transformation, finishing at time 8.