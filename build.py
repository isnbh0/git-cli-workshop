#!/usr/bin/env python3
"""Build platform-specific workshop docs from .src/ templates."""

import re
import sys
from pathlib import Path

VARS = {
    'macos': {
        'Cmd': 'Cmd',
        'terminal_app': 'iTerm2',
        'open_cmd': 'open',
        'file_explorer': 'Finder',
        'search_shortcut': 'Cmd+Space',
        'search_name': 'Spotlight',
        'my_computer_label': 'My MacBook',
        'keyboard_shortcuts_url': 'https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf',
        'keyboard_shortcuts_os': 'macOS',
        'cli_ref': '[macOS Command Line A-Z — SS64](https://ss64.com/mac/)',
        'new_terminal': 'Cmd+N',
    },
    'windows': {
        'Cmd': 'Ctrl',
        'terminal_app': 'Windows Terminal',
        'open_cmd': 'start',
        'file_explorer': 'File Explorer',
        'search_shortcut': 'Win+S',
        'search_name': 'Search',
        'my_computer_label': 'My Windows PC',
        'keyboard_shortcuts_url': 'https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf',
        'keyboard_shortcuts_os': 'Windows',
        'cli_ref': '[PowerShell Documentation — Microsoft](https://learn.microsoft.com/en-us/powershell/)',
        'new_terminal': 'Ctrl+Shift+N',
    },
}

HEADER = "<!-- DO NOT EDIT — generated from .src/ by build.py -->\n\n"
PLATFORMS = ['macos', 'windows']
LANGUAGES = ['en', 'ko']


def process(text, platform):
    """Apply platform fences, variable substitution, and blank collapsing."""
    other = 'windows' if platform == 'macos' else 'macos'
    otag, ttag = other.upper(), platform.upper()

    # Strip other platform's fenced blocks
    text = re.sub(rf'<!-- {otag} -->.*?<!-- /{otag} -->\n?', '', text, flags=re.DOTALL)
    # Unwrap this platform's fence markers
    text = re.sub(rf'<!-- {ttag} -->\n?', '', text)
    text = re.sub(rf'<!-- /{ttag} -->\n?', '', text)

    # Replace {{var}} tokens
    def replace_var(m):
        key = m.group(1)
        if key not in VARS[platform]:
            print(f"ERROR: unknown variable {{{{{key}}}}} in source", file=sys.stderr)
            sys.exit(1)
        return VARS[platform][key]

    text = re.sub(r'\{\{(\w+)\}\}', replace_var, text)

    # Collapse 3+ consecutive blank lines to 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def main():
    root = Path(__file__).resolve().parent
    written = 0

    for lang in LANGUAGES:
        srcdir = root / '.src' / lang
        if not srcdir.is_dir():
            continue
        for platform in PLATFORMS:
            outdir = root / lang / platform
            outdir.mkdir(parents=True, exist_ok=True)

            for src in sorted(srcdir.glob('*.md')):
                # Handle 00-prerequisites platform-specific files
                if src.stem.startswith('00-prerequisites-'):
                    suffix = src.stem.split('00-prerequisites-')[1]
                    if suffix == platform:
                        outname = '00-prerequisites.md'
                    else:
                        continue  # skip other platform's prerequisites
                else:
                    outname = src.name

                text = process(src.read_text(), platform)
                content = HEADER + text

                outpath = outdir / outname
                if outpath.exists() and outpath.read_text() == content:
                    continue  # unchanged — skip write

                outpath.write_text(content)
                written += 1
                print(f"  {outpath.relative_to(root)}")

    print(f"Built {written} file(s).")


if __name__ == '__main__':
    main()
