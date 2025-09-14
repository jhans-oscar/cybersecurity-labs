# OverTheWire Bandit - Level 30

**Goal:** Retrieve the password for level 31.

## Step-by-step walkthrough

1. Connect to the level via SSH:

    ```bash
    ssh bandit30@bandit.labs.overthewire.org -p 2220
    ```

2. Create a working directory and clone the repository:

    ```bash
    mkdir -p bandit30 && cd bandit30
    git clone <repo-url>
    cd <repo-directory>
    ```

3. Do the usual checks (files, git history, branches/tags):

    ```bash
    ls -la
    git status
    git log --oneline --decorate --all
    git tag -l
    ```

4. You’ll notice a tag called `secret`. Show its contents:

    ```bash
    git show secret
    ```

5. The output of `git show secret` contains the password for level 31.

### Key takeaways

- Use `git tag -l` to list all tags in the repository.
- Use `git show <tag-name>` to view the contents of a specific tag.
