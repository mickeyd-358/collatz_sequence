# Collatz sequence (3n+1 problem)


## Introduction
The Collatz conjecture is a famous unsolved problem in mathematics. It proposes that if you start with any positive integer and repeatedly apply a simple set of rules, you will eventually reach the number 1. These rules are: if the number is even, divide it by 2; if it is odd, multiply it by 3 and add 1.


This project utilised a simple while loop to test whether the integer in the sequence is odd or even, then print it. The program stops when the integer = 1, meaning the sequence is true for that number.

``` python
while n != 1:
    print(n)
    if n % 2 == 0:  # n is even
        n = n // 2
    else:  # n is odd
        n = 3 * n + 1
```

## Usage
When you run the script, it will prompt you to enter a positive integer.

Example:

$ python collatz_sequence.py

Enter a positive integer: 6

6

3

10

5

16

8

4

2

1