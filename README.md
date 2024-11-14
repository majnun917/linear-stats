# Linear-stats
The program linear-stats must be able to read a file and print the result of the following statical calculations: <b>Linear Regression</b> and <b>Pearson Correlation Coefficent.</b>. He read the data present in the path passed as argument.

## Input:
A file containing a list of numbers

## Output:
```
Linear Regression: y = ax + b    
Pearson Correlation Coefficent: r
```
avec: 
 y is the predecticted value,   
 x is the value of independence,    
 a the coefficent or estimated slope and    
 b is estimated intercept.    
And r notatiopn of Pearson Correlation Coefficent in the range [-1, 1]

## Usage
1- Clone the repository

```sh
git clone < your-url-repo>
```
2- Open the terminal and run the following command:
```sh
python3 run program-name.py data.txt
```
You need to install python  
(Replace program-name.py with your name actual name of program and data.txt with actual file name)

Example Output:
```
Linear Regression Line: y = -0.007408x + -2195.202493
Pearson Correlation Coefficient: -0.0168392903
```
## How it works

The program uses the numpy library to use its built-in functions to load and read the file and calculate the parameters of the regression line and Pearson's correlation coefficient.
And displays calculation results, with 6 decimal places for the <b>Linear Regression</b> and 10 decimal places for the <b>Pearson Correlation Coefficent.</b>

If numpy is not installed, you can use pip with the following command:
```sh
pip install numpy
```
For more details about [numpy](https://numpy.org/) and statical and probabilities calculations: [Linear Regression Line](https://en.wikipedia.org/wiki/Linear_regression) and [Pearson Correlation Coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)

## Limitations

The program assumes the input file contains valid numbers, it displays an error message if empty lines and non-numerical data.

## Test the program

The program can be tested by providing a sample data file and comparing the output with manually calculated results.
After downloading the [file](https://assets.01-edu.org/stats-projects/stat-bin-dockerized.zip).
Run the script with: ./bin/linear-stats,  then run the program with the created file (data.txt) by the previous command.

## Languages

This specific program is written in python. You can adapt the logic to other languages like Go or JavaScript.