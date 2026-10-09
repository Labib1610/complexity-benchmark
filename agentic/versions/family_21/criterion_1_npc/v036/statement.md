# Divestment Compliance

Time limit: 5 s
Memory limit: 256 MB

## Description
A conglomerate is preparing to spin off several of its business units. The conglomerate consists of $n$ business units. Currently, pairs of these units maintain active joint ventures. Terminating a joint venture between two units requires paying a specific dissolution fee.

Regulators have identified $k$ specific units as flagship brands. Each flagship brand is being acquired by a different competing market player. To prevent anti-competitive practices, the regulators mandate that no two flagship brands can remain indirectly or directly associated. Specifically, after the required terminations are complete, it must be impossible to trace a sequence of active joint ventures that connects any one flagship brand to another.

Other business units that are not flagship brands will be absorbed by whichever buyer they remain associated with, and their exact grouping does not matter as long as the regulatory mandate is satisfied. The conglomerate has allocated a maximum budget $B$ to cover all dissolution fees.

Determine a set of joint ventures to terminate such that the total of their dissolution fees is at most $B$, and the regulatory mandate is met. If it is impossible to achieve this within the budget, report so.

## Input
Line 1: four integers $n$, $m$, $k$, $B$.
Line 2: $k$ integers representing the IDs of the flagship brands.
Next $m$ lines: three integers $u$, $v$, $w$ representing a joint venture between unit $u$ and unit $v$ with a dissolution fee of $w$.

## Output
`YES`, followed by a line with the number $c$ of terminated joint ventures, then $c$ lines each containing the two units $u$ and $v$ whose joint venture is terminated. If it cannot be done within budget, output `NO`.

## Example

### Input
```text
5 5 3 10
1 2 3
1 4 5
2 4 4
4 5 6
2 5 8
3 5 2
```

### Output
```text
YES
2
1 4
3 5
```
