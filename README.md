# encrypter-app
encrypter app (project for a level)

# planning

before i started working on the gui for this project, i sketched out a draft using a photo editor
(you can find this draft at ./plan.png) 
this shows the intended layout of the application. 
making a decent looking gui is almost impossible unless you have a plan because it allows you to reason
on where to place each of the elements and what techniques you can use to place those elements.


# bug #1

the first major bug i ran into while working on this project is the background not displaying for my tkinter window
this issue took a while to find a solution to as just from looking at my code and testing it, everything seemed correct

I found out from a github issue  
https://github.com/ythy/blog/issues/302 
that this was an issue with the tkinter library itself or the python interpreter. the solution to this issue was to create another reference
to the image file as the original image was being deleted by the python garbage collector 
before it could be rendered to the screen. (I really didnt think that memory management would be an issue in a python project XD)