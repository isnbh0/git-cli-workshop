# 03 - VSCode Orientation

**In this section, you'll get familiar with Visual Studio Code — the text editor we'll use throughout the workshop.** Think of it as a "multi-file notepad" that lets you view and edit all the files in a project at once. This should take about 5-10 minutes.

---

## 1. Opening VSCode

There are two ways to open VSCode:

**From Spotlight:**

1. Press `Cmd+Space` to open Spotlight
2. Type "Visual Studio Code"
3. Press Enter

**From the terminal (recommended):**

First, navigate to any folder you want to work in, then type:

```bash
code .
```

**What happens:** VSCode opens with that folder loaded in the sidebar. The `.` means "this folder" — you've seen it before in the CLI section.

**Verify it worked:** A VSCode window appears showing the folder name in the top of the sidebar.

> **Troubleshooting:** If you see "command not found: code", open VSCode manually, press `Cmd+Shift+P`, type "shell command", and select **"Shell Command: Install 'code' command in PATH"**. Close and reopen iTerm2, then try again.

> **Reference:** [VS Code Command Line Interface (CLI)](https://code.visualstudio.com/docs/configure/command-line)

---

## 2. The Sidebar (File Explorer)

On the left side of VSCode, you'll see a column showing all the files and folders in your project. This is the **File Explorer**.

- Click the top icon in the far-left icon bar (it looks like two overlapping documents) to open it
- You can expand folders by clicking the arrow next to them
- This sidebar always reflects the real files on your computer — if you create a file in the terminal, it appears here too

> **Tip:** If the sidebar is hidden, press `Cmd+B` to toggle it.

> **Reference:** [VS Code User Interface](https://code.visualstudio.com/docs/getstarted/userinterface)

---

## 3. Opening and Editing Files

**To open a file:** Click on its name in the sidebar. It opens in the main editing area.

**To edit:** Click anywhere in the file and start typing, just like any text editor.

**To save:** Press `Cmd+S`.

**Verify it worked:** The filename tab at the top shows a dot (or circle) when a file has unsaved changes. After pressing `Cmd+S`, the dot disappears.

> **Tip:** If you see multiple tabs along the top, each tab is a different file. Click a tab to switch between files.

> **Reference:** [VS Code Keyboard Shortcuts for macOS (PDF)](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)

---

## 4. Creating New Files

**From the sidebar:**

1. Hover over the folder name in the sidebar
2. Click the "New File" icon (it looks like a document with a `+`)
3. Type the filename and press Enter

**From the menu:**

1. Go to **File → New File** (or press `Cmd+N`)
2. Type your content
3. Press `Cmd+S` to save — you'll be asked to choose a name and location

**Verify it worked:** The new file appears in the sidebar and opens in a tab.

---

## 5. The Integrated Terminal

VSCode has a built-in terminal. You can open it with **View → Terminal** (or press `` Ctrl+` ``).

We won't use it much in this workshop — we'll keep using iTerm2 as our main terminal. But it's good to know it exists in case you see it mentioned online.

---

## 6. Markdown Preview

Since we'll be writing a lot of markdown files (files ending in `.md`), here's a handy feature:

**To preview a markdown file:**

1. Open a `.md` file in VSCode
2. Press `Cmd+Shift+V`

**What happens:** A preview pane opens showing your markdown rendered with headings, bold text, checkboxes, and so on — instead of the raw text with `#` and `*` symbols.

**Verify it worked:** You see a nicely formatted version of your markdown file in a new tab.

> **Tip:** To see the preview side-by-side with the raw text, press `Cmd+K` then `V` (press `Cmd+K` first, release, then press `V`).

> **Reference:** [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)

---

That's all you need to know about VSCode for now. We'll use it as our file editor while running git commands in iTerm2.
