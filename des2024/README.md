# Problem 2
Implement Python code for encryption and decryption using transposition cipher with key length `L=(P mod 8) + 8` (`P` here stands for the student number from problem 1).

## Description of transposition cipher
1. Let `N` = count of characters in a message.
2. Start writing the message in rows with length `L`.
3. Now record the encrypted message by going down each column. 

So a simple example for msg="DES2024RULES" and key length `L=4`:

| D | E | S | 2 |
| --- | --- | --- | --- |
| 0 | 2 | 4 | R |
| U | L | E | S |

Here the encrypted message will be "D0UE2LS4E2RS"

# Problem 3
Write your own simple symmetric encryption algorithm. A requirement for this algorithm is that length of keys must be equal to `L=(P mod 8) + 8` (like in Problem 2).

So you need to write the following 2 functions:
```Python
def encrypt(msg, key)
def decrypt(msg, key)
```
and verify that
```Python
decrypt(encrypt(msg, key)) == msg
```

# Problem 4
Here you will have to modify included Python scripts `clientA.py` and `clientB.py`.
Add an additional encryption mode named `custom` that will use your own encryption algorithm devised in Problem 3.

## Steps required to run the scripts
1. Install `cryptography` Python package via `pip install cryptography`.
2. In one shell, run `python clientA.py <mode>`, where `mode` is one of `plain`, `sym`, `custom`.
3. In another shell, run `python clientB.py <mode>`.
4. Messages typed in `clientB` should appear in `clientA`.
