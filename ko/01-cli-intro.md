# 01 - CLI 소개

**이 섹션에서는 터미널이 무엇인지 배우고 가장 자주 쓰는 명령어들을 연습합니다.** 끝나고 나면 폴더 이동, 파일 만들기, 정리하기를 모두 타이핑으로 할 수 있게 됩니다.

---

## 1. 터미널이란?

터미널은 텍스트로 컴퓨터에게 말을 거는 방법입니다. Finder에서 클릭으로 하는 모든 것 — 폴더 열기, 파일 복사, 삭제 — 을 명령어로 입력할 수 있습니다.

왜 굳이 이렇게 할까요? 익숙해지면 클릭보다 빠르고 강력하기 때문입니다. 그리고 git을 포함한 많은 개발 도구들은 터미널에서만 작동합니다.

사전 준비에서 설치한 iTerm2가 바로 여러분의 터미널 앱입니다.

> **참고:** [Terminal User Guide for Mac — Apple Support](https://support.apple.com/guide/terminal/welcome/mac)

---

## 2. iTerm2 열기

1. `Cmd+Space`를 눌러 Spotlight 열기
2. "iTerm" 입력
3. Enter 누르기

텍스트 프롬프트가 있는 창이 나타납니다. 이것이 여러분의 터미널이며, 명령어를 입력할 준비가 된 상태입니다.

---

## 3. 프롬프트 구조

iTerm2를 열면 다음과 같은 화면이 보입니다:

```
yourname@yourcomputer ~ %
```

각 부분의 의미는 다음과 같습니다:

| 부분 | 의미 |
|------|------|
| `yourname` | macOS 사용자 이름 |
| `yourcomputer` | 컴퓨터 이름 |
| `~` | 현재 위치 (홈 폴더) |
| `%` | "입력 대기 중" (`$`로 보일 수도 있습니다 — 둘 다 정상) |

모든 것을 이해할 필요는 없습니다. 중요한 것은: **`%` (또는 `$`) 뒤에 명령어를 입력**한다는 것입니다.

---

## 4. 연습할 명령어들

### `ls` — 파일 목록 보기

**하는 일:** 현재 위치에 있는 파일과 폴더를 보여줍니다.

**사용 예시:**

```bash
ls
```

**예상 결과:** 파일과 폴더 목록이 나타납니다:

```
Desktop    Documents  Downloads  Movies  Music  Pictures
```

> **직접 해보세요:** `ls`를 입력하고 Enter를 누르세요. 어떤 파일이 보이나요?

---

### `cd` — 디렉토리 이동

**하는 일:** 다른 폴더(디렉토리)로 이동합니다.

**사용 예시 — Desktop으로 이동:**

```bash
cd Desktop
```

**예상 결과:** 출력이 없습니다 (정상입니다). 프롬프트가 바뀌어 새 위치를 보여줍니다:

```
yourname@yourcomputer Desktop %
```

**현재 위치 확인:**

```bash
pwd
```

**예상 결과:**

```
/Users/yourname/Desktop
```

**자주 쓰는 변형들:**

| 명령어 | 하는 일 |
|--------|---------|
| `cd ~` | 홈 폴더로 돌아가기 |
| `cd ..` | 한 단계 위 폴더(상위 디렉토리)로 이동 |
| `cd` | 홈 폴더로 돌아가기 (`cd ~`와 동일) |
| `cd Documents` | Documents 폴더로 이동 |

> **직접 해보세요:** `cd Desktop`으로 Desktop에 이동한 후, `cd ~`로 홈 폴더로 돌아오세요. 매번 `pwd`로 위치를 확인해 보세요.

---

### `mkdir` — 새 디렉토리 만들기

**하는 일:** 새 폴더를 만듭니다.

**사용 예시:**

```bash
mkdir test-folder
```

**예상 결과:** 출력이 없습니다 (정상입니다 — 폴더가 조용히 생성됩니다).

**정상 생성 확인:**

```bash
ls
```

**예상 결과:** 목록에 `test-folder`가 보여야 합니다.

> **직접 해보세요:** `test-folder`라는 폴더를 만들고 `ls`로 존재하는지 확인하세요.

---

### `open` — Finder 또는 기본 앱으로 열기

**하는 일:** Finder에서 더블클릭하는 것처럼 파일이나 폴더를 엽니다. macOS 전용 명령어로, 익숙한 느낌일 것입니다.

**사용 예시 — 현재 폴더를 Finder에서 열기:**

```bash
open .
```

**예상 결과:** 현재 폴더의 내용을 보여주는 Finder 창이 열립니다.

**사용 예시 — 특정 폴더 열기:**

```bash
open test-folder
```

**예상 결과:** (비어 있는) test-folder를 보여주는 Finder 창이 열립니다.

> **직접 해보세요:** `open .`을 입력해서 현재 폴더를 Finder에서 확인하세요. 그 파일들이 보이나요? `ls`로 보았던 것과 같은 파일들입니다.

---

### `cp` — 파일 복사

**하는 일:** 파일의 사본을 만듭니다.

**사용 예시:**

먼저, 작업할 파일을 만들어 봅시다:

```bash
echo "Hello, terminal!" > greeting.txt
```

(이 명령은 "Hello, terminal!"이라는 내용의 `greeting.txt` 파일을 생성합니다)

이제 복사합니다:

```bash
cp greeting.txt greeting-copy.txt
```

**예상 결과:** 출력이 없습니다 (사본이 조용히 만들어집니다).

**정상 복사 확인:**

```bash
ls
```

**예상 결과:** `greeting.txt`와 `greeting-copy.txt` 모두 보여야 합니다.

> **직접 해보세요:** `greeting.txt`를 만들고 `greeting-copy.txt`로 복사한 후, `ls`로 두 파일이 모두 있는지 확인하세요.

---

### `mv` — 파일 이동 또는 이름 변경

**하는 일:** 파일을 다른 위치로 이동하거나 이름을 바꿉니다. (터미널에서는 이동과 이름 변경이 같은 동작입니다.)

**사용 예시 — 파일 이름 변경:**

```bash
mv greeting-copy.txt farewell.txt
```

**예상 결과:** 출력이 없습니다.

**정상 변경 확인:**

```bash
ls
```

**예상 결과:** `greeting-copy.txt`는 사라지고, `farewell.txt`가 대신 있습니다.

> **직접 해보세요:** `greeting-copy.txt`의 이름을 `farewell.txt`로 변경하고 `ls`로 확인하세요.

---

### `rm` — 파일 삭제

**하는 일:** 파일을 영구적으로 삭제합니다.

> **주의:** 터미널에는 휴지통이 없습니다. `rm`으로 삭제한 파일은 영원히 사라집니다. Enter를 누르기 전에 다시 한번 확인하세요!

**사용 예시:**

```bash
rm farewell.txt
```

**예상 결과:** 출력이 없습니다.

**정상 삭제 확인:**

```bash
ls
```

**예상 결과:** 목록에 `farewell.txt`가 더 이상 없습니다.

폴더와 그 안의 모든 내용을 삭제하려면 `rm -r`을 사용합니다:

```bash
rm -r test-folder
```

> **직접 해보세요:** `farewell.txt`와 `test-folder`를 삭제하세요. `ls`로 사라졌는지 확인하세요.

---

### `less` — 파일 내용 보기

**하는 일:** 터미널에서 파일을 열어 읽을 수 있게 합니다.

**사용 예시:**

```bash
less greeting.txt
```

**예상 결과:** 파일 내용이 표시됩니다:

```
Hello, terminal!
```

**중요:** `q`를 눌러 종료하고 프롬프트로 돌아가세요. (잊으면 뷰어에 갇히게 됩니다!)

> **직접 해보세요:** `less`로 `greeting.txt`를 보고 `q`를 눌러 빠져나오세요.

---

### `history` — 명령어 기록 보기

**하는 일:** 최근에 입력한 명령어 목록을 보여줍니다.

**사용 예시:**

```bash
history
```

**예상 결과:** 번호가 매겨진 최근 명령어 목록:

```
  1  ls
  2  cd Desktop
  3  pwd
  4  cd ~
  5  mkdir test-folder
  ...
```

> **직접 해보세요:** `history`를 입력해서 지금까지 한 모든 명령어를 확인하세요.

> **팁:** 위쪽 화살표 키를 누르면 이전 명령어를 하나씩 불러올 수 있습니다. 명령어를 다시 실행하고 싶을 때 편리합니다.

---

### `exit` — 터미널 세션 종료

**하는 일:** 현재 터미널 탭이나 창을 닫습니다.

**사용 예시:**

```bash
exit
```

**예상 결과:** 터미널 탭이 닫힙니다 (유일한 탭이면 "process completed"라고 표시될 수 있습니다).

> **직접 해보세요:** `exit`을 입력해서 세션을 닫아 보세요. (새 iTerm2 창은 `Cmd+N`으로 언제든 열 수 있습니다.)

> **참고:** macOS 명령어의 상세 문서는 [macOS Command Line A-Z — SS64](https://ss64.com/mac/)를 참고하거나, 터미널에서 `man <명령어>`를 입력하세요 (예: `man ls`).

---

## 5. 종합 연습

지금까지 배운 것을 모두 활용해 봅시다. 순서대로 따라하세요:

### 1단계: `practice` 폴더 만들기

```bash
mkdir practice
```

### 2단계: 폴더로 이동

```bash
cd practice
```

### 3단계: 파일 만들기

```bash
echo "This is my practice file." > notes.txt
```

### 4단계: 파일 존재 확인

```bash
ls
```

**예상 결과:**

```
notes.txt
```

### 5단계: 파일 내용 보기

```bash
less notes.txt
```

**예상 결과:**

```
This is my practice file.
```

`q`를 눌러 빠져나오세요.

### 6단계: 파일 복사

```bash
cp notes.txt notes-backup.txt
```

### 7단계: 사본 이름 변경

```bash
mv notes-backup.txt archive.txt
```

### 8단계: 파일 목록으로 두 파일 확인

```bash
ls
```

**예상 결과:**

```
archive.txt  notes.txt
```

### 9단계: 사본 삭제

```bash
rm archive.txt
```

### 10단계: 상위 폴더로 이동 후 폴더 삭제

```bash
cd ..
rm -r practice
```

### 11단계: 정리 완료 확인

```bash
ls
```

**예상 결과:** `practice` 폴더가 사라졌습니다.

---

축하합니다! 이제 필수 터미널 명령어를 알게 되었습니다. 이 명령어들이 앞으로 git을 배울 때 기초가 됩니다.
