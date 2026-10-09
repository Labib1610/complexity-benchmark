# Curatorial Case Selection

Time limit: 5 s   Memory limit: 256 MB

## Description
A national museum is preparing its grand retrospective. The curators insist that every single historical artifact in their archive must be shown to the public. No artifact can be left in the vault, and it is physically impossible for an artifact to be present in more than one place at a time.

Over the years, the museum commissioned various specialized glass enclosures. To maintain precise structural integrity and humidity, each of these enclosures was manufactured to house exactly three specific artifacts. An enclosure is useless unless it is filled with the exact trio of artifacts it was designed for. Inserting fewer artifacts or swapping in different ones would ruin the climate control.

You must review the museum's inventory of these specialized enclosures and determine if it is possible to choose a subset of them that perfectly houses the entire archive. A successful selection means every artifact is displayed exactly once, with no empty spots in any chosen enclosure and no artifacts left unexhibited.

## Input
The first line contains two integers, **q** and **t**. The value **q** represents the number of display podiums to be used. The museum's floor plan can accommodate a minimum of one and a maximum of two hundred podiums. The total number of artifacts in the archive is exactly three times **q**, and they are identified by integers from 1 up to this exact total. The value **t** represents the number of available specialized enclosures in the museum's ledger, ranging from zero up to an administrative limit of twenty thousand.

Each of the following **t** lines describes one specialized enclosure using three integers **a**, **b**, and **c**. These represent the ID numbers of the artifacts the enclosure is built for. The three IDs on a line are always given in strictly increasing order, and each is a valid artifact ID.

## Output
If there is a valid selection of enclosures, print `YES` on the first line. Following that, print **q** lines, each containing the three artifact IDs for one of the chosen enclosures.
If no such selection is possible, print `NO`.

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
