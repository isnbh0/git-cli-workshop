<!-- DO NOT EDIT — generated from .src/ by build.py -->

# 00 - Prerequisites

**Please complete these steps before the workshop.** Each step includes installation instructions, expected output, and a verification command so you know it worked.

If you get stuck, take a screenshot of the error and send it to the instructor.

This guide covers **native Windows** (not WSL). You will use **PowerShell** as your main terminal and **Git for Windows** for git.

---

## 0. Preflight: Check WinGet

**What this is:** WinGet is Windows' built-in package manager — the equivalent of Homebrew on macOS. It lets you install software with a single command.

Open PowerShell and check whether WinGet is available:

```powershell
winget --version
```

**Expected result:** A version number like `v1.x.x`.

> **If WinGet is missing:** Open the **Microsoft Store**, search for **App Installer**, and install or update it. Then close and reopen PowerShell.

---

## 1. Windows Terminal

**What this is:** A modern terminal app for Windows with tabs, split panes, and theme support. All subsequent steps should be run in PowerShell inside Windows Terminal.\
**Official source:** [Windows Terminal — Microsoft Store](https://aka.ms/terminal)

**Install:**

```powershell
winget install --id Microsoft.WindowsTerminal -e
```

**What you'll see:** WinGet downloads and installs Windows Terminal.

**Configure as default:**

Once installed, open Windows Terminal and set it up:

1. Click **∨** to the right of the tabs → **Settings**
2. Under **Startup**, set **Default terminal application** to `Windows Terminal`
3. Verify **Default profile** is set to `PowerShell`
4. Click **Save**

**Expected result:** From now on, opening a new terminal window automatically starts PowerShell in Windows Terminal.

---

## 2. PowerShell 7

**What this is:** The version of PowerShell included with Windows (5.1) is older. PowerShell 7 is the current version with better features and compatibility.\
**Official source:** [Installing PowerShell on Windows — Microsoft Docs](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows)

**Install:**

```powershell
winget install --id Microsoft.PowerShell -e
```

**After installing,** open Windows Terminal and set PowerShell 7 as the default:

1. Go to **∨** → **Settings** → **Startup** tab
2. Set **Default profile** to `PowerShell` (version 7). The entry named `Windows PowerShell` is version 5.1 — don't select that one.
3. Click **Save**

**Verify it worked:**

Open a new terminal tab, then:

```powershell
$PSVersionTable.PSVersion
```

**Expected result:** The `Major` value is `7` or higher.

---

## 3. Oh My Posh

**What this is:** A theme engine that customizes your PowerShell prompt — similar to Oh My Zsh on macOS. It also requires a Nerd Font for icons to display correctly.\
**Official source:** [Oh My Posh — Installation](https://ohmyposh.dev/docs/installation/windows)

**Install Oh My Posh:**

```powershell
winget install JanDeDobbeleer.OhMyPosh --source winget
```

Close the terminal window and open a new one, then install a Nerd Font:

```powershell
oh-my-posh font install CascadiaCode
```

**Apply the font in Windows Terminal:**

1. Go to **∨** → **Settings** → select the **PowerShell** profile on the left → **Appearance** tab
2. Change **Font face** to `CaskaydiaCove Nerd Font`
3. Click **Save**

**Add Oh My Posh to your PowerShell profile:**

Check whether your profile file exists:

```powershell
Test-Path $PROFILE
```

If the output is `False`, create it first:

```powershell
New-Item -Path $PROFILE -ItemType File -Force
```

Open the profile file:

```powershell
notepad $PROFILE
```

Add this line and save the file:

```powershell
oh-my-posh init pwsh | Invoke-Expression
```

Apply the profile immediately (or close and reopen the terminal):

```powershell
. $PROFILE
```

**Verify it worked:** Your prompt now shows icons and colors instead of the plain `PS C:\Users\name>`.

---

## 4. Git for Windows

**What this is:** The git version control system, packaged for Windows. It also includes Git Bash, which some tools use internally.\
**Official source:** [Git for Windows](https://gitforwindows.org)

**Install:**

```powershell
winget install --id Git.Git -e
```

**What you'll see:** WinGet downloads and installs Git for Windows.

**Verify it worked:**

Open a new terminal window, then:

```powershell
git --version
```

**Expected result:**

```
git version 2.x.x.windows.x
```

---

## 5. GitHub Account

**What this is:** GitHub is a website for storing and sharing code projects. We'll use it to upload your work during the workshop.\
**Official source:** [GitHub](https://github.com)

**Setup:**

1. Go to [https://github.com](https://github.com)
2. Click "Sign up"
3. Follow the steps to create an account
4. Remember your username and email — you'll need them during the workshop

**Verify it worked:** You can log in at [https://github.com](https://github.com) and see your dashboard.

---

## 6. GitHub CLI

**What this is:** The official GitHub command-line tool. It lets you create repos, manage issues, and authenticate with GitHub — directly from the terminal.\
**Official source:** [GitHub CLI](https://cli.github.com)

**Install:**

```powershell
winget install --id GitHub.cli
```

Open a new terminal window so the updated PATH is loaded, then verify:

```powershell
gh --version
```

**Expected result:**

```
gh version 2.x.x (20xx-xx-xx)
```

> **Note:** You'll authenticate `gh` with your GitHub account during the workshop (in the SSH and gh Setup section). No authentication needed now.

---

## 7. Visual Studio Code

**What this is:** A text editor for writing and editing files. Think of it as a "multi-file notepad" — we'll use it to edit our files during the workshop.\
**Official source:** [Visual Studio Code on Windows](https://code.visualstudio.com/docs/setup/windows)

**Install:**

```powershell
winget install --id Microsoft.VisualStudioCode -e
```

**Verify it worked:**

Open a new terminal, then:

```powershell
code --version
```

**Expected result:**

```
1.x.x
(some hash)
```

> **Troubleshooting:** If you see "command not found: code", open Visual Studio Code from the Start menu, press `Ctrl+Shift+P`, type "shell command", and select **"Shell Command: Install 'code' command in PATH"**. Close and reopen Windows Terminal, then try again.

---

## 8. Node.js

**What this is:** A JavaScript runtime. Many developer tools are built with JavaScript and need Node.js to run.\
**Official source:** [Download Node.js](https://nodejs.org/en/download)

**Install:**

```powershell
winget install --id OpenJS.NodeJS.LTS -e
```

**Verify it worked:**

Open a new terminal, then:

```powershell
node --version
```

**Expected result:**

```
v22.x.x
```

(Any version 18 or higher is fine.)

---

## 9. LLM CLI Tool

**What this is:** An AI assistant that runs in your terminal. You'll use it to perform git operations using natural language instead of memorizing commands.

Claude Code is the primary tool for this workshop. Brief setup instructions for Codex (OpenAI) and Gemini CLI are also available, but Windows-specific setup for those is not covered here.

### Claude Code (Anthropic) — Recommended

**Requires:** Claude Max subscription or Anthropic API key\
**Official source:** [Claude Code Setup](https://docs.anthropic.com/en/docs/claude-code/setup)

**Install:**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**If you see a PATH warning** ("native installation exists but ... \.local\bin is not in your PATH"), add it manually:

```powershell
$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
[Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
```

Open a new terminal after running that command.

**Verify it worked:**

```powershell
claude --version
claude doctor
```

> **Note:** `claude doctor` may show a PATH warning even after the fix — this is a known false positive and Claude Code works correctly regardless.

**First-time setup:**

```powershell
claude
```

Follow the prompts to sign in via your browser.

> **Troubleshooting — Git Bash path:** If `claude doctor` reports a Git Bash path error, set the path manually in `~/.claude/settings.json`:
>
> ```powershell
> New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude" | Out-Null
> @'
> {
>   "env": {
>     "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
>   }
> }
> '@ | Set-Content "$env:USERPROFILE\.claude\settings.json"
> ```

---

## Final Checklist

Run each command below. If they all produce output (no errors), you're ready for the workshop!

```powershell
$PSVersionTable.PSVersion
oh-my-posh --version
git --version
node --version
code --version
claude --version
claude doctor
```

| Tool | Check |
|------|-------|
| Windows Terminal | Opens and shows a PowerShell prompt |
| PowerShell 7 | `$PSVersionTable.PSVersion` shows Major: 7+ |
| Oh My Posh | Prompt shows icons/colors; `oh-my-posh --version` works |
| Git for Windows | `git --version` shows a version |
| GitHub account | Can log in at github.com |
| Visual Studio Code | `code --version` shows a version |
| Node.js | `node --version` shows v18+ |
| Claude Code | `claude --version` works; `claude doctor` passes |
| Workshop repos | Cloned into `~/projects/workshop/` |

All done? You're ready for the workshop!

---

## 10. Workshop Setup

**What this is:** Clone the workshop repos so you have all materials and a practice space ready.

> **Important — avoid OneDrive folders:** Do **not** put your workshop folder inside `Documents`, `Desktop`, or anywhere under your OneDrive folder. OneDrive syncs these folders automatically, which can conflict with git repositories. Use `~/projects/workshop/` (which maps to `C:\Users\yourname\projects\workshop\`) instead.

**Step 1: Create a workshop directory:**

```powershell
mkdir ~/projects/workshop
cd ~/projects/workshop
```

**Step 2: Clone the docs repo (teaching materials):**

```powershell
git clone https://github.com/isnbh0/git-cli-workshop.git
```

**Step 3: Clone the demo repo (your practice playground):**

```powershell
git clone https://github.com/isnbh0/git-cli-workshop-demo.git
```

**Verify it worked:**

```powershell
ls ~/projects/workshop
```

**Expected result:**

```
git-cli-workshop    git-cli-workshop-demo
```

**What you now have:**
- `git-cli-workshop/` — Open this in your browser or VSCode to read the docs
- `git-cli-workshop-demo/` — This is where you'll practice git commands during the workshop

> **Important:** You will do all your git practice inside `git-cli-workshop-demo/`. The docs repo is for reading only.

> **Note on paths:** In PowerShell 7, `~` expands to `C:\Users\yourname`. When you see paths like `~/projects/workshop/git-cli-workshop-demo` in the workshop docs, they work the same way on Windows.
