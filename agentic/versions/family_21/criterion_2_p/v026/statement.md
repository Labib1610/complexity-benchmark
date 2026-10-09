# Problem B — Policy Synthesis Pipeline

Time limit: 2 s
Memory limit: 256 MB

## Description
The enterprise security pipeline operates in three distinct stages to ensure compliance:

**Stage 1: Telemetry Aggregation.** Agents deployed across the corporate infrastructure map out $n$ server endpoints and $m$ bidirectional RPC (Remote Procedure Call) channels. Each channel between two endpoints carries an associated disruption impact score, representing the operational cost of disabling it.

**Stage 2: Policy Synthesis (Your Task).** A critical security policy dictates that endpoint $s$ and endpoint $t$ must never be able to exchange data, either directly or via any sequence of intermediate endpoints. You must select a set of RPC channels to disable such that no valid sequence of active channels connects $s$ and $t$. The sum of the disruption impact scores of the disabled channels must not exceed the operational threshold $B$. Other endpoints may end up partitioned in any way; the only requirement is the strict separation of $s$ and $t$.

**Stage 3: Deployment.** The firewall controllers ingest the selected channels from Stage 2 and apply the blocking rules to the network hardware.

Your software is deployed solely to execute Stage 2. You will receive the telemetry data and must either output the configuration for the firewall controllers or report that the policy cannot be enforced within the threshold.

## Input
Line 1: five integers $n$ (number of endpoints), $m$ (number of channels), $s$, $t$ (the two endpoints to separate), and $B$ (the operational threshold).
Next $m$ lines: three integers $u$, $v$, $w$ — representing a bidirectional channel between endpoint $u$ and endpoint $v$ with disruption impact $w$.

## Output
If the policy can be synthesized within the threshold, output `YES`. On the next line, output the number $c$ of channels to disable. On the following $c$ lines, output the two endpoints `u v` for each disabled channel. If there are multiple valid sets of channels, any one that meets the threshold is acceptable.
If it is impossible to enforce the policy without exceeding the threshold, output `NO`.

## Example
### Input
```text
5 6 1 5 10
1 2 4
1 3 5
2 4 6
3 4 3
2 5 8
4 5 5
```
### Output
```text
YES
2
1 2
3 4
```
