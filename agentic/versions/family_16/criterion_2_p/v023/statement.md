# Geode Extraction Protocol

Time limit: 1 s   Memory limit: 256 MB

## Description

You are managing a harvesting operation in the Whispering Caves. Your team must harvest a specific number of geodes. 

The harvesting of each geode requires two sequential phases:
- **Phase 1: Illumination.** The Lightbearer must focus a beam on the geode to weaken its shell.
- **Phase 2: Extraction.** The Miner must strike the geode to free it from the rock.

The operation must follow these strict protocols:
- The team has exactly one Lightbearer and exactly one Miner. Each individual can only work on a single geode at any given moment.
- The Miner cannot begin extraction on a geode until the Lightbearer has completely finished illuminating that specific geode.
- The sequence in which the geodes are illuminated must be exactly the same sequence in which they are extracted. You are responsible for choosing this sequence.

Your goal is to determine the optimal sequence to minimize the total duration of the operation. The operation concludes the moment the Miner finishes extracting the final geode in the sequence. Return this minimum possible completion time.

## Input

The first line contains a single integer **C**, representing the number of geodes. The expedition targets at least a single geode, up to the transport cart's maximum structural limit of exactly 200,000 geodes.

Each of the next **C** lines contains two integers **t1** and **t2**, representing the time in seconds required for the Lightbearer and the Miner to complete their respective phases for that geode. Every phase takes at least a single second. Due to thermal limits on the equipment, no single phase will ever require more than exactly 1,000,000 seconds.

## Output

Print a single integer: the earliest possible second at which all geodes have been completely extracted.

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

In Example 2, the solitary geode requires 5 seconds of illumination followed by 3 seconds of extraction, concluding the operation at exactly 8 seconds.
