# 06 - Git Part 2a: Remotes (Manual Walkthrough)

**In this section, you'll learn how to connect your local git project to GitHub so you can back up your work, share it, and collaborate with others.** We'll take the to-do list project you've been building and put it online.

---

## The Big Picture

So far, git has been tracking your files only on your computer. Everything — your snapshots, your timeline, your files — lives on your machine alone. If your computer breaks, it's all gone.

A **remote** is a copy of your project stored on another computer (like a server on the internet). This gives you three superpowers:

- **Backup:** Your work is safe even if your laptop breaks
- **Sharing:** Others can see your project
- **Collaboration:** Multiple people can work on the same project

**GitHub.com** is a website that hosts git remotes. Think of it as a social media site for code projects — you can browse other people's projects, share your own, and work together.

> **Reference:** [Pro Git — Working with Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)

---

## 1. Quick Tour of GitHub.com

Open your browser and go to [github.com](https://github.com).

If you're logged in, you'll see your dashboard. Let's look at what a repository (project) looks like on GitHub. Visit a well-known repo like:

```
https://github.com/torvalds/linux
```

**What you'll see:**

| Part | What it shows |
|------|---------------|
| File list | All the files in the project, just like a folder on your computer |
| Commits | The snapshot history (same as `git log`) |
| README | A description of the project, rendered nicely at the bottom of the page |
| Green "Code" button | How to download or clone the project |

> **Key point:** A GitHub repository is just a git project hosted on the internet. It has the same snapshots, the same timeline, and the same files as a local git project. GitHub adds a nice web interface on top.

---

## 2. Create a New Repository on GitHub

Now let's create a place on GitHub to store your to-do list project.

**Step 1:** Go to [github.com](https://github.com) and click the **"+"** button in the top-right corner, then select **"New repository"**.

**Step 2:** Fill in the details:

| Field | What to enter |
|-------|---------------|
| Repository name | `my-workshop-demo` |
| Description | (optional) "My personal to-do list" |
| Visibility | Public or Private — your choice |
| Initialize this repository | **Do NOT** check any boxes (no README, no .gitignore, no license) |

> **Why no README?** You already have files in your local project. If GitHub creates files too, you'll have a conflict. We want an empty repository that we can push our existing work into.

> **Reference:** [GitHub Docs — Creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)

**Step 3:** Click **"Create repository"**.

**Step 4:** You'll see a setup page. Find the section that says **"...or push an existing repository from the command line"**. Copy the SSH URL — it looks like:

```
git@github.com:USERNAME/my-workshop-demo.git
```

> **Note:** Replace `USERNAME` with your actual GitHub username. If you see an HTTPS URL instead (starting with `https://`), click the "SSH" button to switch.

---

## 3. Connect Your Local Repo to GitHub

Open iTerm2 and navigate to your demo repo folder:

```bash
cd ~/workshop/git-cli-workshop-demo
```

Now tell git where your remote is:

```bash
git remote add origin git@github.com:USERNAME/my-workshop-demo.git
```

**What this means:**

| Part | Meaning |
|------|---------|
| `git remote add` | "Add a new remote connection" |
| `origin` | A nickname for this remote (like a contact name in your phone) |
| `git@github.com:USERNAME/...` | The actual address of the remote (like a phone number) |

> **Why "origin"?** It's a convention — the default name for the main remote. You could name it anything, but `origin` is what everyone uses.

**Verify it worked:**

```bash
git remote -v
```

**Expected output:**

```
origin	git@github.com:USERNAME/my-workshop-demo.git (fetch)
origin	git@github.com:USERNAME/my-workshop-demo.git (push)
```

**What this means:** You have a remote called `origin` with two directions — `fetch` (downloading) and `push` (uploading). Both point to your GitHub repo.

> **Reference:** [git-remote documentation](https://git-scm.com/docs/git-remote)

---

## 4. Push Your Commits to GitHub

Now let's upload your local snapshots to GitHub:

```bash
git push -u origin main
```

**What each part means:**

| Part | Meaning |
|------|---------|
| `git push` | "Upload my commits to the remote" |
| `-u` | "Remember this connection" (so next time you can just type `git push`) |
| `origin` | Which remote to push to (the GitHub one we just added) |
| `main` | Which branch to push (your main timeline) |

**Expected output:**

```
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (9/9), 789 bytes | 789.00 KiB/s, done.
Total 9 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To github.com:USERNAME/my-workshop-demo.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

**Verify it worked:**

1. Go back to your browser
2. Refresh your GitHub repository page (`github.com/USERNAME/my-workshop-demo`)
3. You should see your files — `TODO.md`, `GOALS.md`, `SANDBOX.md` (and any other files you created)

> **What just happened:** All your local snapshots are now copied to GitHub. Anyone with the link can see your project (if it's public). Your commit history is there too — click "commits" on GitHub to see it.

> **Reference:** [git-push documentation](https://git-scm.com/docs/git-push)

---

## 5. Make a Change, Commit, Push

Now let's practice the full workflow: edit locally, commit, then push to GitHub.

**Step 1:** In VSCode, open `TODO.md` and add a new item:

```markdown
# My To-Do List

## Today
- [x] Buy groceries
- [ ] Reply to emails
- [ ] Read a book
- [ ] Push my project to GitHub

## Notes
Here are some things I want to remember...
```

Save with `Cmd+S`.

**Step 2:** Stage and commit:

```bash
git add TODO.md
git commit -m "Add GitHub task to to-do list"
```

**Expected output:**

```
[main abc1234] Add GitHub task to to-do list
 1 file changed, 1 insertion(+)
```

**Step 3:** Push to GitHub:

```bash
git push
```

**What happens:** Because you used `-u` the first time, git remembers where to push. You no longer need to type `origin main`.

**Expected output:**

```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 312 bytes | 312.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:USERNAME/my-workshop-demo.git
   def5678..abc1234  main -> main
```

**Verify it worked:** Refresh your GitHub page. Click on `TODO.md` — you should see the new "Push my project to GitHub" item. Click "commits" to see your latest commit message.

---

## 6. Pull Changes from GitHub

Sometimes changes happen on GitHub that you don't have locally. This could be because:

- You (or a collaborator) edited a file directly on GitHub's website
- A collaborator pushed changes from their computer
- You worked on a different computer and pushed from there

Let's simulate this by editing a file directly on GitHub.

**Step 1: Edit a file on GitHub.com**

1. Go to your repository on GitHub (`github.com/USERNAME/my-workshop-demo`)
2. Click on `TODO.md`
3. Click the **pencil icon** (edit button) in the top-right of the file view
4. Add a new item to the list:

```markdown
- [ ] Learn about git remotes
```

5. Scroll down to "Commit changes"
6. Type a commit message: `Add remotes task from GitHub`
7. Click **"Commit changes"**

> **Reference:** [GitHub Docs — Editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)

**Step 2: Check your local file**

Go back to iTerm2 and look at `TODO.md`:

```bash
git log --oneline
```

**What you'll see:** Your local log does NOT have the commit you just made on GitHub. Your local copy is behind.

**Step 3: Pull the changes**

```bash
git pull
```

**Expected output:**

```
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:USERNAME/my-workshop-demo
   abc1234..ghi7890  main       -> origin/main
Updating abc1234..ghi7890
Fast-forward
 TODO.md | 1 +
 1 file changed, 1 insertion(+)
```

**Step 4: Verify**

```bash
git log --oneline
```

**What you'll see:** The commit you made on GitHub now appears in your local history.

Open `TODO.md` in VSCode — the "Learn about git remotes" item is there.

**What happened:** `git pull` downloaded the new snapshot(s) from GitHub and updated your local files. Your local copy is now in sync with GitHub.

> **Reference:** [git-pull documentation](https://git-scm.com/docs/git-pull)

---

## 7. The Push/Pull Workflow

Here's the pattern you'll use every day:

```
[Your Computer]  ---push--->  [GitHub]  <---push---  [Other Computer]
[Your Computer]  <---pull---  [GitHub]  ---pull--->  [Other Computer]
```

1. **You make changes locally** → commit → `git push` → changes appear on GitHub
2. **Changes happen on GitHub** → `git pull` → changes appear on your computer

> **Good habit:** Always `git pull` before you start working. This ensures you have the latest changes, especially if you're collaborating with others.

---

## Quick Reference

Here's a summary of the new commands you learned:

| Command | What it does |
|---------|-------------|
| `git remote add origin <URL>` | Connect your local repo to a GitHub repo |
| `git remote -v` | See which remotes are connected |
| `git push -u origin main` | Upload commits to GitHub (first time) |
| `git push` | Upload commits to GitHub (after first time) |
| `git pull` | Download commits from GitHub |

And the complete workflow:

| Step | Command |
|------|---------|
| 1. Make changes | (edit files in VSCode) |
| 2. Check status | `git status` |
| 3. Stage | `git add <file>` |
| 4. Commit | `git commit -m "message"` |
| 5. Push | `git push` |

---

Great work! Your project now lives in two places — your computer and GitHub. In the next section, you'll learn how to do all of this by talking to an AI instead of typing commands.
