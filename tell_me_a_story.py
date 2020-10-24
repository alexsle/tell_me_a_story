import os
import os.path
import random
import pyttsx3

# ----------- Randomizing three characters from 'chars' file ----------- #

if not os.path.exists("chars"):                 #Checking if the text file exists
    sys.exit("Error: No 'chars' file found!")
chars_data = open("chars", "r")
lines_number = len(open("chars").readlines(  )) #Counting the number of lines in the file
if lines_number == 0:                           #Checking if char file is empty
    sys.exit("Error: file 'chars' is empty!")
random_line = random.randrange(0, lines_number) #Picking three random, different characters
random_line2 = random.randrange(0, lines_number)
random_line3 = random.randrange(0, lines_number)
all_lines = chars_data.readlines()
char1 = all_lines[random_line - 1]
char2 = all_lines[random_line2 - 1]
char3 = all_lines[random_line3 - 1]
while char1 == char2 or char1 == char3 or char2 == char3:
    c1 = all_lines[random_line - 1]
    c2 = all_lines[random_line2 - 1]
    c3 = all_lines[random_line3 - 1]
chars_data.close()

# ----------- Randomizing two things from 'things' file ----------- #
if not os.path.exists("things"):
    sys.exit("Error: No 'things' file found!")
things_data = open("things", "r")
lines_number = len(open("things").readlines(  ))
if lines_number == 0:
    sys.exit("Error: file 'things' is empty!")
random_line = random.randrange(0, lines_number)
random_line2 = random.randrange(0, lines_number)
all_lines = things_data.readlines()
thing1 = all_lines[random_line - 1]
thing2 = all_lines[random_line2 - 1]
while thing1 == thing2:
    thing2 = all_lines[random_line2 - 1]
things_data.close()

# ----------- Randomizing two places using 'places' file ----------- #
if not os.path.exists("places"):
    sys.exit("Error: No 'places' file found!")
places_data = open("places", "r")
lines_number = len(open("places").readlines(  ))
if lines_number == 0:
    sys.exit("Error: file 'places' is empty!")
random_line = random.randrange(0, lines_number)
random_line2 = random.randrange(0, lines_number)
all_lines = places_data.readlines()
place1 = all_lines[random_line - 1]
place2 = all_lines[random_line2 - 1]
while place1 == place2:
    place2 = all_lines[random_line2 - 1]
places_data.close()

# ----------- Randomizing an adjective for characters ----------- #
if not os.path.exists("adj_char"):
    sys.exit("Error: No 'adj_char' file found!")
adj_char_data = open("adj_char", "r")
lines_number = len(open("adj_char").readlines(  ))
if lines_number == 0:
    sys.exit("Error: file 'adj_char' is empty!")
random_line = random.randrange(0, lines_number)
random_line2 = random.randrange(0, lines_number)
all_lines = adj_char_data.readlines()
adj_char = all_lines[random_line - 1]
adj_char_data.close()

# ----------- Randomizing an adjective for things ----------- #
if not os.path.exists("adj_thing"):
    sys.exit("Error: No 'adj_thing' file found!")
adj_thing_data = open("adj_thing", "r")
lines_number = len(open("adj_thing").readlines(  ))
if lines_number == 0:
    sys.exit("Error: file 'adj_thing' is empty!")
random_line = random.randrange(0, lines_number)
random_line2 = random.randrange(0, lines_number)
all_lines = adj_thing_data.readlines()
adj_thing = all_lines[random_line - 1]
adj_thing_data.close()

# ----------- Randomizing the Begining of the story ----------- #
list = os.listdir('beginning')
number_of_files = len(list) #Counting files in /begin directory
random_file = random.randrange(1, number_of_files)
begin_file = 'beginning/' + random_file.__str__()
beginning = open(begin_file, "r") #Picking a random file and reading text from it

# ----------- Randomizing the Middle of the story ----------- #
list = os.listdir('middle')
number_of_files = len(list)
random_file = random.randrange(1, number_of_files)
middle_file = 'middle/' + random_file.__str__()
middle = open(middle_file, "r")

# ----------- Randomizing the Ending ----------- #
list = os.listdir('ending')
number_of_files = len(list)
random_file = random.randrange(1, number_of_files)
ending_file = 'ending/' + random_file.__str__()
ending = open(ending_file, "r")

# ----------- Combining the whole story together ----------- #
the_story = beginning.read() + middle.read() + ending.read()
beginning.close()
middle.close()
ending.close()

# ----------- Inserting generated data into the story ----------- #
for r in (("c1", char1), ("c2", char2), ("c3", char3), ("t1", thing1), ("t2", thing2), ("p1", place1), ("p2", place2), ("ac1", adj_char), ("at1", adj_thing)):
    the_story = the_story.replace(*r)
the_story = the_story.replace('\n', '')

# ----------- Initializing Text-to-speech engine and reading the story ----------- #
engine = pyttsx3.init()
engine.setProperty("rate", 120) #Speech speed, words per minute
engine.say(the_story)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #Choosing a voice
print('Stay awhile and listen...', end = '')
engine.runAndWait()