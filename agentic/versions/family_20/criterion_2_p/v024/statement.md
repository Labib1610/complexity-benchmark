# Problem B — Intermodal Terminal Scheduling

Time limit: 2 s   Memory limit: 256 MB

## Description
An intermodal freight terminal transfers shipping containers directly from incoming cargo ships to outbound freight trains. Each container must be moved from a specific ship to a specific train. Operations are divided into one-hour time slots. During any single time slot, a ship can offload at most one container, because it has only one crane access point. Similarly, during any single time slot, a train can load at most one container, because it has only one loading bay.

The terminal manager has identified the busiest vessel (whether a ship or a train) that handles the highest number of containers. Let us call this maximum container count $H$. Because this busiest vessel requires $H$ separate time slots, the entire operation will take at least $H$ hours.

Your task is to assign a specific time slot (an integer from 1 to $H$) to every container transfer such that the terminal completes all operations in exactly $H$ hours, without violating the single-container-per-hour limit for any ship or train. The direct ship-to-train nature of the terminal guarantees that such a schedule is always possible.

## Input
The first line contains three integers $n_L$, $n_R$, and $m$ ($1 \le n_L, n_R \le 100000$, $0 \le m \le 400000$), representing the number of ships, the number of trains, and the total number of containers to transfer.
The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_L$, $1 \le v \le n_R$), indicating that a container must be moved from ship $u$ to train $v$.

## Output
Print `YES` on the first line. On the second line, print $m$ space-separated integers, where the $i$-th integer represents the time slot (from 1 to $H$) assigned to the $i$-th container given in the input.

## Example
### Input
```
3 3 5
1 1
1 2
2 2
2 3
3 3
```

### Output
```
YES
1 2 1 2 1
```
