# 04 - Git Part 1a: 로컬 Git (직접 실습)

**이 섹션에서는 자신의 컴퓨터에서 git을 사용하여 파일 변경 사항을 추적하는 방법을 배웁니다.** 개인 할 일 목록을 만들면서 핵심 git 명령어를 하나씩 연습합니다.

---

## Git이란?

Git은 파일을 위한 **타임라인 관리자**입니다. 여러분이 원하는 순간에 프로젝트의 **스냅샷** ("커밋"이라고 부릅니다)을 찍습니다. 어떤 스냅샷이든 돌아가서 볼 수 있고, 정확히 무엇이 바뀌었는지 확인하고, 실수를 되돌릴 수 있습니다.

Google Docs의 버전 기록과 비슷하지만 — 문서뿐만 아니라 모든 파일에 적용되며, 훨씬 더 강력합니다:

- **스냅샷:** 프로젝트 전체의 특정 시점 저장본
- **타임라인:** 모든 스냅샷이 이어지는 순서
- **여러분이 직접** 언제 스냅샷을 찍을지, 무엇을 포함할지 결정합니다

직접 해봅시다.

---

## 1. 프로젝트 폴더 만들고 Git 초기화하기

iTerm2를 열고 다음을 입력하세요:

```bash
mkdir my-todo-list
cd my-todo-list
git init
```

**어떤 일이 생기나요:** 새 폴더를 만들고, 그 안으로 이동한 다음, git에게 이 폴더를 감시하라고 알려줍니다.

**예상 결과 (`git init`):**

```
Initialized empty Git repository in /Users/yourname/my-todo-list/.git/
```

**확인 방법:**

```bash
ls -la
```

**예상 결과:** 목록에 `.git` 폴더가 보여야 합니다. (`-la` 플래그는 `.`으로 시작하는 숨김 파일을 보여줍니다.)

```
total 0
drwxr-xr-x   3 yourname  staff   96 Jan  1 10:00 .
drwxr-xr-x   5 yourname  staff  160 Jan  1 10:00 ..
drwxr-xr-x   9 yourname  staff  288 Jan  1 10:00 .git
```

> **`.git` 폴더는 뭔가요?** git이 모든 데이터를 저장하는 곳입니다 — 스냅샷, 타임라인, 모든 것. 이 폴더 안을 직접 볼 필요는 없습니다. 이 폴더가 있으면 git이 이 프로젝트에서 활성화되어 있다는 것만 알면 됩니다.

---

## 2. Git 사용자 정보 설정하기

Git은 모든 스냅샷에 여러분의 이름과 이메일을 기록합니다. 설정해 봅시다:

```bash
git config user.name "Your Name"
git config user.email "your@email.com"
```

**어떤 일이 생기나요:** 출력이 없습니다 (정상입니다). Git이 이 프로젝트에 대한 설정을 저장합니다.

**확인 방법:**

```bash
git config user.name
git config user.email
```

**예상 결과:** 입력한 이름과 이메일이 출력됩니다.

> **참고:** `"Your Name"`과 `"your@email.com"`을 여러분의 실제 이름과 GitHub 계정에 사용한 이메일로 바꾸세요.

---

## 3. 첫 번째 파일 만들기

프로젝트를 VSCode에서 열어봅시다:

```bash
code .
```

VSCode에서:
1. 사이드바에 마우스를 올리고 "새 파일" 아이콘 클릭
2. 파일 이름을 `TODO.md`로 입력
3. 다음 내용을 입력:

```markdown
# My To-Do List

## Today
- [ ] Buy groceries
- [ ] Reply to emails
```

4. `Cmd+S`를 눌러 저장

**방금 작성한 내용:** 마크다운 문법입니다. `#`은 제목, `##`은 작은 제목, `- [ ]`은 체크박스 항목을 만듭니다. VSCode에서 `Cmd+Shift+V`를 누르면 깔끔하게 렌더링된 모습을 볼 수 있습니다.

---

## 4. 상태 확인하기

iTerm2로 돌아가서 다음을 입력하세요:

```bash
git status
```

**예상 결과:**

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	TODO.md

