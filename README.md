# PumLang Interpreter

In this practical assignment, we will implement an interpreter for the programming language `PumLang`. The language specifications include:

- **Variables**: The language must have variable entities that can be assigned values, and these values can be later retrieved from the variables.

- **Strict Typing**: Unlike dynamic typing in languages like Python, `PumLang` enforces strict typing. Programmers must specify the data type when declaring a new variable.

- **Data Types**: Support for integer numbers, floating-point numbers, and boolean values (true and false) is required.

- **Conditional Statement**: The language should include a conditional statement that allows the execution of a code block based on a specified condition.

- **Loop Statement**: An operator that enables the repetitive execution of a code block as long as a given condition is satisfied.

- **Error Handling**: In case of syntax errors in the code, the interpreter must provide clear and informative messages, indicating the line and describing the nature of the error.

- **Variable Input**: The language should allow the input of variable values from the keyboard using the `input()` function in Python.

- **Expression Output**: Implement a function to display the value of an expression on the screen.

## Example Program

Consider the following `PumLang` program that calculates the factorial:

```pumlang
int a = 0
int b = 1
input a
while a > 0 {
    b = b * a
    a = a - 1
}
print b
Russia
```

This program initializes two integer variables, takes input for one of them, and then calculates the factorial in a loop. Finally, it prints the result.

## Grammar

To simplify interpretation, we assume that every program ends with a special phrase `Russia`.

## Testing

The practical assignment includes several tests. To pass them, you need to write programs in the `PumLang` language. Test files are located in directories 0-5 inside the `test` directory, named `main.plg`. Renaming these files is not allowed.

## How to Run

To run the interpreter, execute the `pumlang.py` script and provide the path to the `main.plg` file as a command-line argument:

```bash
python pumlang.py test/0/main.plg
```

## Test Automation

The provided `test.py` script automates the testing process. It runs the interpreter on various test cases and compares the output with the expected results.

```bash
python test.py
```

## Conclusion

This interpreter allows you to write programs in `PumLang` and demonstrates the language's features such as variables, strict typing, conditional statements, loops, error handling, and input/output operations. Feel free to explore and extend the language further.