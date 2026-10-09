# Harmonic Alignment Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description
The acoustic grid requires complete synchronization. The equipment is divided into two distinct groups of equal size: synthesizers, which are assigned consecutive identification numbers starting from 1, and resonators, which receive identification numbers in the block immediately following the synthesizers. Every synthesizer and every resonator is a unique piece of equipment, and the protocol demands that every single one of them is integrated into a unified configuration.

A synthesizer can only be linked with a resonator if their specific combination appears on the compatibility registry; unlisted combinations will cause feedback loops and are strictly prohibited. The registry simply lists which specific synthesizer-resonator pairings are safe. The number of safe pairings a piece of equipment belongs to, or the order they are listed in, carries no special meaning.

A valid configuration activates a selection of these listed combinations such that every synthesizer and every resonator is utilized in exactly one active link. This means no equipment is left dormant, and no equipment is shared across multiple active links. Since both groups have the same quantity of equipment, a valid configuration will perfectly exhaust all available items. Determine whether the compatibility registry contains a selection that achieves this complete and exclusive integration. If it does, provide one such configuration; otherwise, declare that a complete integration is impossible.

## Input
The first line contains two integers $q$ and $t$. The facility can host up to one hundred thousand synthesizers, meaning $q$ is a positive integer no greater than this capacity. The compatibility registry length, $t$, can be empty or contain up to four times the maximum synthesizer capacity.

The following $t$ lines each contain two integers $a$ and $b$, representing a safe combination between synthesizer $a$ and resonator $b$. The identifier $a$ is guaranteed to be a valid synthesizer identification number, and $b$ is guaranteed to be a valid resonator identification number.

## Output
If a complete synchronization is possible, output `YES` on the first line, followed by $q$ lines each containing the two identifiers of an activated combination. If no such configuration exists, output `NO`.

## Example

### Input
```
3 4
1 4
1 5
2 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
```
