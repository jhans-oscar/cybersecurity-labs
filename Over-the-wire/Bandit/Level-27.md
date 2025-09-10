## Over the wire: Bandit Level 27 (Ongoing)

**Goal:** Retrieve the password for level 28.

This level is asking me to find the password for the next level, level 28, using git. 

### Steps taken

1. Learning how to use a port and ssh to connect to git

    I researched how to use git over ssh and found that I can use the command `git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo` to clone the repository. (using localhost if you get connected from the shell that you previously open in level 26)

    If you stablish the connection from your local machine, you need to use the IP address of the server instead of localhost (bandit.labs.overthewire.org).

    so it would look like this:

    `git clone ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo`

2. Clone the repository and provide the password for that Level.
3. Navigate into your clone repository, that will be automatically created when you clone it at /home/bandit27-git/repo, but you can also specify a different path when you clone it.

### Key takeaways

- Use git over ssh to clone repositories.
- Use the correct port when connecting to a service.
- Navigate into cloned repositories to find files and information.