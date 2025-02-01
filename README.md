# Personal-library-for-all-programs
## Description/Purpose
  This repository is supposed to encapsulate the growth of this profile's programming career. 
  It shows a "before-and-after" effect of the career. Go to earlier programs to see the "before"
  and go to the newer ones to see the "after".
## Password-Checker
This program checks if a password is okay to set as your official password
- Input:
  - String
- Output:
  - String
### Functionality
This program takes an inputted string and checks if it can pass three "tests"
  1. If it is a generally basic password, it outputs "This is a really common password please change"
  2. If it is less than 6 letters, it outputs "Password is too short"
  3. If it doesn't include special character such as "-" or ".', it outputs "Please add a special character for a hard to guess password"
- Additionally it returns a list of the tests it failed using a for-loop
### Critiques
This is an incredibly early program that has many typos and has primitive techniques to achieve the end goal. This is one of the reasons it is the first program that is part of the repository
### Real-World Uses
- It is used in many password storing apps.
- In many website it shows you a much more advanced version of this program with how good your password is and how to make it better.
## Pasword Synthesizer
This program creates an acceptable password that is able to pass the restrictions of the previous program.
- Input:
  - String & int
- Output:
  - String
### Functionality
1. The program takes the integer and sets the range of a for loop to that integer
2. Adds random characters to a string that are can be used in passwords
3. Returns this string to the user
### Critiques
- It also uses inredibly primitive logic to achieve its goal.
- It doesn't guarantee special characters in the returned string. 
- It also uses an extra string w/o using the more efficient and readily booleans.
### Real World Uses
- Many apps also suggest a password
  - Chrome, for example, suggests a password when it detects you are creating one.
  - It uses much more advanced restrictions and that is why it always outputs complex code.
