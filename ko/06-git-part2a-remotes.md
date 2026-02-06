# 06 - Git Part 2a: 리모트 (직접 실습)

**이 섹션에서는 로컬 git 프로젝트를 GitHub에 연결하여 작업을 백업하고, 공유하고, 다른 사람과 협업하는 방법을 배웁니다.** 지금까지 만들어온 할 일 목록 프로젝트를 온라인에 올려봅시다.

---

## 큰 그림

지금까지 git은 여러분의 컴퓨터에서만 파일을 추적하고 있었습니다. 스냅샷, 타임라인, 파일 — 모든 것이 여러분의 컴퓨터에만 있습니다. 컴퓨터가 고장나면 전부 사라집니다.

**리모트(remote)**는 다른 컴퓨터(인터넷의 서버 같은)에 저장된 프로젝트의 사본입니다. 이것은 세 가지 강력한 기능을 제공합니다:

- **백업:** 노트북이 고장나도 작업이 안전합니다
- **공유:** 다른 사람들이 여러분의 프로젝트를 볼 수 있습니다
- **협업:** 여러 사람이 같은 프로젝트에서 함께 작업할 수 있습니다

**GitHub.com**은 git 리모트를 호스팅하는 웹사이트입니다. 코드 프로젝트를 위한 소셜 미디어 사이트라고 생각하세요 — 다른 사람의 프로젝트를 구경하고, 자신의 프로젝트를 공유하고, 함께 작업할 수 있습니다.

> **참고:** [Pro Git — 리모트 저장소](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)

---

## 1. GitHub.com 둘러보기

