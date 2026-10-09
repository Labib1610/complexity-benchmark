# Compliance Risk Audit

Time limit: 1 s   Memory limit: 256 MB

## Description

A corporate treasury department is finalizing the status of $n$ distinct investment accounts. Each account must be assigned exactly one status: approved (represented by `1`) or suspended (represented by `0`).

The department has logged $m$ risk compliance alerts. Each alert specifies two required mitigations. A mitigation is represented by a non-zero integer $x$: 
- If $x > 0$, the mitigation requires account $x$ to be approved. 
- If $x < 0$, the mitigation requires account $|x|$ to be suspended.

An alert escalates into a critical compliance failure if the final status assignment fails to provide both of its required mitigations simultaneously. 

Your task is to determine whether there is a combination of account statuses that prevents any alert from escalating. If a safe combination exists, you must output one such assignment. Otherwise, report that no safe assignment is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$, where $|l_i| \le n$. These represent the two required mitigations for a single compliance alert.

## Output
If there is no way to assign statuses to all accounts such that zero alerts escalate, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $r_1$ $r_2$ $\dots$ $r_n$ (each being `0` or `1`), representing the status assigned to each account (where $r_i$ corresponds to account $i$).

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple safe status combinations may exist; you may output any of them. The same account index can appear in multiple different alerts, or multiple times within the same alert.
