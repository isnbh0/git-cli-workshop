# 01 - CLI Introduction

**In this section, you'll learn what the terminal is and practice the most common commands.** By the end, you'll be comfortable navigating folders, creating files, and cleaning up after yourself — all by typing.

---

## 1. What Is a Terminal?

A terminal is a text-based way to talk to your computer. Every click you do in Finder — opening a folder, copying a file, deleting something — you can also type as a command.

Why bother? Because once you get the hang of it, typing commands is often faster and more powerful than clicking. And many developer tools (including git) only work from the terminal.

You already installed iTerm2 in the prerequisites. That's your terminal app.

> **Reference:** [Terminal User Guide for Mac — Apple Support](https://support.apple.com/guide/terminal/welcome/mac)

---

## 2. Opening iTerm2

1. Press `Cmd+Space` to open Spotlight
2. Type "iTerm"
3. Press Enter

A window appears with a text prompt. That's your terminal, ready for commands.

---

## 3. Anatomy of a Prompt

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

You don't need to understand everything here. The important thing is: **you type your commands after the `%` (or `$`)**.

---

## 4. Commands to Practice

### `ls` — List files

**What it does:** Shows you what files and folders are in your current location.

**Example:**

```bash
ls
```

**Expected output:** A list of files and folders, something like:

```
Desktop    Documents  Downloads  Movies  Music  Pictures
```

> **Try it yourself:** Type `ls` and press Enter. What files do you see?

---

### `cd` — Change directory

**What it does:** Moves you to a different folder (directory).

**Example — go to your Desktop:**

```bash
cd Desktop
```

**Expected output:** No output (that's normal). Your prompt changes to show your new location:

```
yourname@yourcomputer Desktop %
```

**Verify where you are:**

```bash
pwd
```

**Expected output:**

```
/Users/yourname/Desktop
```

**Other useful variations:**

| Command | What it does |
|---------|-------------|
| `cd ~` | Go back to your home folder |
| `cd ..` | Go up one folder (parent directory) |
| `cd` | Go back to your home folder (same as `cd ~`) |
| `cd Documents` | Go into the Documents folder |

> **Try it yourself:** Move to your Desktop with `cd Desktop`, then go back home with `cd ~`. Use `pwd` each time to confirm where you are.

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

### `open` — Open in Finder or default app

**What it does:** Opens a file or folder just like double-clicking it in Finder. This is macOS-specific and will feel familiar.

**Example — open the current folder in Finder:**

```bash
open .
```

**Expected output:** A Finder window opens showing the contents of your current folder.

**Example — open a specific folder:**

```bash
open test-folder
```

**Expected output:** A Finder window opens showing the (empty) test-folder.

> **Try it yourself:** Type `open .` to see your current folder in Finder. Recognize those files? They're the same ones `ls` showed you.

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

To delete a folder and everything inside it, use `rm -r`:

```bash
rm -r test-folder
```

> **Try it yourself:** Delete `farewell.txt` and `test-folder`. Use `ls` to confirm they're gone.

---

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

---

### `history` — See your command history

**What it does:** Shows a list of commands you've typed recently.

**Example:**

```bash
history
```

**Expected output:** A numbered list of your recent commands:

```
  1  ls
  2  cd Desktop
  3  pwd
  4  cd ~
  5  mkdir test-folder
  ...
```

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

> **Try it yourself:** Type `exit` to close the session. (You can always open a new iTerm2 window with `Cmd+N`.)

> **Reference:** For detailed documentation on any macOS command, see [macOS Command Line A-Z — SS64](https://ss64.com/mac/) or type `man <command>` in the terminal (e.g. `man ls`).

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

```bash
less notes.txt
```

**Expected output:**

```
This is my practice file.
```

Press `q` to exit.

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
rm -r practice
```

### Step 11: Verify everything is cleaned up

```bash
ls
```

**Expected output:** The `practice` folder is gone.

---

Congratulations! You now know the essential terminal commands. These same commands will be the foundation for everything we do with git.
