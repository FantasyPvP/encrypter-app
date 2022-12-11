# encrypter-app
encrypter app (project for a level computer science)

# how to use

to use this project, simply open a terminal and run the command

git clone https://github.com/FantasyPvP/encrypter-app.git

this will download all of the files for this project, you should then cd into the new directory

to use this project you will need the following dependencies:
tkinter
matplotlib
sv_ttk

tkinter will already be installed as it is a part of python's standard set of packages.
matplotlib will also likely be installed however if it is not, simply run the command

> pip install matplotlib

to install the package.
sv_ttk will not be installed by default so you can just install it using 

> pip install sv_ttk 

finally, you can run the project simply by running 

> python ./main.py

# planning

before i started working on the gui for this project, i sketched out a draft using a photo editor
(you can find this draft at ./plan.png) 
this shows the intended layout of the application. 
making a decent looking gui is almost impossible unless you have a plan because it allows you to reason
on where to place each of the elements and what techniques you can use to place those elements.

# making the gui

for this project instead of using the default tkinter widgets, i used a submodule called ttk
tkinter.ttk is a set of themed widgets that can be customised in terms of look by applying external themes. the theme
that i used for this project was sv_ttk which can be applied simply by importing the library and
calling the set_theme() function.


# bug #1

the first major bug i ran into while working on this project is the background not displaying for my tkinter window
this issue took a while to find a solution to as just from looking at my code and testing it, everything seemed correct

I found out from a github issue  
https://github.com/ythy/blog/issues/302 
that this was an issue with the tkinter library itself or the python interpreter. the solution to this issue was to create another reference
to the image file as the original image was being deleted by the python garbage collector 
before it could be rendered to the screen. (I really didnt think that memory management would be an issue in a python project XD)

EDIT: i eventually decided not to use the image at all, instead i used the themed tkinter module as it looked a lot
better than regular tkinter but did not really fit the image

# bug #2

while working with the matplotlib module to display graphs, i had to remove characters from the graph that had a zero value. to do this i tried to use a for char in dict statement to remove unused values. this resulted in an error as the dictionary had changed size during the iteration. 
the solution to this issue was to use a generator to create a new list of keys from the dictionary and iterate through that instead as the list of keys would not change size as i modified the dictionary itself. 

# bug #3

while working on the code for the second encryption algorithm, i ran into an issue where the message did not decrypt correctly. this issue was caused by trailing whitespace.
the solution to this problem was to use the .rstrip() method to remove any whitespace characters at the end of the string so that the 
scrambling function would find the correct length of the string and therefore unscramble it correctly.

# bug #4

when implementing the encryption algorithms, i ran into a bug where the program would always just use one
encryption algorithm regardless of which one was selected. the cause of this error was a catch all else statement

```{python}

encrypt = input()   # creates encryption variable
                    # lets say the input here is 1
                    # encrypt is now a string variable

if encrypt == 1:
    encrypt1()
elif encrypt == 2:
    encrypt2()
else:
    encrypt3()      # the if statement is unable to find any matches 
                    # between the integer and the string
                    # so it always defaults to this final branch
                    # the solution was to convert the value to an integer 
                    # after it is fetched from the gui
```