브라우저를 열고 [github.com](https://github.com)에 접속합니다.

로그인하면 대시보드가 보입니다. GitHub에서 저장소(프로젝트)가 어떻게 보이는지 살펴봅시다. 잘 알려진 저장소를 방문해 보세요:

```
https://github.com/torvalds/linux
```

**보이는 것:**

| 부분 | 보여주는 내용 |
|------|---------------|
| 파일 목록 | 프로젝트의 모든 파일, 컴퓨터의 폴더처럼 |
| 커밋 | 스냅샷 이력 (`git log`와 동일) |
| README | 프로젝트 설명, 페이지 하단에 깔끔하게 렌더링됨 |
| 초록색 "Code" 버튼 | 프로젝트를 다운로드하거나 클론하는 방법 |

> **핵심:** GitHub 저장소는 인터넷에 호스팅된 git 프로젝트일 뿐입니다. 로컬 git 프로젝트와 동일한 스냅샷, 동일한 타임라인, 동일한 파일을 갖고 있습니다. GitHub이 거기에 멋진 웹 인터페이스를 추가한 것입니다.

---

## 2. GitHub에 새 저장소 만들기

이제 할 일 목록 프로젝트를 저장할 공간을 GitHub에 만들어 봅시다.

**1단계:** [github.com](https://github.com)에서 오른쪽 상단의 **"+"** 버튼을 클릭하고 **"New repository"**를 선택합니다.

**2단계:** 세부 사항을 입력합니다:

| 항목 | 입력할 내용 |
|------|-------------|
| Repository name | `my-workshop-demo` |
| Description | (선택) "My personal to-do list" |
| Visibility | Public 또는 Private — 원하는 대로 |
| Initialize this repository | 어떤 체크박스도 **체크하지 마세요** (README 없음, .gitignore 없음, license 없음) |

> **왜 README를 안 만드나요?** 로컬 프로젝트에 이미 파일이 있기 때문입니다. GitHub에서도 파일을 만들면 충돌이 생깁니다. 기존 작업을 올릴 수 있는 빈 저장소가 필요합니다.

> **참고:** [GitHub Docs — 새 저장소 만들기](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)

**3단계:** **"Create repository"**를 클릭합니다.

**4단계:** 설정 페이지가 나타납니다. **"...or push an existing repository from the command line"** 섹션을 찾습니다. SSH URL을 복사합니다 — 다음과 같은 형태입니다:

```
git@github.com:USERNAME/my-workshop-demo.git
```

> **참고:** `USERNAME`을 여러분의 실제 GitHub 사용자 이름으로 바꾸세요. HTTPS URL(`https://`로 시작)이 보이면 "SSH" 버튼을 클릭하여 전환하세요.

---

## 3. 로컬 저장소를 GitHub에 연결하기

iTerm2를 열고 데모 저장소 폴더로 이동합니다:

```bash
cd ~/workshop/git-cli-workshop-demo
```

이제 git에게 리모트 위치를 알려줍니다:

```bash
git remote add origin git@github.com:USERNAME/my-workshop-demo.git
```

**각 부분의 의미:**

| 부분 | 의미 |
|------|------|
| `git remote add` | "새 리모트 연결을 추가해라" |
| `origin` | 이 리모트의 별명 (휴대폰의 연락처 이름과 같음) |
| `git@github.com:USERNAME/...` | 리모트의 실제 주소 (전화번호와 같음) |

> **왜 "origin"인가요?** 관례입니다 — 메인 리모트의 기본 이름입니다. 아무 이름이나 붙일 수 있지만, 모두가 `origin`을 사용합니다.

**확인 방법:**

```bash
git remote -v
```

**예상 결과:**

```
origin	git@github.com:USERNAME/my-workshop-demo.git (fetch)
origin	git@github.com:USERNAME/my-workshop-demo.git (push)
```

**이것이 의미하는 것:** `origin`이라는 리모트가 두 방향으로 설정되어 있습니다 — `fetch` (다운로드)와 `push` (업로드). 둘 다 여러분의 GitHub 저장소를 가리킵니다.

> **참고:** [git-remote 문서](https://git-scm.com/docs/git-remote)

---

## 4. 커밋을 GitHub에 푸시하기

이제 로컬 스냅샷을 GitHub에 업로드합니다:

```bash
git push -u origin main
```

**각 부분의 의미:**

| 부분 | 의미 |
|------|------|
| `git push` | "내 커밋을 리모트에 업로드해라" |
| `-u` | "이 연결을 기억해라" (다음부터는 `git push`만 입력하면 됨) |
| `origin` | 어떤 리모트에 푸시할지 (방금 추가한 GitHub 리모트) |
| `main` | 어떤 브랜치를 푸시할지 (메인 타임라인) |

**예상 결과:**

```
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (9/9), 789 bytes | 789.00 KiB/s, done.
Total 9 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To github.com:USERNAME/my-workshop-demo.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

**확인 방법:**

1. 브라우저로 돌아갑니다
2. GitHub 저장소 페이지를 새로고침합니다 (`github.com/USERNAME/my-workshop-demo`)
3. 파일이 보여야 합니다 — `TODO.md`, `GOALS.md`, `SANDBOX.md` (그리고 만든 다른 파일들)

> **무슨 일이 있었나요:** 모든 로컬 스냅샷이 GitHub에 복사되었습니다. 링크가 있는 누구나 여러분의 프로젝트를 볼 수 있습니다 (공개인 경우). 커밋 이력도 있습니다 — GitHub에서 "commits"를 클릭하면 확인할 수 있습니다.

> **참고:** [git-push 문서](https://git-scm.com/docs/git-push)

---

## 5. 변경하고, 커밋하고, 푸시하기

이제 전체 워크플로우를 연습합시다: 로컬에서 편집하고, 커밋하고, GitHub에 푸시합니다.

**1단계:** VSCode에서 `TODO.md`를 열고 새 항목을 추가합니다:

```markdown
# My To-Do List

## Today
- [x] Buy groceries
- [ ] Reply to emails
- [ ] Read a book
- [ ] Push my project to GitHub

## Notes
Here are some things I want to remember...
```

`Cmd+S`로 저장합니다.

**2단계:** 스테이징하고 커밋합니다:

```bash
git add TODO.md
git commit -m "Add GitHub task to to-do list"
```

**예상 결과:**

```
[main abc1234] Add GitHub task to to-do list
 1 file changed, 1 insertion(+)
```

**3단계:** GitHub에 푸시합니다:

```bash
git push
```

**어떤 일이 생기나요:** 처음에 `-u`를 사용했기 때문에 git이 어디에 푸시할지 기억합니다. 더 이상 `origin main`을 입력할 필요가 없습니다.

**예상 결과:**

```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 312 bytes | 312.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:USERNAME/my-workshop-demo.git
   def5678..abc1234  main -> main
```

**확인 방법:** GitHub 페이지를 새로고침합니다. `TODO.md`를 클릭하면 새로운 "Push my project to GitHub" 항목이 보입니다. "commits"를 클릭하면 최신 커밋 메시지가 보입니다.

---

## 6. GitHub에서 변경 사항 가져오기 (Pull)

때로는 로컬에 없는 변경 사항이 GitHub에 있을 수 있습니다. 이런 경우가 있습니다:

- 여러분(또는 협업자)이 GitHub 웹사이트에서 직접 파일을 편집한 경우
- 협업자가 자신의 컴퓨터에서 변경 사항을 푸시한 경우
- 다른 컴퓨터에서 작업하고 거기서 푸시한 경우

GitHub에서 직접 파일을 편집하여 이 상황을 만들어 봅시다.

**1단계: GitHub.com에서 파일 편집하기**

1. GitHub의 저장소 페이지로 이동합니다 (`github.com/USERNAME/my-workshop-demo`)
2. `TODO.md`를 클릭합니다
3. 파일 보기 오른쪽 상단의 **연필 아이콘** (편집 버튼)을 클릭합니다
4. 목록에 새 항목을 추가합니다:

```markdown
- [ ] Learn about git remotes
```

5. "Commit changes"까지 스크롤합니다
6. 커밋 메시지를 입력합니다: `Add remotes task from GitHub`
7. **"Commit changes"**를 클릭합니다

> **참고:** [GitHub Docs — 파일 편집하기](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)

**2단계: 로컬 파일 확인하기**

iTerm2로 돌아가서 `TODO.md`를 확인합니다:

```bash
git log --oneline
```

**보이는 것:** 로컬 로그에는 방금 GitHub에서 만든 커밋이 없습니다. 로컬 사본이 뒤처져 있습니다.

**3단계: 변경 사항 가져오기**

```bash
git pull
```

**예상 결과:**

```
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:USERNAME/my-workshop-demo
   abc1234..ghi7890  main       -> origin/main
Updating abc1234..ghi7890
Fast-forward
 TODO.md | 1 +
 1 file changed, 1 insertion(+)
```

**4단계: 확인하기**

```bash
git log --oneline
```

**보이는 것:** GitHub에서 만든 커밋이 이제 로컬 이력에 나타납니다.

VSCode에서 `TODO.md`를 열어보세요 — "Learn about git remotes" 항목이 있습니다.

**무슨 일이 있었나요:** `git pull`이 GitHub에서 새 스냅샷을 다운로드하고 로컬 파일을 업데이트했습니다. 이제 로컬 사본이 GitHub과 동기화되었습니다.

> **참고:** [git-pull 문서](https://git-scm.com/docs/git-pull)

---

## 7. Push/Pull 워크플로우

매일 사용할 패턴입니다:

```
[내 컴퓨터]  ---push--->  [GitHub]  <---push---  [다른 컴퓨터]
[내 컴퓨터]  <---pull---  [GitHub]  ---pull--->  [다른 컴퓨터]
```

1. **로컬에서 변경** → 커밋 → `git push` → GitHub에 변경 사항 반영
2. **GitHub에 변경 사항 발생** → `git pull` → 내 컴퓨터에 변경 사항 반영

> **좋은 습관:** 작업을 시작하기 전에 항상 `git pull`을 하세요. 이렇게 하면 최신 변경 사항을 확보할 수 있습니다. 특히 다른 사람과 협업할 때 중요합니다.

---

## 빠른 참고

새로 배운 명령어 요약:

| 명령어 | 하는 일 |
|--------|---------|
| `git remote add origin <URL>` | 로컬 저장소를 GitHub 저장소에 연결 |
| `git remote -v` | 연결된 리모트 확인 |
| `git push -u origin main` | GitHub에 커밋 업로드 (처음) |
| `git push` | GitHub에 커밋 업로드 (이후) |
| `git pull` | GitHub에서 커밋 다운로드 |

전체 워크플로우:

| 단계 | 명령어 |
|------|--------|
| 1. 변경하기 | (VSCode에서 파일 편집) |
| 2. 상태 확인 | `git status` |
| 3. 스테이징 | `git add <파일>` |
| 4. 커밋 | `git commit -m "메시지"` |
| 5. 푸시 | `git push` |

---

잘 하셨습니다! 이제 프로젝트가 두 곳에 있습니다 — 여러분의 컴퓨터와 GitHub. 다음 섹션에서는 명령어를 직접 입력하는 대신 AI와 대화하며 같은 작업을 하는 방법을 알아봅니다.
