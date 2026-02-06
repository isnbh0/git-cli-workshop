# 07 - Git Part 2b: Remotes with AI

**In this section, you'll redo the same remote git operations — but by talking to an AI instead of typing commands.** Now that you understand what pushing, pulling, and remotes mean, you can let the AI handle the syntax while you focus on what you want to accomplish.

---

## 1. Introduction

In the previous section, you typed every remote-related git command by hand. You now understand what a remote is, how `push` uploads your work, and how `pull` downloads changes.

Just like with local git, you don't need to memorize these commands. If you know what "pushing" means, you can tell an AI "upload my changes to GitHub" and it will figure out the right command.

---

## 2. Example Prompts for Remote Operations

Here's how natural language maps to the remote commands you learned:

| What you want | What you say to the AI | What it does |
|---|---|---|
| Connect to GitHub | "Connect this repo to my GitHub repo at git@github.com:USERNAME/my-todo-list.git" | `git remote add origin <URL>` |
| See remote connections | "Show me which remotes are connected" | `git remote -v` |
| Upload my work | "Push my commits to GitHub" | `git push` |
| Upload for the first time | "Push my commits to GitHub and set up tracking" | `git push -u origin main` |
| Download latest changes | "Pull the latest changes from GitHub" | `git pull` |
| Create a GitHub repo | "Create a new GitHub repo called my-todo-list" | `gh repo create` |
| Check if I'm up to date | "Am I in sync with GitHub?" | `git status` + `git fetch` |

> **Note:** You don't have to use these exact phrases. "Upload my work", "send my changes to GitHub", and "push to origin" all work.

---

## 3. Guided Practice

Let's redo the Part 2a flow using your LLM CLI tool.

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

### Step 2: Check remote status

Type something like:

> "Show me the current git status and which remotes are connected"

The AI will run `git status` and `git remote -v` and show you the results.

### Step 3: Create a GitHub repo (if you haven't already)

If you want the AI to create the GitHub repo for you:

> "Create a new public GitHub repo called my-todo-list-ai and connect it to this local repo"

The AI will use `gh repo create` and `git remote add` to set everything up.

> **Note:** This uses the `gh` CLI tool (GitHub CLI) that you installed in the prerequisites section. If you already created a repo in Part 2a, you can skip this step or use a different repo name.

> **Reference:** [gh repo create — GitHub CLI manual](https://cli.github.com/manual/gh_repo_create)

### Step 4: Push your work

> "Push all my commits to GitHub"

The AI will run `git push` (or `git push -u origin main` if it's the first time).

### Step 5: Verify on GitHub

> "What's the URL of my GitHub repo?"

The AI will show you the URL. Open it in your browser to confirm your files are there.

### Step 6: Make a change and push

In VSCode, edit `TODO.md` — add a new item. Save with `Cmd+S`. Then:

> "Commit my changes to TODO.md with message 'Add new task' and push to GitHub"

The AI will stage, commit, and push in one go.

### Step 7: Pull changes

Edit a file on GitHub.com (using the web editor as you learned in Part 2a). Then:

> "Pull the latest changes from GitHub"

The AI will run `git pull` and your local files will be updated.

### Step 8: Check sync status

> "Am I up to date with GitHub? Show me if there are any differences."

The AI will check whether your local copy matches what's on GitHub.

---

## 4. Key Insight

Notice the same pattern from Part 1b: you did the exact same remote operations as Part 2a — remote add, push, pull — but you never had to remember the commands.

**You need to understand the concepts:**

- **Remote** = a copy of your project on another computer (like GitHub)
- **Origin** = the nickname for your main remote
- **Push** = uploading your local commits to the remote
- **Pull** = downloading remote commits to your local machine

Once you understand these ideas, you can express what you want in plain language. The AI translates your intent into the right git commands.

**This is especially useful for remote operations** because the commands can get complex — different flags for first push vs. subsequent pushes, SSH vs. HTTPS URLs, tracking branches, etc. Let the AI handle those details while you focus on the intent: "send my work to GitHub" or "get the latest changes."

---

## 5. When to Use Commands vs. AI

Building on the guide from Part 1b:

| Situation | Recommended approach |
|-----------|---------------------|
| Quick push/pull | Type `git push` or `git pull` directly — it's fast |
| Setting up a new remote for the first time | Ask the AI — the flags are easy to forget |
| Creating a GitHub repo from the terminal | Ask the AI — `gh repo create` has many options |
| Troubleshooting push/pull errors | Ask the AI — it can diagnose and fix issues |
| Checking if you're in sync | Ask the AI — it can combine multiple commands |

> **Tip:** If you get a push or pull error and don't understand it, paste the error message to the AI and ask "What does this mean and how do I fix it?"

---

You've now completed the remotes section — both the manual way and the AI way. You can back up your work, share it on GitHub, and collaborate with others. These are the foundations of working with git in the real world.
