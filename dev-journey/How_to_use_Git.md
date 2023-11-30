# Git
버전을 통해 분산된 방식으로 __코드를 관리하는 도구__  
- SCM (Source Code Management): 코드 관리 도구
- VCS (Version Control System): 버전 관리 시스템(도구)
- DVCS (Distributed VCS): 분산형 버전 관리 시스템(도구)

즉, 쉽게 말하면
- **백업**도구
- **협업**도구
- **배포**도구 인 것이다.  

Git은 폴더(디렉토리) 단위로 코드를 관리한다.

cf) ~~갑자기 다른 말이지만 github외에 bitbucket, gitlab, jira도 있긴함.~~

<br>
<br>

## Git -Commands
### `git init` : Create an empty Git repository or reinitialize an existing one.
### `git clone` : Clone a repository into a new directory
### `git add` : Add file contents to the index
### `git restore` : Restore working tree files
### `git log` :  Show commit logs
- `git log --oneline` : Print in a simple one-liner
- `git log --graph` : Print with graph
### `git status` : Show the working tree status
### `git branch` : List, create, or delete branches
- `git branch -d <branchname>` : Delete a branch. The branch must be fully merged in its upstream branch, or in HEAD
### `git checkout` : Switch branches or restore working tree files
- `git checkout -b <new-branch>` : Create a new branch
### `git switch` : Switch branches
### `git commit` :  Record changes to the repository
### `git merge` : Join two or more development histories together
- merge should be executed from the Parent branch.
### `git rebase` : Reapply commits on top of another base tip
- `git rebase -i HEAD~2` : squash. 불필요하게 어려 개로 나뉜 커밋을 합침. (커밋 2개를 합쳐야 한다면 앞선 명령처럼 입력하면 된다.)
### `git reset` : Reset current HEAD to the specified state
### `git fetch` : Download objects and refs from another repository
- `git fetch <upstream>`
### `git pull` : Fetch from and integrate with another repository or a local branch
- `git pull –rebase <upstream> <feature-user>` : 최신 상위 브랜치로 rebase.
### `git push` : Update remote refs along with associated objects
- need more something

<br>

#### `git diff` : Show changes between commits, commit and working tree, etc
#### `git grep` : Print lines matching a pattern
#### `git bisect`
#### `git show`
#### `git tag`

<br>
<br>

## Git -Collaboration Procedure (with a scenario)
### ticket or issue 발행 후
1. upstream/feature-user 브랜치에서 작업 브랜치(bfm-100_login_layout)를 생성합니다.
```
(feature-user)]$ git fetch upstream  
(feature-user)]$ git checkout -b bfm-100_login_layout –track upstream/feature-user
```

2. 작업 브랜치에서 소스코드를 수정합니다. (뚝딱뚝딱 :hammer:)
3. 작업 브랜치에서 변경사항을 커밋합니다. (보통은 vi editor에서 커밋 메세지를 작성 함)
```
(bfm-100_login_layout)]$ git commit -m "BFM-100 로그인 화면 레이아웃 생성"
```
4. 만약 커밋이 불필요하게 어려 개로 나뉘어져 있다면 squash를 합니다. (커밋 2개를 합쳐야 한다면)
```
(bfm-100_login_layout)]$ git rebase -i HEAD~2
```
5. 작업 브랜치를 upstream/feature-user에 rebase합니다.
```
(bfm-100_login_layout)]$ git pull –rebase upstream feature-user
```
6. 작업 브랜치를 origin에 push합니다.
```
(bfm-100_login_layout)]$ git push origin bfm-100_login_layout
```
7. Github에서 bfm-100_login_layout 브랜치를 feature-user에 merge하는 Pull Request를 생성합니다.
8. 같은 feature를 개발하는 동료에게 리뷰 승인을 받은 후 자신의 Pull Request를 merge합니다. 만약 혼자 feature를 개발한다면 1~2명의 동료에게 리뷰 승인을 받은 후 Pull Request를 merge합니다.

