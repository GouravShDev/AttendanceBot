import custom_web_driver
from datetime import datetime, time, timedelta
from threading import Timer

from time import sleep


def showMenu():
    print("************ATTENDANCE BOT************\n")
    print("1. Schedule a class")
    print("2. Exit ")

    choice = input()
    if(choice == '1'):
        showClassMenu()
    elif(choice == '2'):
        exit

def showClassMenu():
    
    #day = input("\nEnter Date of Class (Only Day) : ")

    time = input("\nEnter the time of Class (HH:MM) : ")
    # Converting HH:MM to Hrs and minutes
    h, m = map(int, time.split(':'))
    classLink = input("\nEnter Link for the Class : ")
    #ScheduledClass( classLink= classLink)
    initiate(hours= h, minutes= m, link= classLink)


def initiate(hours, minutes, link):
    current=datetime.today()
    timeReq = current.replace(hour= hours, minute=minutes)
    delta_t= timeReq - current
    # runAt = currentTime + timedelta(hours= hours, minutes= minutes)
    # delay = (runAt - currentTime).total_seconds()
    delay = delta_t.total_seconds()
    print("Class will start after : " + delay + "sec")
    Timer(delay , lambda : startClass(link)).start()
    # startClass(link)
    

def startClass(link):
    driver = custom_web_driver.CustomWebdriver(link= link)
    driver.launch()


if __name__ == "__main__":
    showMenu()