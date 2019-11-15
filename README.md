# Welcome to the ChickTech kickoff!

## Icebreaker
To get to know each other, lets quickly go around the room.  When it is your turn state:

- Your name
- School you go to
- What your programming and sysadmin excerince is
- Something you like that starts with the first letter of your first name

I'll start.
My name is Dustin.  I've been working in IT as a sysadmin for 15 years now.  I like death metal.

## Intros

Now that the icebreaker is done, we want to tell you a bit more about ourselves and the company we work for.  We hope that this will give you a better idea about what people actually do in IT and steer you towards the person you need to talk to if a specific thing we do in our lab interests you.

My name is Dustin Minnich and I'm a Principal Systems Administrator.  As a sysadmin I'm responsible for:

- Designing, building, documenting and supporting full stack solutions to business problems
- Making sure systems are always reachable by planning and implementing high availability and disaster recovery strategies
- Automating day to day tasks and writing basic scripts and applications
- Rolling out new versions of custom code to systems
- Working closely with developers to ensure that they make good security and performance decisions

My name is Michael White and I'm a Lead Application Integration Engineer, which is just a fancy way to say Senior Software Engineer.  As a Lead Application Integration Engineer I'm responsible for:

- Making sure people don't do dumb shit or recreate the sins of their fathers.
- TODO - miwhite

My name is Alec Henninger and I'm a Senior Software Applications Engineer.  As a Software Engineer I'm responsible for:

- Choosing technology paths that will directly make or break a 34 billion dollar company on a daily basis.
- Designing tools to help other teams build web servers and applications that power redhat.com and some of the world's largest organizations
- Making these servers resilient to bugs or hardware failures so they keep running no matter what happens
- Triaging and fixing outages at any time of day and making sure we learn from failures to always get better

My name is Sneha Gunta and I'm a Senior Software Applications Engineer.  As a Software Engineer, I:
- TODO - sgunta

My name is Claudia Van Valkenhoef and I'm a Manager.  As a Manager I'm responsible for:

- Herding cats and attempting to add stability to a chaotic world.
- Plan the roadmap
- Engage and keep the team focused on delivering on time
- Professional development of your associates
- Remove roadblocks and ensure the team has everything they need to do their job (hardware, software, stuff from other teams)
- Hire/Fire people
- Status updates on ongoing projects, keep stakeholders informed




We all work at a company named Red Hat.  Red Hat is an open source software company.  This means the software we develop is free for anybody to use and improve.  We believe that when people work together, instead of in competition with against one another, great things happen.

Red Hats core product is a version of Linux.  Linux is an Operating System similar to macOS or Windows but is primarily used by servers and not laptops and home pcs. Most of the websites you visit are powered by Linux, Android phones are powered by Linux, nearly all super computers are powered by Linux -- our presence is everywhere, even if you haven't heard of us before today.  Red Hat also offers OpenShift which is an orchestration and management layer on top of Docker like containers and OpenStack which is an alternative to Amazon AWS could as well as tons of other things.

Red Hat is a GREAT company to work for.  It is full of passionate and diverse people with all kinds of skillsets.  Everybody is always willing to pitch in and help in anyway they can despite any formal job duties like those listed above.  The work environment is casual (no fancy clothes, heirarchy means nothing) and fun. There are meetup style groups and events happening on a regular basis.

## Objective
Have you ever been to a concert or a sporting event where they put tweets on the jumbotron(big screen)?

What about watched the news or a TV show where they are displaying a facebook post and are discussing it?

Over the next two days we will be building something similar!

With a Raspberry Pi, Wordpress, some python code and an LCD screen you will be able to post to your blog and see it on your screen.


## Building the stack

### What is a Raspberry Pi?
The Raspberry Pi Foundation is a dream a come true for people interested in technology. For very little money, they will sell you a 'disposable' baby computer that runs standard hardware and is extendable by all kinds of open source software.

Each part of that last sentence is important.

With a standalone Pi costing $35 and a kit costing $80, not only are they accessible to people who couldn't afford computers in the past -- they encourage more well off people to do bold things.  You may be scared to take apart your new iPhone or afraid to load Linux or other custom software on the laptop you use for homework.  The Pi is built to be tinkered with.  It is easy to start over from a software standpoint and if your Pi is in a bad state it impacts only your hobby.  If you do something that kills the hardware, you will have to spend another $35, which sucks, but is way easier to swallow than killing your phone or laptop.

The Raspberry Pi 3 B+ that we are using in this class has the following specs:

- Quad Core A53 1.4GHz ARM Processor
- 1GB DDR2 RAM
- Ethernet, Wifi, Bluetooth
- Mirco SD card slot
- 40 Pin GPIO header

To put in perspective how low power that is, while it isn't an apples to apples comparison, even the Samsung Galaxy S3 released in 2012 had higher specs.  Outside of needing to keep costs low, uniformity is actually more important than horsepower in the hobby market.  The fact that you can build something once and know it will behave the exact same on all devices of that type is huge.  It also allows you to focus on your work and only learn how to troubleshoot one platform.  In contrast, imagine having to write a game that supports running on AMD and Intel process, Windows 7 and Windows 10, AMD and Nvidia grahpics cards, maybe even Xbox and PS4 as well as PC, etc.  Yes APIs, frameworks and libraries abstract away some/most of the pain, but nothing is as nice as having a fleet of all the exact same hardware to build on top of.

Open Source software is about having the freedom to reuse and improve the applications that run on your devices.  Has Apple or Google ever pushed a software update that changed something on your phone in a way you didn't like?  Ever thought this instagram app would be better if it could also do X?  With open source software people write code to meet their needs and then put it out on the internet for anybody to use for free.  This means you can pick it up and use it as-is or if it doesn't quite meet your needs you can alter it and then even put it back out on the internet for other folks to use for free.  This culture has helped the Pi hobby scene flourish.  If you can think of something you'd like your Pi to do, chances are somebody somewhere has already done something similar and you can use their work as a launching off point to accomplish your goal.


