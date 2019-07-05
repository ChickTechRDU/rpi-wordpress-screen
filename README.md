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
- Making sure systems are always reachable by planning and implementing high avalibility and disaster recovery strategies
- Automating day to day tasks and writing basic scripts and applications
- Rolling out new versions of custom code to systems
- Working closely with developers to ensure that they make good security and performance decisions
- Offering consultation and mentoring services
- Staying abreast of industry trends
- Presenting and conferences and doing outreach


My name is Michael White and I'm a Lead Application Integration Engineer.  As a Lead Application Integration Engineer I'm responsible for:

- Making sure people don't do dumb shit or recreate the sins of their fathers.
- TODO


My name is Alec Henninger and I'm a Senior Software Applications Engineer.  As a Sofware Engineer I'm responsible for:

- Choosing techonolgy paths that will directly make or break a 34 billion dollar company on a daily basis.
- TODO


My name is Claudia Van Valkenhoef and I'm a Manager.  As a Manager I'm responsible for:

- Herding cats and attempting to add stability to a chaotic world.
- TODO

We all work at a company named Red Hat.  Red Hat is an open source software company.  This means the software we develop is free for anybody to use and improve.  We believe that when people work together, instead of in competition with against one another, great things happen.

Red Hats core product is a version of Linux.  Linux is an Operating System similar to macOS or Windows but is primarily used by servers and not laptops and home pcs. Most of the websites you visit are powered by Linux, Android phones are powered by Linux, nearly all super computers are powered by Linux -- our presense is everywhere, even if you haven't heard of us before today.  Red Hat also offers OpenShift which is an orchestration and management layer on top of Docker like containers and OpenStack which is an alternative to Amazon AWS could as well as tons of other things.

Red Hat is a GREAT company to work for.  It is full of passonate and diverse people with all kinds of skillsets.  Everybody is always willing to pitch in and help in anyway they can despite any formal job duties like those listed above.  The work environment is casual (no fancy clothes, heiarchy means nothing) and fun. There are meetup style groups and events happening on a regular basis.

## Objective
Have you ever been to a concert or a sporting event where they put tweets on the jumbotron(big screen)?

What about watched the news or a TV show where they are displaying a facebook post and are discussing it?

Over the next two days we will be building something similar!

With a Raspberry Pi, Wordpress, some python code and an LCD screen you will be able to post to your blog and see it on your screen.


## Building the stack

#### What is a Raspberry Pi?
The Raspberry Pi Foundation is a dream a come true for people interested in technology. For very little money, they will sell you a 'disposable' baby computer that runs standard hardware and is extendable by all kinds of open source software.

Each part of that last sentence is important.

With a standalone Pi costing $35 and a kit costing $80, not only are they accessible to people who couldn't afford computers in the past -- they encourage more well off people to do bold things.  You may be scared to take apart your new iPhone or afraid to load Linux or other custom software on the laptop you use for homework.  The Pi is built to be tinkered with.  It is easy to start over from a software standpoint and if your Pi is in a bad state it impacts only your hobby.  If you do something that kills the hardware, you will have to spend another $35, which sucks, but is way easier to swallow than killing your phone or laptop.

The Raspberry Pi 3 B+ that we are using in this class has the following specs:

- Quad Core A53 1.4GHz ARM Processor
- 1GB DDR2 RAM
- Ethernet, Wifi, Bluetooth
- Mirco SD card slot
- 40 Pin GPIO header

To put in perspective how low power that is, while it isn't an apples to apples comparison, even the Samsung Galaxy S3 released in 2012 had higher specs.  Outside of needing to keep costs low, uniformity is actually more important than horsepower in the hobby market.  The fact that you can build something once and know it will behave the exact same on all devices of that type is huge.  It also allows you to focus on your work and only learn how to troubleshoot one platform.  In contrast, imagine having to write a game that supports running on AMD and Intel process, Windows 7 and Windows 10, AMD and Nvidia grahpics cards, maybe even Xbox and PS4 as well as PC, etc.  Yes APIs, frameworks and libraries abstract away some/most of the pain, but nothing is as nices as having a fleet of all the exact same hardware to build on top of.

