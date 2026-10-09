# Problem B — Resonant Bond Excitation

Time limit: 2 s   Memory limit: 256 MB

## Description
A synthetic molecule consists of two distinct groups of atoms: Alpha-type and Beta-type. The structure is held together by resonant bonds. Every bond connects exactly one Alpha-type atom to exactly one Beta-type atom. The internal chemistry dictates that no bond ever forms between two Alpha-type atoms, nor between two Beta-type atoms.

To stabilize the molecule, each bond must be irradiated during a specific excitation phase. The phases are numbered sequentially: 1, 2, 3, and so on. A strict physical limitation dictates that no single atom (whether Alpha or Beta) can have two of its connected bonds irradiated during the same excitation phase, because the overlapping energy would destabilize the atom.

The stabilization process must be as brief as possible. The atom with the highest number of connected bonds dictates the minimum number of phases required; if this busiest atom has $\Delta$ bonds, then at least $\Delta$ phases are strictly necessary. Your task is to assign an excitation phase to every bond using **no more** than $\Delta$ phases. Due to the strict two-sided bonding structure, it is a guaranteed property that exactly $\Delta$ phases are always sufficient to safely irradiate every bond without exceeding this minimum.

## Input
The first line contains three integers $n_L$, $n_R$, and $m$ ($1 \le n_L, n_R \le 100000$, $0 \le m \le 400000$), representing the number of Alpha-type atoms, the number of Beta-type atoms, and the total number of bonds.

The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_L$, $1 \le v \le n_R$), indicating a bond between Alpha-type atom $u$ and Beta-type atom $v$. Multiple bonds can exist between the same pair of atoms.

## Output
Print `YES` on the first line. On the second line, print $m$ space-separated integers in the range $1 \dots \Delta$ — the assigned excitation phase for each bond in the exact order they appear in the input (bonds sharing any atom must receive different phase numbers).

## Example

### Input
```text
3 3 5
1 1
1 2
2 2
2 3
3 3
```

### Output
```text
YES
1 2 1 2 1
```
