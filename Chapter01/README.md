# Calculator Execution Time Optimization

This is a simple Python calculator made for my Distributed and Parallel Computing course.

The calculator performs four basic operations:

* Addition
* Subtraction
* Multiplication
* Division

## Original Calculator

The calculator uses separate functions for each operation:

```python
multiply(a, b)
divide(a, b)
add(a, b)
subtract(a, b)
```

The program also checks for division by zero.

## Execution Time

Jupyter Notebook's `%timeit` command is used to check the execution time of the calculator functions.

First, the original functions are tested.

After that, the code is optimized by removing unnecessary steps while keeping the same operations and results.

## Optimization

The main idea of the optimization is to make the code shorter and remove unnecessary intermediate variables or operations.

For example:

```python
def add(a, b):
    return a + b
```

The result of the operation remains the same, but the code performs fewer unnecessary steps.

## Technologies Used

* Python
* Jupyter Notebook
* GitHub

## Files

`calculator.py` - Contains the calculator program.

`README.md` - Contains information about the project.
