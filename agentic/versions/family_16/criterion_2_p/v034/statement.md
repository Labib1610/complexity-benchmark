# Problem B — Sequential Asset Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

You are tasked with routing a batch of digital assets through a two-phase pipeline. Every asset must pass through the encoding module first, and subsequently through the uploading module. The pipeline operates under the following conditions:

- The encoding module can handle only a single asset at any given moment.
- The uploading module can also handle only a single asset at any given moment.
- An asset becomes available for the uploading module only at the exact moment its encoding is fully completed.
- You must determine a single sequence for the assets. The encoding module will process the assets in this exact sequence, and the uploading module will process them in the very same sequence.

Your objective is to arrange the sequence of assets such that the total time elapsed from the start of the first asset's encoding until the final asset completes its uploading phase is as small as possible. Determine this minimum possible elapsed time for the entire batch.

## Input

The first line provides the number of assets in the batch. This count is at least one, and is constrained by the system's maximum batch capacity of exactly two hundred thousand.

Each subsequent line details an asset by providing two integers: its encoding duration and its uploading duration. Every duration requires at least one unit of time, and cannot exceed the protocol's maximum timeout threshold of exactly one million units of time.

## Output

Provide a single integer representing the minimum possible time elapsed from the start of the pipeline until all assets have successfully completed the uploading phase.

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
