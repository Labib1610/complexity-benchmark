# Problem A — Deep-Sea Fleet Assembly Protocol

Time limit: 5 s
Memory limit: 256 MB

## Description
You are overseeing the construction of a fleet of specialized deep-sea exploration submersibles. Your inventory contains exactly $3q$ unique modular components, which are assigned sequential IDs from $1$ to $3q$.

You are provided with a manufacturing catalog containing $t$ compatible blueprints. Each blueprint identifies a specific combination of exactly three components that can be safely integrated to form a fully functional submersible.

To complete the project, you must select a set of blueprints from the catalog that satisfies the following assembly mechanics:
- **Integration:** Selecting a blueprint immediately commits its three listed components to a new submersible.
- **Isolation:** Once a component is committed to a submersible, it is permanently consumed. A selected blueprint cannot require any component that has already been committed to another submersible.
- **Exhaustion:** The final fleet must incorporate every single one of the $3q$ components from the inventory, leaving none unused.

Additionally, to ensure structural integrity and meet manufacturing tolerances, all blueprints in the catalog are guaranteed to adhere to the following safety margins:
- The ID span (the difference between the highest and lowest component ID) within any single blueprint is strictly less than $3q$.
- The total weight rating (the sum of the three component IDs) of any single blueprint never exceeds $9q - 3$.
- The total count of component references across the entire catalog is exactly $3t$.

Determine whether there is a valid selection of blueprints that successfully assembles the fleet. If such a selection exists, you must also provide the blueprints used.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $3q$ represents the total number of modular components in the inventory, and $t$ is the number of available blueprints in the catalog.
Each of the subsequent $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the IDs of the components required by that specific blueprint.

## Output
If a valid fleet assembly is possible, print `YES` on the first line. Then, output $q$ lines, each containing the three component IDs of a selected blueprint. 
If no such assembly is possible, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
