# matrix-inverse-clicker

A tiny Python program that calculates the inverse of a square matrix using
**Gauss-Jordan elimination**.

No NumPy. No `numpy.linalg.inv()`. Just row operations.

## What it does

The program:

1. Reads an `n x n` matrix.
2. Builds the augmented matrix `[A | I]`.
3. Performs elementary row operations.
4. Shows each step.
5. Returns `A^-1` if it exists.
6. Detects singular matrices whose inverse does not exist.

## Example

Input:

```text
2
1 2
3 4
```

The program starts from:

```text
1  2  |  1  0
3  4  |  0  1
```

and performs Gauss-Jordan elimination until the left side becomes the identity matrix:

```text
1  0  |  -2    1
0  1  |  3/2  -1/2
```

So:

```text
A^-1 =
[ -2      1   ]
[  3/2   -1/2 ]
```

## Why fractions?

The program uses Python's built-in `Fraction` class so that results like
`1/3` stay exact instead of becoming long floating-point decimals.

## Run

Python 3 is enough. No external packages are required.

```bash
python main.py
```

## Example matrices

Invertible:

```text
2
1 2
3 4
```

Singular:

```text
2
1 2
2 4
```

The second matrix has no inverse.

## Goal

This is a small practice project for understanding how matrix inversion
actually works instead of hiding the process behind a library function.
