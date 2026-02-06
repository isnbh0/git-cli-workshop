# 08 - Git Part 3a: 브랜치 (직접 실습)

**이 섹션에서는 브랜치를 사용하여 메인 프로젝트에 영향을 주지 않고 새로운 아이디어를 시도하는 방법을 배웁니다.** 이것은 심화 목표입니다 — 여기까지 왔다면 정말 잘하고 있는 것입니다!

---

## 브랜치란?

브랜치를 **평행 타임라인**이라고 생각하세요. `main` 브랜치는 여러분의 주요 타임라인 — 프로젝트의 "공식" 버전입니다. 새 브랜치를 만들면, 자유롭게 실험할 수 있는 대체 타임라인을 시작하는 것입니다.

- **결과가 마음에 들면:** 메인 타임라인에 합칩니다
- **마음에 들지 않으면:** 브랜치를 버리면 됩니다. 메인 타임라인은 그대로입니다
- **팀이 일하는 방식:** 각자 자기 브랜치에서 작업하고, 준비되면 합칩니다

시각적으로 보면:

```
main:        A --- B --- C
                         \
experiment:               D --- E
```

커밋 A, B, C는 `main`에 있습니다. `experiment`라는 브랜치를 만들면, 커밋 D와 E는 그 브랜치에서만 일어납니다. `main`은 그대로 유지됩니다.

