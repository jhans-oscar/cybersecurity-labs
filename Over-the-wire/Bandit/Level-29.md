# OverTheWire Bandit - Level 29

**Goal:** Retrieve the password for level 30.

## Step-by-step walkthrough

1. Connect to the level (example):
    - `ssh bandit29@bandit.labs.overthewire.org -p 2220`

2. Prepare a workspace:
    - `mkdir -p /tmp/jhans29`
    - `cd /tmp/jhans29`

3. Clone the repository you found:
    - `git clone <repository-ssh-or-https-url>`
    - `cd <repo-directory>`

4. Quickly inspect visible files:
    - `cat README.md`  — the README was empty in this case.

5. Check the commit history:
    - `git log`  — showed nothing useful.

6. Inspect branches:
    - `git branch`  — showed only the current local branch.
    - `git branch -a`  — listed additional remote branches (this revealed more branches).

7. Switch to the development branch:
    - `git checkout dev`

8. Inspect files on the dev branch:
    - `ls -la`
    - `cat README.md` (or open the file you find that looks like the password)

9. Result:
    - The password for level 30 was found on the dev branch after checking out that branch.

## Key takeaways

- Use `git branch -a` to discover all branches, including remote ones.
- Use `git checkout <branch-name>` to switch to a different branch.
- Password for level 30: `qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL`
