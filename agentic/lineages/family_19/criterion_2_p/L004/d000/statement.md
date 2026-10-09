# Asset Block Clearing

Time limit: 2 s
Memory limit: 256 MB

## Description

A financial clearing network consists of $n$ institutional accounts and $m$ one-way transaction channels. Each channel has a strict regulatory limit on the number of asset blocks it can transfer during a single trading session. Every channel's transfer quantity must be a non-negative integer that does not exceed this limit.

During a trading session, the network must obey a strict intermediary rule: for any account—with the exception of a designated originating account and a designated target account—the total number of asset blocks received from incoming channels must exactly equal the total number of asset blocks sent out on outgoing channels. No assets may be temporarily parked, destroyed, or created within these intermediary accounts.

A special operation has been requested. It requires a net outbound transfer of exactly $d$ asset blocks from the originating account $s$, and a net inbound transfer of exactly $d$ asset blocks to the target account $t$. 

Determine if it is possible to assign a transfer quantity to each channel such that the special operation is completed and all limits and intermediary rules are satisfied. If it is possible, provide a valid transfer plan detailing the number of blocks to route through each channel.

## Input

The first line contains three integers: $n$, $m$, and $1$ (indicating a single asset type).
The second line contains three integers: $s$ (the originating account), $t$ (the target account), and $d$ (the required number of asset blocks).
The following $m$ lines each contain three integers $u$, $v$, and $cap$, indicating a one-way channel from account $u$ to account $v$ with a regulatory limit of $cap$ asset blocks.

## Output

If the operation can be completed, print `YES` on the first line. On the second line, print $m$ space-separated integers representing the number of asset blocks transferred on each channel, in the exact order the channels were given in the input.
If the operation cannot be completed under the rules, print `NO`.

## Example

**Input:**
```
4 5 1
1 4 10
1 2 5
1 3 10
2 4 10
3 4 5
3 2 5
```

**Output:**
```
YES
5 5 5 5 0
```