### What is LAMP?
Linux Operating System + Apache Web Server + Maria Database Server + the PHP programming language make up the `LAMP` web services stack.  Together they allow a computer to serve up dynamic and interactive webpages.  According to [netcraft](https://news.netcraft.com/archives/2019/06/17/june-2019-web-server-survey.html) 30% of the internet is ran off of Apache and according to [zdnet](https://www.zdnet.com/article/can-the-internet-exist-without-linux/) 96% of the internet is run on top of Linux.  Those statistics coupled with the widespread useage of things like Wordpress blogs, Drupal CMS systems, Vanilla Foums, ownCloud collaboration servers and MediaWiki systems indicate that the LAMP stack has widespread adoption on the internet.  It is also worth noting that it is one of the oldest stacks.  What these things mean to you is that as you begin to learn this stack, there will be plenty of open source code for you to sample from and plenty of places to look for and ask for help when you need it.


#### Linux
Your Pi is already running an optimized version of Linux called Raspbian.  Raspbian is based on one of the largest distributions of Linux called [Debian](https://www.debian.org/).  If you haven't heard of either of those and have happened to heard of Ubuntu, know that Ubuntu is also based on Debian to some degree.  Backing up a bit, in case all of that was greek to you -- an Operating System is the low level software that runs on your device that determines how you intearct with it via various interfaces (touch screen, mouse, keyboard) and an operating system allows you to install other software on top of it.  Windows is an Operating System, so is iOS on your phone.  The Linux operating system is open source and flexible.  Groups of people package it in different ways (called distributions) to meet different needs.  These different distributions allow linux to power android phones, smart TVs, your Pi, and most of the servers on the internet despite the fact that they are all very different devices filling different needs.

The linux operating system is very tweakable, secure and privacy oriented...
So if I know I'm not going to ever use a webcam I can remove the hardware support for it from the kernel to save on resources.  I can also install a different Desktop Manager (think complex theme) and run stuff on older systems easier.

When you login to a linux system you are a user who can't make changes to the system.  This is what plagued Windows back in the day. Viruses would install and take over the system without every needing to escalate privileges.

Since there is no central linux group and since a lot of people develop it as a hobby there isn't anybody trying to collect data about you to then market things to you, which is great if you care about your privacy.

It also generally features a package manager and treats everything like a file...
When you want to install a piece of software in linux you can run a command or click a couple things and then you have it and it will be easy to keep up to date.  Contrast this to MacOS or Windows where you have to go each vendors website and download and install each piece of software like that.

The fact that linux treats everything as a file allows linux users to easily string together commands for automation and scripting purposes.


#### Apache
Apache is a flexible, well established, powerful and popular web server.  When you open up Chrome and type in `reddit.com`, Chrome is the client and the web server is what Reddit's linux servers use to send you back your memes and cat videos.

Apache on its own can only serve up static content.  You can think of static content as non-interactive sites.  So if you wanted to serve up a copy of your resume and a brief page about yourself, that you write in HTML yourself, Apache alone would be enough.  If you instead wanted a site with an admin front-end that made making changes easy and allowed people to comment on articles and things like that, then you would need a dynamic language and an apache module or proxy to a server that spoke that language.  You would also likely need a datastore.  That is where Maria DB and PHP will come in later.  For the time being, lets install Apache and serve up some static content.

Install Apache

    sudo su -
    apt-get install apache2

Start it and tell it to startup when you Pi boots up

    systemctl restart apache2
    systemctl enable apache2

When accessing websites your browser makes what is called a DNS lookup.  This converts google.com to an IP address/number that the computers actually pay attention to, the words are for our simple human brains.  To simulate that we will be creating what is called a hosts file entry.

Get the IP of your interface

    root@raspberrypi:~/2019-chicktech/files/bin# ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 52:54:00:08:25:14 brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.18/24 brd 192.168.122.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::6858:c1fc:4305:6ce8/64 scope link
       valid_lft forever preferred_lft forever

You are looking for the non `lo` interface that has something on the `inet` line.  Above our IP is `192.168.122.18`. Now lets add that IP address to our hosts file along with a DNS name.  For the name use first letter of your first name and your whole last name. For example

    /opt/bin/add_hosts_line.sh 192.168.122.18 dminnich

Verify it got added

    root@raspberrypi:~/2019-chicktech/files/bin# tail -n1 /etc/hosts
    192.168.122.18    dminnich.example.com

What this means is now whenever my Pi tries to go to `dminnich.example.com` the content for that website will be served by the Pi itself.

Lets add some static content

    echo "hi chicktech" > /var/www/html/index.html

View it by pulling up the browser on your Pi and going to $username.example.com.

If you wanted to create a real webpage you would need to start writing HTML, CSS and javascript. [w3schools](https://www.w3schools.com/html/default.asp) have good tutorials that teach you those languages. Just keep in mind that you won't be able to create terribly interactive webpages until you start doing some of the stuff below as well.


#### Maria DB

Maria DB is highly popular, stable, scalable and free SQL compliant database server.  If you are unfamilar with databases, you can think of them as a complex set of linked spreadsheets.  They allow you to get answers to questions like "who in my class has a name that starts with an M and was born after 1990 and has brown hair". Oh, and sort that by the youngest person first.  As websites and applications become more complex they need to be able to answer questions like that (all posts by author sorted by newest) quickly so a database is used to store the information.  The database not only can answer these questions faster than logic in code could if the web server had to crawl through a bunch of files, it also creates a useful centralization point.  If all of your content is in a database, you only need to backup the database.  Also, you can add more and more web servers as demand grows and they can all talk to the same database, whereas each of them all having the same files at the same time is a much harder problem to sovle.

Lets explore Maria DB.

Install it

    sudo su -
    apt-get install mariadb-server

Start it and tell it to startup when you Pi boots up

    systemctl restart mariadb
    systemctl enable mariadb

Login and create a database

    root@raspberrypi:~/2019-chicktech/files/bin# mysql -uroot
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 2
    Server version: 10.1.38-MariaDB-0+deb9u1 Debian 9.8

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]> create database chicktech_test;
    Query OK, 1 row affected (0.00 sec)

Create a table

    use chicktech_test;
    Database changed
    MariaDB [chicktech_test]> create table people(id INT NOT NULL AUTO_INCREMENT,name VARCHAR(100) NOT NULL,age int NOT NULL,PRIMARY KEY ( id ));
    Query OK, 0 rows affected (0.00 sec)

Add some people to the table

    MariaDB [chicktech_test]> insert into people (name, age) VALUES ("bill", 10), ("bobby", 11), ("samantha", 15), ("kathy", 21);
    Query OK, 4 rows affected (0.01 sec)
    Records: 4  Duplicates: 0  Warnings: 0


Show all people

    MariaDB [chicktech_test]> select * from people;
    +----+----------+-----+
    | id | name     | age |
    +----+----------+-----+
    |  1 | bill     |  10 |
    |  2 | bobby    |  11 |
    |  3 | samantha |  15 |
    |  4 | kathy    |  21 |
    +----+----------+-----+
    4 rows in set (0.00 sec)

Show people whose name starts with a b and is less than 11 years old

    MariaDB [chicktech_test]> select name from people WHERE name LIKE 'b%' AND age<11;
    +------+
    | name |
    +------+
    | bill |
    +------+
    1 row in set (0.00 sec)

Create a user that can use this database

    CREATE USER 'chicktech'@'localhost' IDENTIFIED BY 'chicktech';
    GRANT ALL PRIVILEGES ON chicktech_test.* TO 'chicktech'@'localhost';
    FLUSH PRIVILEGES;

Exit Maria DB

    MariaDB [chicktech_test]> exit
    Bye

[tutorialspoint](https://www.tutorialspoint.com/mysql/index.htm) has a good introductory Maria DB tutorial.  If you enjoy databases lots of companies hire DBAs that do nothing but database work.

#### PHP

PHP is a well established programming language that runs on many operating systems.  It is most commonly used by web developers where it acts as an interpeted language that complies and executes on the server when called.  One of the core features of PHP is that you can easily mix PHP, Javascript and HTML in the same file.  This makes developing simple web applications easy to do as you don't have to learn or be restricted by frameworks or MVC practices.  Some of these same features are also its cons, by the way :).

Lets install PHP

    sudo su -
    apt-get install php-mysql php7.3 libapache2-mod-php

Tell Apache to use PHP

    a2enmod php7.3
    systemctl restart apache2

Create a PHP diagnostics page

    echo "<?php phpinfo(); ?>" > /var/www/html/info.php

See if the page works.

- In the browser on your Pi go to $username.example.com/info.php
- You should see a purple page with a bunch of information on it

Lets quickly look at a page that will show the results of the that query we did in the Maria DB section.

    cat /var/www/html/query.php
    <?php
    $conn = new mysqli('localhost', 'chicktech', 'chicktech', 'chicktech_test');
    if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    }
    $sql = "select name from people WHERE name LIKE 'b%' AND age<11";
    $result = $conn->query($sql);
    while($row = $result->fetch_assoc()) {
    echo $row["name"]. "<br>";
    }
    $conn->close();
    ?>

Now go to $username.example.com/query.php in your browser. Notice how:

- It prints just `bill` like the previous Maria DB query
- You can see how the code connects using the user we create, runs a query then prints a line for each result found.


[w3schools](https://www.w3schools.com/php7/) has a good introductory PHP tutorial if you are interested in learning more about PHP.


### What is Wordpress?

Wordpress is a personal and easy to use blogging plaform that runs on top of a LAMP stack.  It features an extensive plugin and template system and is backed by a large open source community.  [w3techs](https://w3techs.com/technologies/details/cm-wordpress/all/all) estimates that 34% of the internet runs on top of wordpress!

Now that you've seen what its like to create your own web pages and databases, let's have Wordpress do the heavy lifting for us.

Install Wordpress

    sudo su -
    apt-get install wordpress

Wordpress will need a database to store its content.  The install of wordpress in the previous step also installed a script that makes creating that database easier than what we did a few sections ago.

Use the database creation script

    chmod +x /usr/share/doc/wordpress/examples/setup-mysql
    /usr/share/doc/wordpress/examples/setup-mysql -n wordpress $username.example.com

    PING dminnich.example.com (192.168.122.18) 56(84) bytes of data.
    64 bytes from dminnich.example.com (192.168.122.18): icmp_seq=1 ttl=64 time=0.013 ms

    --- dminnich.example.com ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 0.013/0.013/0.013/0.000 ms
    /etc/wordpress/config-dminnich.example.com.php written
    Goto http://dminnich.example.com to setup Wordpress

Wordpress likes to create pretty URLs and to serve content outside of /var/www/html.  For Apache to do that we need enable a couple Apache modules

    a2enmod rewrite
    a2enmod vhost_alias

A single Apache install is capable of serving multiple websites.  This is called Virtual Hosting. A fresh install of Apache, however, is only configured to serve one default site.  The script we will run in a bit will create a new wordpress Apache site, enable it, and disable the default Apache site.

Before we run the script lets learn about what it is doing.  Here is what an Apache site config looks like

    root@raspberrypi:~/2019-chicktech/files/apache2# cat /root/2019-chicktech/files/apache2/wordpress.conf
    <VirtualHost *:80>
        ServerName REPLACEME.example.com

        ServerAdmin webmaster@example.com
        DocumentRoot /usr/share/wordpress

        Alias /wp-content /var/lib/wordpress/wp-content
        <Directory /usr/share/wordpress>
            Options FollowSymLinks
            AllowOverride Limit Options FileInfo
            DirectoryIndex index.php
            Require all granted
        </Directory>
        <Directory /var/lib/wordpress/wp-content>
            Options FollowSymLinks
            Require all granted
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

    </VirtualHost>


`ServerName` determines what hostname to answer on and `DocumentRoot` determines what content to serve for that site.


The script itself contains some commands that disable and enable sites.

    cat /opt/bin/wordpress_apache.sh
    ...
    a2dissite 000-default
    a2dissite default-ssl
    #remove the static page we created earlier
    rm /var/www/html/index.html
    a2ensite wordpress.conf
    ...
    #restart apache to pickup the changes
    systemctl restart apache2

The other stuff in that script tweaks a few Wordpress settings that are specific for our teaching environment.  Lets run the script.

    /opt/bin/wordpress_apache.sh $username

You complete the Wordpress install in your browser.  Go to $username.example.com in your browser and answer the questions the same way I demo now.

Our lab will involve posting lots of comments to blogs. Since Wordpress might detect this as "spam", we are going to turn off some of its anti-spam features.

Make sure all options with red boxes next to them in the below screenshot are unchecked under `Settings > Discussion`

![antispam.png](/docs/antispam.png)


Now that Wordpress is installed.  Watch as I demo a few things:

- Logging in
- Creating a blog post
- Viewing the blog post
- Navigating to the plugin and theme screens



### Bonuses

All of the stuff we've done above are part of a system administrators job.  We built a stack and installed an application. A developer will now pick up from here and start writing custom code or changing things to meet their needs.  While they focus on that stuff the system administrators need to think about things like disaster recovery and uptime.  In the time before the next session feel free to explore simulations of those two objectives using the guidance below.

**#1 Backups**
Using [rsync](https://linux.die.net/man/1/rsync) and [bash](https://ryanstutorials.net/bash-scripting-tutorial/) write a script that copies new and changed files from `/opt/rsync_source` to `/opt/rsync_destination`.  The script `/opt/bin/new_rsync_file.sh` and `ls -lhart /opt/rsync_*` can be used to see if you got it working right.

A solution can be found in `/opt/bin/rsync_solution.sh`.

NOTE: In the real world you'd use some dedicated backup software instead of rsync.  You'd also make sure the destination wasn't on the same machine and you'd schedule regular backups.

**#2 Monitoring**
Using [pgrep](https://linux.die.net/man/1/pgrep) and [bash](https://ryanstutorials.net/bash-scripting-tutorial/) write a script that prints "ALERT" if the process `atestprocess` isn't running.  The script `/opt/bin/atestprocess.sh start|stop` and `ps aux` can be used to see if you got it right.

A solution can be found in `/opt/bin/monitoring_solution.sh`.

NOTE: In the real world a monitoring tool would have mechanisms to do this for you and would bubble up the alert to something that would email/text somebody instead of printing ALERT to the console.

**#3 Wordpress Customization**
Bored with sysadmin work?

Remember the themes and plugins sections of Wordpress I showed you earlier?  Go exploring.  Make your blog beautiful and unique!

## Programming Basics

Programming can be thought of as giving instructions, called **code**, to a computer to carry out on its own. The words and grammar of those instructions is defined by the **programming language** you write them in, just like different languages we may use to communicate between people.

For example, using the Python programming language, we can instruct the computer to display "Hello Chicktech!" to our screen with the following code.

```python
print("Hello Chicktech!")
```

This is an instruction that tells the computer to "print" the text "Hello Chicktech!" to the screen. According to [Tiobe](https://www.infoworld.com/article/3331603/pythons-popularity-surges-as-a-mainstay-language.html), which ranks languages based on numbers of engineers in the field and search trends across search engines, python is currently the third most popular language.  Python will likely continue to gain marketshare since it is easy to learn and use and still powerful enough to be used by some of the most visited sites on the internet like [pintrest](https://www.pinterest.com/) and [reddit](https://www.reddit.com).

Let's try it out!

### Development environments

Writing programs, like playing music or building a house, requires tools. A common tool is an "integrated development environment" or IDE for short. We'll use the **Thonny** IDE today.

![thonny.png](/docs/thonny.png)

Before we start coding, lets turn up the verbosity of Thonny's debugger to make troubleshooting code in the future easier.

![thonnya.png](/docs/thonnya.png)

![thonnyb.png](/docs/thonnyb.png)

Now, in Thonny, type `print("Hello Chicktech!")` into the top window pane.

![first-statement.png](/docs/first-statement.png)

Now click the green run button above.

![run-program.png](/docs/run-program.png)

Congrats! You've got a working program!

### Debugging and expressions

Instructions in Python programs (sometimes also called "scripts") are run line-by-line, one at a time. Let's add another and see. Edit your code to look like the following by adding an additional line.

```python
print("Hello Chicktech!")
print("Hello World!") # Programming is great!
```

Now if we run this, we should see both "Hello Chicktech!" and "Hello World!" displayed in that order.

Our second line also included a **comment**, which started with the `#`. Comments can contain any text you want, and are ignored by the computer. They're just for people to communicate and understand their code better.

One neat feature of IDEs is that they have **debuggers**. These are tools which allow us to watch a program run, pause it mid-execution, and inspect what its doing as it does it. We can trigger pauses by adding **breakpoints** on the lines that we want to pause on. Add breakpoints by double clicking on the first line's line number on the left ("1"). Then click the green debug button above.

![debugging.png](/docs/debugging.png)

When you click debug, notice you do not immediately see "Hello Chicktech!". Instead, execution is paused at the first line (where you added a breakpoint), which is also highlighted in yellow. To execute this first line, press the "step over" button above, which "steps over" and executes the current line.

![step.png](/docs/step.png)

Now you see "Hello Chicktech!" output on the bottom pane. Press it again to see "Hello World!".

To remove a breakpoint, double click the breakpoint icon (the red circle next to the line number) again. Try that now. If we start debugging now, our IDE will start stepping immediately from the first line, as if we set a breakpoint there. Click debug now, but don't step forward yet.

This time, let's use the "step into" button, instead of "step over". "Step into" allows us to see more deeply into what our program is doing, which is useful when we start to define more complex programs. "Step over" is useful when we want an overview, and don't want to get bogged down with the details.

1. Click "Step into" **once**.
   ![step-debug-before-step-in.png](/docs/start-debug-before-step-in.png)
2. Notice that our IDE has popped out the current line and highlighted it, executing it and moving to the next line.
   ![step-in-1](/docs/step-in-1.png)
3. Click "Step into" **two** more times.
4. Now notice the text `"Hello Chicktech!"` changed color. The IDE **evaluated** our **expression** and is showing the result. Our expression, `"Hello Chicktech!"` was very simple, so it evaluated to the same thing, but all kinds of expressions exist in python as a way to compute more interesting values.
   ![step-in-3-string-expression.png](/docs/step-in-3-string-expression.png)
5. Click "Step into" **two** more times.
6. Now notice `print` has turned into a green `None`. The `print` instruction itself is an expression, but it doesn't evaluate to anything. `None` is python's value that represents nothing.
   ![step-in-5-print-expression.png](/docs/step-in-5-print-expression.png)
7. Click "Step into" **one** more time and the debugger will jump to the next line.


### Functions and variables

In our program, `print` is a function. Functions group many instructions together so that they can be reused simply by referencing the function's name. When we reuse a function, we say we're **calling** that function.

We can write our own functions, too. Try this program for example:

```python
# Program 1.3.1
def greet(who):
    print("😎 Hello {}! 😎".format(who))

greet("Chicktech")    
greet("World")
```

If you run this program, you'll see it prints the same as our previous version, but now we can change how say hello in one place and have all greetings be uniform. Let's break this down a little bit.

Defining a function works like this:

1. First write the `def` **keyword**. This tells python we're about to define a function.
2. Then write the function's name next to `def` separated by a space. We'll use the functions name to call it later.
3. Then we have a **parameter list**, surrounded by parenthesis. Parameters allow us to reuse a function with different values. In our `greet` function, the `who` parameter allowed us to print several different greetings reusing the same function. We can refer to that parameter's value by its name inside of the function.

Let's write another function that adds two numbers.

```python
# Program 1.3.2
def add(x, y):
    return x + y

print(add(2, 2))
```

Parameters are very similar to **variables**. You're probably already familiar with variables from algebra. Variables remember a value for later reuse. For example, the below program adds numbers, remembers those results, and then adds those results.

```python
# Program 1.3.3
def add(x, y):
    return x + y

first_number = add(2, 2)
another_number = add(5, 10)
print(add(first_number, another_number))
```

## Interacting with Wordpress via code

So far we've written some small, simple programs. Writing something like a multiplayer game at this rate would take a really long time! Fortunately, when somebody solves a generic problem and is feeling generous they will round up all of their code and let others download it via what are called **packages**.

Let's use one of those packages.  The "requests" package will allow us to communicate with websites, like the blog you're running on your Pi.

> For full documentation of the "requests" package, see: https://requests.readthedocs.io/en/master/

```python
# Program 2.1.1
# Load the package named "requests"
import requests

# Named things like packages and variables can have functions and other variables within them that
# we can reuse. To refer to them use the package name and a . character like so:
response = requests.get("http://$username.example.com/wp-json/wp/v2/posts", params={"per_page": 1})

# We've just requested the latest blog post from our blog server. We've stored the response to
# that request in a variable named "response" above.

# Requests and responses are like letters we can send or get in the mail. They have an envelope,
# mailing and return addresses, and contents inside.
# To get to the content inside our response–the blog post–, we use the "json()" function to
# structure that content in a usable way.
posts = response.json()

# We've stored the content in a variable called "posts" so we can refer to it more easily.
# "posts" is a **list**. Lists are ordered sequences of values.
# How do we know it's a list? We'll come back to this.

# Check if the list is empty by using the "len" (for "length") function, which returns how many
# elements are in a list. This makes sure we don't try to examine a post if there isn't one to
# examine!
if len(posts) == 0:
    print("No blog posts found. You should post something on your blog first!")
else:
    # We can refer to the elements of a list by the index of that element using the [0] syntax,
    # where 0 is the first element in the list. Computers usually start counting from 0.
    post = posts[0]

    # We've stored the first post from our response in a variable named "post". This variable is
    # a dictionary. This means it can have any number of values in it. We can refer to the values
    # using a name, similar to looking up definitions in a dictionary by the word.

    # Wordpress posts have a complicated structure with lots of values within them, and even nested
    # values within those. Below we'll navigate that structure to pull out the date of our post and
    # it's title using the ["word"] syntax – this refers to a value by it's name inside the
    # quotations. In turn, that value can be anything, maybe even another dictionary.
    # How do we know which value is what? Similar to how we knew "posts" was a list. We'll come back
    # to this shortly.
    date_posted = post["date"]
    title = post["title"]["rendered"]

    # Print out the date and title. The "format" function here replaces symbols inside text with
    # values from the variables we just defined above.
    print("{0}: {1}".format(date_posted, title))
```

Copy the above program into your IDE and run it. If you've written any posts in your blog, you should see the latest post and it's title. In a few lines of code (ignoring comments), we've constructed a request from our program, sent it to the blog server, and parsed its response. Cool!

Try debugging your program to watch and inspect the instructions and variables.

Now lets look at the list and dictionary the code used during execution in the debugger.  A list looks like this:

![211-posts-list.png](/docs/211-posts-list.png)

Lists in python are always encompassed inside of square brackets.  The `0` is the first element in the **list**.  Its value is a **dictionary** of **key** **value** pairs.  If we would have asked for `per_page>1` there would have been a `1` second element whose value would have been a dictionary as well --and so on--.

Dictionaries in python are encompassed inside of curly braces.  The dictionary from above comes from the JSON representation of the blog post.  Lets look at it:

![211-post.png](/docs/211-post.png)

You use the "word" syntax like `post["title"]["rendered"]` to get the values from this dictionary and the display the results.

### The World Wide Web and APIs

In the above example, we not only pulled code from another package, we also used code from an entirely separate program: your blog server. We asked the "requests" package to make a request to your blog for us, and we asked the blog server for the latest blog post title. We didn't have to write any of the code to store, manage, or retrieve that information. And similarly, those packages then use other packages, too, and so on. That blog post script you have written above easily spans millions of lines of code if you think about all of the layers of packages that get used, all the way down to your operating system and your computers device drivers.

We can do this because of something called **application programming interfaces**, or **APIs** for short. APIs define a kind of simple language, specific to a certain area–like math, or blogs, or weather, or tweets–that can hide a limitless amount of code underneath it. When we use packages or other servers, all we need are their APIs. Then, the rest of the implementation is hidden to us, and can change and improve without us knowing. We don't need to know or learn all of that code. APIs make us incredibly productive and allow us to create amazing things relatively quickly.

![iot.jpg](/docs/iot.jpg)

Different APIs come in different flavors. When talking to a website server, like the Wordpress blog from our python script, we interact using the HTTP protocol. A protocol is just an agreed way for different parties to communicate or accomplish some task together. Think of snail mail: when you send a letter, we have a protocol that says we use envelopes, we write our addresses a certain way,we put it in a mailbox, and letters get sent back to us in a similar way. The HTTP protocol is what serves websites over the internet.

![HTTP_Steps.png](/docs/HTTP_Steps.png)

> For full documentation of the Wordpress API, see: https://developer.wordpress.org/rest-api/

The Wordpress API can do just about anything we want with our blog. Let's explore!

```python
# Program 2.2.1
import requests
import bs4

# In this program, we're going to make requests to the Wordpress API multiple times. We can start to
# see some patterns in how we make calls to the API. Also, we want our program to easily read in
# instructions we understand. Instead of saying "make a request to this URL with these
# parameters and parse it as JSON" multiple times, which is too detailed to repeat so often, we'd
# like to say more clearly what we're trying to do: "list the latest blog posts". Just like if you
# ask for a ride to school, you don't say "please let me sit in your car, put the car into gear,
# press the gas until the end of the driveway, then turn left, then stop at the stop sign, ..." and
# so on. That is painstakingly detailed, and it would be really hard for the person you're asking to
# understand what you were really asking for. Instead we simply say "may I have a ride to school?"
# Once we do something once, we can refer to it more quickly. The same is true with programs.
# Programs need to be clearly understood by humans, too, not just computers.

# To accomplish this, we're going to create a **class** to help organize our code. A class is a
# collection of functions and variables that we can reuse.

# Start defining a class similar to how you define a function, but instead of the "def" keyword,
# use the "class" keyword, followed by the class's name. Just like with a function, defining the
# class alone doesn't use it. It creates a template that we can reuse later.
class Blog:
    # Now we can define functions inside the class.
    # Classes start with a special "__init__" function which is used to create a new instance of the
    # class based on zero or more parameters. Here we have a "url" variable that remembers the URL
    # of your blog for reuse in other functions.
    def __init__(self, url):
        self.url = url

    # In our last program, we made a request to the Wordpress API to list the latest post. Here
    # we're defining a function inside the class, similar to the functions inside a package, that
    # will list the latest posts, so we can reuse it and more easily understand our code.
    def list_latest_posts(self, at_most):
        response = requests.get(self.url + "/posts", params={"per_page": at_most})
        return response.json()

    # We're going to add a function for another request: get the latest comments on a post. We can
    # use the same class to then list posts and list comments on those posts.
    def list_latest_comments_on_post(self, post_id, at_most):
        # Notice the URL are parameters of the request are different for comments.
        response = requests.get(self.url + "/comments", params={"post": post_id, "per_page": at_most})
        return response.json()

# We'll use this later to display comment text.
def html_to_text(html):
    return bs4.BeautifulSoup((latest_comment['content']['rendered']), 'html.parser').get_text()

# This is the API of your blog.
blog_api_url="http://dminnich.example.com/wp-json/wp/v2"

# Now, we can use our class, and our tasks are easier to write and understand.
# First, create an instance of our blog by calling our class like we would call a function.
# This in turn calls our special initialization function we defined above. That function required
# a url parameter, so we pass that as well. The "self" parameter of class functions is special:
# we don't need to provide it ourselves when we call class functions.
blog = Blog(blog_api_url)

# Now that we have an instance of our blog, we can call "list_latest_posts" on it. This does what
# it says: lists that latest posts. We can also pass a named parameter to the function, "at_most".
# This means we are listing "at most 1" post. We could pass other values here, like 50,
# to get up to 50 posts. Since we only want the latest post, we'll just set at_most to 1.

latest_posts = blog.list_latest_posts(at_most=1)

if len(latest_posts) > 0:
    latest_post = latest_posts[0]

    # Now that we have that the latest post, let's get some of its comments. To do this, we use
    # our class functions again, this time "list_latest_comments_on_post" by providing a post ID
    # and again some max number of comments we want to get back.
    latest_comments = blog.list_latest_comments_on_post(post_id=latest_post['id'], at_most=1)
    latest_comment = latest_comments[0]
    author = latest_comment['author_name']
    date = latest_comment['date']
    comment_text = html_to_text(latest_comment['content']['rendered'])
    words = len(comment_text.split())
    print("{0} commented on your post at {1} and wrote {2} words! :-)".format(author, date, words))
else:
    print("No blog posts found. You should post something on your blog first!")
```
Notice what happens when there are no comments on the blog. You will see that the latest_comments array is empty.
![empty-array-no-comments](/docs/empty-array-no-comments.png)

Now if you try to retrieve the 0th element of latest_comments, it throws an error
![error-message-because-no-comments](/docs/error-message-because-no-comments.png)

Can you modify the program to not throw this error?

Here's a hint:

```python
    if len(latest_comments) > 0:
            latest_comment = latest_comments[0]
            author = latest_comment['author_name']
            date = latest_comment['date']
            comment_text = html_to_text(latest_comment['content']['rendered'])
            words = len(comment_text.split())
            print("{0} commented on your post at {1} and wrote {2} words! :-)".format(author, date, words))
    else:
        print("No comments found! ")
```

Try commenting on your latest post and rerun your program. Each time the program runs it'll reflect the latest comment.

Can you modify the program to summarize the most recent 5 comments instead of just the most recent comment?

Here's a hint:

```python
    latest_comments = blog.list_latest_comments_on_post(post_id=latest_post['id'], at_most=5)

    # Rather than manually going through all of the comments, we can use a for loop to loop
    # through whatever comments there are for us:
    for comment in latest_comments:
        author = comment['author_name']
        date = comment['date']
        comment_text = html_to_text(latest_comment['content']['rendered'])
        words = len(comment_text.split())
        print("{0} commented on your post at {1} and wrote {2} words! :-)".format(author, date, words))
```

### Using your friends' blogs

We can use our newfound API interaction abilities to talk not just to our own blog server, but also our friends' blog servers!

To interact with our friends' blogs, we'll need to get their blogs' IP addresses. Earlier we edited our hosts file so we could access our own blog with a nice url like "$username.example.com". We're going to do the same thing here except using your **friends'** IP addresses so we can also access **their** blogs. 

Ask your friends to get the IP of their interfaces by typing `ip a` in their terminal, just like before:

    root@raspberrypi:~/2019-chicktech/files/bin# ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 52:54:00:08:25:14 brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.18/24 brd 192.168.122.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::6858:c1fc:4305:6ce8/64 scope link
       valid_lft forever preferred_lft forever

They are looking for the non `lo` interface that has something on the `inet` line.  Above their IP is `192.168.122.18`. Now you will add their IP address to your hosts file along with a DNS name.  For the username use first letter of their first name and their whole last name. For example

    /opt/bin/add_hosts_line.sh 192.168.122.18 dminnich

Now we can access their blogs by their usernames just like our own.

Let's use those hosts in the program below to look at the comments from all of our friends blogs and see who has the most. For fun you can try commenting on each other's blogs to see the results change.

```python
# Program 2.3.1
import requests


class Blog:
    def __init__(self, url):
        self.url = url

    def list_latest_posts(self, at_most):
        response = requests.get(self.url + "/posts", params={"per_page": at_most})
        return response.json()

    def list_comments_on_post(self, post_id, at_most):
        response = requests.get(self.url + "/comments", params={"post": post_id, "per_page": at_most})
        return response.json()

    # We added another function to our Blog class: get the total comments for a blog.
    def total_comments(self):
        # Here, we make a request for "comments", but instead of looking at the content, we'll look
        # at a header in the response.
        response = requests.get(self.url + "/comments", params={"per_page": 1})

        # Headers can add extra information. The Wordpress API includes a header named 'X-WP-Total'
        # that tells us the total amount there is of a certain resource, in this case comments.
        # We return that here, after converting the header's value to an integer type.
        return int(response.headers['X-WP-Total'])

# Add all of the blog URLs here for the blogs in your group in what's called a **dictionary**.
# This allows us to refer to the blogs later by a readable name like "Jenn's Blog".
blog_urls = {
    "username1's blog": "http://$username1.example.com/wp-json/wp/v2",
    "username2's blog": "http://$username2.example.com/wp-json/wp/v2"
}

# We need to figure out which blog(s) have the most comments.  We will store the results of
# our investigation in a list. As we process each blog we will either replace the list with a new
# winnig blog or append to the list if a tie is found.
top_blogs = []

# Store how many comments this blog has in a variable
top_blog_total_comments = 0

# Again we'll use a for loop to get the total comments for each blog in the blog_urls dictionary.
for blog_name, blog_url in blog_urls.items():
    blog = Blog(blog_url)
    total_comments = blog.total_comments()

    if total_comments == 0:
        print("{0} doesn't have any comments yet. Go comment on their blog!".format(blog_name))
    else:
        print("{0} has {1} comments!".format(blog_name, total_comments))

    if total_comments == top_blog_total_comments:
        # Tie for top blog!.  Add the tied blog to the list.
        top_blogs.append(blog_name)
        # We don't need to adjust the top_blog_total_comments because this blog has the same number,
        # so it doesn't change.

        # The 'continue' keyword makes us skip to the next iteration of the for loop without running
        # any other code below.
        continue

    if total_comments > top_blog_total_comments:
        # We found a new top blog!
        # Replace the top_blogs list with just this blog since it has the most comments.
        top_blogs = [blog_name]
        # Replace the top_blog_total_comments with how many comments this blog has.
        top_blog_total_comments = total_comments

# Now print out the winner. But first we have to check if there is a tie, so we print out all of the
# winners.
if len(top_blogs) > 1:
    # Since we've got a tie, separate each blog title the list of top blogs with an "and" when
    # printing it out.
    print("There is a tie for the top blog! {0} all have {1} comments.".format(
          " and ".join(top_blogs), top_blog_total_comments))
else:
    # No tie. Just print out the single winner.
    print("{0} is the top blog with {1} comments".format(top_blogs[0], top_blog_total_comments))
```

Take some time to play with this a bit:

- Try commenting on each other's blogs by browsing to the URLs we added to your hosts file and commenting on them. Then, rerun your program so you can watch each others counts go up.
- What happens if you don't put any blog urls in the `blog_urls` dictionary and then run the program?
- Try counting comments on just the latest post. How would our blog request change? Can you add a new method to the class to help?
- Try counting blog posts instead of comments. How would our blog request change? Can you add a new method to the class to help?

## Quick recap
Yesterday we covered:

- Different jobs/roles in IT
- What a Raspberry Pi is
- How to install a LAMP web server stack
- How to install the WordPress blog platform
- What an IDE, API, and a package are
- How to debug your software
- How to use functions, variables, classes, dictionaries, lists, loops and conditional statements in python
- How to use the python requests module to interact with our wordpress blog and do things like print blog titles and comment counts


## Working with hardware

### History and premise

The proliferation of technology, Moore's law and the globalization of the labor force over the last few decades has changed things in interesting ways. Devices used to be expensive and mechanical.  Now they are cheap and electronic.

Below is a contrived example that will help drive home the point I'm trying to make.

A water heater from 20 years ago:

- Had one water setting: on/off
- A bouy would float on top of water in the tank. Once it rose past a certain trip point a switch would flip and the water heater wouldn't collect anymore water.
- Cost $1000 in today's money
- A mechanic/hacker/enthusiast could replace the bouy or physically lower or higher the trip point as fixes/improvements. These would all be cost effective actions that the general public could understand.

A water heater 15 years ago:

- Had two simple settings
- Was controlled by simple electronic componets (resistors, capacitors, timers, etc)
- Cost $700 in today's money
- A mechanic/hacker/enthusiast could replace an electronic component by desoldering it and soldering in a new one.  They could determine which componenets were bad by using a basic multi-meter.


A water heater today:

- Can use a calendar schedule
- Can use environmental presets
- Can react based on gallons dispersed to encourage flat rate bills
- Can email you if there is a problem
- Cost $300
- A mechanic/hacker/enthusiast just sees a bunch of chips when the open up the water heater.  They don't know how it works.  Calling a repair person isn't worth the money because replacing the whole device will likely be cheaper.


As devices have gotten "SMART"er more and more electronic components have been needed.  In the past a TV brand would partner with a microcontroller or processor manufacturer and something custom would be fabricated for their use case. This took a long time and cost a considerable amount of money.  And while that still happens, now days extremely common electronic components are mass produced and sold on the open market for cheap.  Component vendors now compete to document their components and make them as generic and easy to get and use as possible.

This commoditization of electronic components has opened up a new door for hackers.  They can now build their own simplistic SMART devices using off the shelf parts and open source IDEs.  Today we will be hooking up a $8 LCD screen to our Raspberry Pi's and using open source libraries to play with it.


### A word on protocols

Your phone knows how to work with your Bluetooth airpods and your laptop knows how to work with your USB mouse because Bluetooth and USB are standardized protocols.  I2C, SPI and UART are also standardized protocols.

UART or Universal Asynchronous Receiver/Transmitter is a simple protocol for transferring data back and forth between two devices at the same time.  It uses two wires plus possible ground and power lines.  RX/TX are crossed on each side. Meaning RX on sideA goes to TX on sideB. Clocking is set in software via start/stop bits and baud rates.  In microcontroller applications UART is often used by humans for debugging purposes as they have the microcontroller print break points in the code its running to a serial console.

SPI or Serial Peripheral Interface is simple serial protocol that uses four wires plus possible ground and power lines to connect several devices that are a short distance apart together and need rapid data transfer.  Generally one device is considered the master and the rest are considered slaves.  The clock is set with the clock wire and a slave is chosen using the SS wire.  All devices are hooked up in parallel but require their own SS wire from the master.  MOSI(master out slave in) and MISO(master in slave out) allow data to travel both directions between two devices at the same time. An SPI bus can generally support as many devices as SS pins the microcontroller has.

I2C (pronounced I squared C) is an advanced serial protocol that uses two wires plus possible ground and power lines to connect several devices that are a short distance apart and don't require rapid data transfer.  Generally one device is considered the master and the rest are considered slaves.  The master calls out to a slave via a specific hard coded 7bit device address.  Communications happen one direction at a time and there can be up to 127 slaves hooked up in parallel on one I2C bus.  Each device is interconnected via a serial data (SDA) and serial clock(SCL) wires.

The Raspberry Pi can interact with devices that speak these protocols by using special sets of externally exposed pins.

The Raspberry Pi 3 B+ has 40 GPIO (general purpose input/output pins). The pinout looks like

![pinout](/docs/pi-pinout-diagram-01.png)

And the pins are counted like this

![pincount](/docs/RPi-Pinout.jpg)

Additionally, the Pi can interact with devices in generic ways using any of its exposed pins. When working in generic mode, signals can either be `digtal` or `analog` and  the data can flow either `in` or `out`.

Digital is either on or off.  Think of a light switch.
Analog is more like what the ocean looks like or what a song looks like in some editing software if you've ever seen that.  Very fluid.

For example, you could build a clap switch.  You could get a sound sensor and use it as a digital input to the Raspberry Pi.  When it hears a noise it sends a HIGH/ON signal to the Pi and at that point the Pi has a program written to send a TOGGLE to a digital output to an LED.  Noise made, light on.  Noise made, light off.

With analaog in and out you could use a photoresistor (light sensor) as an input to detect the ambient light in your room and then alter the brightness of an LED via a PWM/analog output on the Pi in proportion to ambient light.

If this kind of stuff interests you, you may want to explore `embedded` engineering.  The type of problems these engineers solve and the devices they work with are often quite different from your standard software engineer.

### Using the screen

Enough talk, lets hook up that LCD screen

- Shutdown your Pi and remove its case
- Wire the screen like this...

With the USB ports facing towards you and HDMI port on the left, look at the left column of GPIO pins. You will only use this column.  You will start at the top of the column and count down its pins increasing by an odd number each time.  The top left pin is `1`, the pin below it is, `3`, and so on. Notice that pin `7` is not in use.

The pins on the screen are labelled.

| Screen Pin | Pi Pin |
|--------|--------|
| VCC    | Pin 1 / 3.3V       |
| GND    | Pin 9 / GND |
| SCL    | Pin 5 / SCL |
| SDA    | Pin 3 / SDA |

![hookup1](/docs/hookup1.jpg)

![hookup2](/docs/hookup2.jpg)


- Boot the Pi back up

Now lets print `"Hello World"` on that screen

```python
# Program 3.1.1
#!/usr/bin/env python3
# The screen uses the I2C protocol.  Import a package that makes talking that protocol easy.
from luma.core.interface.serial import i2c
# Import a package that allows for easy drawing on screens
from luma.core.render import canvas
# Our screen has a ssd1306 chip in it
from luma.oled.device import ssd1306

# I2C communicates with devices on defined addresses.  The address the ssd1306 uses is 0x3C. Connect to it.
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)
with canvas(device) as draw:
    # Draw on the screen
    draw.text((10, 40), "Hello World", fill="white")

# Keep this program running so the text stays on the screen
while True:
    pass
```

Raise your hand if this didn't work for you and a volunteer will come around and help you out.

Now lets do something really cool! Lets have the screen print a different emoji based on how many comments your blog has.

TODO: Walk through set up of these packages / necessary drivers

```python
# Program 3.1.2
#!/usr/bin/env python3
import time
import random
import requests
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont, ImageDraw


class Blog:
    def __init__(self, url):
        self.url = url

    def list_latest_posts(self, at_most):
        response = requests.get(self.url + "/posts", params={"per_page": at_most})
        return response.json()

    def list_comments_on_post(self, post_id, at_most):
        response = requests.get(self.url + "/comments", params={"post": post_id, "per_page": at_most})
        return response.json()

    def total_comments(self):
        response = requests.get(self.url + "/comments", params={"per_page": 1})
        return int(response.headers['X-WP-Total'])


# In this program we add a Screen class. Using a device like a screen is complex, and so this class
# models our OLED screen so we can do more advanced interactions in a readable way.
class Screen:
    def __init__(self):
        # Initialize the screen like we did before.
        serial = i2c(port=1, address=0x3c)
        self.device = ssd1306(serial, rotate=0)
        # This time we'll also use a real font so we can write emojis on the screen
        self.font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')

    # This function does what it says!
    def draw_text_at_random_location(self, text, size=10):
        length = len(text)
        font = self.font.font_variant(size=size)
        with canvas(self.device) as draw:
            x = random.randint(0,100 + (length * size / 2)) - (length * size / 2)
            y = random.randint(0,60) - size / 2
            draw.text((x, y), text, font=font, fill="white")

# Define some functions here to organize some simple logic around the number of comments. We'll
# reuse these functions below.
# The first function returns a different emoji depending on how many comments a blog has.
def emoji_for_comment_total(total):
    if total < 5:
        return ":-)"

    if total < 10:
        return ":-)"

    return "B-)"

# This function returns a font size to use depending on how many comments a blog has.
def font_size_for_comment_total(total):
    return (total + 3) * 4

blog = Blog("http://$username.example.com/wp-json/wp/v2")
screen = Screen()

# Keep checking the blog and updating the screen every second until we stop the program.
while True:
    total_comments = blog.total_comments()
    size = font_size_for_comment_total(total_comments)
    emoji = emoji_for_comment_total(total_comments)
    text = "{0} {1} {2}".format(emoji, total_comments, emoji)
    screen.draw_text_at_random_location(text, size=size)
    time.sleep(1)
```

## Presentation preperation
The ability to articulate and defend your ideas is an important skill to have no matter what field you go into.  A piece of general life advice: learn how to patiently communicate and be assertive.  Truth be told, people don't like making decisions or doing research on their own.  The more you bring to them, the more organized you are in your approach, the more passoinate you are -- the more likely they are to support your position/give you a raise/etc.

When giving a presentation:

- Let your personality, body language and passion speak
- Don't use a script
- Focus on one narrow-ish topic the whole time
- Avoid "um", "hmm" and similar filler words when possible
- Practice.  Make sure you cover all the high level topics while finishing in your allocated time
- Keep your slides full of figures, pictures and memes and not walls of text
- Make eye contact
- Focus in on a specific person and look for feedback in their body language
- Be ready for ANY question.  Its ok to say "I don't know"
- Describe shortcomings. Nothing is perfect and it makes you look authentic.
- Do a practice run amongst peers and ask for feedback
- Try not to stress it.  A lot of people will completely tune you out.  Others will have no idea what you are talking about.  People that want to challenge you may opt to do so one-on-one after the talk.

We've pre-created a slide deck for use during our upcoming presentations. It is [here](https://docs.google.com/presentation/d/1r0o8KSgATN6PC5dZ99OmBf6LwJnJ0wWyZS2qvsABIOM/edit#slide=id.p)

We need 3 volunteers.  These girls will:

- Edit the slide deck to their liking
- Practice amongst themselves and one of the volunteers
- Do a practice run in front of the class and receive feedback from the class
- Present to the parents
- Present to the whole kickoff audience

Please raise your hand if you are interested.


## Exploring on your own

Please use any remaining free time to be creative with anything you've learned so far.  Also feel free to ask us any questions you may have.

Need some ideas?  Here are some code samples you can play with.

- Posting a comment via code

```python
# Program 4.1.1
import requests

# As before, we are going to interact with our blogs using the APIs that our blog
# software makes available as part of just running.
class Blog:
    """
    Simple Wordpress blog client.
    """

    def __init__(self, url):
        self.url = url

    def list_latest_posts(self, at_most):
        response = requests.get(self.url + "/posts", params={"per_page": at_most})
        return response.json()

    def list_comments_on_post(self, post_id, at_most):
        response = requests.get(self.url + "/comments", params={"post": post_id, "per_page": at_most})
        return response.json()

    def total_comments(self):
        response = requests.get(self.url + "/comments", params={"per_page": 1})
        return int(response.headers['X-WP-Total'])

    def comment_on_post(self, post_id, comment_to_post):
        url = (self.url + '/comments')

        data = {
            'post':post_id,
            'author_name':'Your name',
            'author_email':'YourEmail@gmail.com',
            'content':comment_to_post
        }
        print("Making a POST request to URL: {}".format(url))
        response = requests.post(url, data)
        return response.content # note, we just assume it succeeded. is this a good idea?


blog = Blog('http://blog.example.com/wp-json/wp/v2')

print('Enter your comment')
comment_to_post = input()

print('Posting your comment')
posts = blog.list_latest_posts(at_most=1)

if len(posts) > 0:
    latest_post = posts[0]
    posted = blog.comment_on_post(post_id=latest_post['id'],comment_to_post=comment_to_post)
    print(posted)

# Some food for thought:
# - how do you detect if the comment failed to be posted?
# - what should you print if there are no posts to comment on?
```

- The Friend Bot

```python
# Program 4.1.2
# We have a few more dependencies this time, one for dates and times, and one for just time.
from datetime import datetime
import time
import requests

class Blog:

    def __init__(self, url):
        self.base_url = url

    def list_latest_posts(self, at_most):
        response = requests.get(self.base_url + "/posts", params={"per_page": at_most})
        return response.json()

    def list_comments_on_post(self, post_id, at_most):
        response = requests.get(self.base_url + "/comments", params={"post": post_id, "per_page": at_most})
        return response.json()

    def total_comments(self):
        response = requests.get(self.base_url + "/comments", params={"per_page": 1})
        return int(response.headers['X-WP-Total'])

    def comment_on_post(self, post_id, comment_to_post):
        url = (self.base_url + '/comments')
        data = {
            'post': post_id,
            'author_name': 'Your name',
            'author_email': 'nobody@example.com',
            'content': comment_to_post
        }
        print("Making a POST request to URL: {}".format(url))
        response = requests.post(url, data)
        return response.content


blog = Blog("http://dminnich.example.com/wp-json/wp/v2")
# We are assuming the value the current time as the date we last commented on a post
# This helps us to use a time value as a starting point to compare our date calculations with
# We will use utc time because UTC is a global time and helps stay consistent across timezones and daylight savings time
last_commented_date = datetime.utcnow()

while True: # run forever until we kill the program
    posts = blog.list_latest_posts(at_most=1)
    if len(posts) > 0:
        latest_post = posts[0]
        latest_post_date = latest_post['date']
        post_date = datetime.fromisoformat(latest_post_date)
        if post_date > last_commented_date:
            last_commented_date = post_date
            print("a new post just came up on ", blog.base_url, "at ", last_commented_date)
            blog.comment_on_post(latest_post['id'],"Hello there, do you want to be my friend!")
    time.sleep(3) # wait 3s before doing anything else.
```


### Pulling weather data from the internet

```python
# Program 4.1.3
#!/usr/bin/env python3
import requests
import json
#raleigh
LAT = "35.7877"
LONG = "-78.6442"
#https://www.weather.gov/documentation/services-web-api#/
#https://rapidapi.com/theapiguy/api/national-weather-service/details
url = "https://api.weather.gov/points/{0},{1}/forecast".format(LAT,LONG)
response = requests.get(url)
j = json.loads(response.text)
tf = (j["properties"]["periods"][0]["temperature"])
print('It is currently {0} °F'.format(tf))
```

## Conclusion
Over the past two days we've covered:

- What various types of people in IT do
- What a Raspberry Pi is
- Installing a LAMP web server stack
- Installing the WordPress blog platform
- What an IDE, API, and a package are
- How to do step through debugging
- Using functions, variables, classes, dictionaries, lists, loops and conditional statements in python
- Using the python requests module to interact with our wordpress blog and do things like print blog titles and comment counts
- Hardware protocols and what an embedded engineer does
- Hooking up a screen to a Raspberry Pi
- Extending our python requests code to print blog titles or interactive comment counts to the screen
- Some tips and tricks for giving a good presentation

Towards the end of the class we also spent some time preparing for our presentation and allowing you to explore the concepts you've learned on your own.

This concludes our lab.  We've had a blast teaching and getting to know all of you.  You get to take the Raspberry Pi and LCD screen home to play with them more.

Have a great rest of the year and we hope to see you at interviews or as interns in a few years!
