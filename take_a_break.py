import time
import webbrowser
#import webbrowser function and timer

breaks = int(input("How many breaks would you like to take? "))
#creates countdown to remove until reaches tally
break_tally = 0

while (break_tally < breaks) : #run a break timer for as many breaks as the user specified
    time.sleep(59*60) #set the timer for 59 minutes 60 seconds/  0 minutes
    webbrowser.open("https://www.youtube.com/watch?v=7Ux--k7uwBY")
    #Lets make a new video to refrence
    time.sleep(64*60) #set timer for 1 hour after video is done
    webbrowser.open("https://www.youtube.com/watch?v=NMBuSMxrSaY")
    time.sleep(64*60) #set timer for 1 hour after video is done
    webbrowser.open("https://www.youtube.com/watch?v=Ef6LwAaB3_E")
    time.sleep(64*60) #set timer for 1 hour after video is done
    webbrowser.open("https://www.youtube.com/watch?v=eLfIsFl1Cac")
    break_tally = break_tally + 1
    #wrote this to not repeat more than once per 4 hours