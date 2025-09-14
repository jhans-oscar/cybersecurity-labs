# OverTheWire Bandit - Level 31

**Goal:** Retrieve the password for level 32.

## Step-by-step walkthrough

1. Connect to the Bandit server over SSH as the level 31 user.
    - Purpose: get an interactive shell on the challenge host.

2. Create a working directory in /tmp and change into it.
    - Command: `mkdir -p /tmp/xzc31 && cd /tmp/xzc31`
    - Purpose: use a writable, ephemeral workspace so you don't clutter your home.

3. Clone the Git repository provided by the challenge.
    - Command: `git clone <repo-url>`
    - Purpose: retrieve the remote project that expects you to add a file.

4. Prepare the file the repo asked for (key.txt).
    - Example: `echo "May I come in?" > key.txt`
    - Purpose: create the file to be tracked and pushed.

5. Attempt to add the file to the index.
    - Command: `git add key.txt`
    - What happened: git refused to add the file because the repository had a `.gitignore` entry that excluded `*.txt`.

6. Inspect the `.gitignore` to confirm the exclusion.
    - Command: `cat .gitignore`
    - Explanation: the line `*.txt` prevents any `.txt` files from being tracked, so `git add` silently ignores them.

7. Remove the `.gitignore` or alternatively edit it.
    - Command: `rm .gitignoriie`

8. Add the key file now that it is no longer ignored.
    - Command: `git add key.txt`

9. Check the repo status to verify changes.
    - Command: `git status`
    - Purpose: confirm `key.txt` is staged and there are no other unexpected changes.

10. Commit and push the change to the remote repository.
     - Commands:
        - `git commit -m "Add key.txt"`
        - `git push`
     - Purpose: upload the new file so the challenge can detect the submission.

11. Verify the push succeeded and cleanup.
     - Command: `git log -1` or check remote repo via web/ssh.
     - Optional cleanup: remove the temporary directory if desired `cd / && rm -rf /tmp/xzc31`

### Key takeaways

- `.gitignore` can prevent files from being added; inspect it if `git add` doesn't work as expected.
- Removing or modifying `.gitignore` allows you to track previously ignored files.
- Always verify your changes with `git status` before committing and pushing.
- Password for level 32: `3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K`
