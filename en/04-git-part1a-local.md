# 04 - Git Part 1a: Local Git (Manual Walkthrough)

**In this section, you'll learn how to use git to track changes to your files on your own computer.** We'll build a personal to-do list and practice every core git command along the way.

---

## What Is Git?

Git is a **timeline manager** for your files. It takes **snapshots** (called "commits") of your project at moments you choose. You can look back at any snapshot, see exactly what changed, and undo mistakes.

Think of it like version history in Google Docs — but for any files, not just documents, and much more powerful:

- **Snapshot:** A saved point in time for your entire project
- **Timeline:** The sequence of all your snapshots
- **You decide** when to take each snapshot and what to include

Let's try it.

---

## 1. Create a Project Folder and Initialize Git

Open iTerm2 and type:

```bash
mkdir my-todo-list
cd my-todo-list
git init
```

**What happens:** You create a new folder, move into it, and tell git to start watching it.

**Expected output (from `git init`):**

```
Initialized empty Git repository in /Users/yourname/my-todo-list/.git/
```

**Verify it worked:**

```bash
ls -la
```

**Expected output:** You should see a `.git` folder in the list. (The `-la` flag shows hidden files — ones starting with `.`.)

```
total 0
drwxr-xr-x   3 yourname  staff   96 Jan  1 10:00 .
drwxr-xr-x   5 yourname  staff  160 Jan  1 10:00 ..
drwxr-xr-x   9 yourname  staff  288 Jan  1 10:00 .git
```

> **What's that `.git` folder?** It's where git stores all its data — your snapshots, your timeline, everything. You never need to look inside it. Just know that if this folder exists, git is active in this project.

---

## 2. Configure Your Git Identity

Git tags every snapshot with your name and email. Let's set those up:

```bash
git config user.name "Your Name"
git config user.email "your@email.com"
```

