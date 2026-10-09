# Phase 2: Rejection Gateway

Time limit: 2 s
Memory limit: 256 MB

## Description

You are building the rejection module for a two-stage distributed computing cluster. The pipeline is structured as follows:
1. **Ingestion**: Validates requests and establishes bounds.
2. **Rejection Gateway (Your Task)**: Emits a mathematical proof of impossibility for request batches that cannot meet the user's latency target.
3. **Scheduler**: Determines the optimal ordering for feasible batches.
4. **Execution**: Dispatches ordered instructions to the hardware.

Your module only handles Phase 2. You will be given a batch of $j$ requests and a target latency $T$. Each request requires a specific duration on Stage 1, followed immediately by a specific duration on Stage 2. A request cannot start Stage 2 until its Stage 1 execution is fully complete. Each stage can only process one request at a time.

To ensure your module can process inputs without accumulator overflow, the Ingestion phase guarantees two global properties for every batch before routing it to you:
- The total aggregate duration of all requests across both stages combined will never exceed $400,000,000,000$.
- The absolute difference between the total workload on Stage 1 and the total workload on Stage 2 across all requests is strictly less than $200,000,000,000$.

Every batch routed to your module has already been determined to be impossible to complete within the latency $T$. Your task is not to schedule them, but to generate a concise rejection certificate for the user.

For all provided inputs, exactly one of the following two conditions is the cause of the impossibility. You must print the corresponding certificate:

- **Individual Bottleneck**: A single request takes too long. If a request's required time on Stage 1 and Stage 2 sums to a value strictly greater than $T$, that request alone cannot finish within the latency target.
  Print: `JOB i` — where $i$ (1-based index) is such a request.

- **Stage Saturation**: A stage is overloaded. Because each stage processes requests sequentially, it requires at least the sum of all its assigned durations. If the total duration across all requests on Stage 1 (or Stage 2) is strictly greater than $T$, the target is unachievable.
  Print: `LOAD c` — where $c$ is either 1 or 2, representing a stage whose total required duration exceeds $T$.

## Input

The first line provides two integers $j$ and $T$ ($1 \le j \le 200,000$, $1 \le T \le 1,000,000,000$).
The following $j$ lines each provide two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1,000,000$): the duration required for the request on Stage 1 and Stage 2, respectively.

## Output

Print a single line containing the exact certificate: either `JOB i` (for a request whose $p_1 + p_2$ exceeds $T$) or `LOAD c` (for a stage $c$ whose total workload exceeds $T$).

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

In Example 1, the first request requires $70 + 60 = 130$ time units. Since $130 > 100$, the latency target is impossible, making `JOB 1` the correct certificate. 
In Example 2, no single request's combined duration exceeds 150. However, Stage 1 must process $50 + 50 + 50 + 50 = 200$ units of work. Since it processes sequentially and $200 > 150$, `LOAD 1` is the correct certificate.
