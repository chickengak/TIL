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
### `git stash` : Stash the changes in a dirty working directory away
- `git stash -a`
- `git stash pop`

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

## Git - **my notes**
### remote에 올라간 최신 커밋 취소.
사용에 매우매우매우 주의해야 한다. 협업자가 이미 pull을 했다면 상당히 골치아파지기 때문. revert 사용을 권장.
```commandline
git reset --hard HEAD~1
git push -f origin main
```


<br>
<br>
<br>
<br>

# Git 팀원 학습 자료
여기 기술된 naming convention은 Jin(본인)이 협업 시 편했던 방법이므로, 모든 상황에서 해야만 하는 convention은 아님을 밝힌다.

### add　commit　push　pull　branch　원격 저장소　로컬 저장소
상기 명령은 다 알고 있다는 가정하에 시작한다.  
협업을 위해 여기서 배울 내용
- Issue
- Pull request
- --rebase
- stash

## 새로운 개발을 시작하기 전
먼저 팀원과 구분된 작업 환경을 만들어야 한다.

Step 1　이슈 발행하기  
github >> Issues >> New issue  
무슨 이슈인지에 관해 작성하고 우측 라벨까지 완성할 것.

Step 2　최신 브랜치에서 이슈 번호로 브랜치 생성
```bash
git fetch
git checkout -b Issue#이슈번호 --track main
```

Step 3　본인이 만든 branch에서 개발 후 commit한다.

Step 4　본인이 만든 branch에 commit한 정보를 원격 저장소에 저장한다.
```bash
git push origin Issue#이슈번호
```

Step 5　PR을 요청한다  
내용과 라벨을 작성 후 팀원의 리뷰가 끝나고 팀원이 PR을 허가를 받는다.  
스스로 PR을 요청하고 스스로 merge하지 않기. (간단한 문서 작성은 허가하기로 한다)  

Step 6　merge가 완료됐기 때문에 branch를 삭제하고, Issue를 닫는다.

## 개발 중에 팀원이 commit을 해서 내 파일을 최신화하고 싶을 때

방법 1  
과거의 main에서 분기한 내 branch를 최신 브랜치로 앞 당긴다.
```bash
git pull --rebase origin main
```
방법 2  
현재 내 변경사항을 임시로 저장한 후 일단 pull하고 변경사항을 꺼내온다.
```bash
git stash -a
git pull
git stash pop
```

## 최신화 도중 파일이 충돌난 경우

방법 1  
과거의 main에서 분기한 내 branch를 최신 브랜치로 앞 당긴다.
```bash
git pull --rebase origin main
# 충돌난 파일을 수정 후
git rebase --continue
```

방법 2  
현재 내 변경사항을 임시로 저장한 후 일단 pull하고 변경사항을 꺼내온다.
```bash
git stash -a
git pull
git stash pop
# 충돌난 파일을 수정
```

## git 협업 주의사항
### 절대로 main에 직접 commit push 하지 말 것.
main 브랜치를 개개인이 수정해버릴 경우, 팀원들의 버전과 코드가 꼬일 수 있음.  
main 브랜치에는 PR로 merge 하기만 한다.

### git이 꼬인 경우
작업을 하다보면 마음대로 안 되는 경우가 발생할 수 있다. 이럴 땐 삭제 후 원격 저장소에서 다시 clone하는게 맘편하다.



