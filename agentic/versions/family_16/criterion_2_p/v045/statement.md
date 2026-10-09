# Problem B — Atmosphere Purification

Time limit: 1 s   Memory limit: 256 MB

## Description

You are overseeing the air purification system on a space station. The system processes a sequence of air canisters. A sequence contains $j$ canisters. There is always at least one canister, and the maximum number of canisters is limited by the storage rack, which contains exactly 2,000 shelves that each hold 100 canisters.

Every canister must pass through the particulate filter first, and then the chemical scrubber.
- Each device can process only one canister at a time.
- A canister cannot enter the chemical scrubber until it has completely finished in the particulate filter.
- The order in which canisters are fed into the system must be decided beforehand, and both devices will process the canisters in this exact same order.

The time required for a canister in each device is given in seconds. Each step takes at least one second. The maximum time any single canister can spend in one device is strictly limited by the device's automatic shutoff timer, which triggers after exactly one million seconds.

Your goal is to determine the sequence that minimizes the time when the last canister finishes its chemical scrubbing, so the station can resume normal operations as early as possible. Output this earliest possible completion time.

## Input

The first line contains a single integer $j$, representing the number of canisters.
Each of the following $j$ lines contains two integers: the time required in the particulate filter and the time required in the chemical scrubber for that canister.

## Output

Print a single integer representing the earliest possible time the entire sequence of canisters is completely finished in the chemical scrubber.

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

In Example 2, the single canister takes 5 seconds in the particulate filter then 3 seconds in the chemical scrubber, finishing at time 8.
