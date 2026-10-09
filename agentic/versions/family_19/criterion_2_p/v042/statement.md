# Problem B — Corporate Capital Transfer

Time limit: 2 s   Memory limit: 256 MB

## Description
A multinational corporation must transfer a specific target amount of capital from a primary holding account to a designated offshore account within a single trading day. The corporate network consists of various subsidiary accounts, connected by authorized one-way transfer agreements. Every agreement allows funds to be moved from one specific account to another, but regulatory rules cap the maximum amount that can be transferred along that specific agreement in a single day. 

Because the subsidiaries strictly act as intermediaries for this operation, their daily balances must remain unchanged by these transfers. Therefore, for every account other than the primary holding account and the offshore destination, the total funds received from incoming transfers must perfectly match the total funds sent out via outgoing transfers. At the primary holding account, the net funds sent must equal the target amount. At the offshore destination, the net funds received must equal the target amount. All transfer values must be non-negative integers.

Determine a set of transfer amounts for each agreement that successfully moves the exact target amount from the holding account to the destination without violating any agreement's daily limit. If it is impossible to move the full target amount in a single day under these rules, report that it cannot be done.

## Input
Line 1: Three integers `n`, `m`, and `1`, representing the number of accounts, the number of transfer agreements, and the number of currencies involved (which is always 1).
Line 2: Three integers `s`, `t`, and `d`, representing the ID of the primary holding account, the ID of the offshore destination account, and the target amount to transfer.
Next `m` lines: Three integers `u`, `v`, and `limit`, representing an agreement allowing up to `limit` units of currency to be transferred from account `u` to account `v`. Accounts are numbered from 1 to `n`.

## Output
If a valid transfer plan exists, print `YES` on the first line, followed by a second line containing `m` integers representing the amount to transfer on each agreement (in the same order they appeared in the input). If no such plan exists, print `NO`.

## Example
**Input**
4 5 1
1 4 10
1 2 10
1 3 10
2 3 5
2 4 10
3 4 10

**Output**
YES
5 5 0 5 5
