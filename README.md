# Python Grader Unit Testing Project

## Project Overview

This project demonstrates how Python's built-in `unittest` framework can be used to test a student grading application. The goal is to verify that the program works correctly under different conditions and to explore software testing coverage.

## Technologies Used

- Python 3
- Python unittest
- Visual Studio Code
- GitHub

## Project Files

The `PythonUnitTesting` folder contains:

- `GraderClass.py` — Contains the grading application and its methods.
- `test_grader.py` — Contains automated unit tests for the grading application.

## Features

The grading application can:

- Calculate the average of student grades.
- Convert numerical scores into letter grades.
- Determine whether a student has passed or failed.
- Validate scores and reject values outside the accepted range.

## Unit Testing

Six automated unit tests were created to verify the application's functionality, including normal inputs, boundary values, invalid inputs, and passing and failing scores.

**Test Results:** All six tests passed successfully.

## Code Coverage

Testing focused on four important types of coverage:

1. Statement Coverage
2. Function Coverage
3. Condition Coverage
4. Branch Coverage

The Python `trace` module reported 100% line coverage for `GraderClass.py`. This confirms that every executable line counted by the report was executed during testing. It does not independently establish 100% branch or condition coverage.

## Running the Tests

Open a terminal in the `PythonUnitTesting` directory and execute:

```bash
python3 -m unittest -v test_grader.py
```

## Conclusion

This project helped me better understand how automated unit testing improves software reliability. I learned how to test expected results, invalid inputs, and boundary conditions instead of only checking whether a program runs successfully.
