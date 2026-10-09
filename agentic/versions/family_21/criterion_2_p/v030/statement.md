# Problem B — Signal Containment

Time limit: 2 s   Memory limit: 256 MB

## Description
A financial system consists of $n$ automated trading agents. Certain pairs of agents maintain a mutual data-sharing agreement. Terminating an agreement requires paying a specific legal fee.

Agent $s$ has been compromised and generates a toxic market signal. The signal propagates through the system according to the following rules:
- Agent $s$ inherently possesses the toxic signal.
- If any agent $X$ possesses the signal, and an active data-sharing agreement exists between agent $X$ and agent $Y$, agent $Y$ will also acquire the signal.
- This propagation continues until no additional agents can acquire the signal.

Agent $t$ is a critical market maker. You must ensure that agent $t$ never acquires the toxic signal. To achieve this, you may terminate some data-sharing agreements (which renders them no longer active). The total legal fees for all terminated agreements combined cannot exceed the allocated budget $B$.

Determine a set of agreements to terminate that prevents the signal from being acquired by agent $t$, such that the sum of their legal fees is within the budget. If no such set of agreements exists for the given budget, you must report this.

## Input
Line 1: five integers $n$, $m$, $s$, $t$, $B$. 
Next $m$ lines: three integers $u$, $v$, $w$ representing a mutual agreement between agent $u$ and agent $v$ with a termination fee of $w$.

## Output
`YES`, then a line with the number $c$ of terminated agreements, then $c$ lines each containing two integers $u$ and $v$ representing a terminated agreement; or `NO`.

## Example 1
**Input:**
```
4 4 1 4 10
1 2 5
1 3 5
2 4 5
3 4 5
```

**Output:**
```
YES
2
1 2
1 3
```
