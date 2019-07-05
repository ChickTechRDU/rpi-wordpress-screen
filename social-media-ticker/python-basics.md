# Getting started with programming

Programming can be thought of as giving instructions and remembering results of instructions for 
use in later instructions. The words and grammar of those instructions is defined by the 
**programming language** you write them in, just like different languages we may use to communicate
between people.

For example, using the Python programming language, we can instruct the computer to display "Hello 
Chicktech!" to our screen with the following code.

```python
print("Hello Chicktech!")
``` 

This is an instruction that tells the computer to "print" the text "Hello Chicktech!" to the 
screen.

Let's try it out!

## Development environments

Writing programs, like playing music or building a house, requires tools. A common tool is an 
"integrated development environment" or IDE for short. We'll use the **Thonny** IDE today.

> Insert pictures of directions to open Thonny here

In Thonny, type `print("Hello Chicktech!")` into the top window pane.

![first-statement.png](first-statement.png)

Now click the green run button above.

![run-program.png](run-program.png)

Congrats! You've got a working program!

## Debugging

Instructions in Python programs (sometimes also called "scripts") are run line-by-line, one at a 
time. Let's add another and see. Edit your code to look like the following by adding an additional
line.

```python
print("Hello Chicktech!")
print("Hello World!")
``` 

Now if we run this, we should see both "Hello Chicktech!" and "Hello World!" displayed in that 
order.

One neat feature of IDEs is that they have **debuggers**. These are tools which allow us to watch a
program run, pause it mid-execution, and inspect it as it does. We can trigger pauses by adding
**breakpoint** on the lines that we want to pause. Add breakpoints by double clicking on the first
line's line number on the left ("1"). Then click the green debug button above.  

![debugging.png](debugging.png)

When you click debug, notice you do not immediate see "Hello Chicktech!". Instead, execution is
paused at the first line (where you added a breakpoint), which is also highlighted in yellow. To 
execute this first line, press the "step over" button above, which "steps over" and executes 
the current line.

![step.png](step.png)

Now you see "Hello Chicktech!" output on the bottom pane. Press it again to see "Hello World!".

## Statements, expressions, and variables, oh my!

