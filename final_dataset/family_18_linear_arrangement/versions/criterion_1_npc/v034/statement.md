# Problem A — Backbone Trenching for the Control Vault

Time limit: 5 s
Memory limit: 256 MB

## Description
A new control vault requires installing an inventory of hardware components along a straight chassis track. The track is divided into a sequence of installation stations. Each hardware component must be secured into exactly one station, and no two components can share a station. The total count of available stations perfectly matches the inventory of components.

Certain pairs of components must communicate directly and are physically linked by a continuous fiber cord. The cords are routed parallel to the track. The amount of cord required to link a pair of components is determined solely by how many station intervals separate them. For instance, if one component is placed in the first station and its linked partner is placed in the fourth station, connecting them consumes exactly three units of cord.

The facility has provisioned a maximum total length of fiber cord for the entire track assembly. There is no restriction on individual cords or how many cords overlap along the track; the only restriction is on the grand total. 

You must determine if there is a way to assign every component to a station such that the sum of the cord lengths used by all required links is within the facility's provisioned limit. A placement that minimizes the cord length for some links might cause others to overshoot the limit, so the overall configuration must be considered.

## Input
The first line contains three values: the inventory count of hardware components, the total count of direct communication links that must be established, and the maximum units of fiber cord provisioned for the facility.

Each of the subsequent lines defines a required communication link by listing two integers. These integers represent the identifiers of the two components to be connected. Components are identified by integers starting at 1 and ending at the total inventory count.

## Output
If the components can be arranged to respect the cord provision, print `YES` on the first line. On the second line, print a sequence of integers where the first integer is the station number assigned to component 1, the second integer is the station assigned to component 2, and so on, continuing up to the final component. The station numbers must be distinct and span from 1 to the total inventory count. 

If no configuration can be built without exceeding the fiber cord provision, print `NO`.

## Example

### Input
```
4 3 4
1 2
1 3
1 4
```

### Output
```
YES
2 1 3 4
```
