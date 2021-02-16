# Exercise A: Connect four - the game

This game is played in the terminal by executing the four_wins.py file. 

It is developed to be played by 2 players who alternately should get access to the keyboard to make their respective inputs to the game. 

The first player gets chosen randomly by the computer, so it would be good to first agree on who's player 1 and 2 first.  

The game is modelled after the dimensions of the original connect four game - the feature to play the game within a field of different dimensions may come in following versions. 

### And now: have some fun :)

# Exercise B: 

### 1 UML
3 UML diagrams to look at. The diagrams are mostly artificially pumped up :). My core project consists of a command line game.

* A [Use case diagram](doc/uml/Use%20Case%20Diagram%20of%20the%20Gaming%20ebsite.pdf) that visualizes different use cases for both the users, the admin and the proprietor.
* A [Sequence diagram](doc/uml/Sequence%20Diagram.pdf) to visualize how different entities of a website 'would' interact in case of a certain procedure of activities.
* An [Activity diagram](doc/uml/Sequence%20Diagram.pdf) that shows an imaginary string of actions and possibilities, when accessing the website. 

### 2 DDD
I modelled the different domains within a Problem space 
# include link
and the bounded contexts and the relationships between them.
# include link

### 3 Metrics
I used Sonarqube for delivering the Metrics as required. The results can be accessed here.
# include link

### 4 Clean Code Development
[the cheatsheet](doc/clean_code/cheatsheet%20clean_code.docx)  (Sorry for the format, but that's what I unfortunately have open when programming)
# include link
and [4](doc/clean_code/code_examples) examples, where I applied different clean code principles.
* [KISS](doc/clean_code/code_examples/KISS%20in%20practice.png)
* [no magic numbers](doc/clean_code/code_examples/no%20magic%20numbers.png)
* [precise naming](doc/clean_code/code_examples/precise%20naming.png)
* [avoidance of negative conditionals and good commenting](doc/clean_code/code_examples/combination.png)

### 5 Build Management
I used a Makefile for local build-management. I didn't do building before (sorry :) ) -- especially automated Unit Tests seem to be quite valuable in the context of later code changes
# link the Makefile

### 6 Unit Tests
Here<> they are. They get automatically run using CICD 
# link to Unit tests

### 7 Continuous Delivery
I used GitHub Action for that purpose. 
# do I have to link sth?

### 8 IDE
I used VisualStudio Code for that effect due to recent (last 5 years) developments and investments through Microsoft. 
Here is my cheatsheet (for Mac)
# include link

### 9 DSL
The DSL implemented by me is used independent from my project. It can be accessed here.
# provide link

### 10 Functional Programming
only final data structures
(mostly) side effect free functions
the use of higher-order functions
functions as parameters and return values
use closures / anonymous functions
# 5 links