nothing added to commit but untracked files present (use "git add" to track)
```

**이것이 의미하는 것:** Git이 `TODO.md`를 빨간색(추적되지 않음)으로 표시합니다. git이 파일이 있다는 것은 알지만 아직 추적하지 않고 있다는 뜻입니다. 문서를 책상 위에 올려놓은 것과 같습니다 — 거기 있지만, 아직 정리하지 않은 상태입니다.

---

## 5. 파일 스테이징하기

"스테이징"이란 다음 스냅샷에 포함할 파일을 git에게 알려주는 것입니다. 파일을 "스냅샷 바구니"에 넣는다고 생각하세요.

```bash
git add TODO.md
```

**예상 결과:** 출력이 없습니다 (정상입니다).

**확인 방법:**

```bash
git status
```

**예상 결과:**

```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   TODO.md
```

**이것이 의미하는 것:** `TODO.md`가 이제 초록색(스테이징됨)입니다. 스냅샷 바구니에 들어가서, 저장할 준비가 된 상태입니다.

---

## 6. 스냅샷 찍기 (커밋)

이제 실제로 스냅샷을 찍어봅시다:

```bash
git commit -m "Add initial to-do list"
```

**`-m`이 뭔가요:** `-m` 플래그는 이 스냅샷에 대한 짧은 설명을 붙입니다. 항상 의미 있는 메시지를 작성하세요 — 미래의 자신이 감사할 것입니다.

**예상 결과:**

```
[main (root-commit) abc1234] Add initial to-do list
 1 file changed, 5 insertions(+)
 create mode 100644 TODO.md
```

**확인 방법:**

```bash
git status
```

**예상 결과:**

```
On branch main
nothing to commit, working tree clean
```

**"clean working tree"란:** 프로젝트의 모든 것이 최신 스냅샷과 일치한다는 뜻입니다. 저장하지 않은 변경 사항이 없습니다.

---

## 7. 타임라인 보기

```bash
git log
```

**예상 결과:**

```
commit abc1234567890abcdef1234567890abcdef123456 (HEAD -> main)
Author: Your Name <your@email.com>
Date:   Wed Jan 1 10:05:00 2025 +0900

    Add initial to-do list
```

**각 부분의 의미:**

| 부분 | 의미 |
|------|------|
| `commit abc123...` | 이 스냅샷의 고유 ID ("해시"라고 불리는 긴 코드) |
| `HEAD -> main` | `main` 브랜치의 최신 스냅샷 (브랜치는 나중에 다룹니다) |
| `Author` | 누가 이 스냅샷을 만들었는지 (설정한 이름/이메일) |
| `Date` | 언제 스냅샷을 찍었는지 |
| `Add initial to-do list` | `-m`으로 작성한 메시지 |

> **팁:** 로그가 화면을 가득 채우면 `q`를 눌러 빠져나올 수 있습니다.

---

## 8. 변경하기

VSCode로 돌아가서 `TODO.md`를 편집합니다. 할 일을 완료 표시하고, 새 항목을 추가하고, Notes 섹션을 만들어 봅시다:

```markdown
# My To-Do List

## Today
- [x] Buy groceries
- [ ] Reply to emails
- [ ] Read a book

## Notes
Here are some things I want to remember...
```

`Cmd+S`를 눌러 저장합니다.

**바뀐 것:** "Buy groceries"를 완료 표시(`[ ]`를 `[x]`로 변경)하고, "Read a book"을 추가하고, 새로운 "Notes" 섹션을 만들었습니다.

---

## 9. 무엇이 바뀌었는지 확인하기

```bash
git diff
```

**예상 결과:**

```diff
diff --git a/TODO.md b/TODO.md
index abc1234..def5678 100644
--- a/TODO.md
+++ b/TODO.md
@@ -1,5 +1,9 @@
 # My To-Do List

 ## Today
-- [ ] Buy groceries
+- [x] Buy groceries
 - [ ] Reply to emails
+- [ ] Read a book
+
+## Notes
+Here are some things I want to remember...
```

**읽는 방법:**

| 기호 | 의미 |
|------|------|
| `-`로 시작하는 줄 (빨간색) | 삭제되거나 변경된 내용 |
| `+`로 시작하는 줄 (초록색) | 추가되거나 변경된 내용 |
| 기호 없는 줄 | 변경 사항 주변의 맥락 — 바뀌지 않은 줄 |

체크박스가 `[ ]`에서 `[x]`로 바뀌고, 새 항목이 추가되고, Notes 섹션이 새로 생긴 것을 볼 수 있습니다.

> **팁:** `q`를 눌러 diff 화면에서 나올 수 있습니다.

---

## 10. 다시 스테이징하고 커밋하기

```bash
git add TODO.md
git commit -m "Check off groceries, add reading and notes"
```

**예상 결과:**

```
[main def5678] Check off groceries, add reading and notes
 1 file changed, 6 insertions(+), 1 deletion(-)
```

---

## 11. 두 개의 스냅샷이 있는 타임라인 보기

```bash
git log
```

**예상 결과:**

```
commit def5678901234567890abcdef1234567890abcdef (HEAD -> main)
Author: Your Name <your@email.com>
Date:   Wed Jan 1 10:15:00 2025 +0900

    Check off groceries, add reading and notes

commit abc1234567890abcdef1234567890abcdef123456
Author: Your Name <your@email.com>
Date:   Wed Jan 1 10:05:00 2025 +0900

    Add initial to-do list
