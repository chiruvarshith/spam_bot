import pyautogui,time
def send_message():
    time.sleep(4)
    list1=tuple(range(1,53))
    for i in range(len(list1)):
        text=list1[i]
        for each_line in text :
            pyautogui.typewrite(each_line)
            pyautogui.press("enter")

        

send_message() 
