# Face Recognition (Using face_recognition_ai API) in Python

The following project uses face_recognition_ai api along with PIL and OpenCV api
for face video capturing and face recognition. It also uses easygui api 
for graphical user interface. Sqlite is also used for database for saving details
of the users. The images are currently stored unencrypted (Working  on encryption though...)
and algorithm is also basic, working for more efficient and complex algorithms.



## 🆕 Features

- Uses GUI for user interface and uses inbuilt SQLite database for data storage.
- Uses Web cam for image capture and face_recognition_ai api which uses yoloV5 in background for better accuracy.


## 💻 Technologies used
This project is made from scratch and no templates were used. This uses the Django framework which is one of the best-suited frameworks for these kinds of projects. Some javascript is also used for some functionalities to work such as timer and all.
It uses the MVT architecture and thus the models.py of the repository has the database model that is used.\
There are 3 tables used for this project:\
 - Clues: stores all the questions answers and the score for each.\
 - Users: Stores the user details.\
 - ScoreAndTime: Stores the score and time of each question attempted by the user.\
The code is not much complicated and is easy to understand. The dead-ends are also linearly arranged and simple logic is applied for that.
## Tables used 

#### Users

| ATTRIBUTE    | DATATYPE       | INDEX         | DESCRIPTION                                  |
|:-------------|:---------------|:--------------|:---------------------------------------------|
| `name`       | `varchar(200)` |               | `stores user Name`                           |
| `phnoneno`   | `varchar(12)`  |               | `Phone number`                               |
| `id`         | `varchar(12)`  | `Primary Key` | `Phone number  is shuffled and stored as ID` |



## 🚀 About Me
I'm a programming enthusiast, always curious to learn new things and try new technologies... I m currently pursuing my Bachelor in Technology in Information Technology. My interests are in full stack and machine learning.
## 🛠 Skills
Python, Java, Javascript, HTML, CSS...## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/this-darshiii/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/this_darshiii)
