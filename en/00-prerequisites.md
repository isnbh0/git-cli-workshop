# 00 - Prerequisites

**Please complete these steps before the workshop.** Each step includes installation instructions, expected output, and a verification command so you know it worked.

If you get stuck, take a screenshot of the error and send it to the instructor.

---

## 1. iTerm2

**What this is:** A terminal app for macOS. The terminal lets you control your computer by typing text commands instead of clicking.\
**Official source:** [iTerm2 Downloads](https://iterm2.com/downloads.html)

**Install:**

1. Go to [https://iterm2.com](https://iterm2.com)
2. Click "Download"
3. Open the downloaded file
4. Drag iTerm2 into your Applications folder

**Verify it worked:**

Open iTerm2 from your Applications folder (or use Spotlight: press `Cmd+Space`, type "iTerm", press Enter).

**Expected result:** A window appears with a text prompt, something like:

```
yourname@yourcomputer ~ %
```

> **Troubleshooting:** If macOS says the app "can't be opened because it is from an unidentified developer", go to System Settings → Privacy & Security → scroll down and click "Open Anyway".

---

## 2. Xcode Command Line Tools

**What this is:** A set of developer tools from Apple that many other tools depend on. You won't use these directly, but they're needed behind the scenes.\
**Official source:** [Installing the Command Line Tools — Apple Developer](https://developer.apple.com/documentation/xcode/installing-the-command-line-tools)

**Install:**

Open iTerm2 and type:

```bash
xcode-select --install
```

**What you'll see:** A popup asking you to install the tools. Click "Install" and wait (this can take 5-15 minutes).

**Verify it worked:**

```bash
xcode-select -p
```

**Expected result:**

```
/Library/Developer/CommandLineTools
```

> **Troubleshooting:** If you see "command line tools are already installed", that's fine — you're all set. If the install fails, try restarting your Mac and running the command again.

---

## 3. Homebrew

**What this is:** A package manager for macOS. It lets you install software from the terminal with a single command, like an app store for developer tools.\
**Official source:** [Homebrew](https://brew.sh)

**Install:**

Open iTerm2 and paste this command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**What you'll see:** A lot of text scrolling by. It will ask for your password (the one you use to log into your Mac). When you type the password, you won't see any characters appear — that's normal. Press Enter after typing it.

At the end of the install, Homebrew may display **"Next steps"** with commands to add brew to your PATH. **Follow those instructions** — copy and paste each command it shows you.

**Verify it worked:**

Close and reopen iTerm2, then type:

```bash
brew --version
```

**Expected result:**

```
Homebrew 4.x.x
```

> **Troubleshooting:** If you see "command not found: brew" after installing, you likely need to run the "Next steps" commands shown at the end of the installation. Look for lines starting with `eval` or `echo` — copy and run them.

---

## 4. uv

**What this is:** A Python package manager. We'll use it in future sessions for running Python scripts.\
**Official source:** [uv Installation — Astral Docs](https://docs.astral.sh/uv/getting-started/installation/)

**Install:**

```bash
brew install uv
```

**What you'll see:** Homebrew will download and install uv. This usually takes less than a minute.

**Verify it worked:**

```bash
uv --version
```

**Expected result:**

```
uv 0.x.x
```

---

## 5. Node.js

**What this is:** A JavaScript runtime. Many developer tools are built with JavaScript and need Node.js to run.\
**Official source:** [Download Node.js via Package Manager](https://nodejs.org/en/download/package-manager)

**Install:**

```bash
brew install node
```

**What you'll see:** Homebrew will download and install Node.js and npm (its package manager).

**Verify it worked:**

```bash
node --version
```

**Expected result:**

```
v22.x.x
```

(Any version 18 or higher is fine.)

---

## 6. Visual Studio Code

**What this is:** A text editor for writing and editing files. Think of it as a "multi-file notepad" — we'll use it to edit our files during the workshop.\
**Official source:** [Visual Studio Code on macOS](https://code.visualstudio.com/docs/setup/mac)

**Install:**

```bash
brew install --cask visual-studio-code
```

**Verify it worked:**

```bash
code --version
```

**Expected result:**

```
1.x.x
(some hash)
(some architecture)
```

> **Troubleshooting:** If you see "command not found: code", open Visual Studio Code manually (from Applications), then press `Cmd+Shift+P` to open the command palette, type "shell command", and select **"Shell Command: Install 'code' command in PATH"**. Close and reopen iTerm2, then try `code --version` again.

---

## 7. LLM CLI Tool (Pick One)

**What this is:** An AI assistant that runs in your terminal. You'll use it to perform git operations using natural language instead of memorizing commands.\
**Official sources:** [Claude Code Setup](https://docs.anthropic.com/en/docs/claude-code/setup) | [Codex CLI Quickstart](https://developers.openai.com/codex/quickstart) | [Gemini CLI Installation](https://geminicli.com/docs/get-started/installation/)

Pick **one** tool based on the subscription you already have:

### Option A: Claude Code (Anthropic)

**Requires:** Claude Max subscription or Anthropic API key

**Install:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Verify it worked:**

Close and reopen iTerm2, then:

```bash
claude --version
```

**First-time setup:** Run `claude` in your terminal and follow the prompts to sign in.

### Option B: Codex (OpenAI)

**Requires:** ChatGPT Plus/Pro subscription or OpenAI API key

**Install:**

```bash
brew install codex
```

**Verify it worked:**

```bash
codex --version
```

**First-time setup:** Run `codex` in your terminal and follow the prompts to sign in.

### Option C: Gemini CLI (Google)

**Requires:** Google account (free tier available)

**Install:**

```bash
brew install gemini-cli
```

**Verify it worked:**

```bash
gemini --version
```

**First-time setup:** Run `gemini` in your terminal and follow the prompts to authenticate.

---

## 8. iTerm2 Natural Text Editing

**What this is:** A keyboard setting that lets you use familiar shortcuts (like Option+Left/Right to move by word) in the terminal.\
**Official source:** [iTerm2 Keys Profiles Preferences](https://iterm2.com/documentation-preferences-profiles-keys.html)

**Setup:**

1. Open iTerm2
2. Go to **iTerm2 → Settings** (or press `Cmd+,`)
3. Click **Profiles** tab
4. Click **Keys** sub-tab
5. Click **Key Mappings** sub-tab
6. At the bottom, click the **Presets...** dropdown
7. Select **Natural Text Editing**

**Verify it worked:**

In iTerm2, type some text, then press `Option+Left` and `Option+Right`.

**Expected result:** Your cursor moves one word at a time (instead of printing special characters).

---

## 9. GitHub Account

**What this is:** GitHub is a website for storing and sharing code projects. We'll use it to upload your work during the workshop.\
**Official source:** [GitHub](https://github.com)

**Setup:**

1. Go to [https://github.com](https://github.com)
2. Click "Sign up"
3. Follow the steps to create an account
4. Remember your username and email — you'll need them during the workshop

**Verify it worked:** You can log in at [https://github.com](https://github.com) and see your dashboard.

---

## Final Checklist

Run each command below. If they all produce output (no errors), you're ready for the workshop!

```bash
xcode-select -p
brew --version
uv --version
node --version
code --version
```

Then verify your LLM CLI tool (whichever you installed):

```bash
claude --version   # if you chose Claude Code
codex --version    # if you chose Codex
gemini --version   # if you chose Gemini CLI
```

| Tool | Check |
|------|-------|
| iTerm2 | Opens and shows a prompt |
| Xcode Command Line Tools | `xcode-select -p` shows a path |
| Homebrew | `brew --version` shows a version |
| uv | `uv --version` shows a version |
| Node.js | `node --version` shows v18+ |
| Visual Studio Code | `code --version` shows a version |
| LLM CLI tool | Version command works |
| iTerm2 Natural Text Editing | Option+Arrow moves by word |
| GitHub account | Can log in at github.com |

All done? You're ready for the workshop!
