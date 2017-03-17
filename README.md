## Use the Python package "itchat" to design a Wechat robot
### Instructions
**Dependence**:  
- Python 2.7
- WeChat app

There are 4 files in this repository:
  - **login.py**: By executing this file, we can get a QR code file downloaded. Scan the QR code and then we can log into the web wechat.
  - **test.py**: This is a script to design the wechat robot by using some functions and packages in python.
  - **Result1.jpg**: A simple example of chatting with the robot
  - **Result2.jpg**: Another simple example of chatting with the robot

**Execution instructions**:

To run the code, we may follow the commands below:

Suppose we're at the directory which contains the files

Enter the following commands and execute the python scripts in the terminal
**Install itchat package**

```bash
sudo pip install itchat --upgrade
```
Check it it's intalled successfully

```bash
python -c "import itchat"
```
If there is no error reported, then the package is installed successfully.

**Log into the web wechat**:

```bash
python login.py
```
**Register the robot and begin the auto response**

```bash
python test.py
```
After starting the auto-response, we can let someone else speak to us by using wechat, and the robot will response to them automatically. 

**Results**

The examples of chatting with the robot are in files **Result1.jpg** and **Result2.jpg** 
The words in the **white dialog boxes** are the robot's responses towards the requests or questions in the **green boxes**. The **green dialog boxes** are in charge of someone else in your wechat contact lists.

**Note**

This "itchat" package supports Chinese language better.
Maybe in the future, I can find out some packages mainly supporting English or other languages and put them into the application.
