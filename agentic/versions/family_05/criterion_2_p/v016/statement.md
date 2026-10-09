# Secure Channel Routing

Time limit: 2 s
Memory limit: 256 MB

## Description

You are configuring a network of secure communication channels. The network consists of three distinct sets of resources, each containing exactly **k** elements:
- **k** transmitters (numbered 1 to **k**)
- **k** cryptographic modules (numbered 1 to **k**)
- **k** carrier frequencies (numbered 1 to **k**)

You are provided with a list of **t** compatible configurations. Each configuration is a triplet `(u, v, w)` indicating that transmitter `u` can operate with cryptographic module `v` on carrier frequency `w`.

The hardware architecture imposes the following strict conditions on the provided list of configurations:
- Each transmitter is physically hardwired to exactly one cryptographic module, and no two transmitters are hardwired to the same module. Thus, for any given transmitter, all its compatible configurations will involve the exact same cryptographic module, and different transmitters will use different modules.
- No carrier frequency is listed in more than **k** compatible configurations.
- The total number of compatible configurations **t** will never exceed **k**².
- A transmitter will never be listed with the same carrier frequency more than once.

You must select exactly **k** compatible configurations from the given list such that every transmitter, every cryptographic module, and every carrier frequency appears in **exactly one** selected configuration. Determine if it is possible to activate exactly **k** channels under these conditions, and if so, output one such valid selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k), representing the number of elements in each resource category and the number of compatible configurations.
The next **t** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v, w ≤ k), representing a compatible configuration. No configuration is repeated in the input.

## Output

If a valid deployment of **k** channels exists, print `YES` on the first line. Then print **k** lines, each containing the three integers `u v w` of an activated channel (the channels can be printed in any order). If there are multiple valid deployments, any of them will be accepted.

If no valid deployment is possible, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
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
2 2 1
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
