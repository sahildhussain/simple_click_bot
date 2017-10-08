import webbrowser, pyautogui
import time
import random
for i in range(1,32,1):
    #random wait time within a range
    k=random.randint(7,19)
    time.sleep(k+3*k+k/2)
    #i am using 3 conditions, you may use as much conditions as you want.
    if k%3==0:
        webbrowser.open("http://www.myewizard.com/advertise.php?j_id = "+str(i+k))
        time.sleep(13+k)
    elif k%5==0:
        webbrowser.open("http://www.myewizard.com/jobs.php")
    else:
        webbrowser.open("http://www.myewizard.com/advertise.php")
        time.sleep(5)
        pyautogui.click(120+k,400+k)