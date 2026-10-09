# Pipeline Stage 2: Link Frequency Assignment

Time limit: 5 s   Memory limit: 256 MB

## Description
The automated deployment of our deterministic communication fabric proceeds in three distinct phases: topology generation, link frequency assignment, and routing rule compilation. 

Phase 1 (Topology Generation) has already been completed. A layout engine has generated a uniform architecture consisting of switching modules and bidirectional links. By design, this phase guarantees a perfectly balanced structure: every single switching module is connected to exactly three other modules. There are no missing connections or variations in port counts. The blueprint produced by Phase 1 is provided as your input.

Your responsibility is to execute Phase 2 (Link Frequency Assignment). The hardware specifications dictate that the network operates using three communication frequencies, designated 1, 2, and 3. To prevent hardware-level signal interference, the three links attached to any given module must be configured to use all three distinct frequencies. Consequently, at every module, exactly one link must operate on frequency 1, one on frequency 2, and one on frequency 3. Depending on the global loop structure generated in Phase 1, such a configuration may or may not be attainable.

If you succeed in finding a valid configuration, your output will be passed directly to Phase 3 (Routing Rule Compilation), which will use your frequency assignments to build the final routing tables. If no valid assignment exists, you must flag the topology as unroutable so the pipeline can be aborted.

## Input
The first line contains two integers **n** and **m** (where **n** is an even integer, **m** = 3**n**/2, and 2 ≤ **n** ≤ 2000), representing the number of switching modules and the total number of bidirectional links produced by Phase 1.
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), representing a bidirectional link between module **u** and module **v**. It is guaranteed that every module appears in exactly three links.

## Output
If a valid Phase 2 frequency assignment exists, print `YES` on the first line. On the second line, print **m** integers chosen from {1, 2, 3}, representing the frequency assigned to each link in the exact order the links were provided in the input. If multiple valid assignments exist, any of them will be accepted by Phase 3.
If no valid assignment is possible, print `NO`.

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
