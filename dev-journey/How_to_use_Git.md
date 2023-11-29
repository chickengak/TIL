# Git
버전을 통해 분산된 방식으로 __코드를 관리하는 도구__  
- 백업도구
- 협업도구
- 배포도구  

cf) 갑자기 다른 말이지만 github외에 bitbucket, gitlab, jira도 있긴함.

<br>

## Git?
- SCM (Source Code Management): 코드 관리 도구
- VCS (Version Control System): 버전 관리 시스템(도구)
- DVCS (Distributed VCS): 분산형 버전 관리 시스템(도구)

Git은 폴더(디렉토리) 단위로 코드를 관리한다.

<br>

## Git Summary
### `git init` : Create an empty Git repository or reinitialize an existing one.
### `git clone` : Clone a repository into a new directory
### `git add` : Add file contents to the index
### `git restore` : Restore working tree files
### `git diff` : Show changes between commits, commit and working tree, etc
### `git grep` : Print lines matching a pattern
### `git log` :  Show commit logs
- `git log --oneline` : 한줄로 출력
### `git status` : Show the working tree status
### `git branch` : List, create, or delete branches
### `git commit` :  Record changes to the repository
### `git merge` : Join two or more development histories together
### `git rebase` : Reapply commits on top of another base tip
### `git reset` : Reset current HEAD to the specified state
### `git switch` : Switch branches
### `git fetch` : Download objects and refs from another repository
### `git pull` : Fetch from and integrate with another repository or a local branch
### `git push` : Update remote refs along with associated objects

#### `git bisect`
#### `git show`
#### `git tag`



<br>

## I. 버전관리 Git 명령어
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



