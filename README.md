# Calculator Project

This is a simple Python project for a calculator that performs basic operations like addition, subtraction, multiplication, division, and exponentiation.

## Features

- The program shows a menu with different operations.
- The user chooses an operation and inputs two numbers.
- The program performs the operation and shows the result.
- After each operation, the user can choose to do another operation or exit.

## How to Run

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/vinicius-schurhaus/calculator-project
    ```
2. Go to the project folder:
    ```bash
    cd calculator-project
    ```
3. Run the program:
    ```bash
    python3 calculator.py
    ```

The program will show the menu, and you can choose the operation. Then, enter the numbers and see the result.

## Code Overview

The code is split into several functions:

1. **showMenu()**: Displays the list of available operations.
2. **displaySelectedOption(option)**: Shows which operation was chosen.
3. **Mathematical Functions**:
   - `add(n1, n2)`: Adds two numbers.
   - `subtract(n1, n2)`: Subtracts two numbers.
   - `multiply(n1, n2)`: Multiplies two numbers.
   - `divide(n1, n2)`: Divides two numbers (handles division by zero).
   - `exponentiate(n1, n2)`: Raises `n1` to the power of `n2`.
4. **calculate(option, n1, n2)**: Performs the chosen operation.
5. **showResult(n1, n2, result, option)**: Displays the result.
6. **askToContinue()**: Asks the user if they want to perform another operation.

## Learning Python

This project covers some important Python concepts, such as:

- **Functions**: Using functions to organize code.
- **Error Handling**: Dealing with invalid inputs.
- **Control Structures**: Using `if-else` and loops.