<!-- DO NOT EDIT — generated from .src/ by build.py -->

# 00 - 사전 준비

**워크숍 전에 아래 단계를 모두 완료해 주세요.** 각 단계에는 설치 방법, 예상 출력, 그리고 정상 설치 확인 방법이 포함되어 있습니다.

막히는 부분이 있으면 오류 화면을 캡처해서 강사에게 보내주세요.

이 가이드는 **네이티브 Windows** 환경(WSL 아님)을 대상으로 합니다. 기본 터미널로 **PowerShell**을, git에는 **Git for Windows**를 사용합니다.

---

## 0. 사전 점검: WinGet 확인

**이것은:** WinGet은 Windows의 기본 패키지 관리자입니다. 명령어 하나로 소프트웨어를 설치할 수 있게 해주는 도구입니다.

(시작 메뉴에서 'PowerShell'을 검색하세요 — 1단계에서 Windows Terminal을 설치한 뒤에는 그것을 사용합니다)

PowerShell을 열고 WinGet을 사용할 수 있는지 확인합니다:

```powershell
winget --version
```

**예상 결과:** `v1.x.x` 같은 버전 번호가 표시됩니다.

> **WinGet이 없는 경우:** **Microsoft Store**를 열고 **앱 설치 관리자(App Installer)**를 검색하여 설치하거나 업데이트하세요. 그런 다음 PowerShell을 완전히 닫고 새로 여세요.

---

## 1. Windows Terminal

