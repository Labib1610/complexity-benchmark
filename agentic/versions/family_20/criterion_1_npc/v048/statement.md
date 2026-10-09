# Link Frequency Allocator

Time limit: 5 s   Memory limit: 256 MB

## Description
You are implementing the Link Frequency Allocator, which serves as Phase 2 of the Quantum Network Compiler pipeline. 

Phase 1 (Topology Ingestion) has already processed the hardware manifest and verified the physical layout. It guarantees that the network consists of a set of switches connected by bidirectional data links, and that the architecture is strictly uniform: every switch serves as the endpoint for exactly three links. Phase 1 passes this validated layout to your module.

Phase 2 (Your Module) must configure the transmission frequency of each link. There are exactly three frequencies available (labeled 1, 2, and 3). To prevent destructive resonance, the hardware multiplexer at each switch requires that the three links connected to it operate on completely different frequencies. Your task is to determine if such a configuration exists and, if so, produce it.

Phase 3 (Routing Initialization) awaits your output. If you produce a valid configuration, Phase 3 will use it to establish quantum entanglement paths. If you determine that no valid configuration is possible, you must abort the pipeline by outputting a failure signal, prompting a physical redesign of the network.

## Input
The input is provided by Phase 1. The first line contains two integers **n** and **m** (**n** is even, **m** = 3**n**/2, 2 ≤ **n** ≤ 2000), representing the number of switches and data links, respectively. Switches are numbered 1 to **n**.
The next **m** lines each contain two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), representing a data link connecting switch **u** and switch **v**.

## Output
If your module can successfully configure the frequencies for Phase 3, print `YES` on the first line. On the second line, output **m** integers from the set {1, 2, 3}, representing the frequency assigned to each data link in the exact order they were received from Phase 1. If no configuration satisfies the resonance constraints at all switches, print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
