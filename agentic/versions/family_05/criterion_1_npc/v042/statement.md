# Problem A — Secure Network Activation

Time limit: 5 s   Memory limit: 256 MB

## Description

A communications network requires exactly **k** secure broadcast channels to be established. Each channel is defined by a combination of three distinct components: a transmitter tower, an encryption key, and a satellite link. The available towers, keys, and links are each uniquely identified by integers from 1 to **k**.

Due to hardware and signal constraints, only certain configurations of a tower, a key, and a link can successfully synchronize. You are provided with a list of these synchronized combinations.

Your task is to activate exactly **k** channels from the provided list such that every transmitter tower is used **exactly once**, every encryption key is used **exactly once**, and every satellite link is used **exactly once** across the active network. 

Determine whether this full activation is possible, and if so, report one valid set of channels.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of required channels (which is also the maximum identifier for each component type) and the number of synchronized combinations.
Each of the next **t** lines contains three integers **p1**, **p2**, **p3** (1 ≤ p1, p2, p3 ≤ k), representing a synchronized combination of a transmitter tower, an encryption key, and a satellite link. No combination is listed more than once.

## Output

If a valid selection of **k** channels exists, print `YES` on the first line, then print **k** lines, each containing the three values `p1 p2 p3` of one chosen channel. Any selection meeting the requirement is accepted; the channels may be printed in any order.

If no valid selection exists, print `NO`.

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

In Example 2, both synchronized combinations require encryption key 1. Therefore, it is impossible to utilize encryption key 2 in any channel, meaning the requirement to use every key exactly once cannot be fulfilled.
