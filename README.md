# Final Project - Physical Computing and the Internet of Things

*Name:* Patricia Torvalds PMT

*Date:* December 2017

## Project:  < Name of your Project / Device Goes here >

My project satirizes the use of the word "China" in order to derail conversations about American policy or internet freedom by taking live tweets which use the word "China" and using natural language processing to rank their favorability on a 180 degree scale, ranking the tweets as "good" or "bad."

### Detailed Project Description

In my time as a computer science major at Duke, discussions of a free internet or other intellectual property rights are derailed by invocations of "China" or Chinese politics. I chose to critically examine and satirize this trend, which plays on Orientalist ideas of a regressive Chinese state and prevents meaningful discussion.
The Raspberry Pi Zero runs a Python script which gathers all public Tweets (not retweets) containing the word "China" and then runs sentiment analysis on them using the TextBlob library to determine the overall sentiment of a tweet from -1.00 to 1.00. All tweets and scores, as well as their timestamps, are saved to a local database using sqlite3 in order to find averages and view data over time.

< Explain the "what" of your project:   What is it?   What does it do?   Explain the "why" of your project:  What problem is it responding to?  What issue is it engaging?   

### Technical Description

The project is made of a Raspberry Pi in a small case and a micro servo with a single-sided pointer in order to convert the data into its physical form. In order to maintain the core idea of the project, which was to simplify the complexity of China as a nation by distilling all meaning into a number based on a Tweet, I decided to also keep the hardware components simple. I soldered headers onto the Raspberry Pi in order to connect the servo, and then used a pointer specifically angled to translate the tweet score into 180 degree motion.

I was originally going to use the graphical interface of NodeRed for the software component of the project. However, with Prof. Kenney's help I set up a Python script and a sqlite3 database in order to store past tweets while collecting, scoring, and sending them to the RasPi in real time. By SSHing in to the Raspberry Pi I was able to upload my script and run it.


< Explain the "how" of your project.  What are the hardware components?  What are the software components?  How do they interact with each other? >

< You can also explain the development process here >


#### Hardware Wiring Diagram
![Wiring Diagram](images/zero-pins.jpg)
![Wiring Diagram](images/Screenshot from 2017-12-13 21-56-52.png)
< Insert Picture and explanation of Your Wiring Diagram here >

#### Code

< Explain your code.  You might include code snippets, either `inline` or
```c++
//Multiline
bool photon_fun = TRUE;
```
You should link to your full code, either included in the repository (e.g. [my_code.ino](code/my_code.ino)  or to the Shared Revision in your Particle IDE. >


### Design / Form

To create a visual representation of an overly simplified idea, I thought it would be fitting to create a simple "spinner" which the pointer would move on to display "bad," "neutral," or "good." 

< Explain the device's form, the aesthetic choices made and how they relate to the concept/function the device is intended to engage >

< include photos of your device >

### Evaluation / Reflection

< What is your own evaluation of your project?   What did you learn through this project?  What would you do differently in the future? >
