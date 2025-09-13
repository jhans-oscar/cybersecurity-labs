# OverTheWire Bandit - Level 25

**Goal:** Retrieve the password for level 26.

The login shell for the user `bandit26` is not the usual `/bin/bash`. I needed to identify the shell and find a way to escape its restriction to read the password.

## Steps taken

1. Inspect the current directory on Bandit 25

   After logging into the Bandit 25 account, I found an SSH key in the home directory named `.bandit26.sshkey`.

2. First connection attempt

   I tried to connect using the key:

   ```bash
   ssh -i bandit26.sshkey bandit26@localhost -p 2220
   ```

   The connection opened briefly and then closed with:

   < Connection to localhost closed.>

   I downloaded the key to my machine to try again. (I initially saved it with the wrong name `.passkey` instead of `.sshkey`, which cost some time.)

3. Identify the login shell

   The system-wide account registry is `/etc/passwd`. I checked the entry for `bandit26`:

   ```bash
   cat /etc/passwd | grep 'bandit26'
   # bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
   ```

   The login program is `/usr/bin/showtext`.

4. Inspect `showtext`

   Viewing the script revealed:

   ```bash
   cat /usr/bin/showtext
   # exec more ~/text.txt
   # exit 0
   ```

   So the account's “shell” runs `more` on `~/text.txt`.

5. Escape the pager and retrieve the password

   On my machine I set the key to the required permissions and reconnected:

   ```bash
   chmod 600 bandit26.sshkey
   ssh -i bandit26.sshkey -p 2220 bandit26@bandit.labs.overthewire.org
   ```

   `more` occupies the terminal until the displayed content fits the window. By resizing the terminal and interacting with `more` I was able to trigger its visual mode and run an editor (pressing `v` opens `vim`). From there I navigated to `/etc/bandit_pass/bandit26` and retrieved the password for the next level.

### Key takeaways

- `/etc/passwd` shows the login program for each account.
- SSH keys require secure permissions (e.g., `chmod 600`) to be accepted.
- Terminal pagers and editors can sometimes be used to escape restricted shells.
- Understanding how login shells and file permissions behave is essential when working in restricted environments.
