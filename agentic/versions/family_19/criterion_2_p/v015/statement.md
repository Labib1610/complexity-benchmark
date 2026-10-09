# Problem B — Gas Injection Routing

Time limit: 2 s   Memory limit: 256 MB

## Description
An energy company must transfer a fixed total volume of liquefied gas from an import terminal to a regional storage facility through a network of one-way transmission pipelines during a single operational shift. Each pipeline has a strict upper limit on the volume of gas it can safely transport per shift. The volume routed through any individual pipeline must be a non-negative integer and cannot exceed this upper limit.

The network contains intermediate junction stations where pipelines meet. At every junction station, the total volume of gas flowing in must exactly equal the total volume flowing out, ensuring no gas is vented or stored mid-route. At the import terminal, the net outgoing volume must exactly match the required total volume, and at the storage facility, the net incoming volume must exactly match this required total volume. 

Determine a valid routing strategy that successfully transfers the required volume without violating any pipeline limits, or determine that the network cannot support this transfer volume in a single shift. 

## Input
The first line contains three integers: $n$ (the number of stations), $m$ (the number of pipelines), and the number $1$.
The second line contains three integers: $s$ (the import terminal station), $t$ (the storage facility station), and $d$ (the required total volume).
The following $m$ lines each contain three integers $u$, $v$, and $cap$, indicating a one-way pipeline from station $u$ to station $v$ with a maximum volume limit of $cap$.

## Output
If the required volume can be transferred, output `YES` on the first line. On the second line, output $m$ integers representing the volume routed through each pipeline, in the exact order the pipelines were given in the input. 
If the required volume cannot be transferred, output `NO`.

## Example
### Input
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10

### Output
YES
5 5 0 5 5
