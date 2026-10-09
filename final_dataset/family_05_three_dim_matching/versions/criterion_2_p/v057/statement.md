# Orbital Observatory: Observation Workflow

Time limit: 2 s   Memory limit: 256 MB

## Description
The orbital observatory processes deep-space imagery through a strict three-stage workflow:

**Stage 1: Target Locking.** The observatory focuses on $k$ celestial targets using $k$ guide sensors (each numbered 1 to $k$). During this initialization, the tracking software permanently pairs each celestial target with exactly one unique guide sensor. This one-to-one pairing is fixed and cannot be modified. This stage has already completed.

**Stage 2: Spectrometer Routing.** The observatory contains $k$ spectrometer banks, numbered 1 to $k$. To capture the data, the system must finalize exactly $k$ observation configurations. A complete configuration requires exactly one celestial target, one guide sensor, and one spectrometer bank. The central computer has generated a list of verified configuration options. Your task is to select exactly $k$ configurations from this list so that every celestial target, every guide sensor, and every spectrometer bank is included in exactly one active configuration.

**Stage 3: Exposure and Downlink.** Once the configurations are finalized, the observatory will execute the exposures and transmit the data to Earth.

Given the list of verified configuration options (which strictly follow the pairings established in Stage 1), determine if a valid Stage 2 routing selection exists. If successful, output the chosen configurations.

## Input
The first line provides two integers $k$ and $t$ ($1 \le k \le 1200$, $0 \le t \le k \cdot k$). These represent the total number of items in each category (celestial targets, guide sensors, spectrometer banks) and the total number of verified configuration options, respectively.

The following $t$ lines each contain three integers $c$, $g$, and $s$ ($1 \le c, g, s \le k$), detailing a verified configuration option that links celestial target $c$, guide sensor $g$, and spectrometer bank $s$. All configuration options in the list are distinct. Because of the permanent pairings established in Stage 1, whenever a verified configuration option includes a celestial target $c$, it invariably includes its uniquely paired guide sensor $g$. Furthermore, no two celestial targets share the same guide sensor.

## Output
If a valid set of exactly $k$ configurations can be selected to satisfy the Stage 2 requirements, print `YES` on the first line. Following this, output $k$ lines, each containing the three integers $c$ $g$ $s$ of a chosen configuration. The configurations may be printed in any order. If multiple valid sets exist, any correct set is acceptable.

If no such set can be selected, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```
