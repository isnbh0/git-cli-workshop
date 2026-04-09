# Git+CLI Workshop - Agent Instructions

This is a bilingual teaching materials project (English + Korean).

## Two-Repo Structure

The workshop uses two repos:
- **This repo** (`git-cli-workshop`) — teaching docs only; participants read these
- **Demo repo** (`git-cli-workshop-demo`) — participant playground; this is where exercises happen

When docs reference participant exercises, use the demo repo directory path (`~/projects/workshop/git-cli-workshop-demo/`).

## Source-and-Build System

Output files in `en/` and `ko/` are **generated** — do not edit them directly. Edit the source templates in `.src/` instead, then run `python3 build.py` to regenerate output.

### Directory structure

```
.src/                        # SOURCE — edit these
  en/
    00-prerequisites-macos.md    # standalone (no template syntax)
    00-prerequisites-windows.md  # standalone (no template syntax)
    01-cli-intro.md              # fences + {{vars}}
    02-ssh-and-gh-setup.md       # fences + {{vars}}
    03-git-part0-vscode.md       # {{vars}} + minor fences
    04-09...                     # {{Cmd}} vars only
  ko/                            # mirrors en/ exactly

en/                          # OUTPUT — generated, committed
  macos/
    00-prerequisites.md  …  09-git-part3b-branches-ai.md
  windows/
    00-prerequisites.md  …  09-git-part3b-branches-ai.md
ko/                          # same structure
  macos/ …
  windows/ …
```

### Template syntax

**Variables** — `{{var}}` is replaced with platform-specific values:

| Variable | macOS | Windows |
|----------|-------|---------|
| `{{Cmd}}` | `Cmd` | `Ctrl` |
| `{{terminal_app}}` | `iTerm2` | `Windows Terminal` |
| `{{open_cmd}}` | `open` | `start` |
| `{{file_explorer}}` | `Finder` | `File Explorer` |
| `{{search_shortcut}}` | `Cmd+Space` | `Win+S` |
| `{{search_name}}` | `Spotlight` | `Search` |
| `{{my_computer_label}}` | `My MacBook` | `My Windows PC` |
| `{{cli_ref}}` | `[macOS Command Line A-Z — SS64](…)` | `[PowerShell Documentation — Microsoft](…)` |

**Platform fences** — HTML comments that include/exclude blocks per platform:

```markdown
<!-- MACOS -->
macOS-only content (stripped on Windows build)
<!-- /MACOS -->
<!-- WINDOWS -->
Windows-only content (stripped on macOS build)
<!-- /WINDOWS -->
```

### How to add new content

1. Edit the source template in `.src/en/` (and `.src/ko/` for Korean)
2. Use `{{Cmd}}` instead of `Cmd` or `Ctrl` for keyboard shortcuts
3. Use fences for blocks that differ structurally between platforms
4. Run `python3 build.py` to regenerate output
5. Verify with `grep -r '{{' en/ ko/` (should find no unresolved variables)

### Pre-commit hook

Run `make install-hooks` to install a pre-commit hook that auto-rebuilds output and stages it.

## Platform Support

The workshop supports both macOS and Windows with fully isolated output — each platform directory contains only content relevant to that platform.

- **Prerequisites** are separate source files per platform (no template syntax)
- **Files 01-03** use both fences and variables for platform differences
- **Files 04-09** use `{{Cmd}}` variable substitution only
- **`~/projects/workshop/git-cli-workshop-demo`** works on both platforms (PowerShell 7 expands `~`)

## Key rules
- English is the canonical language; Korean is a translation
- When editing content, update BOTH `.src/en/` and `.src/ko/` source templates
- Always run `python3 build.py` after editing source templates
- Never edit files in `en/macos/`, `en/windows/`, `ko/macos/`, `ko/windows/` directly
- Target audience: absolute beginners with zero CLI experience
- Every command must show: what to type, what happens, how to verify
- Cross-repo links use absolute GitHub URLs (https://github.com/isnbh0/git-cli-workshop-demo)
- Exercise working directory is always `~/projects/workshop/git-cli-workshop-demo/`
- Docs repo should never contain practice/exercise files (SANDBOX.md, TODO.md, etc.)
