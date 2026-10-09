# Problem B — Complete Neutralization Protocol

Time limit: 2 s
Memory limit: 256 MB

## Description
A waste management plant must safely process an accumulated stockpile of reactive substances. The current inventory contains exactly $2q$ substances, divided evenly into $q$ acidic agents and $q$ alkaline agents. Each acidic agent is uniquely labeled with an integer from $1$ up to $q$. Each alkaline agent is uniquely labeled with an integer from $q+1$ up to $2q$.

Processing the inventory requires neutralizing the substances by mixing them in one-to-one pairs (one acid and one alkali). Because these agents are highly reactive, mixing arbitrary agents can cause dangerous thermal runaways. The plant engineers have compiled a comprehensive registry of approved, stable mixtures. A mixture is strictly forbidden unless it appears in this registry. Note that the registry might contain duplicate entries for the same mixture; these redundancies have no effect on stability.

Your task is to determine whether the entire stockpile can be neutralized simultaneously. A valid full neutralization plan must satisfy all of the following conditions:
- Each of the $q$ acidic agents is assigned to exactly one mixture.
- Each of the $q$ alkaline agents is assigned to exactly one mixture.
- Every planned mixture corresponds to an approved entry in the registry.
- For every planned mixture, the combined sum of the two agents' labels must not exceed $3q$ (to prevent exceeding the reactor's thermal capacity).
- For every planned mixture, the absolute difference between the two agents' labels must be at least $1$ (to ensure a sufficient pH gradient for the reaction).

If such a comprehensive plan exists, you must output one valid set of $q$ mixtures. If the stockpile cannot be fully neutralized under these rules, you must report that it is impossible.

## Input
The first line provides two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of acidic agents (which equals the number of alkaline agents) and the total number of approved mixtures in the registry.
The following $t$ lines each provide two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), specifying that the acidic agent $a$ can be safely mixed with the alkaline agent $b$.

## Output
If a full neutralization plan is possible, output `YES` on the first line, followed by $q$ lines that each contain the two labels of a chosen mixture. If it is impossible, output `NO`.

## Example 1

### Input
3 4
1 4
1 5
2 6
3 5

### Output
YES
1 4
3 5
2 6

## Example 2

### Input
2 2
1 3
2 3

### Output
NO
