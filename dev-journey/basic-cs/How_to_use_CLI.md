# CLI
__Command Line Interface__  
커맨드(명령어)를 통해 작동하는 인터페이스  
<-> GUI(Graphic User Interface, 보통의 프로그램)

<br>

## CLI vs GUI

- CLI(Command Line Interface): 명령행/줄 인터페이스.
- GUI(Graphic User Interface): 말 그대로 GUI

대부분의 회사에서 CLI로  한다.

<br>

## 명령어
~는 home directory를 뜻한다.  
/는 root directory를 뜻한다.  
$는 터미널에 명령어 입력준비를 뜻함.
### (1) pwd (print working directory): 현재 위치를 출력.
### (2) ls (list): 현재 폴더의 파일/폴더 출력
### (3) cd (change directory): 폴더 변경.
- `cd [경로명]`
- `cd ..`: 상위 폴더로 이동
- `cd .`: 현재 폴더로 이동
- `cd ~`: home directory로 이동
### (4) mkdir (make directory): directory(folder) 만들기.
- `mkdir [폴더명]`
### (5) rm (remove)
- `rm [파일명]`: 파일 삭제
- `rm -r [폴더삭제]`: 폴더 삭제. -r은 recursive를 뜻하는 말로 안에 있는 내용들을 모두 같이 삭제하기 때문.
### (6) touch: 파일 생성
- `touch [파일명]` 
### (7) cp: 복사
- `cp [파일명] [위치]`: 파일 복사
- `cp -r [폴더명] [위치]`: 폴더를 복사
### (8) mv: 이동 or 이름 변경
- `mv [파일명/폴더명] [파일명/폴더명]`: 파일/폴더명 변경
- `mv [파일/폴더명] [위치]`: 파일 또는 폴더를 이동
### (9) open: 파일 탐색기로 연다.
- `open .`: 현재 폴더를 파일 탐색기로 연다.
### (10) cat: 파일 내용을 출력
- `cat [파일명]`
### (11) sudo: 관리자 권한으로 명령 실행
### (12) ctl+I: 터미널 정리. clear
### (13) ctl+c: 취소. cancle

