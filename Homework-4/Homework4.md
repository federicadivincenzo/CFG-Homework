## Homework week 4
Federica Di Vincenzo

#### *TASK 1 (Git and GitHub)*
1. Question 1 

Complete definitions for key Git & GitHub terminology
  - **GIT WORKFLOW FUNDAMENTALS** 
    - Working Directory -> _The working directory (workspace) is essentially your project folder._
    - Staging Area -> _The staging area is a middle ground between what you have done to your files (the working directory) and what you have last committed_
    - Local Repo (head) -> _The local repo refer to the repository on the computer and has all the files and their commit history, enabling full diffs, history review, and committing when offline._
    - Remote repo (master) -> _Git refers to a centralized server as a “remote repository”. The remote repo is usually not on the local machine and is shared by the team. The team “pushes” commits to it when ready to share with the team._
 

- **WORKING DIRECTORY STATES**:
  - Staged -> _Staging the changes to include in the next commit._
  - Modified -> _Modify your files in the working tree to be staged._
  - Committed -> _Once all files changed have been staged, those changes are commited alongside with a descriptive message. The modified files will then be safely stored in the repo._ 
 

- **GIT COMMANDS**:
  - Git add -> _Git add command includes all the changes of a file(s) into the next commit. _
  - Git commit -> _Git commit is like a checkpoint in the development process which you can go back to later if needed._
  - Git push -> _After committing your changes, the next thing you want to do is send your changes to the remote server. Git push uploads your commits to the remote repository._
  - Git fetch -> _gets the updates from remote repository_
  - Git merge -> _applies the latest changes in your local_ 

#### *TASK 2 (Exception Handling)*
1. Question 1
- **Simple ATM program**
  - Using exception handling code blocks such as try/ except / else / finally, write a program that simulates an ATM machine to withdraw money. (NB: the more code blocks the better, but try to use at least two key words e.g.
  try/except)
  - Tasks:
    1. Prompt user for a pin code
     2. If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again. You can give a user a maximum of 3 attempts and then exit a program. 
     3. Set account balance to 100. 
     4. Now we need to simulate cash withdrawal 
     5. Accept the withdrawal amount 
     6. Subtract the amount from the account balance and display the remaining balance (NOTE! The balance cannot be negative!)
     7. However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to raise an error an exit the program.


#### *TASK 3 (Testing)*
1. Question 1 
   - Use the Simple ATM program to write unit tests for your functions.
       You are allowed to re-factor your function to ‘untangle’ some logic into smaller 
       blocks of code to make it easier to write tests. 
       Try to write at least 5 unit tests in total covering various cases.