> **참고:** [Pro Git — 브랜치란 무엇인가](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

---

## 1. 현재 브랜치 확인하기

iTerm2를 열고 데모 저장소 폴더로 이동합니다:

```bash
cd ~/workshop/git-cli-workshop-demo
```

어떤 브랜치에 있는지 확인합니다:

```bash
git branch
```

**예상 결과:**

```
* main
```

**이것이 의미하는 것:** `*`는 현재 브랜치를 나타냅니다. 지금은 `main` 브랜치 하나만 있습니다.

---

## 2. 새 브랜치 만들기

`experiment`라는 브랜치를 만들어 봅시다:

```bash
git branch experiment
```

**예상 결과:** 출력이 없습니다 (정상입니다).

**확인 방법:**

```bash
git branch
```

**예상 결과:**

```
  experiment
* main
```

**이것이 의미하는 것:** 이제 두 개의 브랜치가 있습니다. `*`는 아직 `main`에 있습니다 — 브랜치를 만들었지만 아직 전환하지 않았습니다.

> **참고:** [git-branch 문서](https://git-scm.com/docs/git-branch)

---

## 3. 새 브랜치로 전환하기

```bash
git switch experiment
```

**예상 결과:**

```
Switched to branch 'experiment'
```

**확인 방법:**

```bash
git branch
```

**예상 결과:**

```
* experiment
  main
```

**이것이 의미하는 것:** `*`가 이제 `experiment`에 있습니다. 이제 변경하고 커밋하면 `main`이 아닌 이 브랜치에 기록됩니다.

> **단축키:** `git switch -c experiment` (또는 이전 방식인 `git checkout -b experiment`)로 브랜치 생성과 전환을 한 번에 할 수 있습니다. `-c` 플래그는 "create(생성)"를 의미합니다.

> **참고:** [git-switch 문서](https://git-scm.com/docs/git-switch)

---

## 4. 브랜치에서 변경하기

VSCode에서 `TODO.md`를 열고 새 섹션을 추가합니다:

```markdown
# My To-Do List

## Today
- [x] Buy groceries
- [ ] Reply to emails
- [ ] Read a book

## Notes
Here are some things I want to remember...

## Stretch Goals
- [ ] Learn about git branches
- [ ] Try a new recipe
```

`Cmd+S`로 저장합니다.

**하는 일:** "Stretch Goals" 섹션을 추가합니다. 이 변경 사항은 `experiment` 브랜치에만 존재합니다.

---

## 5. 브랜치에서 커밋하기

```bash
git add TODO.md
git commit -m "Add stretch goals section"
```

**예상 결과:**

```
[experiment abc1234] Add stretch goals section
 1 file changed, 4 insertions(+)
```

**확인 방법:**

```bash
git log --oneline
```

**예상 결과:**

```
abc1234 (HEAD -> experiment) Add stretch goals section
def5678 (main) Check off groceries, add reading and notes
ghi7890 Add initial to-do list
```

**이것이 의미하는 것:** 새 커밋은 `experiment`에 있습니다 (`HEAD -> experiment`로 표시됨). `main` 브랜치는 여전히 이전 커밋을 가리키고 있습니다.

---

## 6. Main으로 돌아가기

이제 `main`으로 돌아가서 무슨 일이 일어나는지 봅시다:

```bash
git switch main
```

**예상 결과:**

```
Switched to branch 'main'
```

**이제 VSCode에서 `TODO.md`를 열어보세요.**

**보이는 것:** "Stretch Goals" 섹션이 사라졌습니다! 파일이 변경하기 전 상태로 돌아갔습니다.

**놀라지 마세요.** 변경 사항이 사라진 게 아닙니다 — `experiment` 브랜치에 안전하게 저장되어 있습니다. 지금 보고 있는 것은 `main` 타임라인이고, 여기에는 그 변경 사항이 아직 없습니다.

**확인:**

```bash
git log --oneline
```

**예상 결과:**

```
def5678 (HEAD -> main) Check off groceries, add reading and notes
ghi7890 Add initial to-do list
```

"Add stretch goals section" 커밋이 여기에는 없습니다 — 다른 브랜치에 있기 때문입니다.

---

## 7. 브랜치 병합하기 (Merge)

Stretch Goals 섹션이 마음에 들어서 `main`에 가져오고 싶습니다. `main` 브랜치에 있는 상태에서:

```bash
git merge experiment
```

**예상 결과:**

```
Updating def5678..abc1234
Fast-forward
 TODO.md | 4 ++++
 1 file changed, 4 insertions(+)
```

**"fast-forward"란:** `experiment`에서 작업하는 동안 `main`에 새 커밋이 없었기 때문에, git이 단순히 `main` 포인터를 앞으로 이동시킵니다. `experiment`가 이미 도달한 지점으로 따라잡는 것과 같습니다.

**확인 방법:**

VSCode에서 `TODO.md`를 열어보세요 — "Stretch Goals" 섹션이 돌아왔습니다!

```bash
git log --oneline
```

**예상 결과:**

```
abc1234 (HEAD -> main, experiment) Add stretch goals section
def5678 Check off groceries, add reading and notes
ghi7890 Add initial to-do list
```

**이것이 의미하는 것:** `main`과 `experiment` 모두 같은 커밋을 가리킵니다. 타임라인이 다시 합쳐졌습니다.

> **참고:** [git-merge 문서](https://git-scm.com/docs/git-merge)

---

## 8. 브랜치 삭제하기

`experiment`가 병합되었으므로 더 이상 필요하지 않습니다:

```bash
git branch -d experiment
```

**예상 결과:**

```
Deleted branch experiment (was abc1234).
```

**확인 방법:**

```bash
git branch
```

**예상 결과:**

```
* main
```

다시 브랜치 하나로 돌아왔습니다. `experiment`의 커밋은 이제 `main`의 일부입니다.

> **참고:** `-d` 플래그는 "안전한 삭제"입니다 — git은 아직 병합되지 않은 브랜치를 삭제하지 않습니다. 병합되지 않은 브랜치를 정말로 버리고 싶다면 `-D` (대문자 D)를 사용하세요.

---

## 빠른 참고

배운 브랜치 명령어 요약:

| 명령어 | 하는 일 |
|--------|---------|
| `git branch` | 모든 브랜치 목록 (현재 브랜치에 `*` 표시) |
| `git branch <이름>` | 새 브랜치 만들기 |
| `git switch <이름>` | 브랜치로 전환 |
| `git switch -c <이름>` | 새 브랜치를 만들고 전환 |
| `git merge <이름>` | 브랜치를 현재 브랜치에 병합 |
| `git branch -d <이름>` | 병합된 브랜치 삭제 |

---

잘 하셨습니다! 이제 git의 가장 강력한 기능 중 하나인 브랜치를 이해했습니다. 다음 섹션에서는 명령어를 직접 입력하는 대신 AI와 대화하며 같은 작업을 하는 방법을 알아봅니다.
