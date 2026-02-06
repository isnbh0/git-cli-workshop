# 00 - 사전 준비

**워크숍 전에 아래 단계를 모두 완료해 주세요.** 각 단계에는 설치 방법, 예상 출력, 그리고 정상 설치 확인 방법이 포함되어 있습니다.

막히는 부분이 있으면 에러 화면을 캡처해서 강사에게 보내주세요.

---

## 1. iTerm2

**이것은:** macOS용 터미널 앱입니다. 터미널은 마우스 클릭 대신 텍스트 명령어를 입력해서 컴퓨터를 제어하는 도구입니다.\
**공식 출처:** [iTerm2 Downloads](https://iterm2.com/downloads.html)

**설치:**

1. [https://iterm2.com](https://iterm2.com) 에 접속
2. "Download" 클릭
3. 다운로드된 파일 열기
4. iTerm2를 응용 프로그램(Applications) 폴더로 드래그

**정상 설치 확인:**

응용 프로그램 폴더에서 iTerm2를 열어보세요 (또는 Spotlight: `Cmd+Space` 누르고 "iTerm" 입력 후 Enter).

**예상 결과:** 다음과 같은 텍스트 프롬프트가 있는 창이 나타납니다:

```
yourname@yourcomputer ~ %
```

> **문제 해결:** macOS에서 "확인되지 않은 개발자"라는 메시지가 나오면, 시스템 설정 → 개인 정보 보호 및 보안 → 아래로 스크롤하여 "확인 없이 열기"를 클릭하세요.

---

## 2. Xcode Command Line Tools

**이것은:** Apple에서 제공하는 개발자 도구 모음입니다. 직접 사용하진 않지만 다른 도구들이 작동하는 데 필요합니다.\
**공식 출처:** [Installing the Command Line Tools — Apple Developer](https://developer.apple.com/documentation/xcode/installing-the-command-line-tools)

**설치:**

iTerm2를 열고 다음을 입력하세요:

```bash
xcode-select --install
```

**예상 화면:** 도구를 설치할지 묻는 팝업이 나타납니다. "설치"를 클릭하고 기다리세요 (5-15분 소요).

**정상 설치 확인:**

```bash
xcode-select -p
```

**예상 결과:**

```
/Library/Developer/CommandLineTools
```

> **문제 해결:** "command line tools are already installed"라는 메시지가 나오면 이미 설치된 것이니 괜찮습니다. 설치가 실패하면 Mac을 재시작한 후 다시 시도해 보세요.

---

## 3. Homebrew

**이것은:** macOS용 패키지 관리자입니다. 터미널에서 명령어 하나로 소프트웨어를 설치할 수 있게 해주는, 개발자용 앱 스토어 같은 도구입니다.\
**공식 출처:** [Homebrew](https://brew.sh)

**설치:**

iTerm2를 열고 다음 명령어를 붙여넣으세요:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**예상 화면:** 많은 텍스트가 스크롤됩니다. 비밀번호(Mac 로그인 비밀번호)를 입력하라고 합니다. 비밀번호를 입력할 때 화면에 아무것도 표시되지 않는 것은 정상입니다. 입력 후 Enter를 누르세요.

설치 마지막에 **"Next steps"** 가 표시될 수 있습니다. **그 안내를 따라하세요** — 표시된 명령어를 복사해서 실행하세요.

**정상 설치 확인:**

iTerm2를 닫았다가 다시 열고 다음을 입력하세요:

```bash
brew --version
```

**예상 결과:**

```
Homebrew 4.x.x
```

> **문제 해결:** "command not found: brew"가 나오면 설치 마지막에 표시된 "Next steps" 명령어를 실행해야 합니다. `eval`이나 `echo`로 시작하는 줄을 찾아서 복사하여 실행하세요.

---

## 4. uv

**이것은:** Python 패키지 관리자입니다. 향후 세션에서 Python 스크립트를 실행할 때 사용합니다.\
**공식 출처:** [uv Installation — Astral Docs](https://docs.astral.sh/uv/getting-started/installation/)

**설치:**

```bash
brew install uv
```

**예상 화면:** Homebrew가 uv를 다운로드하고 설치합니다. 보통 1분 이내에 완료됩니다.

**정상 설치 확인:**

```bash
uv --version
```

**예상 결과:**

```
uv 0.x.x
```

---

## 5. Node.js

**이것은:** JavaScript 런타임입니다. 많은 개발 도구들이 JavaScript로 만들어져 있어서 Node.js가 필요합니다.\
**공식 출처:** [Download Node.js via Package Manager](https://nodejs.org/en/download/package-manager)

**설치:**

```bash
brew install node
```

**예상 화면:** Homebrew가 Node.js와 npm(패키지 관리자)을 다운로드하고 설치합니다.

**정상 설치 확인:**

```bash
node --version
```

**예상 결과:**

```
v22.x.x
```

(버전 18 이상이면 됩니다.)

---

## 6. Visual Studio Code

**이것은:** 파일을 작성하고 편집하는 텍스트 에디터입니다. "여러 파일을 다룰 수 있는 메모장" 같은 것으로, 워크숍에서 파일 편집에 사용합니다.\
**공식 출처:** [Visual Studio Code on macOS](https://code.visualstudio.com/docs/setup/mac)

**설치:**

```bash
brew install --cask visual-studio-code
```

**정상 설치 확인:**

```bash
code --version
```

**예상 결과:**

```
1.x.x
(해시 문자열)
(아키텍처)
```

> **문제 해결:** "command not found: code"가 나오면, Visual Studio Code를 직접 열고(응용 프로그램에서), `Cmd+Shift+P`를 눌러 명령 팔레트를 열고, "shell command"를 입력한 후 **"Shell Command: Install 'code' command in PATH"** 를 선택하세요. iTerm2를 닫았다가 다시 열고 `code --version`을 다시 시도하세요.

---

## 7. LLM CLI 도구 (하나 선택)

**이것은:** 터미널에서 실행되는 AI 어시스턴트입니다. 명령어를 외우는 대신 자연어로 git 작업을 수행할 때 사용합니다.\
**공식 출처:** [Claude Code Setup](https://docs.anthropic.com/en/docs/claude-code/setup) | [Codex CLI Quickstart](https://developers.openai.com/codex/quickstart) | [Gemini CLI Installation](https://geminicli.com/docs/get-started/installation/)

이미 가지고 있는 구독에 따라 **하나**를 선택하세요:

### 옵션 A: Claude Code (Anthropic)

**필요:** Claude Max 구독 또는 Anthropic API 키

**설치:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**정상 설치 확인:**

iTerm2를 닫았다가 다시 열고:

```bash
claude --version
```

**초기 설정:** 터미널에서 `claude`를 실행하고 안내에 따라 로그인하세요.

### 옵션 B: Codex (OpenAI)

**필요:** ChatGPT Plus/Pro 구독 또는 OpenAI API 키

**설치:**

```bash
brew install codex
```

**정상 설치 확인:**

```bash
codex --version
```

**초기 설정:** 터미널에서 `codex`를 실행하고 안내에 따라 로그인하세요.

### 옵션 C: Gemini CLI (Google)

**필요:** Google 계정 (무료 등급 가능)

**설치:**

```bash
brew install gemini-cli
```

**정상 설치 확인:**

```bash
gemini --version
```

**초기 설정:** 터미널에서 `gemini`을 실행하고 안내에 따라 인증하세요.

---

## 8. iTerm2 자연스러운 텍스트 편집 설정

**이것은:** 터미널에서 익숙한 단축키(예: Option+좌/우 화살표로 단어 단위 이동)를 사용할 수 있게 해주는 키보드 설정입니다.\
**공식 출처:** [iTerm2 Keys Profiles Preferences](https://iterm2.com/documentation-preferences-profiles-keys.html)

**설정:**

1. iTerm2 열기
2. **iTerm2 → Settings** (또는 `Cmd+,` 누르기)
3. **Profiles** 탭 클릭
4. **Keys** 하위 탭 클릭
5. **Key Mappings** 하위 탭 클릭
6. 하단의 **Presets...** 드롭다운 클릭
7. **Natural Text Editing** 선택

**정상 설정 확인:**

iTerm2에서 텍스트를 입력한 후 `Option+Left`와 `Option+Right`를 눌러보세요.

**예상 결과:** 커서가 한 단어씩 이동합니다 (특수 문자가 출력되는 대신).

---

## 9. GitHub 계정

**이것은:** 코드 프로젝트를 저장하고 공유하는 웹사이트입니다. 워크숍에서 작업물을 업로드할 때 사용합니다.\
**공식 출처:** [GitHub](https://github.com)

**설정:**

1. [https://github.com](https://github.com) 에 접속
2. "Sign up" 클릭
3. 안내에 따라 계정 생성
4. 사용자명과 이메일을 기억해두세요 — 워크숍에서 필요합니다

**정상 설정 확인:** [https://github.com](https://github.com) 에 로그인하여 대시보드가 보이는지 확인하세요.

---

## 최종 체크리스트

아래 명령어를 각각 실행하세요. 모두 에러 없이 출력이 나오면 워크숍 준비 완료입니다!

```bash
xcode-select -p
brew --version
uv --version
node --version
code --version
```

설치한 LLM CLI 도구도 확인하세요:

```bash
claude --version   # Claude Code를 선택한 경우
codex --version    # Codex를 선택한 경우
gemini --version   # Gemini CLI를 선택한 경우
```

| 도구 | 확인 |
|------|------|
| iTerm2 | 열면 프롬프트가 보임 |
| Xcode Command Line Tools | `xcode-select -p`가 경로를 표시 |
| Homebrew | `brew --version`이 버전을 표시 |
| uv | `uv --version`이 버전을 표시 |
| Node.js | `node --version`이 v18 이상 표시 |
| Visual Studio Code | `code --version`이 버전을 표시 |
| LLM CLI 도구 | 버전 명령어가 작동 |
| iTerm2 자연스러운 텍스트 편집 | Option+화살표로 단어 단위 이동 |
| GitHub 계정 | github.com에 로그인 가능 |

모두 완료했나요? 워크숍 준비가 끝났습니다!