**What happens:** No output (that's normal). Git stores these settings for this project.

**Verify it worked:**

```bash
git config user.name
git config user.email
```

**Expected output:** Your name and email printed back to you.

> **Note:** Replace `"Your Name"` and `"your@email.com"` with your actual name and the email you used for your GitHub account.

---

## 3. Create Your First File

Open the project in VSCode:

```bash
code .
```

In VSCode:
1. Hover over the sidebar and click the "New File" icon
2. Name the file `TODO.md`
3. Type the following content:

```markdown
# My To-Do List

## Today
- [ ] Buy groceries
- [ ] Reply to emails
```

4. Press `Cmd+S` to save

**What you just wrote:** This is markdown syntax. `#` makes a heading, `##` makes a smaller heading, and `- [ ]` creates a checkbox item. Press `Cmd+Shift+V` in VSCode to see it rendered nicely.

---

## 4. Check Status

Go back to iTerm2 and type:

```bash
git status
```

**Expected output:**

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	TODO.md

nothing added to commit but untracked files present (use "git add" to track)
```

**What this means:** Git sees `TODO.md` in red (untracked). That means git knows the file exists but isn't tracking it yet. It's like putting a document on your desk — it's there, but you haven't filed it.

---

## 5. Stage the File

"Staging" means telling git which files to include in the next snapshot. Think of it as placing files into a "snapshot basket."

```bash
git add TODO.md
```

**Expected output:** No output (that's normal).

**Verify it worked:**

```bash
git status
```

**Expected output:**

```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   TODO.md
```

**What this means:** `TODO.md` is now in green (staged). It's in the snapshot basket, ready to be saved.

---

## 6. Take the Snapshot (Commit)

Now let's take the actual snapshot:

```bash
git commit -m "Add initial to-do list"
```

**What `-m` means:** The `-m` flag lets you attach a short message describing what this snapshot contains. Always write something meaningful — future you will thank you.

**Expected output:**

```
[main (root-commit) abc1234] Add initial to-do list
 1 file changed, 5 insertions(+)
 create mode 100644 TODO.md
```

**Verify it worked:**

```bash
git status
```

**Expected output:**

```
On branch main
nothing to commit, working tree clean
```

**What "clean working tree" means:** Everything in your project matches the latest snapshot. There are no unsaved changes.

---

## 7. View Your Timeline

```bash
git log
```

**Expected output:**

```
commit abc1234567890abcdef1234567890abcdef123456 (HEAD -> main)
Author: Your Name <your@email.com>
Date:   Wed Jan 1 10:05:00 2025 +0900

    Add initial to-do list
```

**What each part means:**

| Part | Meaning |
|------|---------|
| `commit abc123...` | The unique ID of this snapshot (a long code called a "hash") |
| `HEAD -> main` | This is the latest snapshot on the `main` branch (we'll cover branches later) |
| `Author` | Who made this snapshot (the name/email you configured) |
| `Date` | When the snapshot was taken |
| `Add initial to-do list` | The message you wrote with `-m` |

> **Tip:** Press `q` to exit the log view if it fills up your screen.

---

## 8. Make Changes

Go back to VSCode and edit `TODO.md`. Check off a task, add a new one, and add a Notes section:

```markdown
# My To-Do List

## Today
- [x] Buy groceries
- [ ] Reply to emails
- [ ] Read a book

## Notes
Here are some things I want to remember...
```

Press `Cmd+S` to save.

**What changed:** You checked off "Buy groceries" (changed `[ ]` to `[x]`), added "Read a book", and added a new "Notes" section.

---

## 9. See What Changed

```bash
git diff
```

**Expected output:**

```diff
diff --git a/TODO.md b/TODO.md
index abc1234..def5678 100644
--- a/TODO.md
+++ b/TODO.md
@@ -1,5 +1,9 @@
 # My To-Do List

 ## Today
-- [ ] Buy groceries
+- [x] Buy groceries
 - [ ] Reply to emails
+- [ ] Read a book
+
+## Notes
+Here are some things I want to remember...
```

**How to read this:**

| Symbol | Meaning |
|--------|---------|
| Lines starting with `-` (red) | Content that was removed or changed |
| Lines starting with `+` (green) | Content that was added or changed to |
| Lines with no symbol | Context — unchanged lines around the changes |

So you can see: the checkbox changed from `[ ]` to `[x]`, a new item was added, and the Notes section is new.

> **Tip:** Press `q` to exit the diff view.

---

## 10. Stage and Commit Again

```bash
git add TODO.md
git commit -m "Check off groceries, add reading and notes"
```

**Expected output:**

```
[main def5678] Check off groceries, add reading and notes
 1 file changed, 6 insertions(+), 1 deletion(-)
```

---

## 11. View the Timeline with Two Snapshots

```bash
git log
```

**Expected output:**

```
commit def5678901234567890abcdef1234567890abcdef (HEAD -> main)
Author: Your Name <your@email.com>
Date:   Wed Jan 1 10:15:00 2025 +0900

    Check off groceries, add reading and notes

commit abc1234567890abcdef1234567890abcdef123456
Author: Your Name <your@email.com>
Date:   Wed Jan 1 10:05:00 2025 +0900

    Add initial to-do list
```

**What you're seeing:** Your timeline now has two snapshots, newest first. You can see exactly when each change was made and what it was about.

> **Tip:** For a more compact view, try `git log --oneline`:
>
> ```
> def5678 Check off groceries, add reading and notes
> abc1234 Add initial to-do list
> ```

---

## 12. Undo a Change

Let's practice recovering from a mistake.

**Step 1: Make a bad edit.** Go to VSCode, select all the text in `TODO.md` (press `Cmd+A`), delete it, and save (`Cmd+S`). The file is now empty.

**Step 2: See the damage:**

```bash
git status
```

**Expected output:**

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   TODO.md
```

```bash
git diff
```

**Expected output:** All your content shows in red (deleted).

**Step 3: Restore the file from the last snapshot:**

```bash
git restore TODO.md
```

**Expected output:** No output.

**Step 4: Verify the recovery:**

Open `TODO.md` in VSCode — all your content is back! You can also verify in the terminal:

```bash
git status
```

**Expected output:**

```
On branch main
nothing to commit, working tree clean
```

**What happened:** You told git "throw away my current changes to this file and go back to the version from the last snapshot." This is one of git's superpowers — you can always get back to any saved snapshot.

> **Note:** `git restore` only works for changes that haven't been committed yet. Once you've committed something, it becomes part of your timeline (and you'd need different commands to undo it — we'll cover that later).

---

## 13. Freeform Practice

You now know all the essential local git commands. Take 5-10 minutes to practice on your own:

1. In VSCode, create a new file called `SANDBOX.md`
2. Write whatever you want in it — notes, a story, a recipe, anything
3. Practice the workflow:
   - `git status` — see what changed
   - `git add SANDBOX.md` — stage it
   - `git commit -m "your message here"` — take a snapshot
   - `git log` — view your timeline
4. Make more changes, then use `git diff` to see them before committing
5. Try making a bad edit and recovering with `git restore`

---

## Quick Reference

Here's a summary of every command you learned:

| Command | What it does |
|---------|-------------|
| `git init` | Start tracking a folder with git |
| `git config user.name "..."` | Set your name for commits |
| `git config user.email "..."` | Set your email for commits |
| `git status` | See what files have changed |
| `git add <file>` | Stage a file for the next snapshot |
| `git commit -m "message"` | Take a snapshot with a description |
| `git log` | View your timeline of snapshots |
| `git diff` | See what changed since the last snapshot |
| `git restore <file>` | Undo changes to a file (back to last snapshot) |

---

Nice work! You now understand the core git workflow: **edit → status → add → commit → log**. In the next section, you'll see how to do all of this by talking to an AI instead of typing commands.

---

## References

Official documentation for each git command used in this section:

- [git init](https://git-scm.com/docs/git-init) — Create an empty Git repository
- [git config](https://git-scm.com/docs/git-config) — Get and set repository or global options
- [git status](https://git-scm.com/docs/git-status) — Show the working tree status
- [git add](https://git-scm.com/docs/git-add) — Add file contents to the index (staging area)
- [git commit](https://git-scm.com/docs/git-commit) — Record changes to the repository
- [git log](https://git-scm.com/docs/git-log) — Show commit logs
- [git diff](https://git-scm.com/docs/git-diff) — Show changes between commits, commit and working tree, etc.
- [git restore](https://git-scm.com/docs/git-restore) — Restore working tree files
- [First-Time Git Setup (Pro Git Book)](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) — Initial configuration walkthrough
