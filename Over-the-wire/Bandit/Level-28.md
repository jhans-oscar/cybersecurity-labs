# OverTheWire Bandit - Level 28

**Goal:** Retrieve the password for level 29.

for this level i need to keep using git commands to get the password.

## Steps taken

1. SSH into the Bandit host (port 2220):
    - `ssh bandit28@bandit.labs.overthewire.org -p 2220`

2. Create a temporary working directory and enter it:
    - `mkdir -p /tmp/jhans1`
    - `cd /tmp/jhans1`

3. Clone the Git repository over SSH specifying port 2220 (example form):
    - `git clone ssh://bandit28@bandit.labs.overthewire.org:2220/<repository>`

4. Inspect the repository contents; the README did not contain the password:
    - `ls -la`
    - `cat README`

5. View the commit history to find earlier changes:
    - `git log --oneline`

6. Checkout a specific commit to inspect its state:
    - `git checkout <commit-hash>`

7. Read the files at that commit (repeat with other commits as needed):
    - `ls -la`
    - `cat README` (or other relevant files)

8. After checking the second commit, the password for level 29 was found in the checked-out files.

9. (Optional) Return to the default branch when finished:
    - `git checkout master` or `git checkout main`

### Key takeaways
- Use `git log` to explore commit history.
- Use `git checkout <commit-hash>` to view the repository at a specific commit.
- Password for level 29: `4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7`
