# OverTheWire Bandit - Level 32 Final Level

**Goal:** Retrieve the password for level 33.

## Step-by-step walkthrough

1. SSH to the Bandit host as the level32 user:
    - ssh <bandit32@bandit.labs.overthewire.org> -p 2220

2. Run the challenge program provided in your home directory (the executable the level gives you). It will complain that everything must be uppercase and will not accept normal lowercase commands.

3. At the program prompt type the literal string:
    - $0
    Press Enter. This invokes an interactive shell from the running program.

4. From the spawned shell, display the next level's password:
    - cat /etc/bandit_pass/bandit33

5. Copy the password and use it to log into level 33.

Notes:

- The key trick is that typing "$0" at the program prompt yields a usable shell despite the uppercase restriction.

### Key takeaways

- Use `$0` at the program prompt to spawn a shell.
- Password for level 33: tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0
