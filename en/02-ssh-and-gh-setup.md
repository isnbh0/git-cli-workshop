# 02 - SSH Key and gh CLI Setup

> **Note:** This document is meant to be followed during the workshop with instructor guidance. Don't worry if the steps feel unfamiliar — we'll go through them together.

---

## 1. What Is SSH?

SSH is a way for your computer to securely identify itself to another computer — in our case, GitHub.

Think of it like a secret handshake: your computer and GitHub agree on a unique pair of keys that only they know. Once the handshake is set up, you can push and pull code without typing your password every time.

You'll create this key pair once and register it with GitHub. After that, it works automatically.

---

## 2. Generate an SSH Key

Open iTerm2 and type:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Replace `your_email@example.com` with the email address you used for your GitHub account.

**What you'll see:**

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/yourname/.ssh/id_ed25519):
```

**What to do:** Press Enter to accept the default location.

```
Enter passphrase (empty for no passphrase):
```

**What to do:** Press Enter to skip the passphrase (you can add one later if you want).

```
Enter same passphrase again:
```

**What to do:** Press Enter again.

**Expected output:**

```
Your identification has been saved in /Users/yourname/.ssh/id_ed25519
Your public key has been saved in /Users/yourname/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx your_email@example.com
The key's randomart image is:
+--[ED25519 256]--+
|     ...         |
|    . . .        |
|     (random art)|
+----[SHA256]-----+
```

You now have two files:
- **Private key** (`~/.ssh/id_ed25519`) — This stays on your computer. Never share it.
- **Public key** (`~/.ssh/id_ed25519.pub`) — This is the one you give to GitHub.

> **Reference:** [Generating a new SSH key and adding it to the ssh-agent — GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

---

## 3. Add Your SSH Key to GitHub

### Step 1: Copy your public key

```bash
cat ~/.ssh/id_ed25519.pub
```

**Expected output:** A long line starting with `ssh-ed25519` and ending with your email:

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG... your_email@example.com
```

Select and copy the entire output (`Cmd+A` then `Cmd+C` in the terminal, or triple-click the line to select it).

### Step 2: Add it to GitHub

1. Go to [https://github.com/settings/keys](https://github.com/settings/keys)
   - (Or: GitHub.com → click your profile picture → **Settings** → **SSH and GPG keys**)
2. Click **New SSH key**
3. **Title:** Give it a name like "My MacBook" (this is just a label for you)
4. **Key type:** Leave as "Authentication Key"
5. **Key:** Paste the key you copied
6. Click **Add SSH key**
7. GitHub may ask for your password to confirm

> **Reference:** [Adding a new SSH key to your GitHub account — GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

---

## 4. Test the Connection

```bash
ssh -T git@github.com
```

**What you'll see (first time only):**

```
The authenticity of host 'github.com (...)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

**What to do:** Type `yes` and press Enter.

**Expected output:**

```
Hi yourusername! You've successfully authenticated, but GitHub does not provide shell access.
```

If you see your GitHub username in that message, the SSH key is working.

> **Troubleshooting:** If you see "Permission denied (publickey)", the key wasn't added correctly. Run `cat ~/.ssh/id_ed25519.pub` again and make sure you copied the entire line (including `ssh-ed25519` at the beginning and your email at the end). Then re-add it on GitHub.

> **Reference:** [Testing your SSH connection — GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

---

## 5. Install the gh CLI

The `gh` CLI is GitHub's official command-line tool. It lets you create repos, manage issues, and more — directly from the terminal.

> **Reference:** [GitHub CLI Manual](https://cli.github.com/manual/)

### Step 1: Install

```bash
brew install gh
```

**What you'll see:** Homebrew downloads and installs the gh tool. This usually takes less than a minute.

**Verify it installed:**

```bash
gh --version
```

**Expected output:**

```
gh version 2.x.x (20xx-xx-xx)
```

### Step 2: Log in to GitHub

```bash
gh auth login
```

> **Reference:** [gh auth login — CLI Manual](https://cli.github.com/manual/gh_auth_login)

**What you'll see:** A series of prompts. Choose these options:

```
? What account do you want to log into?  GitHub.com
? What is your preferred protocol for Git operations on this host?  SSH
? Upload your SSH key to your GitHub account?  Skip
? How would you like to authenticate GitHub CLI?  Login with a web browser
```

**Note:** We choose "Skip" for uploading the SSH key because we already added it manually in the previous step.

After selecting "Login with a web browser":

```
! First copy your one-time code: XXXX-XXXX
Press Enter to open github.com in your browser...
```

**What to do:**
1. Copy the code shown
2. Press Enter — your browser opens
3. Paste the code into the browser
4. Click "Authorize"
5. Come back to the terminal

**Expected output:**

```
✓ Authentication complete.
- gh config set -h github.com git_protocol ssh
✓ Configured git protocol
✓ Logged in as yourusername
```

---

## 6. Verify Everything Works

```bash
gh auth status
```

**Expected output:**

```
github.com
  ✓ Logged in to github.com account yourusername (keyring)
  - Active account: true
  - Git operations protocol: ssh
  - Token: gho_****
  - Token scopes: 'gist', 'read:org', 'repo', 'workflow'
```

If you see a checkmark and your username, you're all set.

---

## Summary

Here's what you set up in this section:

| What | Why |
|------|-----|
| SSH key | Secure, password-free connection to GitHub |
| SSH key on GitHub | GitHub recognizes your computer |
| gh CLI | Manage GitHub repos from the terminal |
| gh auth | gh CLI is connected to your account |

You're now ready to push and pull code to GitHub.
