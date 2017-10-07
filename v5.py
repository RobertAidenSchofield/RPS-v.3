from graphics import *
from time import *

def IsValidClick(win, x1, y1, x2, y2):
    p1 = win.getMouse()
    if p1.getX() >=x1 and p1.getX() <=x2 and p1.getY() >=y1 and p1.getY() <= y2:
        return True
    else:
        return False

def CreateText(win, x1, y1, text, color, style, font, size):
    tempText = Text(Point(x1, y1), text)
    tempText.setTextColor(color)
    tempText.setStyle(style)
    tempText.setFace(font)
    tempText.setSize(size)
    return tempText

def main():
    win = GraphWin("Rock,Paper,Scissors Game!", 1000, 1000)
    win.setCoords(0,0,10,10)
    #background
    imgBackground = Image(Point(5,5),"Black-Background-2.gif")
    imgBackground.draw(win)
    #display into
    intro = CreateText(win,5,9,"Welcome to the Rock,Paper,Scissors Game!","white","bold","courier",20)
    intro.draw(win)
    #weapon menu    
    menuChoice1 = CreateText(win,5,8, "Player 1 Enter your choice of 1) Rock 2) Paper 3) Scissors:","white","bold","courier",12)
    menuChoice1.draw(win)
    menuChoice2 = CreateText(win,5,7, "Player 2 Enter your choice of 1) Rock 2) Paper 3) Scissors:","white","bold","courier",12)
    menuChoice2.draw(win)
    #prompt for user choice 
    entChoice1 = Entry(Point(9.5,8), 3)
    entChoice1.draw(win)
    entChoice2 = Entry(Point(9.5,7), 3)
    entChoice2.draw(win)
    #draw rectangle 
    rectButton = Rectangle(Point(4,4), Point(6,6))
    rectButton.setOutline("white")
    rectButton.setWidth(2)
    rectButton.draw(win)
    #display play in rectangle button 
    txtButton = CreateText(win, 5,5, "Play!","white","bold","courier",14)
    txtButton.draw(win)
    #click validation 
    while IsValidClick(win,4,4,6,6,) == False:
        #dummy code
        x = 10
    #assign user choice
    choice1 = float(entChoice1.getText())
    choice2 = float(entChoice2.getText())

   
    #selection structure for winner 
    if choice1 == 1 and choice2 == 3:
        imgRock = Image(Point(5,2.3),"Clipart-alpine-landscape-rock-rubble-al1-2.gif")
        imgRock.draw(win)
        sleep(1)
        txtWin = CreateText(win, 5,1.7, "Rock Smashes Scissors","white","bold","courier",12)
        txtWin.draw(win)
        sleep(1)
        imgScissors = Image(Point(5,1),"Scissors-clip-art-8.gif")
        imgScissors.draw(win)
        sleep(.5)
        winner = CreateText(win,5,3,"The Winner is: Player 1 ","white","bold","courier",12)
        

    elif choice1 ==2 and choice2 ==1:
        imgPaper = Image(Point(5,2.3),"paper-clipart-eiMyezain.gif")
        imgPaper.draw(win)
        sleep(1)
        txtWin = CreateText(win, 5,1.5, "Paper covers Rock!","white","bold","courier",12)
        txtWin.draw(win)
        sleep(1)
        imgRock = Image(Point(5,1),"Clipart-alpine-landscape-rock-rubble-al1-2.gif")
        imgRock.draw(win)
        sleep(.5)
        winner = CreateText(win,5,3,"The Winner is: Player 1 ","white","bold","courier",12)

    elif choice1 == 3 and choice2 == 2:
        imgScissors = Image(Point(5,2.3),"Scissors-clip-art-8.gif")
        imgScissors.draw(win)
        sleep(1)
        txtWin = CreateText(win, 5,1.7, "Scissors cut Paper!","white","bold","courier",12)
        txtWin.draw(win)
        sleep(1)    
        imgPaper = Image(Point(5,1),"paper-clipart-eiMyezain.gif")
        imgPaper.draw(win)
        sleep(.5)
        winner = CreateText(win,5,3,"The Winner is: Player 1","white","bold","courier",12)
        
        
     
    elif choice2 == 1 and choice1 == 3:
        imgRock = Image(Point(5,2.3),"Clipart-alpine-landscape-rock-rubble-al1-2.gif")
        imgRock.draw(win)
        sleep(1)
        txtWin = CreateText(win, 5,1.7, "Rock Smashes Scissors","white","bold","courier",12)
        txtWin.draw(win)
        sleep(1)
        imgScissors = Image(Point(5,1),"Scissors-clip-art-8.gif")
        imgScissors.draw(win)
        sleep(.5)
        winner = CreateText(win,5,3,"The Winner is: Player 2 ","white","bold","courier",12)
     
    elif choice2 ==2 and choice1 ==1:
        imgPaper = Image(Point(5,2.3),"paper-clipart-eiMyezain.gif")
        imgPaper.draw(win)
        sleep(1)
        txtWin = CreateText(win, 5,1.5, "Paper covers Rock!","white","bold","courier",12)
        txtWin.draw(win)
        sleep(1)
        imgRock = Image(Point(5,1),"Clipart-alpine-landscape-rock-rubble-al1-2.gif")
        imgRock.draw(win)
        sleep(.5)
        winner = CreateText(win,5,3,"The Winner is: Player 2 ","white","bold","courier",12)
     
    elif choice2 == 3 and choice1 == 2:
        imgScissors = Image(Point(5,2.3),"Scissors-clip-art-8.gif")
        imgScissors.draw(win)
        sleep(1)
        txtWin = CreateText(win, 5,1.7, "Scissors cut Paper!","white","bold","courier",12)
        txtWin.draw(win)
        sleep(1)    
        imgPaper = Image(Point(5,1),"paper-clipart-eiMyezain.gif")
        imgPaper.draw(win)
        sleep(.5)
        winner = CreateText(win,5,3,"The Winner is: Player 2","white","bold","courier",12)
     
    #draw to window 
    winner.draw(win)

main()
