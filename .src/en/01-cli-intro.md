# 01 - CLI Introduction

**In this section, you'll learn what the terminal is and practice the most common commands.** By the end, you'll be comfortable navigating folders, creating files, and cleaning up after yourself — all by typing.

---

## 1. What Is a Terminal?

A terminal is a text-based way to talk to your computer. Every click you do in {{file_explorer}} — opening a folder, copying a file, deleting something — you can also type as a command.

Why bother? Because once you get the hang of it, typing commands is often faster and more powerful than clicking. And many developer tools (including git) only work from the terminal.

You already installed your terminal app in the prerequisites.

<!-- MACOS -->
> **Reference (macOS):** [Terminal User Guide for Mac — Apple Support](https://support.apple.com/guide/terminal/welcome/mac)
<!-- /MACOS -->

---

## 2. Opening Your Terminal

<!-- MACOS -->
1. Press `{{search_shortcut}}` to open {{search_name}}
2. Type "iTerm"
3. Press Enter

A window appears with a text prompt. That's your terminal, ready for commands.
<!-- /MACOS -->
<!-- WINDOWS -->
1. Press `{{search_shortcut}}` to open {{search_name}} (or click the search bar in the taskbar)
2. Type "{{terminal_app}}"
3. Press Enter

A window appears with a PowerShell prompt. That's your terminal, ready for commands.
<!-- /WINDOWS -->

---

## 3. Anatomy of a Prompt

<!-- MACOS -->
When iTerm2 opens, you see something like this:

```
yourname@yourcomputer ~ %
```

Here's what each part means:

| Part | Meaning |
|------|---------|
| `yourname` | Your macOS username |
| `yourcomputer` | Your computer's name |
| `~` | Your current location (home folder) |
| `%` | "Ready for input" (you may see `$` instead — both are fine) |
<!-- /MACOS -->

<!-- WINDOWS -->
When Windows Terminal opens, you see something like this:

```
PS C:\Users\yourname>
```

Here's what each part means:

| Part | Meaning |
|------|---------|
| `PS` | PowerShell (your shell) |
| `C:\Users\yourname` | Your current location (home folder) |
| `>` | "Ready for input" |
<!-- /WINDOWS -->

You don't need to understand everything here. The important thing is: **you type your commands after the `%`, `$`, or `>`**.

---

## 4. Commands to Practice

### `pwd` — Print working directory

**What it does:** Shows you where you are right now in the file system — your current folder's full path.

**Example:**

```bash
pwd
```

**Expected output:**

<!-- MACOS -->
```
/Users/yourname
```
<!-- /MACOS -->
<!-- WINDOWS -->
```
C:\Users\yourname
```
<!-- /WINDOWS -->

This tells you you're in your home folder. Every time you're unsure where you are, `pwd` is the command to reach for.

> **Try it yourself:** Type `pwd` and press Enter. That's your home folder — the starting point when you open a new terminal.

---

### `cd` — Change directory

**What it does:** Moves you to a different folder (directory).

**Example — go to your Desktop:**

```bash
cd Desktop
```

**Expected output:** No output (that's normal). Your prompt changes to show your new location:

<!-- MACOS -->
```
yourname@yourcomputer Desktop %
```
<!-- /MACOS -->
<!-- WINDOWS -->
```
PS C:\Users\yourname\Desktop>
```
<!-- /WINDOWS -->

**Verify where you are:**

```bash
pwd
```

**Expected output:**

<!-- MACOS -->
```
/Users/yourname/Desktop
```
<!-- /MACOS -->
<!-- WINDOWS -->
```
C:\Users\yourname\Desktop
```
<!-- /WINDOWS -->

**Other useful variations:**

| Command | What it does |
|---------|-------------|
| `cd ~` | Go back to your home folder |
| `cd ..` | Go up one folder (parent directory) |
| `cd` | Go back to your home folder (same as `cd ~`) |
| `cd Documents` | Go into the Documents folder |

> **Try it yourself:** Move to your Desktop with `cd Desktop`, then go back home with `cd ~`. Use `pwd` each time to confirm where you are.

---

### `ls` — List files

**What it does:** Shows you what files and folders are in your current location.

**Example:**

```bash
ls
```

**Expected output:** A list of files and folders, something like:

<!-- MACOS -->
```
Desktop    Documents  Downloads  Movies  Music  Pictures
```
<!-- /MACOS -->
<!-- WINDOWS -->
```
Desktop  Documents  Downloads  Music  Pictures  Videos
```
<!-- /WINDOWS -->

> **Try it yourself:** Type `ls` and press Enter. What files do you see?

---

### `mkdir` — Make a new directory

**What it does:** Creates a new folder.

**Example:**

```bash
mkdir test-folder
```

**Expected output:** No output (that's normal — it just creates the folder silently).

**Verify it worked:**

```bash
ls
```

**Expected output:** You should see `test-folder` in the list.

> **Try it yourself:** Create a folder called `test-folder`, then use `ls` to confirm it exists.

---

### `{{open_cmd}}` — Open in {{file_explorer}} or default app

**What it does:** Opens a file or folder just like double-clicking it.

<!-- MACOS -->
**Open the current folder in Finder:**

```bash
open .
```

**Expected output:** A Finder window opens showing the contents of your current folder.
<!-- /MACOS -->

<!-- WINDOWS -->
**Open the current folder in File Explorer:**

```powershell
start .
```

**Expected output:** A File Explorer window opens showing the contents of your current folder.
<!-- /WINDOWS -->

> **Try it yourself:** Type `{{open_cmd}} .` to see your current folder in {{file_explorer}}. Recognize those files? They're the same ones `ls` showed you.

---

### `cp` — Copy a file

**What it does:** Makes a copy of a file.

**Example:**

First, let's create a file to work with:

```bash
echo "Hello, terminal!" > greeting.txt
```

(This creates a file called `greeting.txt` containing the text "Hello, terminal!")

Now copy it:

```bash
cp greeting.txt greeting-copy.txt
```

**Expected output:** No output (the copy is made silently).

**Verify it worked:**

```bash
ls
```

**Expected output:** You should see both `greeting.txt` and `greeting-copy.txt`.

> **Try it yourself:** Create `greeting.txt`, copy it to `greeting-copy.txt`, and use `ls` to confirm both exist.

---

### `mv` — Move or rename a file

**What it does:** Moves a file to a different location, or renames it. (Moving and renaming are the same operation in the terminal.)

**Example — rename a file:**

```bash
mv greeting-copy.txt farewell.txt
```

**Expected output:** No output.

**Verify it worked:**

```bash
ls
```

**Expected output:** `greeting-copy.txt` is gone, and `farewell.txt` is there instead.

> **Try it yourself:** Rename `greeting-copy.txt` to `farewell.txt` and confirm with `ls`.

---

### `rm` — Delete a file

**What it does:** Permanently deletes a file.

> **Warning:** There is no trash can in the terminal. When you `rm` a file, it's gone forever. Double-check before you press Enter!

**Example:**

```bash
rm farewell.txt
```

**Expected output:** No output.

**Verify it worked:**

```bash
ls
```

**Expected output:** `farewell.txt` is no longer in the list.

<!-- MACOS -->
To delete a folder and everything inside it, use `rm -r`:

```bash
rm -r test-folder
```
<!-- /MACOS -->
<!-- WINDOWS -->
To delete a folder and everything inside it, use `Remove-Item -Recurse`:

```powershell
Remove-Item -Recurse test-folder
```
<!-- /WINDOWS -->

> **Try it yourself:** Delete `farewell.txt` and `test-folder`. Use `ls` to confirm they're gone.

---

<!-- MACOS -->
### `less` — View file contents

**What it does:** Opens a file so you can read it in the terminal.

**Example:**

```bash
less greeting.txt
```

**Expected output:** The contents of the file are displayed:

```
Hello, terminal!
```

**Important:** Press `q` to quit and go back to the prompt. (If you forget, you'll be stuck in the viewer!)

> **Try it yourself:** View `greeting.txt` with `less`, then press `q` to exit.
<!-- /MACOS -->
<!-- WINDOWS -->
### `cat` — View file contents

**What it does:** Prints the contents of a file to the terminal.

**Example:**

```powershell
cat greeting.txt
```

**Expected output:**

```
Hello, terminal!
```

> **Try it yourself:** View `greeting.txt` with `cat`.
<!-- /WINDOWS -->

---

### `history` — See your command history

**What it does:** Shows a list of commands you've typed recently.

**Example:**

```bash
history
```

**Expected output:** A numbered list of your recent commands:

<!-- MACOS -->
```
  1  ls
  2  cd Desktop
  3  pwd
  4  cd ~
  5  mkdir test-folder
  ...
```
<!-- /MACOS -->
<!-- WINDOWS -->
```
  Id CommandLine
  -- -----------
   1 ls
   2 cd Desktop
   3 pwd
   4 cd ~
   5 mkdir test-folder
   ...
```
<!-- /WINDOWS -->

> **Try it yourself:** Type `history` to see everything you've done so far.

> **Tip:** You can also press the Up arrow key to scroll through previous commands one at a time. This is handy when you want to re-run a command.

---

### `exit` — Close the terminal session

**What it does:** Closes the current terminal tab or window.

**Example:**

```bash
exit
```

**Expected output:** The terminal tab closes (or shows "process completed" if it's the only tab).

> **Try it yourself:** Type `exit` to close the session. (You can always open a new terminal window: `{{new_terminal}}` on {{terminal_app}}.)

<!-- MACOS -->
> **Reference:** For command documentation, see {{cli_ref}}. You can also type `man <command>` in the terminal (e.g. `man ls`).
<!-- /MACOS -->
<!-- WINDOWS -->
> **Reference:** For command documentation, see {{cli_ref}}. You can also type `Get-Help <command>` in the terminal (e.g. `Get-Help ls`).
<!-- /WINDOWS -->

---

## 5. Practice Exercise

Let's put it all together. Follow these steps in order:

### Step 1: Create a folder called `practice`

```bash
mkdir practice
```

### Step 2: Move into it

```bash
cd practice
```

### Step 3: Create a file

```bash
echo "This is my practice file." > notes.txt
```

### Step 4: Verify the file exists

```bash
ls
```

**Expected output:**

```
notes.txt
```

### Step 5: View the file

<!-- MACOS -->
```bash
less notes.txt
```

**Expected output:**

```
This is my practice file.
```

Press `q` to exit.
<!-- /MACOS -->
<!-- WINDOWS -->
```powershell
cat notes.txt
```

**Expected output:**

```
This is my practice file.
```
<!-- /WINDOWS -->

### Step 6: Copy the file

```bash
cp notes.txt notes-backup.txt
```

### Step 7: Rename the copy

```bash
mv notes-backup.txt archive.txt
```

### Step 8: List files to see both

```bash
ls
```

**Expected output:**

```
archive.txt  notes.txt
```

### Step 9: Delete the copy

```bash
rm archive.txt
```

### Step 10: Go back up and remove the folder

```bash
cd ..
```

<!-- MACOS -->
```bash
rm -r practice
```
<!-- /MACOS -->
<!-- WINDOWS -->
```powershell
Remove-Item -Recurse practice
```
<!-- /WINDOWS -->

### Step 11: Verify everything is cleaned up

```bash
ls
```

**Expected output:** The `practice` folder is gone.

---

Congratulations! You now know the essential terminal commands. These same commands will be the foundation for everything we do with git.
