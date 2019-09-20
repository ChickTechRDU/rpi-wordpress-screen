# Python workshop

## 1. Getting started with programming

Programming can be thought of as giving instructions, called **code**, to a computer to carry out on
its own. The words and grammar of those instructions is defined by the **programming language** you 
write them in, just like different languages we may use to communicate between people.

For example, using the Python programming language, we can instruct the computer to display "Hello 
Chicktech!" to our screen with the following code.

```python
print("Hello Chicktech!")
```

This is an instruction that tells the computer to "print" the text "Hello Chicktech!" to the 
screen. Python is a simple but powerful programming language that is famously easy to learn but 
still powerful enough to --insert some cool statistic about how widely python is used--.

Let's try it out!

### 1.1 Development environments

Writing programs, like playing music or building a house, requires tools. A common tool is an 
"integrated development environment" or IDE for short. We'll use the **Thonny** IDE today.

> Insert pictures of directions to open Thonny here

In Thonny, type `print("Hello Chicktech!")` into the top window pane.

![first-statement.png](first-statement.png)

Now click the green run button above.

![run-program.png](run-program.png)

Congrats! You've got a working program!

### 1.2 Debugging and expressions

Instructions in Python programs (sometimes also called "scripts") are run line-by-line, one at a 
time. Let's add another and see. Edit your code to look like the following by adding an additional
line.

```python
print("Hello Chicktech!")
print("Hello World!") # Programming is great!
``` 

Now if we run this, we should see both "Hello Chicktech!" and "Hello World!" displayed in that 
order.

Our second line also included a **comment**, which started with the `#`. Comments can contain any 
text you want, and are ignored by the computer. They're just for people to communicate and 
understand their code better.

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

To remove a breakpoint, double click the breakpoint icon (the red circle next to the line number)
again. Try that now. If we start debugging now, our IDE will start stepping immediately from the 
first line, as if we set a breakpoint there. Click debug now, but don't step forward yet.

This time, let's use the "step into" button, instead of "step over". "Step into" allows us to see 
more deeply into what our program is doing, which is useful when we start to define more complex 
programs. "Step over" is useful when we want an overview, and don't want to get bogged down with 
the details.

1. Click "Step into" **once**.
   ![step-debug-before-step-in.png](start-debug-before-step-in.png)
2. Notice that our IDE has popped out the current line and highlighted it, executing it and moving 
   to the next line.
   ![step-in-1](step-in-1.png)
3. Click "Step into" **two** more times.
4. Now notice the text `"Hello Chicktech!"` changed color. The IDE **evaluated** our **expression**
   and is showing the result. Our expression, `"Hello Chicktech!"` was very simple, so it evaluated 
   to the same thing, but all kinds of expressions exist in python as a way to compute more 
   interesting values.
   ![step-in-3-string-expression.png](step-in-3-string-expression.png)
5. Click "Step into" **two** more times. 
6. Now notice `print` has turned into a green `None`. The `print` instruction itself is an 
   expression, but it doesn't evaluate to anything. `None` is python's value that represents nothing.
   ![step-in-5-print-expression.png](step-in-5-print-expression.png)
7. Click "Step into" **one** more time. 
8. Notice the expression from the previous line remains, even though our debugger is now paused 
   before the next line. This helps us keep track of previous expressions. 
   ![step-in-6-previous-expression.png](step-in-6-previous-expression.png)

### 1.3 Functions and variables

In our program, `print` is a function. Functions group many instructions together so than can
be reused simply by referencing the function's name. When we reuse a function, we say we're 
**calling** that function. 

We can write our own functions, too. Try this program for example:

```python
# Program 1.3.1
def greet(who):
    print("Hello {}!".format(who))

greet("Chicktech")    
greet("World")
```

If you run this program, you'll see it prints the same as our previous version, but now we can 
change how say hello in one place and have all greetings be uniform. Let's break this down a little 
bit.

Defining a function works like this:

