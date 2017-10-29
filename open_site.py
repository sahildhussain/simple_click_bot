import webbrowser, pyautogui
import time
import random
for i in range(1,32,1):
    #random wait time within a range
    k=random.randint(7,19)
    time.sleep(k+3*k+k/2)
    #i am using 3 conditions, you may use as much conditions as you want.
    if k%3==0:
        webbrowser.open("http://www.yourptcsite.com/complete/url.php = "+str(i+k))
        time.sleep(13+k)
        pyautogui.click(AAAAA+k,BBBB+k)
    elif k%5==0:
        webbrowser.open("http://www.yourptcsite2.com/complete/url.php")
        pyautogui.click(AAAAA+k,BBBB+k)
    else:
        webbrowser.open("http://www.yourptcsite3.com/complete/url.php")
        time.sleep(5)
        pyautogui.click(AAAAA+k,BBBB+k)
#Replace AAAAA and BBBB with approx ad position. lot of tools are available on net.
