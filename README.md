# Passwordlocker
Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

# User Stories/BDD
These are the behaviours/features that the application implements for use by a user.

As a user I would like:

To create an account with my details - log in and password
Store my existing login credentials
Generate a password for a new credential/account
Copy my credentials to the clipboard
Specifications

# Behaviour	Input	Output
Display codes for navigation	In terminal: $./passwordLocker.py	Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit
Display prompt for creating an account	Enter: ca	Enter your first name, last name and password
Display prompt for login in	Enter: li	Enter your account name and password
Display codes for navigation	Successful login	Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit
Display prompt for creating a credential	Enter: cc	Enter the social media name, your username/social media handle and password which can be auto generated after you specify the length or input your own
Display a list of credentials	Enter: dc	Prints a list of saved credentials
Display prompt for which credential to copy	Enter: copy	Enter the social media name of the credential you wish to copy.
Exit application	Enter: ex	Exit the current navigation stage

# SetUp / Installation Requirements
Prerequisites
python3.6-Installation guide
pyperclip-sudo apt-get install python-pyperclip
Cloning
In your terminal:

  $ git clone my repo
  $ cd Python-pwd-locker
Testing the Application
To run the tests for the class file:

$ python3.6 credentials_test.py

# Technologies Used
Python3.6

# Known Bugs
Copy function not fully functional

# License
Copyright (c) 2020 cyriannmkangoma
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.