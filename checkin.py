
#checkin.py
#import pyperclip

def bend():         #This function is used to determine if there is a bend, and if so, the severity
    weakBend = "Device has a minor bend in the frame."
    medBend = "Device has a moderate bend in the frame."
    strongBend = "Device has a severe bend in the frame."
    bend = eval(input("If device has bend in frame, input 1. \nIf not, input 2.\n"))
    bendList = [weakBend,medBend,strongBend]
    if bend == 1:
        bend = eval(input("If bend is minor, input 1. \nIf moderate, input 2. \nIf severe, input 3.\n"))
        bend = bend - 1
        try:
            return bendList[bend]
        except:
            return bend()
    else: 
        return ("")

#checkin.py


def screen():       #This function is to differentiate between broken glass, glass/lcd, or just LCD
    try:
        glass = "broken glass, LCD still functional."
        lcd = "broken LCD."
        glassLcd = "broken glass and LCD."
        workList = [glass,lcd,glassLcd]
        workScreen = eval(input("Glass broken? 1, \nLCD broken? 2, \nGlass and LCD broken? 3\n"))
                    #This will become incorporated with the gui. We are simply using temporary
                    #numbers to produce the same output
        workScreen = workScreen - 1
        return workList[workScreen]
    except:
        return screen()

def turnaround():
    time1 = eval(input("How long will this take to get done?"))
def abletotest():
    test = eval(input("Were you able to test the device? Input a 1, \notherwise input a 2\n"))
    if test == 1:
        return ""
    elif test == 2:
        return "Device was unable to be tested at check-in due to the nature of the damage. Device will be tested after the repair, and customer will be notified if any additional damage is identified."
    else:
        return abletotest()

def screenrepair():
    deviceName = input("What is the device name? i.e. Samsung Galaxy S7 Edge\n")
    deviceColor = input("What color is the screen? i.e. White, Rose Gold, Black\n")
    screenWork = screen()
    bendWork = bend()
    turnaroundWork = input("How long will this take to get done? i.e. '2.5 hours,' ',3-5 days,'\n")
    testWork = abletotest()
    print("Customer has brought in a",deviceColor,deviceName,"with a",
    screenWork,bendWork,"Customer understands turn-around time of",turnaroundWork,testWork)
    #pyperclip.copy("Customer has brought in a",deviceColor,deviceName,"with a",
    #screenWork,bendWork,"Customer understands turn-around time of",turnaroundWork,testWork)

def waterdiag():
    return

def chargeport():
    return

def miscdiag():
    return

def laptopglass():
    return



def main():
    screenrepair()

