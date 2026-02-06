# 02 - SSH 키 및 gh CLI 설정

> **안내:** 이 문서는 워크숍 중에 강사의 안내에 따라 진행하기 위한 것입니다. 단계가 낯설게 느껴져도 걱정하지 마세요 — 함께 하나씩 진행하겠습니다.

---

## 1. SSH란?

SSH는 여러분의 컴퓨터가 다른 컴퓨터(여기서는 GitHub)에게 안전하게 자신을 증명하는 방법입니다.

비밀 악수라고 생각하면 됩니다: 여러분의 컴퓨터와 GitHub이 서로만 아는 고유한 키 쌍에 합의합니다. 한번 설정하면, 매번 비밀번호를 입력하지 않아도 코드를 주고받을 수 있습니다.

키 쌍을 한 번 만들어서 GitHub에 등록하면, 이후에는 자동으로 작동합니다.

---

## 2. SSH 키 생성

iTerm2를 열고 다음을 입력하세요:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

`your_email@example.com`을 GitHub 계정에 사용한 이메일 주소로 바꾸세요.

**예상 화면:**

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/yourname/.ssh/id_ed25519):
```

**할 일:** Enter를 눌러 기본 위치를 수락하세요.

```
Enter passphrase (empty for no passphrase):
```

**할 일:** Enter를 눌러 비밀번호를 건너뛰세요 (나중에 추가할 수 있습니다).

```
Enter same passphrase again:
```

**할 일:** Enter를 다시 누르세요.

**예상 결과:**

```
Your identification has been saved in /Users/yourname/.ssh/id_ed25519
Your public key has been saved in /Users/yourname/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx your_email@example.com
The key's randomart image is:
+--[ED25519 256]--+
|     ...         |
|    . . .        |
|     (random art)|
+----[SHA256]-----+
```

이제 두 개의 파일이 생겼습니다:
- **개인 키** (`~/.ssh/id_ed25519`) — 여러분의 컴퓨터에만 보관합니다. 절대 공유하지 마세요.
- **공개 키** (`~/.ssh/id_ed25519.pub`) — GitHub에 등록할 키입니다.

> **참고:** [Generating a new SSH key and adding it to the ssh-agent — GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

---

## 3. SSH 키를 GitHub에 추가

### 1단계: 공개 키 복사

```bash
cat ~/.ssh/id_ed25519.pub
```

**예상 결과:** `ssh-ed25519`로 시작하고 이메일로 끝나는 긴 한 줄:

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG... your_email@example.com
```

출력 전체를 선택하여 복사하세요 (터미널에서 `Cmd+A` 후 `Cmd+C`, 또는 해당 줄을 트리플 클릭하여 선택).

### 2단계: GitHub에 등록

1. [https://github.com/settings/keys](https://github.com/settings/keys) 에 접속
   - (또는: GitHub.com → 프로필 사진 클릭 → **Settings** → **SSH and GPG keys**)
2. **New SSH key** 클릭
3. **Title:** "My MacBook" 같은 이름을 입력 (본인을 위한 라벨입니다)
4. **Key type:** "Authentication Key"를 그대로 둡니다
5. **Key:** 복사한 키를 붙여넣기
6. **Add SSH key** 클릭
7. GitHub에서 비밀번호 확인을 요청할 수 있습니다

> **참고:** [Adding a new SSH key to your GitHub account — GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

---

## 4. 연결 테스트

```bash
ssh -T git@github.com
```

**예상 화면 (처음 한 번만):**

```
The authenticity of host 'github.com (...)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

**할 일:** `yes`를 입력하고 Enter를 누르세요.

**예상 결과:**

```
Hi yourusername! You've successfully authenticated, but GitHub does not provide shell access.
```

이 메시지에 여러분의 GitHub 사용자명이 보이면 SSH 키가 정상적으로 작동하는 것입니다.

> **문제 해결:** "Permission denied (publickey)"가 나오면 키가 올바르게 추가되지 않은 것입니다. `cat ~/.ssh/id_ed25519.pub`를 다시 실행하고 전체 줄을 복사했는지 확인하세요 (맨 앞의 `ssh-ed25519`부터 맨 끝의 이메일까지). 그런 다음 GitHub에서 다시 추가하세요.

> **참고:** [Testing your SSH connection — GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

---

## 5. gh CLI 설치

`gh` CLI는 GitHub의 공식 명령줄 도구입니다. 터미널에서 직접 저장소 생성, 이슈 관리 등을 할 수 있게 해줍니다.

> **참고:** [GitHub CLI Manual](https://cli.github.com/manual/)

### 1단계: 설치

```bash
brew install gh
```

**예상 화면:** Homebrew가 gh 도구를 다운로드하고 설치합니다. 보통 1분 이내에 완료됩니다.

**설치 확인:**

```bash
gh --version
```

**예상 결과:**

```
gh version 2.x.x (20xx-xx-xx)
```

### 2단계: GitHub 로그인

```bash
gh auth login
```

> **참고:** [gh auth login — CLI Manual](https://cli.github.com/manual/gh_auth_login)

**예상 화면:** 여러 질문이 나타납니다. 다음과 같이 선택하세요:

```
? What account do you want to log into?  GitHub.com
? What is your preferred protocol for Git operations on this host?  SSH
? Upload your SSH key to your GitHub account?  Skip
? How would you like to authenticate GitHub CLI?  Login with a web browser
```

**참고:** SSH 키 업로드는 "Skip"을 선택합니다. 이전 단계에서 이미 수동으로 추가했기 때문입니다.

"Login with a web browser"를 선택하면:

```
! First copy your one-time code: XXXX-XXXX
Press Enter to open github.com in your browser...
```

**할 일:**
1. 표시된 코드를 복사
2. Enter 누르기 — 브라우저가 열립니다
3. 브라우저에 코드 붙여넣기
4. "Authorize" 클릭
5. 터미널로 돌아오기

**예상 결과:**

```
✓ Authentication complete.
- gh config set -h github.com git_protocol ssh
✓ Configured git protocol
✓ Logged in as yourusername
```

---

## 6. 전체 확인

```bash
gh auth status
```

**예상 결과:**

```
github.com
  ✓ Logged in to github.com account yourusername (keyring)
  - Active account: true
  - Git operations protocol: ssh
  - Token: gho_****
  - Token scopes: 'gist', 'read:org', 'repo', 'workflow'
```

체크 표시와 사용자명이 보이면 모든 설정이 완료된 것입니다.

---

## 요약

이 섹션에서 설정한 내용:

| 항목 | 이유 |
|------|------|
| SSH 키 | GitHub과의 안전한 비밀번호 없는 연결 |
| GitHub에 SSH 키 등록 | GitHub이 여러분의 컴퓨터를 인식 |
| gh CLI | 터미널에서 GitHub 저장소 관리 |
| gh 인증 | gh CLI가 여러분의 계정에 연결됨 |

이제 GitHub에 코드를 push하고 pull할 준비가 되었습니다.