<br>

### develop 변경사항을 feature로 가져오기
작업을 할 때 브랜치의 수명은 되도록 짧게 가져가는 게 좋지만, feature 브랜치에서 기능을 완료하는데 해야 할 작업들이 많아서 오래 걸리는 경우 들이 있습니다. 그러다 보면 develop에 추가된 기능들이 필요한 경우가 종종 생기게 됩니다. 그럴 때는 feature 브랜치에 develop의 변경사항들을 가져와야 합니다.  
1. feature-user 브랜치에 upstream/develop 브랜치를 merge 합니다.
```
(feature-user)]$ git fetch upstream
(feature-user)]$ git merge –no-ff upstream/develop
```
2. upstream/develop의 변경사항이 merge된 feature-user를 upstream에 push 합니다.
```
(feature-user)]$ git push upstream feature-user
```
<br>

### 버그 수정하기
개발을 완료한 후 QA 중 버그가 발생하지 않으면 좋겠지만 항상 생각지 못한 예외 상황들이 발생하게 됩니다. 예외 상황이 발생할 때마다 버그 티켓이 하나씩 생성되는데 이 티켓들을 모두 해결해야만 앱을 출시할 수 있습니다.
버그 티켓들도 티켓이기 때문에 ‘1. 티켓 처리하기’와 같은 방법으로 처리합니다.

<br>
<br>

## Git - **Git-flow**
### PROMISES
1. 작업을 시작하기 전에 티켓을 생성합니다.
2. 하나의 티켓은 되도록 하나의 커밋으로 합니다.
3. 커밋 그래프는 최대한 단순하게 가져갑니다.
4. 서로 공유하는 브랜치의 커밋 그래프는 함부로 변경하지 않습니다.
5. 리뷰어에게 꼭 리뷰를 받습니다.
6. 자신의 Pull Request는 스스로 merge 합니다.


### 5 types of branches
- main(master) : 제품으로 출시될 수 있는 브랜치
- develop : 다음 출시 버전을 개발하는 브랜치
- feature : 기능을 개발하는 브랜치
- release : 이번 출시 버전을 준비하는 브랜치
- hotfix : 출시 버전에서 발생한 버그를 수정 하는 브랜치

<br>

### Outline of Git-flow

![git_flow](https://techblog.woowahan.com/wp-content/uploads/img/2017-10-30/git-flow_overall_graph.png)
- 나동호. 우린 Git-flow를 사용하고 있어요. https://techblog.woowahan.com/2553/

<br>
<br>
<br>
<br>

## I. 버전관리 Git 명령어 (실습내용. 위를 이해했다면 중요하지 않음.)
### `git init`: git을 시작함.
Git으로 코드 관리를 시작
- 코드 관리 단위(기준): 폴더
- (master): ~~현재 브랜치명~~
- .git 폴더 생성: Git 관리와 관련된 파일
### `git status`: Git 상태 출력. 파일 상태 확인
```bash
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```
#### `a.txt` 파일 생성 후
```bash
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt

nothing added to commit but untracked files present (use "git add" to track)
```

#### `git add a.txt` 입력 후
```bash
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt
```

### `git commit -m "메시지"`
```bash
[master (root-commit) ae9a478] First commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt
```

### `git log`
```bash
commit ae9a478fbf5173b3fb3d7155521c6a2fcbc63104 (HEAD -> master)
Author: Jin <peyoumonephu@gmail.com>
Date:   Tue Nov 28 16:41:14 2023 +0900

    First commit
```

### `git status`
```bash
On branch master
nothing to commit, working tree clean
```

<br>

## II. 백업 Git 명령어
### `git remote`
- 원격 저장소 (Remote Repository)에 대한 정보
- git remote add: 원격 저장소 추가
    - git remote add [저장소 이름] [저장소 주소]
    - git remote add origin "http... 주소이름 혹은 SSH"

### `git push`: 원격 저장소에 프로젝트 업로드



