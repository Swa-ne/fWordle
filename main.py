from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle, Color, BorderImage
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.clock import Clock
import sqlite3
import pickle
import os
from datetime import datetime, date, timedelta

# Get date today
today = date.today()
date_format = "%m/%d/%Y"
now = datetime.strptime(today.strftime(date_format), date_format)
start = datetime.strptime('11/20/2022', date_format)
delta = (now - start).days

# To store data of different modes
# First Time open
inGameStats = {
    "played": 0,
    "wins": 0,
    "winRate": 0,
    "cStreak": 0,
    "mStreak": 0,
    "gDistribution": {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    },
    "history": {
        0: {"text": 0, "color": [0, 0, 0, 0, 0]},
        1: {"text": 0, "color": [0, 0, 0, 0, 0]},
        2: {"text": 0, "color": [0, 0, 0, 0, 0]},
        3: {"text": 0, "color": [0, 0, 0, 0, 0]},
        4: {"text": 0, "color": [0, 0, 0, 0, 0]},
        5: {"text": 0, "color": [0, 0, 0, 0, 0]}
    },
    "grey": [],
    "yellow": [],
    "green": [],
    "lastWord": ""
}
inGameStatsEasy = {
    "played": 0,
    "wins": 0,
    "winRate": 0,
    "cStreak": 0,
    "mStreak": 0,
    "gDistribution": {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    },
    "history": {
        0: {"text": 0, "color": [0, 0, 0, 0, 0]},
        1: {"text": 0, "color": [0, 0, 0, 0, 0]},
        2: {"text": 0, "color": [0, 0, 0, 0, 0]},
        3: {"text": 0, "color": [0, 0, 0, 0, 0]},
        4: {"text": 0, "color": [0, 0, 0, 0, 0]},
        5: {"text": 0, "color": [0, 0, 0, 0, 0]}
    },
    "grey": [],
    "yellow": [],
    "green": [],
    "lastWord": ""
}
inGameStatsHard = {
    "played": 0,
    "wins": 0,
    "winRate": 0,
    "cStreak": 0,
    "mStreak": 0,
    "gDistribution": {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    },
    "history": {
        0: {"text": 0, "color": [0, 0, 0, 0, 0]},
        1: {"text": 0, "color": [0, 0, 0, 0, 0]},
        2: {"text": 0, "color": [0, 0, 0, 0, 0]},
        3: {"text": 0, "color": [0, 0, 0, 0, 0]},
        4: {"text": 0, "color": [0, 0, 0, 0, 0]},
        5: {"text": 0, "color": [0, 0, 0, 0, 0]}
    },
    "grey": [],
    "yellow": [],
    "green": [],
    "lastWord": ""
}
inGameStatsSpecial = {
    "played": 0,
    "wins": 0,
    "winRate": 0,
    "cStreak": 0,
    "mStreak": 0,
    "gDistribution": {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    },
    "history": {
        0: {"text": 0, "color": [0, 0, 0, 0, 0]},
        1: {"text": 0, "color": [0, 0, 0, 0, 0]},
        2: {"text": 0, "color": [0, 0, 0, 0, 0]},
        3: {"text": 0, "color": [0, 0, 0, 0, 0]},
        4: {"text": 0, "color": [0, 0, 0, 0, 0]},
        5: {"text": 0, "color": [0, 0, 0, 0, 0]}
    },
    "grey": [],
    "yellow": [],
    "green": [],
    "lastWord": ""
}
inGameStatsDaily = {
    "played": 0,
    "wins": 0,
    "winRate": 0,
    "cStreak": 0,
    "mStreak": 0,
    "gDistribution": {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    },
    "history": {
        0: {"text": 0, "color": [0, 0, 0, 0, 0]},
        1: {"text": 0, "color": [0, 0, 0, 0, 0]},
        2: {"text": 0, "color": [0, 0, 0, 0, 0]},
        3: {"text": 0, "color": [0, 0, 0, 0, 0]},
        4: {"text": 0, "color": [0, 0, 0, 0, 0]},
        5: {"text": 0, "color": [0, 0, 0, 0, 0]}
    },
    "grey": [],
    "yellow": [],
    "green": [],
    "lastWord": ""
}
# Not First Time playing
pathE = r'data\easyInGameStats.dat'
pathH = r'data\hardInGameStats.dat'
pathS = r'data\specialInGameStats.dat'
pathD = r'data\dailyInGameStats.dat'
if os.path.exists(pathE):
    with open(pathE, "rb") as db:
        inGameStatsEasy = pickle.load(db)
