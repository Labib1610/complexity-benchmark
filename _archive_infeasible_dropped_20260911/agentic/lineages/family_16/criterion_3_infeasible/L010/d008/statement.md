# Problem C — Impossible Allocation: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A network router must process traffic over a strict window of $T$ timeslots. There are $j$ active data flows. For each flow $i$, the router must schedule exactly $p1_i$ Ingress packets and exactly $p2_i$ Egress packets. 

The router's schedule is represented as a log of $T$ timeslots. Each timeslot $k \in \{1, \dots, T\}$ has two fields: `IngressID` and `EgressID`. Each field contains the ID of a flow ($1 \dots j$) or $0$ if idle.
This means:
- The router can schedule at most one Ingress packet per timeslot (across all flows).
- The router can schedule at most one Egress packet per timeslot (across all flows).

Additionally, the router enforces a strict causal firewall. For a schedule to be valid, the following verification routine must return `PASS` for every flow $i \in \{1, \dots, j\}$:

```python
def check_firewall(flow_id, router_log):
    egress_seen = False
    for k in range(1, T + 1):
        if router_log[k].EgressID == flow_id:
            egress_seen = True
            
        if router_log[k].IngressID == flow_id and egress_seen:
            return "BLOCKED"
            
    return "PASS"
```

Every provided configuration is mathematically impossible to route—there is no valid way to construct the schedule to accommodate all required packets while passing the firewall for all flows. Your task is to identify the bottleneck that proves the configuration is unachievable.

Exactly one of the following foundational requirements is broken. Output the applicable certificate:

- **Causal Violation:** For some flow $i$, it is impossible to schedule its $p1_i$ Ingress and $p2_i$ Egress packets within $T$ timeslots without the firewall returning `BLOCKED` (even if it were the only flow on the router). Output `JOB i` (where $i$ is the 1-based index of the flow).
- **Ingress Saturation:** It is impossible to schedule all required Ingress packets for all $j$ flows within $T$ timeslots. Output `LOAD 1`.
- **Egress Saturation:** It is impossible to schedule all required Egress packets for all $j$ flows within $T$ timeslots. Output `LOAD 2`.

You are guaranteed that exactly one of these requirements will be broken for the given input.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required number of Ingress packets and Egress packets respectively for flow $i$ (i.e., $p1_i$ and $p2_i$).

## Output

Print a single line: `JOB i` (for a causal violation) or `LOAD c` (for a saturation failure, where **c** is 1 for Ingress saturation or 2 for Egress saturation).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, flow 1 requires 70 Ingress packets and 60 Egress packets. It is impossible to schedule them within $T=100$ timeslots without the firewall returning `BLOCKED` for flow 1. Thus `JOB 1` is the correct proof of impossibility. 

In Example 2, no single flow violates the causal firewall on its own. However, the sum of required Ingress packets across all 4 flows is 200. Since the router can only process 1 Ingress packet per timeslot, it is impossible to schedule them all in $150$ timeslots. Thus `LOAD 1` is the correct output.