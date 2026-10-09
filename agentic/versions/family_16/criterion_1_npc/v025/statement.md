# Problem A — Alchemical Apprenticeship

Time limit: 5 s   Memory limit: 256 MB

## Description

As a novice alchemist, you have been tasked with brewing **j** complex potions using the laboratory's **m** unique apparatuses (numbered 1 to **m**). Each potion requires a specific sequence of enchantments. Each enchantment must be channeled through a specific apparatus for a given number of minutes.

The brewing process must strictly adhere to the following physical laws:

- The enchantments for any given potion must be performed sequentially in the exact order listed. An enchantment can only begin after the previous one for that same potion has completely finished.
- Each apparatus is highly volatile and can safely channel only one enchantment at a time.
- Once an enchantment is initiated on an apparatus, it must run continuously to completion without interruption.
- Enchantments for different potions can run simultaneously, provided they do not require the same apparatus.

Furthermore, you are guaranteed that all assigned orders comply with the following Guild Regulations:
- **Regulation 4-A**: The sum of the durations of all enchantments across all potions will never exceed 50,000 minutes.
- **Regulation 4-B**: No single potion will require more than 50 enchantments in its sequence.

Determine the earliest possible minute by which all potions can be completely brewed (i.e., the time at which the final enchantment finishes is as small as possible).

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of potions and the number of apparatuses.
Each of the next **j** lines describes the recipe for one potion: an integer **o** (the number of enchantments) followed by **o** pairs of integers `apparatus duration` (1 ≤ apparatus ≤ m, 1 ≤ duration ≤ 1000), listing the potion's enchantments in order.
The total number of enchantments across all potions is at most 50.

## Output

Print a single integer: the earliest possible minute at which all potions are finished.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical potions each pass through apparatuses 1, 2, and 3 (requiring 2 minutes each). The second potion's enchantments trail the first's through the apparatuses, finishing at minute 8. In Example 3, the two potions use different apparatuses and run entirely in parallel, finishing at minute 4.
