import os
import random
import sqlite3
import cv2
import easygui
from pathlib import Path
import face_recognition_ai
from PIL import Image


def registerFace(id: str) -> None:
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Register")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("register", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            savepath = f'registeredFaces/{id}.jpeg'
            cv2.imwrite(savepath, frame)
            print("{} written!".format(savepath))
            img_counter += 1
            break
    cam.release()
    cv2.destroyAllWindows()


def recogniseFace(inp_image: Image) -> str:
    for file in os.listdir('registeredFaces'):
        image = Image.open('registeredFaces/' + file)
        print(file)
        match = face_recognition_ai.face_recognition.match_faces(inp_image, image, 0.75)
        print(match)
        if len(match) == 0:
            continue
        if match[0] == True:
            id = "".join(list(file[:file.index(".")]))
            return id
        image.close()
    return ""

def updateimage(id: str):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Register")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("register", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            os.remove(f'registeredFaces/{id}.jpeg')
            savepath = f'registeredFaces/{id}.jpeg'
            cv2.imwrite(savepath, frame)
            print("{} written!".format(savepath))
            img_counter += 1
            break
    cam.release()
    cv2.destroyAllWindows()

def getImage():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Detect")
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Detect", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            cv2.imwrite('temp.jpeg', frame)
            break
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':


    Path("registeredFaces").mkdir(exist_ok=True)
    db = sqlite3.connect("userdata.db")

    reg = easygui.boolbox(msg="Already Registered", title="Registered?", choices=["[Y]es", "[N]o"],
                          default_choice="[Y]es", cancel_choice="[N]o")
    try:
        if reg:
            easygui.msgbox(msg="Press 'Space bar' to detect Face.\nPress 'Esc' to Exit.", title="Information")
            getImage()
            imagename = "temp.jpeg"
            image = Image.open('temp.jpeg')
            if imagename != "":
                image = Image.open(imagename)
                val = recogniseFace(image)
                image.close()
                os.remove(imagename)
                cursor = db.cursor()
                print(val)
                cursor.execute(f"select * from users where id={val}")
                row = cursor.fetchall()
                if len(row)>0:
                    name,phno,id = row[0]
                    easygui.msgbox(msg=f"Hey {name.title()},\nYou have logged in successfully!\nPhone number: {phno}\nLogin id: {id}\n", title=f"Login Successful! {name.title()}",ok_button="Close")
                    upimage = easygui.boolbox(msg="want to update image?", title="Update image?",
                                              choices=["[Y]es", "[N]o"], default_choice="[N]o", cancel_choice="[N]o")

                    if upimage:
                        phno = easygui.enterbox(title="Enter phone no", msg="Enter Phone no.: ")
                        if phno != "" and len(phno) == 10:
                            curs = db.cursor()
                            curs.execute(f"select * from users where phoneno={phno}")
                            row = curs.fetchall()
                            if len(row) > 0:
                                n, p, id = row[0]
                                updateimage(id)
                            else:
                                print("Error")
                        else:
                            print("Error")

                else:
                    print("Error")
            else:
                print("Error")
        else:

            data = easygui.multenterbox(msg="Enter the Detials", title="User Data", fields=["Name", "Phone no."])
            if data:
                for val in data:
                    if val.strip() == "":
                        exit(1)
                name = data[0]
                name = str(name).title()
                phno = data[1]
                phno = str(phno).title()
                id = list(data[1])
                random.shuffle(id)
                id = "".join(id)
                registerFace(id)
                cursor = db.cursor()
                cursor.execute("insert into users (name,phoneno,id) values(?,?,?)", [name, phno, id])
                db.commit()
                easygui.msgbox(title="Registration done", msg="Registered Successfully")
            else:
                print("Error")
    except Exception as e:
        print(str(e))
