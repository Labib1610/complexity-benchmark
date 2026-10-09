# Component Transfer Allocation

Time limit: 2 s
Memory limit: 256 MB

## Description
The daily production cycle begins after the forecasting model finalizes the demand. Today, the model dictates that exactly $d$ units of a specialized component must be moved from the manufacturing site to the final assembly plant. Prior to this, the legal team has secured a network of transfer agreements with independent couriers. Each agreement allows moving components from one specific facility to another, but strictly limits the maximum number of units that can be moved per day over that connection.

Your task is to determine how many components to allocate to each transfer agreement to satisfy the daily demand. The allocation must adhere to the following rules:
- The number of components assigned to an agreement must be a non-negative integer and cannot exceed its negotiated maximum daily allowance.
- Facilities other than the manufacturing site and the assembly plant are not permitted to hold inventory overnight. Therefore, the total number of components arriving at any intermediate facility must perfectly match the total number of components leaving it.
- The total number of components leaving the manufacturing site minus the total number entering it must be exactly $d$. Similarly, the total number of components entering the assembly plant minus the total number leaving it must also be exactly $d$.

Once you provide this allocation, the dispatchers will step in to assign actual driver shifts and license plates, and the finance team will process the courier payments based on your numbers. You only need to verify if the demand can be met under the current agreements and provide the allocation; driver scheduling and billing are outside the scope of this step.

## Input
The first line contains three integers: $n$ (the number of facilities), $m$ (the number of transfer agreements), and $1$.
The second line contains three integers: $s$ (the manufacturing site ID), $t$ (the assembly plant ID), and $d$ (the required number of components).
Each of the next $m$ lines contains three integers $u$, $v$, and $c$, indicating a one-way transfer agreement from facility $u$ to facility $v$ with a maximum daily allowance of $c$ components.

## Output
If the components can be successfully allocated to meet the exact demand $d$, print `YES` on the first line. On the second line, print $m$ integers separated by spaces, representing the number of components assigned to each transfer agreement, in the exact order they were given in the input.
If it is impossible to meet the demand, print `NO`.

## Example

**Input**
```
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

**Output**
```
YES
5 5 0 5 5
```
