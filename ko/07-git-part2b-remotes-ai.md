# 07 - Git Part 2b: AI와 함께하는 리모트

**이 섹션에서는 동일한 리모트 git 작업을 다시 해봅니다 — 하지만 이번에는 명령어를 직접 입력하는 대신 AI와 대화합니다.** 푸시, 풀, 리모트가 무엇인지 이해했으니, AI가 문법을 처리하도록 하고 여러분은 하고 싶은 것에 집중하면 됩니다.

---

## 1. 소개

이전 섹션에서는 리모트 관련 git 명령어를 모두 직접 타이핑했습니다. 이제 리모트가 무엇인지, `push`가 어떻게 작업을 업로드하는지, `pull`이 어떻게 변경 사항을 다운로드하는지 이해했습니다.

로컬 git과 마찬가지로, 이 명령어들을 외울 필요가 없습니다. "푸시"가 무엇인지 알면 AI에게 "내 변경 사항을 GitHub에 올려줘"라고 말할 수 있고, AI가 적절한 명령어를 알아냅니다.

---

## 2. 리모트 작업을 위한 프롬프트 예시

자연어가 배운 리모트 명령어와 어떻게 대응되는지 살펴봅시다:

| 하고 싶은 것 | AI에게 말하는 내용 | 실행되는 명령어 |
|---|---|---|
| GitHub에 연결 | "이 저장소를 git@github.com:USERNAME/my-workshop-demo.git에 있는 GitHub 저장소에 연결해줘" | `git remote add origin <URL>` |
| 리모트 연결 확인 | "어떤 리모트가 연결되어 있는지 보여줘" | `git remote -v` |
| 작업 업로드 | "내 커밋을 GitHub에 푸시해줘" | `git push` |
| 처음으로 업로드 | "내 커밋을 GitHub에 푸시하고 트래킹 설정해줘" | `git push -u origin main` |
| 최신 변경 사항 다운로드 | "GitHub에서 최신 변경 사항을 가져와줘" | `git pull` |
| GitHub 저장소 만들기 | "my-workshop-demo라는 새 GitHub 저장소를 만들어줘" | `gh repo create` |
| 최신 상태인지 확인 | "GitHub과 동기화되어 있어?" | `git status` + `git fetch` |

> **참고:** 정확히 이 문구를 사용할 필요는 없습니다. "작업 올려줘", "변경 사항을 GitHub에 보내줘", "origin에 푸시해줘" 등 다 통합니다.

---

## 3. 가이드 실습

LLM CLI 도구를 사용하여 Part 2a의 흐름을 다시 해봅시다.

### 1단계: LLM CLI 도구 시작하기

iTerm2를 열고 데모 저장소 폴더로 이동한 다음 도구를 실행합니다:

```bash
cd ~/workshop/git-cli-workshop-demo
```

설치한 도구를 시작합니다:

| 도구 | 명령어 |
|------|--------|
| Claude Code | `claude` |
| Codex | `codex` |
| Gemini CLI | `gemini` |

