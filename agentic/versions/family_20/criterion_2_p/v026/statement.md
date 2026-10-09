# Phase 2: Compliance Batch Scheduling

Time limit: 2 s   Memory limit: 256 MB

## Description
The annual security audit of our corporate network operates as a three-stage automated pipeline. 

In **Phase 1**, a log aggregator scans the previous year's traffic to isolate sensitive data transfers. Each transfer occurs strictly between one Internal Employee ID and one External Vendor ID. Internal employees never transfer sensitive data directly to other internal employees, and external vendors never transfer directly to other external vendors. The aggregator outputs a raw list of these flagged transfers.

You are responsible for implementing **Phase 2**, the batch scheduling step. The inspection system that analyzes these transfers cannot process multiple transfers involving the same Employee ID or the same Vendor ID at the same time. Therefore, the transfers must be grouped into distinct "audit batches". 

To keep the pipeline efficient, the number of batches must equal the unavoidable minimum: the highest frequency $F$ of transfers associated with any single entity (whether an Employee or a Vendor). Your task is to assign each transfer to a batch numbered from $1$ to $F$ such that no Employee ID or Vendor ID is involved in more than one transfer per batch. (The strict internal-to-external nature of the data guarantees that such an assignment using exactly $F$ batches is always possible).

In **Phase 3**, the deep-packet inspection tools execute the scheduled batches sequentially, and a final compliance certificate is generated. Your program only needs to handle the logic for Phase 2.

## Input
The first line contains three integers $N_{emp}$, $N_{ven}$, and $M$ ($1 \le N_{emp}, N_{ven} \le 100000$, $0 \le M \le 400000$), representing the number of Employee IDs, the number of Vendor IDs, and the total number of flagged transfers produced by Phase 1.
The next $M$ lines each contain two integers $u$ and $v$ ($1 \le u \le N_{emp}$, $1 \le v \le N_{ven}$), indicating a transfer between Employee $u$ and Vendor $v$.

## Output
First, print `YES`.
On the second line, print $M$ space-separated integers, where the $i$-th integer (in the order the transfers were provided in the input) is the batch number (from $1$ to $F$) assigned to the $i$-th transfer.

## Example

### Input
```text
4 4 6
1 1
1 2
2 2
3 3
3 4
4 4
```

### Output
```text
YES
1 2 1 1 2 1
```
