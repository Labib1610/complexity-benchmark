# Symbiotic Synthesis

Time limit: 2 s   Memory limit: 256 MB

## Description
In the deep-sea research station, scientists are cultivating a new form of bioluminescent algae. Each organism is formed by fusing exactly one alpha-strain cell and one beta-strain cell. 

You are given a cultivation batch consisting of a set of alpha-strain cells and an equally sized set of beta-strain cells. The researchers have performed chemical assays to determine which specific alpha-strain cells can successfully fuse with which specific beta-strain cells. A fusion is only viable if the assay confirmed their compatibility. 

To maximize the light output for the upcoming deep-sea expedition, the researchers must achieve total synthesis: every single cell in the batch must be fused. This means every alpha-strain cell and every beta-strain cell must be part of exactly one viable fusion, leaving no cells unused and no cell participating in more than one fusion. 

You need to determine if it is possible to achieve total synthesis for the entire batch. If it is possible, provide the exact list of fusions to perform.

## Input
The first line contains two integers $q$ and $t$. 
The batch contains exactly $q$ alpha-strain cells (assigned identification numbers sequentially starting from $1$) and exactly $q$ beta-strain cells (assigned identification numbers sequentially starting immediately after the last alpha-strain cell). 

The cultivation tank can hold a maximum combined total of two hundred thousand cells across both strains. The batch will always contain at least one alpha-strain cell.
The assay machine's memory bank can store a maximum number of positive compatibility records equal to exactly four times the maximum possible number of alpha-strain cells in a fully loaded tank. The number of records $t$ ranges from zero up to this memory bank limit.

The next $t$ lines each contain two integers $a$ and $b$. Each line represents a confirmed compatibility. The first integer $a$ will always be the identification number of an alpha-strain cell, and the second integer $b$ will always be the identification number of a beta-strain cell.

## Output
If total synthesis is possible, output `YES` on the first line. Then, output $q$ lines, each containing the two identification numbers of a fused pair. You may output the fusions in any order. If there are multiple ways to achieve total synthesis, any valid assignment will be accepted.
If total synthesis is impossible and some cells must inevitably be left out, output `NO`.

## Example 1
### Input
```
3 5
1 4
1 5
2 4
2 6
3 5
```
### Output
```
YES
1 4
2 6
3 5
```

## Example 2
### Input
```
2 2
1 3
2 3
```
### Output
```
NO
```
