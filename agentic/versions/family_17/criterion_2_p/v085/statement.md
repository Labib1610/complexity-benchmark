# Problem B — Comprehensive Controller/Platform Pairing

Time limit: 2 s
Memory limit: 256 MB

## Description
The directorate oversees a collection of specialized assets split equally into two distinct types. The first half consists of controllers, which are assigned sequential IDs beginning at 1. The second half is made up of platforms, which are assigned sequential IDs immediately continuing from where the controller IDs left off.

A controller may only link with a platform if that exact pairing has successfully passed diagnostic testing. All approved pairings are recorded as entries in a certification log. For any given deployment, a subset of these approved pairings is chosen for activation. To avoid signal interference, a deployment is only valid if no single controller and no single platform is involved in more than one active pairing.

A comprehensive operational drill is being planned, requiring the entire asset collection to be utilized. You must determine if a valid deployment exists that simultaneously incorporates every controller and every platform. If such a complete deployment is achievable, output the list of active pairings; if it cannot be done, indicate that it is impossible.

## Input
The first line provides two integers $q$ and $t$. The integer $q$ represents the total count of controllers, and $t$ represents the total count of approved pairings in the log.
The directorate guarantees at least one controller is present. The maximum number of controllers is limited by the storage warehouse, which has 1,000 racks that each hold 100 controllers, meaning $q$ is at most 100,000. The log may be empty, but is restricted by a database limit of 400 pages, each allowing 1,000 entries, capping $t$ at 400,000.

This is followed by $t$ lines, each containing two integers $a$ and $b$ detailing an approved pairing. The value $a$ represents the controller's ID, and $b$ represents the platform's ID. As established by the naming convention, the controller ID will be a valid ID from the first half of the assets, and the platform ID will be a valid ID from the second half.

## Output
If a complete deployment can be formed, print `YES` on the first line. Then, output $q$ lines, each containing the two IDs of an active pairing. Any valid complete deployment is acceptable. If a complete deployment is impossible, print `NO`.

## Example

### Input
```text
3 4
1 4
1 6
2 5
3 4
```

### Output
```text
YES
1 6
2 5
3 4
```
