# Problem B — Operation Cipher Syndicate

Time limit: 2 s   Memory limit: 256 MB

## Description

An intelligence agency manages a sleeper network of **n** operatives (numbered 1 to **n**). To avoid detection, direct communication is strictly limited. There are **m** pre-arranged secure contact channels, each allowing two specific operatives to exchange messages. Activating a channel requires a specific expenditure of untraceable funds.

The network's architecture was designed with two strict operational rules regarding the contact channels:
1. There are exactly **n − 1** contact channels in existence.
2. If all channels were activated, any operative would be able to pass a message to any other operative in the network through some sequence of channels.

A crisis has occurred, and **t** specific operatives, known as the keyholders, each possess a fragment of a critical password. These keyholders must pool their fragments. To achieve this, you must activate a subset of the contact channels so that messages can circulate among all keyholders. Specifically, for any pair of keyholders, there must exist a sequence of activated channels that allows a message to pass from one to the other (possibly being relayed through other non-keyholder operatives along the way).

Determine the minimum total funds required to activate a valid subset of channels.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the keyholders.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a contact channel between operative u and operative v that costs w funds to activate. The available channels follow the architectural rules described above.

## Output

Print a single integer: the minimum total funds required to activate the necessary channels.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1, keyholders 1 and 4 can only exchange messages if the sequence of channels passing through operatives 2 and 3 is activated, meaning all three available channels (5 + 1 + 2 = 8) must be funded. In Example 2, there is only one keyholder, so the communication requirement is already met without activating any channels.
