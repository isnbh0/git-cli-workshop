# 08 - Git Part 3a: Branches (Manual Walkthrough)

**In this section, you'll learn how to use branches to work on new ideas without affecting your main project.** This is a stretch goal — if you've made it this far, you're doing great!

---

## What Are Branches?

Think of branches as **parallel timelines**. Your `main` branch is your primary timeline — the "official" version of your project. When you create a new branch, you're starting an alternate timeline where you can experiment freely.

- **If you like the result:** you merge it back into your main timeline
- **If you don't like it:** you throw the branch away, and your main timeline is untouched
- **This is how teams work:** each person works on their own branch, then merges when ready

Here's a visual:

```
main:        A --- B --- C
                         \
experiment:               D --- E
```

Commits A, B, C are on `main`. When you create a branch called `experiment`, commits D and E happen only on that branch. `main` stays exactly as it was.

> **Reference:** [Pro Git — Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

---

## 1. See Your Current Branch

Open iTerm2 and navigate to your `my-todo-list` folder:

```bash
cd my-todo-list
```

Check which branch you're on:

```bash
git branch
```

**Expected output:**

```
* main
```

**What this means:** The `*` shows your current branch. Right now you only have one branch: `main`.

---

## 2. Create a New Branch

Let's create a branch called `experiment`:

```bash
git branch experiment
```

**Expected output:** No output (that's normal).

**Verify it worked:**

```bash
git branch
```

**Expected output:**

```
  experiment
* main
```

**What this means:** You now have two branches. The `*` is still on `main` — you created the branch but haven't switched to it yet.

> **Reference:** [git-branch documentation](https://git-scm.com/docs/git-branch)

---

## 3. Switch to the New Branch

```bash
git switch experiment
```

**Expected output:**

```
Switched to branch 'experiment'
```

**Verify it worked:**

```bash
git branch
```

**Expected output:**

```
* experiment
  main
```

**What this means:** The `*` is now on `experiment`. Any changes you make and commit will go on this branch, not on `main`.

> **Shortcut:** You can create and switch to a new branch in one step with `git switch -c experiment` (or the older `git checkout -b experiment`). The `-c` flag means "create."

> **Reference:** [git-switch documentation](https://git-scm.com/docs/git-switch)

---

## 4. Make Changes on the Branch

In VSCode, open `TODO.md` and add a new section:

```markdown
# My To-Do List

## Today
- [x] Buy groceries
- [ ] Reply to emails
- [ ] Read a book

## Notes
Here are some things I want to remember...

## Stretch Goals
- [ ] Learn about git branches
- [ ] Try a new recipe
```

Save with `Cmd+S`.

**What you're doing:** Adding a "Stretch Goals" section. This change only exists on the `experiment` branch.

---

## 5. Commit on the Branch

```bash
git add TODO.md
git commit -m "Add stretch goals section"
```

**Expected output:**

```
[experiment abc1234] Add stretch goals section
 1 file changed, 4 insertions(+)
```

**Verify it worked:**

```bash
git log --oneline
```

**Expected output:**

```
abc1234 (HEAD -> experiment) Add stretch goals section
def5678 (main) Check off groceries, add reading and notes
ghi7890 Add initial to-do list
```

**What this means:** The new commit is on `experiment` (shown by `HEAD -> experiment`). The `main` branch is still pointing to the previous commit.

---

## 6. Switch Back to Main

Now let's go back to `main` and see what happens:

```bash
git switch main
```

**Expected output:**

```
Switched to branch 'main'
```

**Now open `TODO.md` in VSCode.**

**What you'll see:** The "Stretch Goals" section is gone! The file looks like it did before your changes.

**Don't panic.** Your changes aren't lost — they're safely stored on the `experiment` branch. You're looking at the `main` timeline, where those changes don't exist yet.

**Verify:**

```bash
git log --oneline
```

**Expected output:**

```
def5678 (HEAD -> main) Check off groceries, add reading and notes
ghi7890 Add initial to-do list
```

The "Add stretch goals section" commit doesn't appear here — it's on the other branch.

---

## 7. Merge the Branch

You like the stretch goals section and want to bring it into `main`. While on the `main` branch:

```bash
git merge experiment
```

**Expected output:**

```
Updating def5678..abc1234
Fast-forward
 TODO.md | 4 ++++
 1 file changed, 4 insertions(+)
```

**What "fast-forward" means:** Since `main` didn't have any new commits while you were on `experiment`, git simply moved the `main` pointer forward. It's like catching up to where `experiment` already was.

**Verify it worked:**

Open `TODO.md` in VSCode — the "Stretch Goals" section is back!

```bash
git log --oneline
```

**Expected output:**

```
abc1234 (HEAD -> main, experiment) Add stretch goals section
def5678 Check off groceries, add reading and notes
ghi7890 Add initial to-do list
```

**What this means:** Both `main` and `experiment` now point to the same commit. The timelines have been reunited.

> **Reference:** [git-merge documentation](https://git-scm.com/docs/git-merge)

---

## 8. Delete the Branch

Now that `experiment` has been merged, you don't need it anymore:

```bash
git branch -d experiment
```

**Expected output:**

```
Deleted branch experiment (was abc1234).
```

**Verify it worked:**

```bash
git branch
```

**Expected output:**

```
* main
```

You're back to one branch. The commits from `experiment` are part of `main` now.

> **Note:** The `-d` flag is a "safe delete" — git won't let you delete a branch that hasn't been merged yet. If you really want to throw away an unmerged branch, use `-D` (capital D) instead.

---

## Quick Reference

Here's a summary of the branch commands you learned:

| Command | What it does |
|---------|-------------|
| `git branch` | List all branches (current one has `*`) |
| `git branch <name>` | Create a new branch |
| `git switch <name>` | Switch to a branch |
| `git switch -c <name>` | Create and switch to a new branch |
| `git merge <name>` | Merge a branch into the current branch |
| `git branch -d <name>` | Delete a merged branch |

---

Nice work! You now understand branching — one of git's most powerful features. In the next section, you'll see how to do all of this by talking to an AI instead of typing commands.
