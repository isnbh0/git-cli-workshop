# 09 - Git Part 3b: Branches with AI

**In this section, you'll redo the same branch operations — but by talking to an AI instead of typing commands.** Now that you understand what branches, switching, and merging mean, you can let the AI handle the syntax while you focus on what you want to accomplish.

---

## 1. Introduction

In the previous section, you typed every branch-related command by hand. You now understand that branches are parallel timelines, how to switch between them, and how to merge them back together.

Just like with local git and remotes, you don't need to memorize these commands. If you know what "merging" means, you can tell an AI "combine my experiment branch into main" and it will figure out the right command.

---

## 2. Example Prompts for Branch Operations

Here's how natural language maps to the branch commands you learned:

| What you want | What you say to the AI | What it does |
|---|---|---|
| Create a new branch | "Create a branch called experiment" | `git branch experiment` + `git switch experiment` |
| Switch branches | "Switch to the main branch" | `git switch main` |
| See all branches | "Show me all branches" | `git branch` |
| Merge a branch | "Merge experiment into main" | `git switch main` + `git merge experiment` |
| Delete a branch | "Delete the experiment branch" | `git branch -d experiment` |
| Create and switch at once | "Create a new branch called feature and switch to it" | `git switch -c feature` |
| See which branch I'm on | "Which branch am I on?" | `git branch` |

> **Note:** You don't have to use these exact phrases. "Make a new branch", "go to the main branch", and "combine experiment with main" all work.

---

## 3. Guided Practice

Let's redo the Part 3a scenario using your LLM CLI tool.

### Step 1: Start your LLM CLI tool

Open iTerm2, navigate to your `my-todo-list` folder, and launch your tool:

```bash
cd my-todo-list
```

Then start whichever tool you installed:

| Tool | Command |
|------|---------|
| Claude Code | `claude` |
| Codex | `codex` |
| Gemini CLI | `gemini` |

> **Reference:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) | [OpenAI Codex CLI](https://github.com/openai/codex) | [Gemini CLI](https://github.com/google-gemini/gemini-cli)

### Step 2: Check your branches

Type something like:

> "Show me all my branches and which one I'm on"

The AI will run `git branch` and show you the results.

### Step 3: Create and switch to a new branch

> "Create a new branch called experiment and switch to it"

The AI will run `git switch -c experiment` (or equivalent commands).

### Step 4: Make changes and commit

In VSCode, edit `TODO.md` — add a "Stretch Goals" section (or any new content you like). Save with `Cmd+S`. Then:

> "Commit my changes to TODO.md with message 'Add stretch goals section'"

The AI will stage and commit on the `experiment` branch.

### Step 5: Switch back to main

> "Switch back to the main branch"

The AI will run `git switch main`. Open `TODO.md` in VSCode — your changes are gone (they're on the other branch).

### Step 6: Merge the branch

> "Merge the experiment branch into main"

The AI will run `git merge experiment`. Open `TODO.md` — your changes are back!

### Step 7: Clean up

> "Delete the experiment branch"

The AI will run `git branch -d experiment`.

---

## 4. Key Insight

Notice the same pattern from Parts 1b and 2b: you did the exact same branch operations as Part 3a — branch, switch, merge, delete — but you never had to remember the commands.

**You need to understand the concepts:**

- **Branch** = a parallel timeline for your project
- **Switch** = moving between timelines
- **Merge** = combining one timeline into another
- **Delete** = cleaning up a branch you no longer need

Once you understand these ideas, you can express what you want in plain language. The AI translates your intent into the right git commands.

**Branches are where AI assistance really shines** because the commands can get tricky — especially when dealing with merge conflicts, rebasing, or managing multiple branches. Let the AI handle those details while you focus on the intent: "combine my work" or "start a new experiment."

---

## 5. Workshop Recap

Congratulations! You've completed all three parts of the git workshop. Here's everything you've learned:

### Part 1: Local Git

| Concept | What it means |
|---------|---------------|
| **Snapshot (commit)** | A saved point in time for your project |
| **Staging** | Choosing which files go into the next snapshot |
| **Timeline (log)** | The history of all your snapshots |
| **Diff** | Seeing exactly what changed |
| **Restore** | Undoing uncommitted changes |

### Part 2: Remotes

| Concept | What it means |
|---------|---------------|
| **Remote** | A copy of your project on another computer (like GitHub) |
| **Push** | Uploading your commits to the remote |
| **Pull** | Downloading commits from the remote |

### Part 3: Branches

| Concept | What it means |
|---------|---------------|
| **Branch** | A parallel timeline for experimentation |
| **Switch** | Moving between timelines |
| **Merge** | Combining timelines together |

### The Big Takeaway

You don't need to memorize every git command. What matters is understanding the concepts — snapshots, timelines, remotes, branches. Once you have the mental model, you can either type the commands yourself or ask an AI to do it for you.

**Learn the concepts. Let the AI handle the syntax.**

---

> **Reference:** [Pro Git Book](https://git-scm.com/book/en/v2) — a comprehensive free resource for continuing your git learning journey.

Great work completing this workshop! You now have a solid foundation in git — the tool that developers use every day to manage their code. Keep practicing, keep experimenting, and don't be afraid to ask your AI assistant for help.
