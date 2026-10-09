# Interplanetary Relay

Time limit: 1 s   Memory limit: 256 MB

## Description

You need to transmit **j** data packets from Earth to a base on Mars. The transmission requires two steps: first, Earth sends the packet to an orbital relay; second, the relay forwards the packet to Mars.

For each packet, you are given the time it takes to upload from Earth to the relay, and the time it takes to download from the relay to Mars. 

The communication system operates under the following rules:
- You must choose a single sequence in which the packets will be transmitted.
- The Earth transmitter sends the packets to the relay one by one in your chosen sequence, with no gaps between packets.
- The relay sends the packets to Mars in the exact same sequence. It can only transmit one packet at a time.
- The relay can begin transmitting a packet to Mars only after two conditions are met: it has completely received that specific packet from Earth, and it has completely finished transmitting all earlier packets in the sequence to Mars.
- If the relay is ready to transmit but Earth has not yet finished uploading the necessary packet, the relay remains idle.

Your goal is to arrange the sequence of packets to minimize the total time elapsed from the start of the first upload until Mars has fully received the final packet. Report this minimum possible time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000), the number of data packets.
Each of the next **j** lines contains two integers **U** and **D** (1 ≤ U, D ≤ 1000000): the upload time from Earth to the relay, and the download time from the relay to Mars for that packet.

## Output

Print a single integer: the earliest possible time at which the final packet finishes its download to Mars.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single packet takes 5 units of time to upload to the relay, then 3 units to download to Mars, finishing at time 8.