if os.path.exists(pathH):
    with open(pathH, "rb") as db:
        inGameStatsHard = pickle.load(db)
if os.path.exists(pathS):
    with open(pathS, "rb") as db:
        inGameStatsSpecial = pickle.load(db)
if os.path.exists(pathD):
    with open(pathD, "rb") as db:
        inGameStatsDaily = pickle.load(db)

# Stores the Objects
gameMode = ""
stats = [0, 0]
root = [0]
gameDistr = [0, 0]
guesses = [[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)]]
chances = 0
resultShow = [1, 1]
settingShow = [1]
notWordShow = [1]
timeRShow = [1, 1]
notEnoughShow = [1]
allbtn = [i for i in range(28)]

# To change every letter in the keyboard
greyLetter = set(inGameStats["grey"])
yellowLetter = set(inGameStats["yellow"])
greenLetter = set(inGameStats["green"])

# Game Logic
# Save Every Game Mode Data
def saveEasyData():
    with open(r"data\easyInGameStats.dat", "wb") as dbEasy:
        pickle.dump(inGameStatsEasy, dbEasy)
def saveHardData():
    with open(r"data\hardInGameStats.dat", "wb") as dbHard:
        pickle.dump(inGameStatsHard, dbHard)
def saveSpecialData():
    with open(r"data\specialInGameStats.dat", "wb") as dbSpecial:
        pickle.dump(inGameStatsSpecial, dbSpecial)
def saveDailyData():
    with open(r"data\dailyInGameStats.dat", "wb") as dbDaily:
        pickle.dump(inGameStatsDaily, dbDaily)

# Variable for Objects
words = sqlite3.connect("words.db")
c = words.cursor()
# Fetch all words and save in a variable
dictWord = {}
c.execute("SELECT * FROM words")
for i in c.fetchall():
    dictWord[i[0]] = 1

# Fetch easy words and save in a variable
c.execute("SELECT * FROM easy")
easyWords = {str(i) : s for i, s in c.fetchall()}

# Fetch Hard words and save in a variable
c.execute("SELECT * FROM hard")
hardWords = {str(i) : s for i, s in c.fetchall()}

# Fetch special words and save in a variable
c.execute("SELECT * FROM special")
specialWords = {str(i) : s for i, s in c.fetchall()}

c.execute("SELECT * FROM daily")
dailyWords = {str(i) : s for i, s in c.fetchall()}

words.commit()
words.close()

word = ""

def getTime():
    global timeRemaining
    today = datetime.now()
    tom = date.today() + timedelta(1)
    date_format = "%Y-%m-%d %H:%M:%S"
    nowTime = datetime.strptime(today.strftime("%Y-%m-%d %H:%M:%S"), date_format)
    next = datetime.strptime(tom.strftime("%Y-%m-%d %H:%M:%S"), date_format)
    timeRemaining = next - nowTime
    return timeRemaining

def addLastWord():
    if gameMode == "Daily Puzzle":
        inGameStats["lastWord"] = word.lower()

def gameInProgress():
    global chances, guesses
    if inGameStats["history"][0] != 0:
        for i in range(6):
            if inGameStats["history"][i]['text'] == 0:
                chances = i
                break
            else: 
                for n in range(5):
                    guesses[i][n].text = inGameStats["history"][i]['text'][n]
                    guesses[i][n].background_color = inGameStats["history"][i]['color'][n]

def getWordGameMode():
    global inGameStats, greyLetter, yellowLetter, greenLetter
    if gameMode == "Easy":
        getEasyWord()
        inGameStats = inGameStatsEasy
        greyLetter = set(inGameStats["grey"])
        yellowLetter = set(inGameStats["yellow"])
        greenLetter = set(inGameStats["green"])
    elif gameMode == "Hard":
        getHardWord()
        inGameStats = inGameStatsHard        
        greyLetter = set(inGameStats["grey"])
        yellowLetter = set(inGameStats["yellow"])
        greenLetter = set(inGameStats["green"])
    elif gameMode == "Special":
        getSpecialWord()
        inGameStats = inGameStatsSpecial        
        greyLetter = set(inGameStats["grey"])
        yellowLetter = set(inGameStats["yellow"])
        greenLetter = set(inGameStats["green"])
    elif gameMode == "Daily Puzzle":
        getDailyWord()
        inGameStats = inGameStatsDaily
        if word != inGameStats["lastWord"]:
            greyLetter = set(inGameStats["grey"])
            yellowLetter = set(inGameStats["yellow"])
            greenLetter = set(inGameStats["green"])
        else:
            timeRShow[0].opacity = 1
            Clock.schedule_once(hideNotTimeR, 2)