> **참고:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) | [OpenAI Codex CLI](https://github.com/openai/codex) | [Gemini CLI](https://github.com/google-gemini/gemini-cli)

### 2단계: 리모트 상태 확인

다음과 같이 입력합니다:

> "현재 git 상태와 어떤 리모트가 연결되어 있는지 보여줘"

AI가 `git status`와 `git remote -v`를 실행하고 결과를 보여줍니다.

### 3단계: GitHub 저장소 만들기 (아직 만들지 않은 경우)

AI에게 GitHub 저장소를 만들어 달라고 할 수 있습니다:

> "my-workshop-demo-ai라는 새 공개 GitHub 저장소를 만들고 이 로컬 저장소에 연결해줘"

AI가 `gh repo create`와 `git remote add`를 사용하여 모든 것을 설정합니다.

> **참고:** 이것은 사전 준비 섹션에서 설치한 `gh` CLI 도구 (GitHub CLI)를 사용합니다. Part 2a에서 이미 저장소를 만들었다면 이 단계를 건너뛰거나 다른 저장소 이름을 사용할 수 있습니다.

> **참고:** [gh repo create — GitHub CLI 매뉴얼](https://cli.github.com/manual/gh_repo_create)

### 4단계: 작업 푸시하기

> "내 모든 커밋을 GitHub에 푸시해줘"

AI가 `git push` (또는 처음이라면 `git push -u origin main`)를 실행합니다.

### 5단계: GitHub에서 확인하기

> "내 GitHub 저장소 URL이 뭐야?"

AI가 URL을 보여줍니다. 브라우저에서 열어 파일이 있는지 확인합니다.

### 6단계: 변경하고 푸시하기

VSCode에서 `TODO.md`를 편집하여 새 항목을 추가합니다. `Cmd+S`로 저장합니다. 그런 다음:

> "TODO.md의 변경 사항을 'Add new task'라는 메시지로 커밋하고 GitHub에 푸시해줘"

AI가 스테이징, 커밋, 푸시를 한 번에 처리합니다.

### 7단계: 변경 사항 가져오기

GitHub.com에서 파일을 편집합니다 (Part 2a에서 배운 웹 에디터를 사용). 그런 다음:

> "GitHub에서 최신 변경 사항을 가져와줘"

AI가 `git pull`을 실행하고 로컬 파일이 업데이트됩니다.

### 8단계: 동기화 상태 확인

> "GitHub과 최신 상태인지 확인해줘. 차이점이 있으면 보여줘."

AI가 로컬 사본이 GitHub의 내용과 일치하는지 확인합니다.

---

## 4. 핵심 통찰

Part 1b와 같은 패턴을 주목하세요: Part 2a와 정확히 같은 리모트 작업 — remote add, push, pull — 을 했지만, 명령어를 기억할 필요가 없었습니다.

**개념을 이해하는 것이 중요합니다:**

- **리모트** = 다른 컴퓨터(GitHub 같은)에 있는 프로젝트 사본
- **Origin** = 메인 리모트의 별명
- **푸시** = 로컬 커밋을 리모트에 업로드
- **풀** = 리모트 커밋을 로컬 컴퓨터에 다운로드

이 개념들을 이해하면, 원하는 것을 자연어로 표현할 수 있습니다. AI가 여러분의 의도를 올바른 git 명령어로 변환합니다.

**리모트 작업에서 특히 유용합니다.** 명령어가 복잡해질 수 있기 때문입니다 — 처음 푸시와 이후 푸시의 플래그 차이, SSH vs. HTTPS URL, 트래킹 브랜치 등. 세부 사항은 AI에게 맡기고 여러분은 의도에 집중하세요: "내 작업을 GitHub에 올려줘" 또는 "최신 변경 사항을 가져와줘."

---

## 5. 명령어 직접 입력 vs. AI 사용

Part 1b의 가이드를 확장합니다:

| 상황 | 권장 방식 |
|------|-----------|
| 간단한 push/pull | `git push` 또는 `git pull`을 직접 입력 — 빠릅니다 |
| 새 리모트를 처음 설정할 때 | AI에게 요청 — 플래그를 잊기 쉽습니다 |
| 터미널에서 GitHub 저장소를 만들 때 | AI에게 요청 — `gh repo create`에 많은 옵션이 있습니다 |
| push/pull 오류 해결 | AI에게 요청 — 문제를 진단하고 해결할 수 있습니다 |
| 동기화 상태 확인 | AI에게 요청 — 여러 명령어를 조합할 수 있습니다 |

> **팁:** push나 pull 오류가 발생하고 이해되지 않으면, 오류 메시지를 AI에게 보여주고 "이게 무슨 뜻이고 어떻게 해결해?"라고 물어보세요.

---

리모트 섹션을 모두 완료했습니다 — 직접 명령어를 입력하는 방법과 AI를 사용하는 방법 모두. 이제 작업을 백업하고, GitHub에 공유하고, 다른 사람과 협업할 수 있습니다. 이것은 실제 환경에서 git을 사용하는 기본기입니다.
