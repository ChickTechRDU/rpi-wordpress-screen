#Welcome to the ChickTech kickoff!

##Icebreaker
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

##Objective
Have you ever been to a concert or a sporting event where they put tweets on the jumbotron(big screen)?

What about watched the news or a TV show where they are displaying a facebook post and are discussing it?

Over the next two days we will be building something similar!

With a Raspberry Pi, Wordpress, some python code and an LCD screen you will be able to post to your blog and see it on your screen.


##Building the stack
TODO

SysAdmin work
What is a Pi? (10 minutes)
Baby computer
1GB SRAM,  Quad core 64-bit processor clocked at 1.4GHz (ARM is different), Ethernet, Wifi, SD card
Your phones are similar infra and likely more powerful
Cheap, ubiquitous, open and standard 
$35 or kit full kit for  $80ish.  Freedom to explore without worry. 
Share and jointly improve upon common ideas.  
Exposed hardware points and standard protocols allows unprecedented level of access to do physical things with the device 
Microcontroller vs general purpose computer
Realtime 
You can’t live patch your microwave (yet)
Install updates
Install Linux, Apache, MySQL PHP.   (2 minutes)
LAMP.  Huge community 
Unzip a file (5 mins)
Use a script to setup a database
What is a database?
Looking inside the database
SORT LIKE query
Enabling services so they start at boot (15 minutes)
Basic network tests
Ping
Curl
Netstat
Netcat
Hostnames
dig
Security  
Users / groups
Sudo
Iptables
Create a static webpage (5 minutes)
Static content like pics and resumes.   HTML markup. Light weight. 
Dynamic like reddit.   Users interact.  Languages instead of markup and 
PHP (5 minutes)
Heavier than static
Phpinfo
Install wordpress (20 minutes)
about 40% of the web is wordpress
A personal blog. A CMS
Widely customizable way to easily build a webpage. 
Show how to create and edit an entry 
Show some basic how to change appearance stuff
Show plugin system 

Sysadmin bonuses
Cron an rsync job that copies a file from one dir to another
Simulating backups.  
Edit the original file and watch the destination file change
Write a script that looks at the last line of a file for ERROR
Simulating monitoring
When found restart a service and notes that it did so in another file



##Writing the code
TODO
Customize wordpress
themes and plugins


Review IDE and python basics (45 minutes)
https://thonny.org/
Hello World program run and debug
Statements
Debugging (step through multiple statements)
Variables
Functions
Classes
Coding/Debugging (1.5-2 hours) - python + requests to pull data from wordpress
API: What is an API? Why use APIs? (5 minutes)
Examples: SmartTV apps, "liking" on a page links to Facebook
Packages: What are packages? Download requests (5 minutes)
Program script to talk to wordpress API and display latest post title to console (15 minutes)
Step through
Add timestamp to output
Add blog post, rerun
Repeat for more additions:
Iterate through all posts by date
Sort by oldest first
Methods for organizing code (put below into own methods for reuse tomorrow)
Summarize number of comments for whole blog
Summarize number of comments per post
Summarize number of comments per person
Query all blogs in classroom for most posts
Query all blogs in classroom for most comments


Bonus material


##Quick recap
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

##Adding the hardware

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
install package
write script
execute script

Raise your hand if this didn't work for you and a volunteer will come around and help you out.


Now lets edit the code we wrote yesterday so the title of your blog entry appears on the screen
TODO

Adding some sparkle:
TODO
Polling so keeps updating when new post
Random positioning of title
Scroll title to fit
Use font that's more readable, supports emojis (UTF-8)

References:

- [pinout](https://docs.particle.io/datasheets/discontinued/raspberrypi-datasheet/)
- [other pinout](https://randomnerdtutorials.com/getting-started-with-raspberry-pi/)
- [UART](https://www.allaboutcircuits.com/technical-articles/back-to-basics-the-universal-asynchronous-receiver-transmitter-uart/)
- [I2C](https://robot-electronics.co.uk/i2c-tutorial)
- [SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi/all)
- [I2C/SPI](https://www.byteparadigm.com/applications/introduction-to-i2c-and-spi-protocols/)
- [I2C/SPI](https://aticleworld.com/difference-between-i2c-and-spi/)




##Doing more
TODO
Stalking bot
Update screen with notification when someone comments on your posts
Update blog title based on number of comments
Weather API
Post comments on X random blogs
Game on the LCD screen


##Presentation preperation
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

##Conclusion
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






