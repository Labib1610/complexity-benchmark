# Problem A — Clockwork Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description
A master watchmaker is tasked with fulfilling an order for custom gearboxes. Every gearbox requires exactly three distinct interlocking cogs to function correctly. The workshop has received a single bulk shipment of cogs specifically for this order. Because no cog can be left unused and no cog can be used more than once, the total number of cogs provided is exactly three times the number of requested gearboxes. Each cog is engraved with a unique serial number, starting from one and counting up continuously to the total number of cogs in the shipment.

Not all cogs mesh together. The watchmaker consults a master catalog of known, tested combinations. Each entry in this catalog specifies three specific cog serial numbers that perfectly interlock to form a working gearbox. The watchmaker may only assemble a gearbox if its exact three cogs appear together as a single entry in the catalog. 

The objective is to determine if it is possible to group every single cog from the shipment into valid gearboxes, such that each cog is used exactly once and every assembled gearbox exactly matches an entry in the catalog. If such an arrangement is possible, the watchmaker must determine one valid way to assemble them.

## Input
The first line of the manifest contains two integers **q** and **t**. 
The first integer **q** is the number of gearboxes ordered. Every order requires at least one gearbox, but a single work order is physically capped at two hundred gearboxes to prevent workbench clutter. 
The second integer **t** is the number of entries in the catalog. A new workshop might have zero cataloged combinations, while an established one will have no more than twenty thousand.

The following **t** lines each contain three integers **a**, **b**, and **c**, representing the serial numbers of the cogs in a cataloged combination. These three integers always form a strictly increasing sequence. The lowest possible serial number is one, and the highest possible serial number is exactly the total inventory size (which is always three times the gearbox order).

## Output
If it is possible to use every cog to build the requested gearboxes using only combinations from the catalog, output `YES` on the first line. Then, output **q** lines, each containing the three cog serial numbers of one assembled gearbox. 
If it is impossible to use all the cogs under these rules, output `NO`.

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
