# Python_Swercher

This program is similar to to search bar in windows 10 in the sense that when searching for something on the drive it will return a result 
of everything wit the same name or similar to it.

What is different is that you are not searching.

#################################################################################################################################
HOW TO USE

There are 4 main commands:
insert
delete 
quit
showall

When starting the program by default it will create an sqlite db in the same directory as the python program.

the terminal will as you "what would you like:" 
in this scenario type "insert" 
"NAME:" will show up, your input needs custom variable that needs to be unique. e.g. yt
"PATH:" will show up after hitting enter, the path can be a url, directory,  anything. 

EXAMPLES of PATHS you might choose. (these last 2 are only exclusive to my machine, don't use them to test it out)
# https://www.youtube.com ("this is the youtube website")
# E:\visual share\sqlite programs\pythonswercher ("this is the directory of the python program")
# E:\visual share\Music\orchestraic music\Avatar Soundtrack.mp3 ("this is a specific soundtrack")

lets say we paste ######## E:\visual share\Music\orchestraic music\Avatar Soundtrack.mp3 ######## into path 
a message will show ######## yt E:\visual share\Music\orchestraic music\Avatar Soundtrack.mp3 has been successfully added to the database ########
showing the unique name (yt) and the path assigned to it (being the soundtrack).

so now when you type "yt"  the soundtrack will start playing.

e.g. for delete:
"what would you like:"
delete
"NAME:" yt
"yt has been delete successfully for the database"


now if you just type yt the soundtrack won't play

showall will display all the names and paths stored on the database, in case you forget what name goes with what path.

EXAMPLE of showall:

what would you like:
showall
sublime C:\Program Files\Sublime Text 3
swercher C:\Users\Madara\Desktop\pythonswercher
sublimeapp C:\Program Files\Sublime Text 3\sublime_text.exe
youtube https://www.youtube.com
banggood https://www.banggood.com
music F:\visual share\Music
movies D:\movies

#################################################################################################################################







