# Multiplexer Topology Lock

Time limit: 2 s   Memory limit: 256 MB

## Description
A high-throughput multiplexer's lifecycle consists of three distinct operational phases: the Integrity Sweep, the Topology Lock, and Flux Initiation.

**Phase 1: Integrity Sweep**  
This involves a hardware diagnostic that tests all potential conduits between the $q$ injector nodes (labeled $1$ through $q$) and the $q$ extractor nodes (labeled $q+1$ through $2q$). It measures signal attenuation and logs conduits that meet the safety threshold. This phase has already concluded, yielding a log of exactly $t$ stable conduits. Each logged conduit links one specific injector to one specific extractor.

**Phase 2: Topology Lock**  
Your software module is responsible for this phase. You receive the log of stable conduits from Phase 1 and must select a subset of them to become permanently locked. The multiplexer's architecture imposes a strict rule for this phase: every single node in the system—all $q$ injectors and all $q$ extractors—must be engaged by exactly one locked conduit. A node cannot remain idle, nor can it be engaged by multiple locked conduits.

**Phase 3: Flux Initiation**  
If your module successfully determines a configuration that satisfies the rule, the system automatically transitions to this final phase. The multiplexer routes data streams parallelized across the locked conduits determined in Phase 2. If the strict rule cannot be satisfied by any subset of the logged conduits, Phase 2 aborts and the multiplexer initiates a hardware reset.

Your task is to process the Phase 1 logs and execute Phase 2.

## Input
The first line contains two integers $q$ and $t$ (1 ≤ $q$ ≤ 100000, 0 ≤ $t$ ≤ 400000) — the number of injectors (which is also the number of extractors) and the number of stable conduits.
The following $t$ lines each contain two integers $a$ and $b$ (1 ≤ $a$ ≤ $q$ < $b$ ≤ $2q$), indicating a stable conduit between injector $a$ and extractor $b$.

## Output
If Phase 2 can be completed successfully, output `YES` on the first line. Then, output $q$ lines specifying the locked conduits (each line must contain the two node labels of a locked conduit). If it is impossible to satisfy the hardware rule, output `NO`.

## Example 1

### Input
```
3 4
1 4
2 5
3 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
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