Open Source software is about having the freedom to reuse and improve the applications that run on your devices.  Has Apple or Google ever pushed a software update that changed something on your phone in a way you didn't like?  Ever thought this instagram app would be better if it could also do X?  With open source software people write code to meet their needs and then put it out on the internet for anybody to use for free.  This means you can pick it up and use it as-is or if it doesn't quite meet your needs you can alter it and then even put it back out on the internet for other folks to use for free.  This culture has helped the Pi hobby scene flourish.  If you can think of something you'd like your Pi to do, chances are somebody somewhere has already done something similar and you can use their work as a launching off point to accomplish your goal.


#### What is LAMP?
Linux Operating System + Apache Web Server + Maria Datbase Server + the PHP programming language make up the `LAMP` web services stack.  Together they allow a computer to serve up dynamic and interactive webpages.  According to [netcraft](https://news.netcraft.com/archives/2019/06/17/june-2019-web-server-survey.html) 30% of the internet is ran off of Apache and according to [zdnet](https://www.zdnet.com/article/can-the-internet-exist-without-linux/) 96% of the internet is ran on top of Linux.  Those statistics coupled with the widespread useage of things like Wordpress blogs, Drupal CMS systems, Vanilla Foums, ownCloud collaboration servers and MediaWiki systems indicate that the LAMP stack has widespread adoption on the internet.  It is also worth noting that it is one of the oldest stacks.  What these things mean to you is that as you begin to learn this stack, there will be plenty of open source code for you to sample from and plenty of places to look for and ask for help when you need it.


##### Linux
Your Pi is already running an optimized version of Linux called Raspbian.  Raspbian is based on one of the largest distributions of Linux called [Debian](https://www.debian.org/).  If you haven't heard of either of those and have happened to heard of Ubuntu, know that Ubuntu is also based on Debian to some degree.  Backing up a bit, in case all of that was greek to you -- an Operating System is the low level software that runs on your device that determines how you intearct with it via various interfaces (touch screen, mouse, keyboard) and an operating system allows you to install other software on top of it.  Windows is an Operating System, so is iOS on your phone.  The Linux operating system is open source and flexible.  Groups of people package it in different ways (called distributions) to meet different needs.  These different distributions allow linux to power android phones, smart TVs, your Pi, and most of the servers on the internet despite the fact that they are all very different devices filling different needs.

The linux operating system is very tweakable, secure and privacy oriented...
So if I know I'm not going to ever use a webcam I can remove the hardware support for it from the kernel to save on resources.  I can also install a different Desktop Manager (think complex theme) and run stuff on older systems easier.

When you login to a linux system you are a user who can't make changes to the system.  This is what plagued Windows back in the day. Viruses would install and take over the system without every needing to escalate privileges.

Since there is no central linux group and since a lot of people develop it as a hobby there isn't anybody trying to collect data about you to then market things to you, which is great if you care about your privacy.

It also generally features a package manager and treats everything like a file...
When you want to install a piece of software in linux you can run a command or click a couple things and then you have it and it will be easy to keep up to date.  Contrast this to MacOS or Windows where you have to go each vendors website and download and install each piece of software like that.

The fact that linux treats everything as a file allows linux users to easily string together commands for automation and scripting purposes.


##### Apache
Apache is a flexible, well established, powerful and popular web server.  When you open up Chrome and type in `reddit.com`, Chrome is the client and the web server is what Reddit's linux servers use to send you back your memes and cat videos.

Apache on its own can only serve up static content.  You can think of static content as non-interactive sites.  So if you wanted to serve up a copy of your resume and a brief page about yourself, that you write in HTML yourself, Apache alone would be enough.  If you instead wanted a site with an admin front-end that made making changes easy and allowed people to comment on articles and things like that, then you would need a dynamic language and an apache module or proxy to a server that spoke that language.  You would also likely need a datastore.  That is where Maria DB and PHP will come in later.  For the time being, lets install Apache and serve up some static content.


	TODO


##### Maria DB

Maria DB is highly popular, stable, scalable and free SQL compliant database server.  If you are unfamilar with databases, you can think of them as a complex set of linked spreadsheets.  They allow you to get answers to questions like "who in my class has a name that starts with an M and was born after 1990 and has brown hair". Oh, and sort that by the youngest person first.  As websites and applications become more complex they need to be able to answer questions like that (all posts by author sorted by newest) quickly so a database is used to store the information.  The database not only can answer these questions faster than logic in code could if the web server had to crawl through a bunch of files, it also allows creates a useful centralization point.  If all of your sites real content is in a database, you only need to backup the database.  Also, you can add more and more web servers as demand grows and they can all talk to the same database whereas each of them all having the same files at the same time is a much harder problem to sovle.

Lets install Maria DB and create a datbase and a table with some sample data

	TODO


##### PHP

PHP is a well established programming language that runs on many operating systems.  It is most commonly used by web developers where it acts as an interpeted language that complies and executes on the server when called.  One of the core features of PHP is that you can easily mix PHP, Javascript and HTML in the same file.  This makes developing simple web applications easy to do as you don't have to learn or be restricted by frameworks or MVC practices.  Some of these same features are also its cons, by the way :).

Lets make a basic PHP page

	TODO


#### What is Wordpress?

Wordpress is a personal and easy to use blogging plaform that runs on top of a LAMP stack.  It features an extensive plugin and template system and is backed by a large open source community.  [w3techs](https://w3techs.com/technologies/details/cm-wordpress/all/all) estimates that 34% of the internet runs on top of wordpress!

Now that you've seen what its like to create your own HTML and PHP pages, lets install Wordpress and let it do the hard stuff for us.

	TODO

Now that Wordpress is installed.  Watch as I demo a few things:

- Logging in
- Creating a blog post
- Viewing the blog post
- Navigating to the plugin and theme screens


#### Bonuses

All of the stuff we've done above are part of a system administrators job.  We built a stack and installed an application. A developer will now pick up from here and start writing custom code or changing things to meet their needs.  While they focus on that stuff the system administrators need to think about things like disaster recovery and uptime.  In the time before the next session feel free to explore simulations of those two objectives using the guidance below.

**#1 Backups**
Using [rsync](https://linux.die.net/man/1/rsync) and [bash](https://ryanstutorials.net/bash-scripting-tutorial/) write a script that copies new and changed files `/opt/rsync_source` and `/opt/rsync_destination`.  The script `/opt/bin/new_rsync_file` and `ls -lhart` can be used to see if you got it working right.

A solution can be found in `/opt/bin/rsync_solution`.

NOTE: In the real world you'd use some dedicated backup software instead of rsync.  You'd also make sure the destination wasn't on the same machine and you'd schedule regular backups.

**#2 Monitoring**
Using [pgrep](https://linux.die.net/man/1/pgrep) and [bash](https://ryanstutorials.net/bash-scripting-tutorial/) write a script that prints "ALERT" if the process `atestprocess` isn't running.  The script `/opt/bin/atestprocess start|stop` and `ps aux` can be used to see if you got it right.

A solution can be found in `/opt/bin/monitoring_solution`.

NOTE: In the real world a monitoring tool would have mechanisms to do this for you and would bubble up the alert to something that would email/text somebody instead of printing ALERT to the console.


## Writing the code
TODO

- Customize wordpress
- themes and plugins
- Review IDE and python basics (45 minutes)
- https://thonny.org/
- Hello World program run and debug
- Statements
- Debugging (step through multiple statements)
- Variables
- Functions
- Classes
- Coding/Debugging (1.5-2 hours) - python + requests to pull data from wordpress
- API: What is an API? Why use APIs? (5 minutes)
- Examples: SmartTV apps, "liking" on a page links to Facebook
- Packages: What are packages? Download requests (5 minutes)
- Program script to talk to wordpress API and display latest post title to console (15 minutes)
- Step through
- Add timestamp to output
- Add blog post, rerun
- Repeat for more additions:
- Iterate through all posts by date
- Sort by oldest first
- Methods for organizing code (put below into own methods for reuse tomorrow)
- Summarize number of comments for whole blog
- Summarize number of comments per post
- Summarize number of comments per person
- Query all blogs in classroom for most posts
- Query all blogs in classroom for most comments
- Bonus material


## Quick recap
Yesterday we covered:

- What various types of people in IT do
- What a Raspberry Pi is
- Basic security, network and database skills
- Installing a LAMP web server stack
- Installing and customizing the WordPress blog platform
- What an IDE, API, a package and JSON are
- Using python and the requests module to get data from web pages
- Running loops and processing data structures
- How to do step through debugging

## Adding the hardware

The prolilferation of technology, Moore's law and the golablization of the labor force over the last few decades has changed things in interesting ways. Things used to be expensive and mechnical.  Now they are cheap and electronic.

Below is a contrived example that will help drive home the point I'm trying to make.

A water heater from 20 years ago:

- Had one water setting: on/off
- A bouy would float on top of water in the tank. Once it rose past a certain trip point a switch would flip and the water heater wouldn't collect anymore water.
- Cost $1000 in todays money
- A mechanic/hacker/enthusiast could replace the bouy or physically lower or higher the trip point as fixes/improvements. These would all be cost effective actions that the general public could understand.

A water heater 15 years ago:

- Had two simple settings
- Was controlled by simple electronic componets (resistors, capacitors, timers, etc)
- Cost $700 in todays money
- A mechanic/hacker/enthusiast could replace an electronic component by desoldering it and soldering in a new one.  They could determine which componenets were bad by using a basic multi-meter.


A water heater today:

- Can use a calendar schedule
- Can use enviromental presets
- Can react based on gallons dispersed to encourage flat rate bills
- Can email you if there is a problem
- Cost $300
- A mechanic/hacker/enthusiast just sees a bunch of chips when the open up the water heater.  They don't know how it works.  Calling a repair person isn't worth the money because replacing the whole device will likely be cheaper.


As devices have gotten "SMART"er more and more electronic components have been needed.  In the past a TV factory would partner with a microcontroller or processor manufacturer and something custom would be fabricated for their use case. This took a long time and cost a considerable amount of money.  And while that still happens, now days exteremly common electronic componets are mass produced and sold on the open market for cheap.  Component vendors now compete to document their components and make them as generic and easy to get and use as possible.

This commoditization of electronic compontes has opened up a new door for hackers.  They can now build their own simplistic SMART devices using off the shelf parts and open source IDEs.  Today we will be hooking up a $8 LCD screen to our Raspberry Pi's and using open source libraries to play with it.

The Raspberry Pi 3 B+ has 40 GPIO (general purpose input/output pins). The pinout looks like
![pinout](https://gitlab.corp.redhat.com/dminnich/2019-chicktech/raw/master/pi-pinout-diagram-01.png)

And the pins are counted like this


![pincount](https://gitlab.corp.redhat.com/dminnich/2019-chicktech/raw/master/RPi-Pinout.jpg)

Your phone knows how to work with your Bluetooth earpods and your laptop knows how to work with your USB mouse because of standardized protocols.  I2C, SPI and UART are also standardized protocols.

UART or Universal Asynchronous Reciver/Transmitter is a simple protocol for transferring data back and forth between two devices at the same time.  It uses two wires plus possible ground and power lines.  RX/TX are crossed on each side. Meaning RX on sideA goes to TX on sideB. Clocking is set in software via start/stop bits and baud rates.  In microcontroller applications UART is often used by humans for debugging purposes as they have the microcontroller print break points in the code its running to a serial console.

SPI or Serial Peripheral Interface is simple serial protocol that uses four wires plus possible ground and power lines to connect several devices that are a short distance apart together and need rapid data transfer.  Generally one device is condered the master and the rest are considered slaves.  The clock is set with the clock wire and a slave is chosen using the SS wire.  All devices are hooked up in parrallel but require their own SS wire from the master.  MOSI(master out slave in) and MISO(master in slave out) allow data to travel both directions between two devices at the same time. An SPI bus can generally support as many devices as SS pins the microcontroller has.

I2C (pronounced I squared C) is an advanced serial protocol that uses two wires plus possible ground and power lines to connect several devices that are a short distance apart and don't require rapid data transfer.  Generally one device is considered the master and the rest are considered slaves.  The master calls out to a slave via a specific hard coded 7bit device address.  Communications happen one direction at a time and there can be up to 127 slaves hooked up in parrallel on one I2C bus.  Each device is interconnected via a serial data (SDA) and serial clock(SCL) wires.

In addition to supporting the protocols above, the Raspberry Pi also offers GPIO pins.  When working with those signals can either be `digtal` or `analog` and  the data can flow either `in` or `out`.

Digital is either on or off.  Think of a light switch.
Analog is more like what the ocean looks like or what a song looks like in some editing software if you've ever seen that.  Very fluid.

For example, you could build a clap switch.  You could get a sound sensor. It is an digital input to the Raspberry Pi.  When it hears a noise it sends a HIGH signal to the Pi and at that point the Pi has a program written to send a HIGH to a digital output to an LED.  Noise made, light on.  Noise made, light off.

With analaog in and out you use a photoresistor(light sensor) as an input to detect the ambient light in your room and then alter the brightness of an LED via a PWM/analog output on the Pi in proportion to ambient light.


If this kind of stuff interests you, you may want to explore `embedded` engineering.  The type of problems these types of engineers solve and the devices they work with are often quite different from your standard softwared engineer.

Enough talk, lets hook up that LCD screen

- Shutdown your Pi
- Wire the screen like [this](TODO)
- Boot the Pi back up

Now lets print `hello world` on that screen
TODO

- install package
- write script
- execute script

Raise your hand if this didn't work for you and a volunteer will come around and help you out.


Now lets edit the code we wrote yesterday so the title of your blog entry appears on the screen
TODO

Adding some sparkle:
TODO

- Polling so keeps updating when new post
- Random positioning of title
- Scroll title to fit
- Use font that's more readable, supports emojis (UTF-8)

References:

- [pinout](https://docs.particle.io/datasheets/discontinued/raspberrypi-datasheet/)
- [other pinout](https://randomnerdtutorials.com/getting-started-with-raspberry-pi/)
- [UART](https://www.allaboutcircuits.com/technical-articles/back-to-basics-the-universal-asynchronous-receiver-transmitter-uart/)
- [I2C](https://robot-electronics.co.uk/i2c-tutorial)
- [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi/all)
- [I2C/SPI](https://www.byteparadigm.com/applications/introduction-to-i2c-and-spi-protocols/)
- [I2C/SPI](https://aticleworld.com/difference-between-i2c-and-spi/)




## Doing more
TODO

- Stalking bot
- Update screen with notification when someone comments on your posts
- Update blog title based on number of comments
- Weather API
- Post comments on X random blogs
- Game on the LCD screen


## Presentation preperation
The ability to articulate and defend your ideas is an important skill to have no matter what field you go into.  A piece of general life advice: learn how to patiently communicate and be assertive.  Truth be told, people don't like making decisions or doing research on their own.  The more you bring to them, the more organized you are in your approach, the more passoinate you are -- the more likely they are to support your position/give you a raise/etc.

When giving a presentation:

- Let your personality, body language and passion speak
- Don't use a script
- Focus on one narrowish topic the whole time
- Avoid "um", "hmm" and similar filler words when possible
- Practice.  Make sure you cover all the high level while finishing in your allocated time
- Keep your slides full of figures, pictures and memes and not walls of text
- Make eye contact
- Focus in on a specific person and look for feedback in their body language
- Be ready for ANY question.  Its ok to say "I don't know"
- Describe shortcomings. Nothing is perfect and it makes you look authentic.
- Do a practice run amongst peers and ask for feedback
- Try not to stress it.  A lot of people will completly tune you out.  Others will have no idea what you are talking about.  People that want to challenge you may opt to do so one-on-one after the talk.

We've pre-created a slide deck for use during our upcoming presentations.

We need TODO volunteers.  These girls will:

- Edit the slide deck to their liking
- Practice amongst themselves and one of the volunteers
- Do a practice run in front of the class and recieve feedback from the class
- Present to the parents
- Present to the whole kickoff audience

Please raise your hand if you are interested.

## Conclusion
Over the past two days we've covered:

- What various types of people in IT do
- What a Raspberry Pi is
- Basic security, network and database skills
- Installing a LAMP web server stack
- Installing and customizing the WordPress blog platform
- What an IDE, API, a package and JSON are
- Using python and the requests module to get data from web pages
- Running loops and processing data structures
- How to do step through debugging
- Hardware protocols and the re-birth of the hobbyist
- Hooking up a screen to a Raspberry Pi and printing text on it
- How the technical stuff we covered can be altered to meet other use cases (weather).
- Some presentation skills

This concludes our lab.  We've had a blast teaching and getting to know all of you.  You get to take the Raspberry Pi and LCD screen home to play with them more.

If you have any questions about anything at all, feel free to ask now.  All the volunteers will be around until the end of todays events so feel free to talk to us individually as well.

Have a great rest of the year and we hope to see you at interviews or as interns in a few years!