**이것은:** 탭, 분할 창, 테마 등을 지원하는 현대적인 Windows 터미널 앱입니다. 이후 모든 단계는 Windows Terminal의 PowerShell에서 실행하는 것을 권장합니다.\
**공식 출처:** [Windows Terminal — Microsoft Store](https://aka.ms/terminal)

**설치:**

```powershell
winget install --id Microsoft.WindowsTerminal -e
```

**예상 화면:** WinGet이 Windows Terminal을 다운로드하고 설치합니다.

**기본 터미널로 설정:**

설치 후 Windows Terminal을 열고 설정합니다:

1. 탭 오른쪽의 **∨** → **설정** 클릭
2. **시작** 탭에서 **기본 터미널 응용 프로그램**을 `Windows 터미널`로 설정
3. **기본 프로필**이 `PowerShell`로 설정되어 있는지 확인
4. **저장** 클릭

**예상 결과:** 이후 새 터미널 창을 열면 자동으로 Windows Terminal의 PowerShell이 시작됩니다.

---

## 2. PowerShell 7

**이것은:** Windows에 기본 내장된 PowerShell 5.1은 구버전입니다. PowerShell 7은 더 나은 기능과 호환성을 제공하는 최신 버전입니다.\
**공식 출처:** [Windows에서 PowerShell 설치 — Microsoft Docs](https://learn.microsoft.com/ko-kr/powershell/scripting/install/installing-powershell-on-windows)

**설치:**

```powershell
winget install --id Microsoft.PowerShell -e
```

**설치 후** Windows Terminal을 열고 PowerShell 7을 기본 프로필로 설정합니다:

1. **∨** → **설정** → **시작** 탭으로 이동
2. **기본 프로필**을 `PowerShell` (버전 7)로 선택합니다. 이름이 `Windows PowerShell`인 항목은 5.1이니 선택하지 마세요.
3. **저장** 클릭

**정상 설치 확인:**

새 터미널 탭을 열고 다음을 입력하세요:

```powershell
$PSVersionTable.PSVersion
```

**예상 결과:** `Major` 값이 `7` 이상입니다.

---

## 3. Oh My Posh

**이것은:** PowerShell 프롬프트를 꾸밀 수 있는 테마 엔진입니다. 아이콘이 제대로 표시되려면 Nerd Font도 설치해야 합니다.\
**공식 출처:** [Oh My Posh — 설치](https://ohmyposh.dev/docs/installation/windows)

**Oh My Posh 설치:**

```powershell
winget install JanDeDobbeleer.OhMyPosh --source winget
```

터미널 창을 닫고 새로 연 다음, Nerd Font를 설치합니다:

```powershell
oh-my-posh font install CascadiaCode
```

**Windows Terminal에서 폰트 적용:**

1. **∨** → **설정** → 좌측에서 **PowerShell** 프로필 선택 → **모양** 탭
2. **글꼴**을 `CaskaydiaCove Nerd Font`로 변경
3. **저장** 클릭

**PowerShell 프로필에 Oh My Posh 추가:**

프로필 파일이 있는지 확인합니다:

```powershell
Test-Path $PROFILE
```

`False`가 출력되면 먼저 파일을 생성합니다:

```powershell
New-Item -Path $PROFILE -ItemType File -Force
```

프로필 파일을 엽니다:

```powershell
notepad $PROFILE
```

다음 줄을 추가하고 저장합니다:

```powershell
oh-my-posh init pwsh | Invoke-Expression
```

즉시 적용하거나 (터미널을 닫고 다시 열어도 됩니다):

```powershell
. $PROFILE
```

> **프로필 실행이 차단되는 경우:** `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`를 실행한 뒤 다시 시도하세요.

**정상 설치 확인:** 프롬프트에 아이콘과 색상이 표시되고 기존의 `PS C:\Users\이름>` 형태가 바뀌었으면 정상입니다.

---

## 4. Git for Windows

**이것은:** Windows용으로 패키지된 git 버전 관리 시스템입니다. 일부 도구가 내부적으로 사용하는 Git Bash도 함께 설치됩니다.\
**공식 출처:** [Git for Windows](https://gitforwindows.org)

**설치:**

```powershell
winget install --id Git.Git -e
```

**예상 화면:** WinGet이 Git for Windows를 다운로드하고 설치합니다.

**정상 설치 확인:**

새 터미널 창을 열고 다음을 입력하세요:

```powershell
git --version
```

**예상 결과:**

```
git version 2.x.x.windows.x
```

---

## 5. GitHub 계정

**이것은:** 코드 프로젝트를 저장하고 공유하는 웹사이트입니다. 워크숍에서 작업물을 업로드할 때 사용합니다.\
**공식 출처:** [GitHub](https://github.com)

**설정:**

1. [https://github.com](https://github.com) 에 접속
2. "Sign up" 클릭
3. 안내에 따라 계정 생성
4. 사용자명과 이메일을 기억해두세요 — 워크숍에서 필요합니다

**정상 설정 확인:** [https://github.com](https://github.com) 에 로그인하여 대시보드가 보이는지 확인하세요.

---

## 6. GitHub CLI

**이것은:** GitHub 공식 명령줄 도구입니다. 터미널에서 직접 저장소 생성, 이슈 관리, GitHub 인증 등을 할 수 있게 해줍니다.\
**공식 출처:** [GitHub CLI](https://cli.github.com)

**설치:**

```powershell
winget install --id GitHub.cli
```

새 터미널 창을 열어 업데이트된 PATH가 반영되도록 한 다음 확인합니다:

```powershell
gh --version
```

**예상 결과:**

```
gh version 2.x.x (20xx-xx-xx)
```

> **참고:** GitHub 계정으로 `gh` 인증은 워크숍 중에 진행합니다 (SSH 및 gh 설정 섹션). 지금은 인증이 필요 없습니다.

---

## 7. Visual Studio Code

**이것은:** 파일을 작성하고 편집하는 텍스트 에디터입니다. "여러 파일을 다룰 수 있는 메모장" 같은 것으로, 워크숍에서 파일 편집에 사용합니다.\
**공식 출처:** [Visual Studio Code on Windows](https://code.visualstudio.com/docs/setup/windows)

**설치:**

```powershell
winget install --id Microsoft.VisualStudioCode -e
```

**정상 설치 확인:**

새 터미널을 열고 다음을 입력하세요:

```powershell
code --version
```

**예상 결과:**

```
1.x.x
(해시 문자열)
```

> **문제 해결:** "command not found: code"가 나오면, 시작 메뉴에서 Visual Studio Code를 열고 `Ctrl+Shift+P`를 누른 후 "shell command"를 입력하고 **"Shell Command: Install 'code' command in PATH"**를 선택하세요. Windows Terminal을 닫고 다시 연 다음 다시 시도하세요.

---

## 8. Node.js

**이것은:** JavaScript 런타임입니다. 많은 개발 도구들이 JavaScript로 만들어져 있어서 Node.js가 필요합니다.\
**공식 출처:** [Node.js 다운로드](https://nodejs.org/en/download)

**설치:**

```powershell
winget install --id OpenJS.NodeJS.LTS -e
```

**정상 설치 확인:**

새 터미널을 열고 다음을 입력하세요:

```powershell
node --version
```

**예상 결과:**

```
v22.x.x
```

(버전 18 이상이면 됩니다.)

---

## 9. LLM CLI 도구

**이것은:** 터미널에서 실행되는 AI 어시스턴트입니다. 명령어를 외우는 대신 자연어로 git 작업을 수행할 때 사용합니다.

이 워크숍의 기본 도구는 Claude Code입니다. Codex(OpenAI)와 Gemini CLI도 Windows에서 사용할 수 있지만, Windows 전용 설정 방법은 이 가이드에서 다루지 않습니다.

### Claude Code (Anthropic) — 권장

**필요:** Claude Max 구독 또는 Anthropic API 키\
**공식 출처:** [Claude Code 설정](https://docs.anthropic.com/en/docs/claude-code/setup)

**설치:**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**PATH 경고가 나타나는 경우** ("native installation exists but ... \.local\bin is not in your PATH"), 수동으로 추가합니다:

```powershell
$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
[Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
```

명령 실행 후 새 터미널을 여세요.

**정상 설치 확인:**

```powershell
claude --version
claude doctor
```

> **참고:** `claude doctor`에서 PATH 경고가 계속 표시될 수 있지만, 이는 알려진 오탐(false positive)이며 Claude Code는 정상 작동합니다.

**초기 설정:**

```powershell
claude
```

안내에 따라 브라우저에서 로그인하세요.

> **문제 해결 — Git Bash 경로:** `claude doctor`에서 Git Bash 경로 오류가 나오면, `~/.claude/settings.json` 파일에 경로를 직접 지정하세요:
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

## 10. 워크숍 설정

**이것은:** 워크숍 저장소를 클론하여 모든 자료와 실습 공간을 준비합니다.

> **중요 — OneDrive 폴더 주의:** `문서`, `바탕 화면`, 또는 OneDrive 폴더 안 어디에도 워크숍 폴더를 만들지 마세요. OneDrive가 이 폴더들을 자동으로 동기화하기 때문에 git 저장소와 충돌할 수 있습니다. 대신 `~/projects/workshop/` (즉 `C:\Users\사용자명\projects\workshop\`)을 사용하세요.

**1단계: 워크숍 디렉토리 만들기:**

```powershell
mkdir ~/projects/workshop
cd ~/projects/workshop
```

**2단계: 문서 저장소 클론 (교육 자료):**

```powershell
git clone https://github.com/isnbh0/git-cli-workshop.git
```

**3단계: 실습 저장소 클론 (실습 공간):**

```powershell
git clone https://github.com/isnbh0/git-cli-workshop-demo.git
```

**정상 설정 확인:**

```powershell
ls ~/projects/workshop
```

**예상 결과:**

```
git-cli-workshop    git-cli-workshop-demo
```

**준비된 것:**
- `git-cli-workshop/` — 브라우저나 VSCode에서 열어 문서를 읽으세요
- `git-cli-workshop-demo/` — 워크숍에서 git 명령어를 연습할 공간입니다

> **중요:** 모든 git 실습은 `git-cli-workshop-demo/` 안에서 합니다. 문서 저장소는 읽기 전용입니다.

> **경로 안내:** PowerShell 7에서 `~`는 `C:\Users\사용자명`으로 확장됩니다. 워크숍 문서에서 `~/projects/workshop/git-cli-workshop-demo` 같은 경로가 나오면 Windows에서도 동일하게 작동합니다.

---

## 최종 체크리스트

아래 명령어를 각각 실행하세요. 모두 에러 없이 출력이 나오면 워크숍 준비 완료입니다!

```powershell
$PSVersionTable.PSVersion
oh-my-posh --version
git --version
node --version
code --version
claude --version
claude doctor
```

| 도구 | 확인 |
|------|------|
| Windows Terminal | 열면 PowerShell 프롬프트가 보임 |
| PowerShell 7 | `$PSVersionTable.PSVersion`의 Major가 7 이상 |
| Oh My Posh | 프롬프트에 아이콘/색상 표시; `oh-my-posh --version` 작동 |
| Git for Windows | `git --version`이 버전을 표시 |
| GitHub 계정 | github.com에 로그인 가능 |
| Visual Studio Code | `code --version`이 버전을 표시 |
| Node.js | `node --version`이 v18 이상 표시 |
| Claude Code | `claude --version` 작동; `claude doctor` 통과 |
| 워크숍 저장소 | `~/projects/workshop/`에 클론 완료 |

모두 완료했나요? 워크숍 준비가 끝났습니다!
