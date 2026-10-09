# Problem B — Two-Stage Assembly

Time limit: 1 s   Memory limit: 256 MB

## Description

You are managing a data pipeline that processes a batch of **j** distinct files. Each file must undergo two sequential operations: compression, followed by encryption.

The pipeline consists of a Compressor module and an Encryptor module. Both modules can operate simultaneously, but each can only process a single file at a time. The system enforces the following mechanics:

- You must choose a single sequence in which all **j** files are fed into the Compressor. The Compressor processes the files one by one strictly in this chosen order.
- As soon as a file completes compression, it is immediately appended to a FIFO (First-In, First-Out) buffer for the Encryptor.
- The Encryptor continuously monitors this buffer. Whenever the Encryptor is idle and the buffer is not empty, it removes the oldest file from the buffer and begins encrypting it.
- A file's encryption cannot commence until its compression has fully concluded.

Because the two modules operate independently, the Compressor can be compressing one file while the Encryptor is encrypting an earlier file. You must determine the optimal sequence to feed the files into the Compressor to minimize the total elapsed time until the Encryptor finishes the final file in the batch.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the duration the file requires in the Compressor and the Encryptor, respectively.

## Output

Print a single integer: the minimum possible time at which the Encryptor finishes the final file.

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

In Example 2, the single file occupies the Compressor for 5 time units, and then the Encryptor for 3 time units. It finishes at time 8.