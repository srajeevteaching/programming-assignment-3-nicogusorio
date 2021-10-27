CS151 PROGRAMMING ASSIGNMENT #3
DUE: Wednesday 10/27/2021 

PROBLEM
Create a program that will calculate various sports statistics for the user, based on the user’s choice of statistic.

PURPOSE OF THE ASSIGNMENT
The purpose of this assignment is to give you practice with

input & output
decision making
function design and implementation
error checking

REQUIREMENTS ANALYSIS
Your program will give the user the option of calculating statistics relevant to three sports. You must do the calculations for the following sports in your program:

1 - Quarterback rating in American football

The quarterback rating determines how good a quarterback is in passing (throwing) a football. A perfect passer rating in the NFL is considered to be a 158.3.

QB rating = 100 * [5(completions/attempts – 0.3) + 0.25(passing_yards/attempts-3) + 20(touchdown_passes/attempts) + 2.375 – (25 * interceptions/attempts)]/6

Note that attempts means the number of passing attempts made, and is the same number used throughout the equation.
Eventually, you will want to tell the user whether or not the quarterback is a perfect passer.

2 - Calculate the score for a team in a game of Quidditch as described by the International Quidditch Association (http://www.iqasport.com/).

A goal is scored by propelling the quaffle through a hoop. The team earns 10 points per goal.
If the team has caught the snitch, the team earns an additional 30 points (note that there is only one snitch).   

3 - Calculate the final score for a gymnast on any apparatus.

Assume there are 6 scores (we’re simplifying slightly from the real world). One score is on difficulty. The other 5 scores are on execution. All scores are between 0 and 10 (assuming the user enters integers, you do not have to check for they are between 0 and 10). The final score is computed by adding the difficulty score to the average of the execution scores.

In your program, you must do some basic error checking: check if you are going to divide by zero when relevant, and don’t do the calculation if that’s the case; and before typecasting input to an int, check that it is only digits, and don’t convert to an int or do the calculation otherwise. In any case where an error is detected, output that it was an error, and don’t continue the calculation – you may return a zero for the result of that calculation.

**You need to code 3 different functions to calculate the scores of the 3 sports. There should not be any input or output inside the three functions**. 

Make the main part of your program be in a "main" function. The main function never takes parameters, and does not return anything. The main function will call the other functions.

PROGRAMMING REQUIREMENTS
After your first part is complete and correct, it’s time to start programming and then testing:

Follow good usability/HCI principles in your input and output (make it clear the type of input you are asking for)
Follow good use of functions
Remember to define functions before they are used (so if function A calls function B, you need to define function B first in your program)
Remember to state the purpose of the program.

Create a partial flowchart for your program. For calculations, just draw a box and state "calculations for X" where X is replaced with the name of the sport (essentially, "calculations for X" represents a function call).

Label the control paths in your flowchart. For each control path related to the sport in your flowchart, list a test case.
Test your program using the test cases. You ALSO need to make sure you test your other sport calculations even though they aren’t part of your flowchart. If it doesn’t give the expected output, find the error and fix it. You are expected to turn in a fully functioning program without errors.

FINAL SUBMISSION  
To Moodle:
  Your .py file
  Your flow chart
  Your test cases based on your flowchart in testcases.xlsx. You should have at least 1 test case per control path, using boundary values.
To github:
  Your .py file
Remember to double check on github.com that your files pushed. If they didn’t, you need to push them. I can only see what is on github.com, not what is only on your computer.