```

**보이는 것:** 타임라인에 두 개의 스냅샷이 있으며, 최신 것이 먼저 표시됩니다. 각 변경이 언제, 어떤 내용으로 이루어졌는지 정확히 볼 수 있습니다.

> **팁:** 더 간결하게 보려면 `git log --oneline`을 사용해 보세요:
>
> ```
> def5678 Check off groceries, add reading and notes
> abc1234 Add initial to-do list
> ```

---

## 12. 변경 사항 되돌리기

실수를 복구하는 연습을 해봅시다.

**1단계: 잘못된 편집을 합니다.** VSCode에서 `TODO.md`의 모든 텍스트를 선택(`Cmd+A`)하고, 삭제하고, 저장(`Cmd+S`)합니다. 이제 파일이 비어 있습니다.

**2단계: 피해를 확인합니다:**

```bash
git status
```

**예상 결과:**

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   TODO.md
```

```bash
git diff
```

**예상 결과:** 모든 내용이 빨간색(삭제됨)으로 표시됩니다.

**3단계: 마지막 스냅샷에서 파일을 복원합니다:**

```bash
git restore TODO.md
```

**예상 결과:** 출력이 없습니다.

**4단계: 복구를 확인합니다:**

VSCode에서 `TODO.md`를 열어보세요 — 모든 내용이 돌아와 있습니다! 터미널에서도 확인할 수 있습니다:

```bash
git status
```

**예상 결과:**

```
On branch main
nothing to commit, working tree clean
```

**무슨 일이 있었나요:** git에게 "이 파일의 현재 변경 사항을 버리고 마지막으로 저장된 스냅샷으로 돌아가라"고 했습니다. 이것이 git의 강력한 기능 중 하나입니다 — 저장된 스냅샷이 있으면 언제든 돌아갈 수 있습니다.

> **참고:** `git restore`는 아직 커밋하지 않은 변경 사항에만 작동합니다. 이미 커밋한 내용은 타임라인의 일부가 되며, 되돌리려면 다른 명령어가 필요합니다 — 나중에 다루겠습니다.

---

## 13. 자유 연습

이제 로컬 git의 핵심 명령어를 모두 배웠습니다. 5-10분 동안 자유롭게 연습해 보세요:

1. VSCode에서 `SANDBOX.md`라는 새 파일을 만드세요
2. 원하는 내용을 작성하세요 — 메모, 이야기, 레시피, 무엇이든
3. 워크플로우를 연습하세요:
   - `git status` — 무엇이 바뀌었는지 보기
   - `git add SANDBOX.md` — 스테이징하기
   - `git commit -m "여기에 메시지"` — 스냅샷 찍기
   - `git log` — 타임라인 보기
4. 더 수정한 다음, 커밋하기 전에 `git diff`로 변경 사항 확인하기
5. 일부러 잘못된 편집을 하고 `git restore`로 복구해 보기

---

## 빠른 참고

배운 모든 명령어 요약:

| 명령어 | 하는 일 |
|--------|---------|
| `git init` | 폴더를 git으로 추적 시작 |
| `git config user.name "..."` | 커밋에 사용할 이름 설정 |
| `git config user.email "..."` | 커밋에 사용할 이메일 설정 |
| `git status` | 어떤 파일이 변경되었는지 확인 |
| `git add <파일>` | 다음 스냅샷에 파일 스테이징 |
| `git commit -m "메시지"` | 설명을 붙여 스냅샷 찍기 |
| `git log` | 스냅샷 타임라인 보기 |
| `git diff` | 마지막 스냅샷 이후 변경 사항 보기 |
| `git restore <파일>` | 파일 변경 사항 되돌리기 (마지막 스냅샷으로) |

---

잘 하셨습니다! 이제 핵심 git 워크플로우를 이해했습니다: **편집 → status → add → commit → log**. 다음 섹션에서는 명령어를 직접 입력하는 대신 AI와 대화하며 같은 작업을 하는 방법을 알아봅니다.

---

## 참고 자료

이 섹션에서 사용한 각 git 명령어의 공식 문서:

- [git init](https://git-scm.com/docs/git-init) — 빈 Git 저장소 생성
- [git config](https://git-scm.com/docs/git-config) — 저장소 또는 전역 옵션 설정
- [git status](https://git-scm.com/docs/git-status) — 작업 트리 상태 표시
- [git add](https://git-scm.com/docs/git-add) — 파일 내용을 인덱스(스테이징 영역)에 추가
- [git commit](https://git-scm.com/docs/git-commit) — 변경 사항을 저장소에 기록
- [git log](https://git-scm.com/docs/git-log) — 커밋 로그 표시
- [git diff](https://git-scm.com/docs/git-diff) — 커밋 간, 커밋과 작업 트리 간 변경 사항 표시
- [git restore](https://git-scm.com/docs/git-restore) — 작업 트리 파일 복원
- [Git 최초 설정 (Pro Git Book)](https://git-scm.com/book/ko/v2/시작하기-Git-최초-설정) — 초기 설정 안내
