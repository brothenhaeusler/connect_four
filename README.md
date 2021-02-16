Welcome!
# Exercise A: 
Code execution [here](src/four_wins.py) - and here's my [documentation](doc/documentation.pdf)

# Exercise B: 

### 1 UML
3 UML diagrams to look at. The diagrams are mostly artificially pumped up :). My core project consists of a command line game.

* A [Use case diagram](doc/uml/use_case_diagram_of_the_gaming_website.pdf) that visualizes different use cases for the users, the admin and the proprietor.
* A [Sequence diagram](doc/uml/Sequence%20Diagram.pdf) to visualize how different entities of a website *would* interact in case of a certain procedure of activities.
* An [Activity diagram](doc/uml/Activity%20Diagram.pdf) that shows an imaginary string of actions and possibilities, when accessing the website. 

### 2 DDD
I modelled the different domains within a [problem space](doc/ddd/ddd_problemspace.pdf) and later on carved out the [bounded contexts and the relationships between them](doc/ddd/bounded_contexts_diagram.pdf). Beware the pixie dust of artificialness :).

### 3 Metrics
I used Radon for delivering the Metrics as required. This in particular includes the Cyclomatic complexity and the Halstead metrics. The results can be accessed in my latest [GitHub Workflow](https://github.com/brothenhaeusler/connect_four/actions).

### 4 Clean Code Development
[The cheatsheet](doc/clean_code/cheatsheet%20clean_code.docx)  (Sorry for the format, but that's what I unfortunately have open while programming) and [4](doc/clean_code/code_examples) examples, where I applied different clean code principles.
* before: sth about adding 1, modulo, etc.. -- now: embarrassingly [simple](doc/clean_code/code_examples/KISS_in_practice.png)
* [no magic numbers](doc/clean_code/code_examples/no%20magic%20numbers.png)
* before: I called the variable 'player' --- now: more [precise naming](doc/clean_code/code_examples/precise%20naming.png)
* [avoidance of negative conditionals and good commenting](doc/clean_code/code_examples/avoidance_of_negative_conditionals_and_good_commenting.png)

### 5 Build Management
I use [make](https://en.wikipedia.org/wiki/Make_(software)) for local build-management. I didn't do building before (sorry :) ) -- especially automated Unit Tests seem to be quite valuable in the context of later code changes.
[Here](Makefile) is my Makefile.

### 6 Unit Tests
[Here](src/four_wins_functional_test.py) they are. They get automatically run using my [Makefile](Makefile) or via [GitHub](https://github.com/brothenhaeusler/connect_four/blob/main/.github/workflows/python-app.yml) [Action](https://github.com/brothenhaeusler/connect_four/actions). They also include one visual test (commented out) for testing the create_board() function defined in [here](src/four_wins_functions_functional.py).  

### 7 Continuous Delivery
I used GitHub Action for that purpose. See [here](https://github.com/brothenhaeusler/connect_four/blob/main/.github/workflows/python-app.yml). As can be seen in my latest builds, I included in there: Metrics generation, Unit Testing as well as generating the user documentation for the program. Last time I checked, it was working [fine](https://github.com/brothenhaeusler/connect_four/actions).

### 8 IDE
I used VisualStudio Code for that effect due to recent (last 5 years) developments and investments through Microsoft. 
[Here](doc/ide/VisualStudioCode_shortcuts.docx) is my cheatsheet (for Mac). Unfortunately, it was written on - you probably guessed it - MS Word :). 

### 9 DSL
The DSL implemented by me is - as regards subject matter - quite remote from my game project. It relates to my [2nd favourite topic](doc/dsl/flowers.py) besides writing Clean Code ;):D. Lamentably the latter can't quite compete with reading [Martin Wolf opinion pieces](https://www.ft.com/martin-wolf). 

### 10 Functional Programming
"Here I stand, I can do no other...". Actually I can't proof but only propose my solution as consistent with the following functional programming principles:
* only final data structures
* side effect free functions
* the use of higher-order functions (filter)
* functions as parameters and return values (filter)
* use of an anonymous function (lambda)   

.. all happening in [here](src/four_wins_functions_functional.py). I have to declare that there's a certain tension between writing functional and writing clean code. Especially for amateurs, notably the 'final data structure' criterion most certainly shoots KISS. My prejudice is, that that is also the case for a significant part of the experienced programmers. For that matter I also included a mostly functional (fulfilling all criteria but the final data structuring), more [readable version of my central functions](src/four_wins_functions.py).