1. First write the `def` **keyword**. This tells python we're about to define a function.
2. Then write the function's name next to `def` separated by a space.
3. Then we have a **parameter list**, surrounded by parenthesis. Parameters allow us to reuse a 
function with different values. In our `greet` function, the `who` parameter allowed us to print 
several greetings with the same function. We can refer to that parameter's value by its name.

Let's write another function that adds two numbers.

```python
# Program 1.3.2
def add(x, y):
    return x + y

print(add(2, 2))
```

Parameters are very similar to **variables**. You're probably already familiar with variables from
algebra. Variables remember a value for later reuse. For example, the below program adds numbers,
remembers those results, and then adds those results.

```python
# Program 1.3.3
def add(x, y):
    return x + y

firstNumber = add(2, 2)
anotherNumber = add(5, 10)
print(add(firstNumber, anotherNumber))
```

## 2. Writes scripts to interact with your blog

### 2.1 The amazing world of open source

So far we've written some small, simple programs. Writing something like a multiplayer game or a 
blog website at this rate would take a really long time! Fortunately, the cool thing about code is
that it can be easily shared and reused. By collaborating with others, we can build incredibly 
powerful programs in a fraction of the time it would take any one person alone to do it from 
scratch. Amazingly, there is a global community of sharing "open source" code: code that is freely 
available to be used, and free for you to modify and share your contributions back. This code is
bundled up into **packages** that can be downloaded and imported into your programs.

Let's use one of those packages, called "requests", that allows us to communicate with other 
websites, like the blog you're running, in our code. In this way, we can write programs that 
interact with our blog: automating tasks, summarizing posts, even displaying posts screens hooked up
to our Raspberry Pis. The sky is the limit!

> For full documentation of the "requests" package, see: https://2.python-requests.org/en/master/

```python
# Program 2.1.1
import requests
response = requests.get('http://blog.example.com/wp-json/wp/v2/posts', params={'per_page': 1})
posts = response.json()
if not posts:
    print("No posts found!")
else:
    post = posts[0]
    print('{0}: {1}'.format(post['date'], post['title']['rendered']))
```

Copy the above program into your IDE and run it. If you've written any posts in your blog, you 
should see the latest post and it's title. In a few lines of code, we've constructed a request 
from our program, sent it to the blog server, and parsed its response. Cool!

### 2.2 The World Wide Web and APIs

In the above example, we not only pulled code from another package, but we also used code from an
entirely separate program: your blog server. We asked the "requests" package to make a request to 
your blog for us, and we asked the blog server for the latest blog post title. We didn't have to 
write any of the code to store, manage, or retrieve that information. And similarly, those packages
then use other packages, too, and so on. That blog post script you have written above easily spans 
millions of lines of code if you think about all of the layers of packages that get used, all the 
way down to your operating system and your computers device drivers.

We can do this because of something called **application programming interfaces**, or **APIs** for 
short. APIs define a kind of simple language, specific to a certain area–like math, or blogs, or 
weather, or tweets–that can hide a limitless amount of code underneath it. When we use packages or
other servers, all we need are their APIs. Then, the rest of the implementation is hidden us, and 
can change and improve without us. We don't need to know or learn all of that code. APIs make us 
incredibly productive and allow us to create amazing things relatively quickly.

--TODO: insert diagram about APIs--

Different APIs come in different flavors. When talking to a website server, like the Wordpress blog 
from our python script, we interact using the HTTP protocol. A protocol is just an agreed way for
different parties to communicate or accomplish some task together. Think of snail mail: when you 
send a letter, we have a protocol that says we use envelopes, we write our addresses a certain way,
we put it in a mailbox, and letters get sent back to us in a similar way. The HTTP protocol is what 
serves websites over the internet.

--TODO: insert diagram about web service communication--

> For full documentation of the Wordpress API, see: https://developer.wordpress.org/rest-api/

The Wordpress API can do just about anything we want with our blog. Let's explore!










