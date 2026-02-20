import  os #library to get terminal size
import numpy as np #numpy to modify the map
import keyboard as kb #get keyboard input without inturupting the game
import time as task #time to make the script pose later
from threading import Thread #threading
import random #you know random

class snake: #blue print of the snake 
    def __init__(self,termap): #getting the main data here
        self.length = 3
        self.map = np.array(termap)
        self.mapsize = self.map.shape
        self.y = self.mapsize[0]
        self.x = self.mapsize[1]
        self.movehistory = []
    def run(self,key,begin,points): #the main function
        if key == None or key == "d": #this block is the same for every button wasd
            if begin != None: #if its the 1st frame we put the snake in the middle
                self.map[self.y//2,self.x//5] = 2
            indice = np.where(self.map == 2) #1these two blocks to get the snakes head location
            self.location = np.array(list(zip(*indice)))#2
            try:
                self.locationY = self.location[0][0] #getting the x and y of the head location
                self.locationX = self.location[0][1]
                self.map.fill(0)  #every frame the terminal gets cleared to avoid bugs
                self.map[self.locationY,self.locationX] = 0 #updating the map after getting the snake location
                self.map[self.locationY,self.locationX+1] = 2 #updating the map after getting the snake location
            except IndexError as e:
                pass


        elif key == "w":
            if begin != None:
                self.map[y//2,x//5] = 2
            indice = np.where(self.map == 2)
            self.location = np.array(list(zip(*indice)))
            try:
                self.locationY = self.location[0][0]
                self.locationX = self.location[0][1]
                self.map.fill(0)  
                self.map[self.locationY,self.locationX] = 0
                self.map[self.locationY-1,self.locationX] = 2
            except IndexError as e:
                pass

        elif key == "a":
            if begin != None:
                self.map[y//2,x//5] = 2
            indice = np.where(self.map == 2)
            self.location = np.array(list(zip(*indice)))
            try:
                self.locationY = self.location[0][0]
                self.locationX = self.location[0][1]
                self.map.fill(0)  
                self.map[self.locationY,self.locationX] = 0
                self.map[self.locationY,self.locationX-1] = 2
            except IndexError as e:
                pass

        elif key =="s":
            if begin != None:
                self.map[y//2,x//5] = 2
            indice = np.where(self.map == 2)
            self.location = np.array(list(zip(*indice)))
            try:
                self.locationY = self.location[0][0]
                self.locationX = self.location[0][1]
                self.map.fill(0)  
                self.map[self.locationY,self.locationX] = 0
                self.map[self.locationY+1,self.locationX] = 2
            except IndexError as e:
                pass
        self.movehistory.append([self.locationY,self.locationX]) #we saveevery x and y of the head in every frame here so we can add the tail
        if len(self.movehistory) > self.length + points: #if the history has more cordinations than the lenght of the snake than we delet the last cordination
            self.movehistory.pop(0)
        for pos_y,pos_x in self.movehistory: #for every cordination of the tail we put 1 on the map
            self.map[pos_y,pos_x] = 1  
                
        return self.map #we return the value of the final map



key = None
def userinput(): #a loop that we will thread to get the input wasd
    while True:
        global key
        key = kb.read_key().lower()

begin = True
inputthread = Thread(target=userinput) # we start the thread here
inputthread.start()
x,y = os.get_terminal_size() #we use the os library to get the terminal size
termap = np.array([[0], #we put 1 x and 1y
                    [0]])
termap = np.resize(termap,(y,x)) #we change each dimension size by the x and y of the terminal size so we get the terminal map or "termap"
snake1 = snake(termap) #we put the snake data once
time = 0.1 #the freshrate
points = 0 #beggining points dont work now but after we add fruits it should increase

try: #we use try so if the player press contro + c the game stops
    while True:
        frame = [] #the frame that will get printed gets cleared after every ime so we avoid bugs
        snakemap=snake1.run(key,begin,points) #we runn the snake.run() method in every iteration
        termap = snakemap #the snake returns the map value and we change our termap to the snake map value i know its not pro move but it works ¯\_(ツ)_/¯
        for row in range(y):
            line = "" #in every line we clear the line hehe
            for bit in range(x): #in every letter we cheke
                if termap[row,bit] == 0: #if there is nothing print space
                    line += " "
                elif termap[row,bit] == 2: #if there is 2 = snake head print red = \033[33m 0 and put it back to default color 0m
                    line += '\033[33m'+"0"+'\033[0m'
                elif  termap[row,bit] == 1: # if its the tail = 1 print yellow 0
                    line+= '\033[31m'+"0"+'\033[0m'
                elif termap[row,bit] == 3: #if its fruit = 3 print blue O
                    line += '\033[34m'+"O"+'\033[0m'
            frame.append(line) #we add every line in the frame
        print('\033[H'+"\n".join(frame),end="") # we print the frame
        begin = None #now we disable the begin since the first iteration is done
        task.sleep(time) #it waits the times value befor rendering the next frame
except KeyboardInterrupt:

    print("quiting") #just print after u press control + c
