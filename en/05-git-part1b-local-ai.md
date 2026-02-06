# 05 - Git Part 1b: Local Git with AI

**In this section, you'll redo the same local git operations — but by talking to an AI instead of typing commands.** Now that you understand what each git command does, you can let the AI handle the syntax while you focus on what you want to accomplish.

---

## 1. Introduction

In the previous section, you typed every git command by hand. That's valuable — you now understand what staging, committing, and diffing actually mean.

But here's the thing: you don't need to memorize those commands. You can describe what you want in plain English, and an LLM CLI tool will figure out the right commands for you.

The key insight is this: **understanding the concepts matters more than memorizing the syntax.** If you know what "staging" means, you can tell an AI "stage my changes" and it will run `git add` for you. If you know what a "commit" is, you can say "save a snapshot" and the AI knows what to do.

---

## 2. Starting Your LLM CLI Tool

Open iTerm2, navigate to your `git-cli-workshop-demo` folder (the one you used in Part 1a), and launch your tool:

```bash
cd ~/workshop/git-cli-workshop-demo
```

Then start whichever tool you installed:

| Tool | Command |
|------|---------|
| Claude Code | `claude` |
| Codex | `codex` |
| Gemini CLI | `gemini` |

**What happens:** The AI starts a conversation in your terminal. You can now type natural language instead of commands.

> **Tip:** Make sure you're inside the `git-cli-workshop-demo` folder before starting the tool. The AI works with the files in your current folder.

> **References:**
> - [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Anthropic's agentic coding tool
> - [Codex CLI](https://developers.openai.com/codex/cli/) — OpenAI's terminal-based coding agent
> - [Gemini CLI](https://github.com/google-gemini/gemini-cli) — Google's open-source AI agent for the terminal

---

## 3. Example Prompts Mapped to Git Commands

Here's how natural language maps to the commands you learned:

| What you want | What you say to the AI | What it does (git command) |
|---|---|---|
| Start tracking this folder | "Initialize a git repo here" | `git init` |
| Set your identity | "Set my git name to Jane and email to jane@example.com" | `git config user.name` + `git config user.email` |
| See what changed | "Show me what files I've changed" | `git status`, `git diff` |
| Stage a file | "Stage TODO.md for commit" | `git add TODO.md` |
| Save my work | "Commit my changes with message 'update to-do list'" | `git add` + `git commit` |
| View my history | "Show me the commit history" | `git log` |
| Undo my changes | "Undo my changes to TODO.md" | `git restore TODO.md` |
| See a compact history | "Show me a short one-line commit log" | `git log --oneline` |

> **Note:** You don't have to use these exact phrases. The AI understands natural language, so "what's changed?", "any modified files?", and "show me the status" all work.

---

## 4. Guided Practice

Let's redo the to-do list scenario from Part 1a, but this time using your LLM CLI tool.

### Step 1: Check the current state

Type something like:

> "Show me the current git status and commit history"

The AI will run `git status` and `git log` and show you the results.

### Step 2: Create a new file

In VSCode, create a new file called `GOALS.md` with this content:

```markdown
# My Goals

## This Week
- [ ] Learn git basics
- [ ] Practice using the terminal
- [ ] Try an LLM CLI tool
```

Save it with `Cmd+S`.

### Step 3: Ask the AI what changed

> "What files have I changed or added?"

The AI should show you that `GOALS.md` is a new untracked file.

### Step 4: Stage and commit

> "Commit the new GOALS.md file with the message 'Add weekly goals'"

The AI will stage the file and create a commit for you.

### Step 5: Make edits

Edit `GOALS.md` in VSCode — check off "Learn git basics" and add a new goal:

```markdown
# My Goals

## This Week
- [x] Learn git basics
- [ ] Practice using the terminal
- [ ] Try an LLM CLI tool
- [ ] Build something fun
```

Save with `Cmd+S`.

### Step 6: Review and commit the changes

> "Show me what I changed, then commit it with message 'Check off git basics, add new goal'"

The AI will show you the diff and then commit.

### Step 7: View the timeline

> "Show me all my commits"

You should see your full history — both the commits you made by hand in Part 1a and the ones the AI just made.

### Step 8: Practice undo

Delete all the content in `GOALS.md` (select all, delete, save). Then:

> "I made a mistake — restore GOALS.md to the last committed version"

The AI will recover your file.

---

## 5. Key Insight

Notice what just happened: you did the exact same git operations as Part 1a — init, status, add, commit, log, diff, restore — but you never had to remember the commands.

**You need to understand the concepts:**

- **Staging** = choosing what goes into the next snapshot
- **Committing** = taking the snapshot
- **Diffing** = seeing what changed
- **Restoring** = undoing uncommitted changes

Once you understand these ideas, you can express what you want in plain language. The AI translates your intent into the right git commands.

This is a general pattern that applies far beyond git: **learn the concepts, then let the AI handle the syntax.**

---

## 6. When to Use Commands vs. AI

Both approaches are valid. Here's a rough guide:

| Situation | Recommended approach |
|-----------|---------------------|
| Quick, simple operations (`git status`, `git log`) | Type the command directly — it's faster |
| Complex operations you don't remember | Ask the AI |
| Learning something new | Ask the AI to explain what it's doing |
| Repetitive workflows | Ask the AI to do the whole sequence |
| When you're unsure what to do next | Ask the AI for guidance |

> **Tip:** You can always ask the AI "what git command would you use for this?" if you want to learn the syntax without having it run the command.

---

You've now completed the local git section — both the manual way and the AI way. Next, we'll learn how to share your work with others using GitHub.
