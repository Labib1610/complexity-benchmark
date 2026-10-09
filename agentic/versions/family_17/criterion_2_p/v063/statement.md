# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate's remote segment must be fully committed for an upcoming drill. The assets are divided into two equal-sized groups. The first group consists of controllers, which are assigned consecutive integer IDs starting from 1. The second group consists of platforms, which are assigned consecutive integer IDs in the block immediately following the controllers. The command insists that every single asset must be committed simultaneously in a single plan.

A controller can only be teamed with a platform if their specific combination appears on the authorization list. A controller might be authorized for several platforms, and vice versa. The authorization list might contain many more combinations than the plan will ultimately use.

An acceptable roster activates authorized combinations such that every controller and every platform is committed in exactly one activated combination. No asset can be omitted, and no asset can be shared between two combinations. Determine whether the authorization list admits such a complete and exclusive commitment of all assets. If it does, output one such roster; otherwise, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$. The number of controllers $q$ will be at least one, and is constrained by the directorate's maximum hardware capacity of one hundred thousand controllers. The number of authorization entries $t$ can be zero and is bounded by the communications log capacity, which holds a number of entries up to exactly four times the maximum possible number of controllers.

The next $t$ lines each contain two integers $a$ and $b$ representing an authorized combination. The controller ID $a$ will be a valid controller (from 1 up to the total number of controllers). The platform ID $b$ will strictly exceed the number of controllers, but will not exceed the total number of assets (which is exactly twice the number of controllers).

## Output
If an acceptable roster can be formed, print `YES` on the first line, followed by $q$ lines each containing the two IDs of an activated combination. If no such roster is possible, print `NO`.

## Example

### Input
```
3 4
1 4
1 5
2 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
```
