## OverTheWire Bandit - Level 26 (easy) 

**Goal:** Retrieve the password for level 27.

For this level, I needed to keep using the shell I got to open in the previous level.

### Steps taken

1. Getting a Shell

    In the same MORE error mode, I typed :shell and i get a shell for the level 26 user. 

2. Reading the password file

    With the shell, you can navigate as usual and run commands. LS to list files and in the ~ directory you can find an executable file called bandit27-do. 

3. Executing the bandit27-do script

    To get the password for level 27, I executed the bandit27-do script with the following command:

    ./bandit27-do
    
    The output of the command is the password for level 27.

### Key takeaways

- Use the shell to navigate and find files.
- Executable scripts can be run directly to perform actions.
-