def getEasyWord():
    global word
    word = easyWords[str(inGameStatsEasy["played"] + 1)]
    print(word)
    
def getHardWord():
    global word
    word = hardWords[str(inGameStatsHard["played"] + 1)]
    print(word)

def getSpecialWord():
    global word
    word = specialWords[str(inGameStatsSpecial["played"] + 1)]
    print(word)

def getDailyWord():
    global word
    word = dailyWords[str(delta)]
    print(word)

def lockButtons():
    for i in allbtn:
        i.disabled = True

def unlockButtons():
    for i in allbtn:
        i.disabled = False

def hideNotTimeR(dataType):
    timeRShow[0].opacity = 0
    timeRShow[1].opacity = 0

def Goto(btn):
    if btn.text == 'Menu':
        root[0].current = 'start'
        settingShow[0].width = 0
        settingShow[0].opacity = 0
    elif btn.text == 'Play Again' and gameMode != "Daily Puzzle":
        global chances, counter
        getWordGameMode()
    elif btn.text == 'Play Again' and gameMode == "Daily Puzzle":
        timeRShow[0].opacity = 1
        getTime()
        Clock.schedule_once(hideNotTimeR, 2)
        return
    elif btn.text == "Continue Playing":
        settingShow[0].width = 0
        settingShow[0].opacity = 0
        unlockButtons()
    if btn.text != "Continue Playing":
        resultShow[0].width = 0
        resultShow[0].opacity = 0
        chances = 0
        counter = 0
        for i in range(6):
            for n in range(5):
                guesses[i][n].text=""
                guesses[i][n].background_color = (1, 1, 1, 1)
    unlockButtons()

def removeGrey(letter):
    if letter in greyLetter:
        greyLetter.remove(letter)
        
def removeYellow(letter):
    if letter in yellowLetter:
        yellowLetter.remove(letter)
    
def checkIfWord(word):
    if word.lower() in dictWord:
        return True
    else:
        return False

def find(string, letter):
    for idx, ltr in enumerate(string):
        if ltr == letter:
            yield idx

def checkEveryLetter(guess):
    wordLetterCount = {}
    for ltr in word:
        if ltr not in wordLetterCount:
            wordLetterCount[ltr] = 0
        wordLetterCount[ltr] += 1
    guessedLetter = [0, 0, 0, 0, 0]
    for idx, letter in enumerate(guess):
        letter = letter.lower()
        indexes = list(find(word, letter))
        if letter in wordLetterCount and wordLetterCount[letter] > 0:
            if idx in indexes:
                guessedLetter[idx] = 2
                removeGrey(letter)
                removeYellow(letter)
                greenLetter.add(letter)
            elif idx not in indexes:
                guessedLetter[idx] = 1
                removeGrey(letter)
                yellowLetter.add(letter)
            wordLetterCount[letter] -= 1
        else:
            greyLetter.add(letter)
    return guessedLetter

def changeKeyboardColor():
    for keys in allbtn:
        letter = keys.text.lower()
        if letter in inGameStats["yellow"]:
            keys.background_color = (1, 1, 0, 1)
        elif letter in inGameStats["green"]:
            keys.background_color = (0, 1, 0, 1)
        elif letter in inGameStats["grey"]:
            keys.background_color = (0.5, 0.5, 0.5, 1)
        else:
            keys.background_color = (1, 1, 1, 1)

def clearKeyboardColor():
    global inGameStats, greyLetter, yellowLetter, greenLetter
    
    greyLetter = set()
    yellowLetter = set()
    greenLetter = set()
    inGameStats["grey"] = greyLetter
    inGameStats["yellow"] = yellowLetter
    inGameStats["green"] = greenLetter
    for keys in allbtn:
        keys.background_color = (1, 1, 1, 1)


