# Project Report

## Introduction

### What is the program about?

We developed one classic game, namely, "Pong". Our program is about creating our very own version of an already existing game. We therefore had an idea in mind when agreeing on the project and our task was to think about adaptions to make our program unique. Now, one can play our game which is a new "original".

### Where is it used?

There exist many different platforms ([agame.com](https://www.agame.com/search?term=pong) for example) in the internet on which users can play so called minigames online. Developers have the opportunity to publish their own games and offer it to a broad mass here. Also, due to its cult status, Pong has motivated people to create own websites just all around the game. These could be suitable enviroments for our programs as well. However, our program should only be used for private joy, so we won't share it with third parties.

### Why is it important?

In the history of games, Pong plays a prominent role as one of the revolutionaries, or more precisely, as one of the evolutionaries. With regard to the importance of our program in particular, the main aspect is about our very own learning progress. This project was useful to learn some very basics about data science and explore the world of programing. More about our learning progress can be found in the section "What was accomplished / learned?" below.

### Overview of the rest of the report

In the following, we will provide a brief insight into what makes our code "stand out" and how we approached to project. Next to this, we share insights about what worked well and what did not work well. We conclude with our key learnings for the next project and the references of this project.

## Background

### Problems and shortcomings of their work

As mentioned, there exist various versions of Pong. We do not claim to have seen each and every version existing. However, what united these we found and tried is, they offered the very basic and original version of Pong. This means that in order to extend the game beyond a basic version, we had to come up with our own ideas for adaptions. Also, we could find guidance for the code, but we did write it ourselves using our own structure and implementing our own extensions.

### How your work is different and/or better

Our program has its own specifications. First, we used sound modules. One can find versions with and without sound modules. Our sound modules in this context are unique. Furthermore, we created "Disco Pong" as written in our initial project specification. This means that any time the ball hits one of the paddles, all three - ball and both of the paddles - change their color randomly.

## Project

### Your approach to the problem

First, we based our program on the lecture. It gave good guidance about how to reasonably approach such a project. Therefore, we made use of what we learned so far and structured our code by using four different modules. This helped us in keeping a clear overview of our project and furthermore, from an interpreter's perspective, the program is easier to read and understand by a third person. We furthermore used abstract classes and functions, so that our program was not overwhelmed with repeatedly used chunks of code. Thus, we decomposed our program properly. This sums up to an approach of object oriented programming, which we tried to apply.

### Design

Among all the openly accessible projects, we figured the following two gave us good ideas about what we would like to achieve. First, there is a general [tutorial](https://realpython.com/pygame-a-primer/) for Pygame, which *is a set of Python modules designed for writing video games.* . Next, we looked at the following, already existing [project](https://gist.github.com/vinothpandian/4337527) for some idea.

### What did work?

The way we approached our program turned out to be working well. It took us some time to do so properly, but in the end, we have written a program which we do understand and could reproduce. Also, based on our code, we could make further adaptions to the program without the need to revise at some point in the code.
Finally, we have a program which offers a game flow with a clear logic.

### What didn't work?

With regard to the game's interface, we would have liked to implement a proper game menu with interactive buttons. We could argue that this was just a matter of time. However, it was a task of this course to plan a project and in the given frame, we could not accomplish this goal. In general, we are thankful for the lecturer's advice to write the project's specification in a way that it gets clear that we implement our adaptions based on our project's progress. This gave us the opportunity to write a solid working program that we understand and therefore waive adaptions instead of rush through the code and eventually make use of code that we do not understand.
In terms of code, we would have liked to work with gloabal variables. This would insofar have improved our code, as we would not have had to write as many input per function as we now had to do.

## Conclusion

### What was accomplished / learned?

The project was very useful to apply the new gained knowledge of the course. With the tutorials, we already had the chance to apply the theoretical knowledge. What was different about the application in an own project was the fact that we had less guidance which forced us to think from the scratch and also figure out the right problems to solve. Also, we applied the theoretical knowledge of each lesson combined, so this was a holistic approach here. Projects of this kind are an ideal way of consolidating what has been learned.
We made a lot of trial and error, which as well helped us to understand the solution, when something finally worked.

### Is there something you would do differently next time?

Before the start of the project, we thought that we first need to have the basic game and from there on write all further adaptions. Now, after the project is finished, we come the conclusion that next time, we would have started with a framework first and then write the code for the game. This means, we would have created the menu before the actual game.
Furthermore, we could have used even more classes, since these give the code a clear structure. This could have looked similar to [this](https://www.youtube.com/watch?v=a5JWrd7Y_14&ab_channel=CDcodes)

### Future work

## References

### Cites of work

#### Sound effects and music

- [Sound when ball touches paddle](https://github.com/attreyabhatt/Space-Invaders-Pygame/blob/master/laser.wav)

- [Cheering when player wins](https://www.youtube.com/watch?v=yLNALmt6KFs&ab_channel=Music%26SoundsEffectLibrary)

- [Disappointed crowd when player loses](https://www.youtube.com/watch?v=bR_wr5HRdl4&ab_channel=IISOUNDEFFECT)

- [Sound when goal is scored](https://www.youtube.com/watch?v=-at1woVuDtY&ab_channel=mamu)

- [Sound when ball hits upper or lower edge](https://www.youtube.com/watch?v=jKVtoh05N-s&ab_channel=BerlinAtmospheres)

- [Background music](https://www.youtube.com/watch?v=p6p_UYwnUTw&t=75s&ab_channel=MusicforVideoLibrary)

*Note:*
The links above lead to the raw data files. Some sound effects had to be extracted and altered to fit our needs. The software which was used for this cause was [Audiotonic](https://www.microsoft.com/de-de/p/audiotonic-audio-editor-recorder-based-on-audacity/9n66vbrr4dpl?activetab=pivot:overviewtab)

#### Images

- [Background image](https://wallpapersafari.com/w/h5YuPd)

### Other

- [First inspiration for how to code pong](https://gist.github.com/vinothpandian/4337527)

- [Pygame documentation](https://www.pygame.org/docs/)