class OptionButton(BoxLayout):
    pass

class OptionMain(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.background_color = (0, 1, 0, 1)
        self.size_hint = (.14, .2)
        self.add_widget(OptionBtn())
        self.add_widget(OptionFloat())

class OptionBtn(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = "setting.png"
        self.size = (1, 1)
        self.background_down = self.background_normal
        self.pos_hint = {"center_x": 0.5}
        self.bind(on_press=self.openSetting)
        
    def openSetting(self, dataType):
        settingShow[0].width = 100
        settingShow[0].opacity = 1
        lockButtons()

class OptionFloat(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 100
        self.pos = (0, 0)
        self.background_color = (0, 1, 0, 1)
        self.size_hint = (.14, .2)
        self.add_widget(LBBtn(pos = (370, 660)))
    
class LBBtn(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = "lbs.png"
        self.size = (1, 1)
        self.background_down = self.background_normal
        self.bind(on_press=self.openResult)
        
    def openResult(self, dataType):
        stats[1].updateValue(inGameStats)
        gameDistr[1].updateValue(inGameStats)
        resultShow[1].width = 100
        resultShow[1].opacity = 1
        lockButtons()
        
class Main(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation ="vertical"
        for chances in range(6):
            self.add_widget(MainWord(chances))

class MainWord(GridLayout):
    def __init__(self, row, **kwargs):
        super().__init__(**kwargs)
        self.rows=1
        for col in range(5):
            btn = MainWordBox()
            guesses[row][col] = btn
            self.add_widget(btn)

class MainWordBox(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.disabled = True
        self.disabled_color = (1, 1, 1, 1)
        self.background_disabled_normal = 'border.png'
        if 'text' not in kwargs:
            self.text = ""
        else:
            self.text = kwargs["text"]


counter = 0
class KeyboardButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = kwargs["text"]
        self.bind(on_press=self.enterValue)
        
    def enterValue(self, dataType):
        global counter
        global chances
        global resultShow
        global inGameStats
        if self.text == "ENTER" and counter< 5:
            notEnoughShow[0].width = 100
            notEnoughShow[0].opacity = 1
            Clock.schedule_once(hideNotEnough, 2)
        if self.text == "ENTER" and chances == 5 and counter == 5:
            word = ''.join([guesses[chances][0].text,guesses[chances][1].text,guesses[chances][2].text,guesses[chances][3].text,guesses[chances][4].text])
            if checkIfWord(word):
                checker = checkEveryLetter(word)
                if checker != [2, 2, 2, 2, 2]:
                    resultShow[0].width = 100
                    resultShow[0].opacity = 1
                    inGameStats["played"] += 1
                    inGameStats["cStreak"] = 0
                    inGameStats["winRate"] = int(inGameStats["wins"] / inGameStats["played"] * 100)
                    stats[0].updateValue(inGameStats)
                    gameDistr[0].updateValue(inGameStats)
                    lockButtons()
                    for i in range(6):
                        inGameStats['history'][i] = {"text": 0, "color": [0, 0, 0, 0, 0]}
                    clearKeyboardColor()
                    changeKeyboardColor()
                    addLastWord()
        elif self.text not in ["ERASE", "ENTER"] and counter < 5:
            guesses[chances][counter].text = self.text
            counter = counter + 1
        elif self.text == "ERASE" and counter > 0:
            guesses[chances][counter - 1].text = ""
            counter = counter - 1
        elif self.text == "ENTER" and counter == 5:
            word = ''.join([guesses[chances][0].text,guesses[chances][1].text,guesses[chances][2].text,guesses[chances][3].text,guesses[chances][4].text])
            if checkIfWord(word):
                inGameStats['history'][chances]['text'] = word
                checker = checkEveryLetter(word)
                inGameStats["grey"] = greyLetter
                inGameStats["yellow"] = yellowLetter
                inGameStats["green"] = greenLetter
                changeKeyboardColor()
                for idx, val in enumerate(checker):
                    if val == 1:
                        guesses[chances][idx].background_color = (1, 1, 0, 1)
                        inGameStats['history'][chances]['color'][idx] = (1, 1, 0, 1)
                    elif val == 2:
                        guesses[chances][idx].background_color = (0, 1, 0, 1)
                        inGameStats['history'][chances]['color'][idx] = (0, 1, 0, 1)
                    else:
                        guesses[chances][idx].background_color = (0.5, 0.5, 0.5, 1)
                        inGameStats['history'][chances]['color'][idx] = (0.5, 0.5, 0.5, 1)
                        
                if checker == [2, 2, 2, 2, 2]:
                    resultShow[0].width = 100
                    resultShow[0].opacity = 1
                    inGameStats["played"] += 1
                    inGameStats["wins"] += 1
                    inGameStats["cStreak"] += 1
                    inGameStats["winRate"] = int(inGameStats["wins"] /inGameStats["played"] * 100)
                    inGameStats["gDistribution"][chances + 1] += 1
                    if inGameStats["mStreak"] < inGameStats["cStreak"]:
                        inGameStats["mStreak"] = inGameStats["cStreak"]
                    stats[0].updateValue(inGameStats)
                    gameDistr[0].updateValue(inGameStats)
                    addLastWord()
                    lockButtons()
                    for i in range(6):
                        inGameStats['history'][i] = {"text": 0, "color": [0, 0, 0, 0, 0]}
                    clearKeyboardColor()
                counter = 0
                chances += 1
            else:
                notWordShow[0].width = 100
                notWordShow[0].opacity = 1
                Clock.schedule_once(hideNotWord, 2)

def hideNotWord(n):
    notWordShow[0].width = 0
    notWordShow[0].opacity = 0
def hideNotEnough(n):
    notEnoughShow[0].width = 0
    notEnoughShow[0].opacity = 0

class Keyboard(BoxLayout):
    pass

class KeyboardRow1(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        for idx, ltr in enumerate(letters):
            btn = KeyboardButton(text=ltr)
            self.add_widget(btn)
            allbtn[idx] = btn


class KeyboardRow2(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        letters = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
        for idx, ltr in enumerate(letters):
            btn = KeyboardButton(text=ltr)
            self.add_widget(btn)
            allbtn[idx + 10] = btn
class KeyboardRow3(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        letters = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', "ERASE"]
        for idx, ltr in enumerate(letters):
            btn = KeyboardButton(text=ltr)
            self.add_widget(btn)
            allbtn[idx + 19] = btn

class Submit(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = KeyboardButton(text="ENTER")
        self.add_widget(btn)
        allbtn[27] = btn
        res = Result()
        resultShow[0] = res
        self.add_widget(res)
        res1 = Result1()
        resultShow[1] = res1
        self.add_widget(res1)
        sett = Settings()
        settingShow[0] = sett
        self.add_widget(sett)
        hover = Hover()
        self.add_widget(hover)

class Settings(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0, 0)
        self.width = 0
        self.opacity = 0
        self.add_widget(SettingsMain(size_hint = (2.8, 1.5)))

class SettingsMain(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = kwargs['size_hint']
        self.orientation = "vertical"
        self.pos_hint = {"x": -3.35, 'top': 4.5}
        self.background_color = (1,1,1, 1)
        with self.canvas.before:
            Color(0.55, 0.55, 0.55)
            Rectangle(pos=(60, 250), size=(280, 250))
        self.add_widget(SettingButton(size_hint = (1,.2)))

class SettingButton(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (.8, .1)
        self.pos_hint = {'center_x': .5}
        P = Button(text="Continue Playing", size_hint = (1,1))
        M = Button(text="Menu", size_hint = (1,1))
        M.bind(on_press=Goto)
        P.bind(on_press=Goto)
        self.add_widget(P)
        self.add_widget(M)

class Result1(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0, 0)
        self.width = 0
        self.opacity = 0
        self.add_widget(ResultMain1(size_hint = (3.8, 5.5)))

class ResultMain1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = kwargs['size_hint']
        self.orientation = "vertical"
        self.pos_hint = {"x": -3.87, 'top': 6.7}
        self.background_color = (1,1,1, 1)
        with self.canvas.before:
            Color(0.55, 0.55, 0.55)
            Rectangle(pos=(10, 100), size=(380, 580))
        self.add_widget(Label(text = "STATISTICS", size_hint = (1,.1)))
        self.add_widget(ResultStats1(size_hint = (1,.1)))
        self.add_widget(Label(text = "GAME DISTRIBUTION", size_hint = (1,.1)))
        GR1 = ResultGameDistribution(size_hint = (1,.3))
        self.add_widget(GR1)
        gameDistr[1] = GR1
        btn = Button(text = "Continue Playing", size_hint = (.9,.2), pos_hint={'center_x': 0.5})
        btn.bind(on_press=self.exitResult)
        self.add_widget(btn)
    def exitResult(self, dataType):
        resultShow[1].width = 0
        resultShow[1].opacity = 0
        unlockButtons()

class Result(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0, 0)
        self.width = 0
        self.opacity = 0
        self.add_widget(ResultMain(size_hint = (3.8, 5.5)))

class ResultMain(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = kwargs['size_hint']
        self.orientation = "vertical"
        self.pos_hint = {"x": -3.87, 'top': 6.7}
        self.background_color = (1,1,1, 1)
        with self.canvas.before:
            Color(0.55, 0.55, 0.55)
            Rectangle(pos=(10, 100), size=(380, 580))
        self.add_widget(Label(text = "STATISTICS", size_hint = (1,.1)))
        self.add_widget(ResultStats(size_hint = (1,.1)))
        self.add_widget(Label(text = "GAME DISTRIBUTION", size_hint = (1,.1)))
        GR1 = ResultGameDistribution(size_hint = (1,.3))
        self.add_widget(GR1)
        gameDistr[0] = GR1
        self.add_widget(ResultButton(size_hint = (1,.2)))

class ResultGameDistribution(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 6
        self.cols = 1
        self.value = inGameStats
        self.max = self.value["played"]
        self.updateValue(inGameStats)

    def updateValue(self, value):
        self.clear_widgets()
        self.value = value
        self.add_widget(ResultProgress(text="1",max=self.value["played"],score=self.value["gDistribution"][1]))
        self.add_widget(ResultProgress(text="2",max=self.value["played"],score=self.value["gDistribution"][2]))
        self.add_widget(ResultProgress(text="3",max=self.value["played"],score=self.value["gDistribution"][3]))
        self.add_widget(ResultProgress(text="4",max=self.value["played"],score=self.value["gDistribution"][4]))
        self.add_widget(ResultProgress(text="5",max=self.value["played"],score=self.value["gDistribution"][5]))
        self.add_widget(ResultProgress(text="6",max=self.value["played"],score=self.value["gDistribution"][6]))

class ResultProgress(BoxLayout):
    def __init__(self, text,max, score, **kwargs):
        super().__init__(**kwargs)
        self.right = 0
        self.add_widget(Label(text=text, size_hint = (.1,1)))
        self.add_widget(ProgressBar(max=max, value=score))
        self.add_widget(Label(text=str(score), size_hint = (.1,1)))     

class ResultButton(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint = (.8, .1)
        self.pos_hint = {'center_x': .5}
        M = Button(text="Menu", size_hint = (.1,1))
        P = Button(text="Play Again", size_hint = (.1,1))
        M.bind(on_press=Goto)
        P.bind(on_press=Goto)
        self.add_widget(M)
        self.add_widget(P)

class ResultStats1(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = kwargs['size_hint']
        self.rows = 2
        RS1 = resultStatsTop()
        self.add_widget(RS1)
        stats[1] = RS1
        t = str(getTime())
        timeR = HoverTimeR(size_hint = (0, 0), time=t)
        timeRShow[0] = timeR
        self.add_widget(timeR)
        self.add_widget(resultStatsBottom())

class ResultStats(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = kwargs['size_hint']
        self.rows = 2
        RS1 = resultStatsTop()
        self.add_widget(RS1)
        stats[0] = RS1
        t = str(getTime())
        timeR = HoverTimeR(size_hint = (0, 0), time=t)
        timeRShow[0] = timeR
        self.add_widget(timeR)
        self.add_widget(resultStatsBottom())

class HoverTimeR(FloatLayout):
    def __init__(self, time, **kwargs):
        super().__init__(**kwargs)
        self.pos=(0, 0)
        self.width = 100
        self.opacity = 0
        with self.canvas.before:
            Color(0.2, 0.2, 0.2)
            Rectangle(pos=(160, 650), size=(80, 30))
        self.add_widget(Label(text = time, pos=(200, 645)))

class resultStatsTop(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.value = inGameStats
        self.updateValue(inGameStats)

    def updateValue(self, value):
        self.clear_widgets()
        self.value = value
        self.add_widget(Label(text = str(self.value["played"]), size_hint = (.1,.1), halign="center"))
        self.add_widget(Label(text = str(self.value["winRate"]), size_hint = (.1,.1), halign="center"))
        self.add_widget(Label(text = str(self.value["cStreak"]), size_hint = (.1,.1), halign="center"))
        self.add_widget(Label(text = str(self.value["mStreak"]), size_hint = (.1,.1), halign="center"))

class resultStatsBottom(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text = "Played", size_hint = (.1,.1), halign="center"))
        self.add_widget(Label(text = "Win %", size_hint = (.1,.1), halign="center"))
        self.add_widget(Label(text = "Current Streak", size_hint = (.1,.1), halign="center"))
        self.add_widget(Label(text = "Max Streak", size_hint = (.1,.1), halign="center"))

class Title(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Rectangle(source="bg.jpg", pos=(0,0), size=(400, 700))

class StartMenuButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1,.3)
        self.text = kwargs['text']
        self.pos =  (150, 0)

    def Goto(self, dataType):
        global gameMode
        gameMode = self.text
        getWordGameMode()
        if gameMode != "Daily Puzzle" and inGameStatsDaily["lastWord"] != word:
            root[0].current = 'game'
        elif gameMode == "Daily Puzzle" and inGameStatsDaily["lastWord"] != word:
            root[0].current = 'game'
        elif gameMode == "Daily Puzzle" and inGameStatsDaily["lastWord"] == word:
            timeRShow[1].opacity = 1
            getTime()
            Clock.schedule_once(hideNotTimeR, 2)
        gameInProgress()
        changeKeyboardColor()
        

class StartButtons(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, .4)
        self.orientation = "vertical"
        DP = StartMenuButton(text = "Daily Puzzle")
        E = StartMenuButton(text = "Easy")
        H = StartMenuButton(text = "Hard")
        S = StartMenuButton(text = "Special")
        self.pos_hint = {"x": 0.05}
        DP.bind(on_press=DP.Goto)
        E.bind(on_press=E.Goto)
        H.bind(on_press=H.Goto)
        S.bind(on_press=S.Goto)
        
        self.add_widget(DP)
        self.add_widget(E)
        self.add_widget(H)
        self.add_widget(S)

class StartMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (.90, .90)
        with self.canvas:
            Rectangle(size=(400, 700))
            Color(1, 1, 1)
        t = str(getTime())
        timeR = HoverTimeR2(size_hint = (0, 0), time=t)
        timeRShow[1] = timeR
        self.add_widget(Title())
        self.add_widget(timeR)
        self.add_widget(StartButtons())

class HoverTimeR2(FloatLayout):
    def __init__(self, time, **kwargs):
        super().__init__(**kwargs)
        self.pos=(0, 0)
        self.width = 100
        self.opacity = 0
        with self.canvas.before:
            Color(0.2, 0.2, 0.2)
            Rectangle(pos=(160, 650), size=(80, 30))
        self.add_widget(Label(text = time, pos=(150, 615)))

class Hover(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0, 0)
        notWord = HoverNotWord(size_hint = (0, 0))
        short = HoverShort(size_hint = (0, 0))
        notWordShow[0] = notWord
        notEnoughShow[0] = short
        self.add_widget(notWord)
        self.add_widget(short)

class HoverNotWord(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos=(200, 665)
        self.width = 0
        self.opacity = 0
        self.add_widget(Label(text = "Not a Word"))
        with self.canvas.before:
            Color(0.55, 0.55, 0.55)
            Rectangle(pos=(160, 650), size=(80, 30))

class HoverShort(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos=(200, 665)        
        self.width = 0
        self.opacity = 0
        with self.canvas.before:
            Color(0.55, 0.55, 0.55)
            Rectangle(pos=(130, 650), size=(140, 30))
        self.add_widget(Label(text = "Not Enough Letters"))


class MainWidget(BoxLayout):
    pass

class Screen(Screen):
    pass

class StartScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        global root
        root[0] = sm
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(Screen(name='game'))

        return sm


MainApp().run()
saveEasyData()
saveHardData()
saveSpecialData()
saveDailyData()