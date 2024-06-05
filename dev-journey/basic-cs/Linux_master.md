# 리눅스

### 리눅스 배포판의 종류
- 슬랙웨어 Slackware
    - 가장 오래된 배포판
- 데비안 Debian
    - Ubuntu, Linux Mint, Kali Linux ...
- 레드햇 RedHat
    - 유료인 RHEL(Ted Hat Enterprise Linux)와 무료인 Fedora(페도라)로 나누어 배포
    - RHEL, Fedora, CentOS, ...
- 수세 SUSE
    - 독일에서 개발, 배포. 유럽에서 많이 씀.

### 리눅스 특징
- 오픈 소스
- 다중 사용자, 다중 작업 (multi user, multi tasking)
- 강력한 네트워킹, 다양한 파일 시스템 지원
- 이식성, 유연성, 확장성, 안정석, 보안성 좋음
- 가성비 굳, 다양한 응용프로그램을 제공, 다양한 배포판 존재.

|   |   |
|---|---|
| 장점 | - 유닉스와 완벽한 호환 <br> - POSIX 규격을 따름 <br> - 안정적인 운영체제 <br> - 하드웨어의 효율적 운영  |
| 단점 | - 무료 공개용은 기술지원을 받기 어려움 <br> - 특정 하드웨어에 대한 지원 부족 <br> - 다소 어렵고 한글 지원이 미흡 |

- 리눅스 파일 시스템은 계층형 트리 구조
- 리눅스 커널은 C언어로 작성됨

### 라이센스 License
1. GNU
    - GNU is Not Unix
    - 리차드 스톨만, 자유 소프트웨어 재단(FSF)
    - GNU 프로젝트는 최초로 Linux를 개발한 프로젝트다
2. GNU GPL
    - GNU General Public License
    - FSF에서 만듦
    - 내부에서 사용할 때는 소스코드 공개할 필요 X
    - 외부에 배포할 때는 소스코드 공개
3. GNU LGPL
    - GNU Lesser General Public License
    - LGPL이 적용된 라이브러리를 이용해 개발했을 경우, 사용했음만 명시하면 됨.
    - 단, LGPL 소스 코드를 단순히 이용하는 것이 아니라, 수정 혹은 파생된 라이브러리를 배포하는 경우에는 소스 코드를 공개해야 함.
4. BSD
    - Berkeley Software Distribution
    - 소프트웨어의 수정 배포에 제한이 없음
    - 소스 코드 공개 의무 X, 상용 소프트웨어에서도 자유롭게 사용 가능
5. 아파치 라이센스
    - 누구나 파생 상품 개발 가능. 저장권을 양도하거나 배포할 수도 있다.
    - 재배포 아파치 라이센스 2.0을 포함해야 함.
6. MIT 라이센스
    - BSD 계열
    - 누구나 개작 가능. 수정본의 재배포 시 소스 코드 비공개 가능
    - 대표적으로 X Window System (X11)
7. MPL
    - Mozilla Public License
    - BSD + GNU GPL
    - 소스 코드와 실행 파일의 라이센스를 분리.
    - 사용한 MPL과 수정한 MPL 소프트웨어에 대한 공개 의무만 가지며, 별도의 소스 코드와 실행 파일은 독점적인 라이센스를 지닌다.

## 리눅스 부트

### 부트 매니저
부트 매니저는 부팅할 때 사용자의 PC에 설치되어 있는 운영체제 중 하나를 선택하여 부팅하는 기능

### 부트 로더
컴퓨터를 사용자가 사용할 수 있도록 하드디스크에 저장된 운영체제를 주기억장치에 적재해주는 프로그램
- Boot Loader. Bootstrap Loader의 약자
- 운영체제가 실행되기 전에 미리 실행되어, 커널이 안정적으로 실행되기 위한 모든 관련 작업을 완료하는 프로그램
- 여러개의 운영체제가 설치되어 있을 경우 선택하여 부팅. (멀티 부팅)

| LILO (Linux Loader) | GRUB (Grand Unified Bootloader) |
|---|---|
| 리눅스에서만 사용 가능 | 리눅스 외에도 사용 가능  |
|   | LILO의 단점 보완 |
|   | 대화형이므로, 커널의 경로와 파일 이름만 알면 부팅 가능 |
|   | 메뉴설정 환경을 지원, 대화형 모드로 부트 정보 설정 가능 |

GRUB 환경설정 파일 내용
- p.59

GRUB 편집 모드
- p.60

### 런레벨
- 부팅 시 init 프로세스가 참조하는 것이 런레벨.
- 런 레벨은 0 ~ 6 이 있다.

런레벨 실행 스크립트 파일
- init.d
- rc.local
- rc0.d ~ rc6.d

런레벨 운영 모드

| 런레벨 | 운영모드 |
|---|---|
| 0 | Halt |
| 1 | Single User Mode |
| 2 | Multi User Mode (without networking) |
| 3 | Multi User Mode (only console login) |
| 4 | Not Used |
| 5 | Multi User Mode with Display Manager |
| 6 | Reboot |

### 로그인 및 로그아웃

### 시스템 종료 명령어
shutdown
```bash
shutdown [옵션] [시간] [경고 메시지]
```
- -c　종료 명령 취소
- -h　안전하게 종료
- -k　
- +m　m분 후에 종료
- -P　강제 종료
- -r　재시작
- -t　시간 지정

init
```bash
init [런 레벨]
```

halt
```bash
halt [옵션]
```
- 옵션 없이 사용하면, 모든 프로세스는 종료되지만 전원은 꺼지지 않는다.
- -f　강제 종료. 포로세스, 전원 모두 꺼진다.

poweroff
```bash
poweroff
```

reboot
```bash
reboot [옵션]
```
- -r　강제 재시작


## 파일 시스템과 파티션
### 파일 시스템
- 파일에 대한 다양한 종류의 접근제어 방법을 제공
- 데이터의 백업 및 복구 기능 제공
- 데이터의 효율적인 저장과 관리 방법을 제공

파일 시스템의 종류

| 종류 | 유형 |
|---|---|
| 리눅스 | ext, ext2, ext3, ext4 |
| 저널링 | JFS, XFS, ReiserFS |
| 네트워크 | SMB, CIFS, NFS |
| 윈도 | FAT, FAT32, VFAT, NTFS |
| CD-ROM | iso9660 |
| 유닉스 | HPFS, SysV |
| 클러스터링 | RedHat GFS, IBM GPFS, IBM SanFS, Compaq CFS, Oracle OCFS2 |

### 파티션
- 하나의 물리적인 디스크를 여러 논리 디스크로 분할하는 것
- 파티션 상태를 확인하는 파일: /proc/partitins

파티션 종류
- 기본 파티션
     - 하나의 디스크에 기본 파티션과 황장 파티션 모두 4개의 파티션까지 분할 가능
- 확장 파티션
     - 논리 파티션을 만들 수 있게 하는 공간으로 디스크당 하나만 만들 수 있음.
- 논리 파티션
     - 4개 이상의 파티션을 사용하게 된느 경우 확장 파티션 내에 논리 파티션을 생성.
     - 하나의 하드디스크에서 논리 파티션의 수는 최대 12개까지 가능
- 스왑 파티션
     - 하드디스크 일부를 주기억장치처럼 쓰는 가상기억장치
     - 리눅스 설치 시 반드시 필요한 영역
     - 기본 파티션 또는 논리 파티션에 생성
     - 스왑 영역의 크기는 일반적으로 주기억 장치의 2배로 설정

파티션의 장점
- 부팅시간 단축
- 안정성을 높임
- 백업과 업그레이드가 편리

파티션 분할
- fdisk 명령으로 파티션을 생성, 수정 삭제 등 관리 가능
```bash
fdisk [옵션] [장치명]
```
- -a　부팅 가능한 플래그로 지정
- -l　알려진 파티션 유형 목록 출력
- -m　이 목록 출력
- -n　새로운 파티션 생성
- -t　파티션 유형 변경
- -w　파티션 정보를 디스크 레이블에 기록
- -p　파티션 정보 확인
- -q　작업 종료 후 나가기

디스크와 장치명
- 플로피 디스크
     - /dev/fd0　첫 번째 플로피 디스크
     - /dev/fd1　두 번째 플로피 디스크
- IDE 유형 디스크
     - /dev/hda　Primary Master
     - /dev/hdb　Primary Slave
     - /dev/hdc　Secondary Master
     - /dev/hdd　Secondary Slave
- SCSI 유형 디스크
     - /dev/sda　첫 번째 드라이브
     - /dev/sdb　두 번째 드라이브
- CD-ROM
     - /dev/scd0 또는 /dev/sr0　SCSI CD-ROM

### 디렉토리
|   |   |
|---|---|
| / |   |
| /bin |   |
| /usr |   |
| /etc |   |
| /sbin |   |
| /lib |   |
| /var |   |
| /temp |   |
| /root |   |
| /proc |   |
| /dev |   |
| /home |   |


### LVM
- PV > VG > LV
- 여러 개의 물리 디스크를 하나의 대용량 파일시스템으로 만든다.

### RAID
- Redundant Array of Independent Disks
- 여러 개의 물리적인 디스크를 하나의 논리 디스크로 인식하게 만드는 기술
- 중요한 데이터를 가지고 있는 서버에서 주로 사용. 중복 저장 기술 있음.
- 레벨에 따라 성능을 향상시키거나, 신뢰성을 높이는데 사용

종류
- 하드웨어 RAID
     - 안정적이지만 고가
- 소프트웨어 RAID
     - 언정성이 떨어지고 성능향상이 적지만 저가

RAID 레벨 구조
- RAID 0
     - 빠른 입출력. 스트라이핑(Striping)
- RAID 1
     - 두 개 이상의 디스크를 미러링(Mirroring)
- RAID 0+1
     - RAID 0과 RAID 1의 결합 방식
     - 최소 4개 이싱의 디스크에서 2개씩 RAID 0으로 묶고, 묶인 RAID 0을 RAID 1로 결합함
- RAID 2
     - 오류 정정을 위해 해밍코드를 사용. 비트 단위에 해밍 코드를 적용.
     - 최근 디스크 드라이브는 기본적인 오류 검출 기능이 있어서 거의 사용 안함
- RAID 3/4
     - 하나의 디스크를 패리티(Parity)
     - 읽기 성능은 RAID 0과 비슷하나 쓰기는 패리티 처리로 인해 일부 성능 저하
     - 병목 현상(bottle neck)이 발생하면 성능 저하가 발생
- RAID 5
     - 3개 이상의 디스크를 사용하여 하나의 디스크처럼 사용하고, 각각의 디스크에 패리티 정보를 가지고 있음.
     - 패리티 디스크를 별도로 사용하지 않으므로 병목 현상이 발생하지 않음
- RAID 6
     - 하나의 패리티를 두 개의 디스크에 분산 저장하는 방식
     - 패리티를 이중으로 저장하기 때문에, 두 개의 디스크에서 오류가 발생해도 복구 가능
     - 쓰기 속도는 패리티를 10번 쓰기 때문에 느려질 수 있지만, 안정성은 높아진다.

<br>
<br>
<br>

# 기본 명령어

## 사용자 및 그룹

useradd
- -c
- -d
- -e
- -f
- -G
- -s

passwd
- -d
- -l
- -S
- -u

su
- \-　-l　--login
- -c
- -s

----

/etc/default/useradd

/etc/login.defs

/etc/skel

/etc/passwd

/etc/shadow

----

usermod
- -c
- -d
- -e
- -f
- -g
- -G
- -s
- -u

userdel
- -r

----

users
> 로그인한 사용자의 이름을 출력

w
> 로그인한 사용자의 정보를 자세하게 출력

who
> 로그인한 사용자의 정보를 간단하게 출력

whoami

id
> 로그인한 사용자의 UID, GID, GROUP 정보를 출력

----

groupadd
- -g
- -o
- -r

groupdel

groupmod
- -g
- -n

----

/etc/group

/etc/gpasswd

----

groups
> 현재 사용자가 속한 그룹들을 출력


## 디렉토리 및 파일

mkdir
- -m　권한 설정
- -p　하위 디렉토리를 한 번에 생성
- -v　verbose, 만들고 디렉토리 정보 출력

rmdir

cd
- ~
- .
- ..

pwd
- -L　심볼릭 링크의 경로를 표시 (기본)
- -P　심볼릭 링크 대신 원래 경로를 표시

ls
- -a　숨김 파일도 출력
- -d　디렉토리만 출력
- -F　파일이 디렉토리면 / , 실행 파일이면 * , 소켓이면 = , 심볼릭 링크면 @ 를 파일 뒤에 표시
- -l　상세히 출력
- -m　, 로 구분하여 출력
- -r　역순 출력
- -R　하위 디렉토리 목록까지 출력
- -s　Kbyte로 출력
- -t　최종 수정 시간 기준으로 출력

cp
- -b　동일한 파일명이 있으면, 복사본을 만듦
- -f　강제
- -i　덮어쓰기 여부를 묻기
- -p　원본의 모드, 소유자, 시간 정보를 유지하면서 복사
- -P　원본이 디렉토리 경로와 함께 지정됐을 경우, 지정된 디렉토리 경로를 그대로 복사
- -r　하위 디렉토리까지 복사
- -S　동일한 파일명이 있으면, 백업파일을 생성하지만, 백업파일 접미사를 지정
- -u　동일하 파일명이 있으면, 최신일 경우에만 복사

mv
- -b　동일한 파일명이 있으면, 복사본을 만듦
- -f　강제
- -i　덮어쓰기 여부를 묻기
- -u　동일하 파일명이 있으면, 최신일 경우에만 복사
- -v　verbose

rm
- -d　디렉토리 삭제
- -f　강제
- -i　삭제 여부를 묻기
- -r　하위 디렉토리도 삭제
- -v　verbose

touch
- -c　기존에 파일이 없으면, 파일이 생성되지 않음
- -a　현재 시간으로 접근 시간, 변경 시간을 수정
- -m　현재 시간으로 수정 시간, 변경 시간을 수정
- -d　지정한 시간으로 접근 시간, 수정되고, 변경 시간은 현재 시간으로 수정
- -t　지정한 시간으로 접근 시간, 수정되고, 변경 시간은 현재 시간으로 수정
- -r　지정한 파일의 접근 시간, 수정 시간으로 파일이 수정되고, 변경시간은 현재로 수정

file
- -b　파일의 유형을 출력
- -f　
- -i　
- -L　심볼릭 링크된 파일을 추적하여 원본 파일 정보를 출력
- -z　압축된 파일의 내용 출력

find
- -delete
- -empty
- -exec
- -name
- -print
- -size
- -type
- -atime
- -ctime
- -mtime

locate
> 미리 만들어 놓은 DB 파일에서 검색하기 때문에 빠르지만, 업데이트를 하지 않으면 최근에 삭제된 파일도 검색되는 문제가 발생함. 이럴 때는 updatedb 명령을 실행 후 locate를 하면 된다.
- e　검색에서 제외할 디렉토리 지정
- n　지정한 개수만큼 검색

whereis
> 명령어의 바이너리(실행 파일), 소스, 매뉴얼 파일의 위치를 검색

which
> 명령어 실행 파일 또는 링크의 위치를 검색

----
### 출력 명령어

cat
- -b　행번호 출력. (비어 있는 행 제외)
- -n　행번호 출력. (비어 있는 행 포함)
- -e　제어 문자를 ^ 형태로 출력하면서, 각 행의 끝에 $ 문자 추가
- -s　연속되는 비어 있는 행을 하나로 출력

head
- -c --byte　byte 단위 출력
- -n　n 행 출력
- -v　파일 이름을 헤더에 출력
- -q　파일 이름을 헤더에 출력하지 않음 (기본)

tail
- -c --byte　byte 단위 출력
- -n　n 행 출력
- -v　파일 이름을 헤더에 출력
- -f　파일의 마지막 10줄을 실시간으로 연속해서 출력
- -F　파일의 마지막 10줄을 실시간으로 연속해서 출력하며, 로그 파일처럼 특정시간이 지난 후 파일이 변동하게 되면 새로운 파일을 출력
- -n +n　처음 +n 번째 줄 이후부터 마지막까지

more
> 파일의 내용을 화면 단위로 출력
- 엔터　한 행씩 아래로
- -b　한 화면씩 위로 이동
- 스페이스바　한 화면씩 아래로
- n:/문자열　문자열 검색
- q　나가기
- v　현재 위치에서 vi 편집기 실행
- =　현재 위치의 행 번호 출력

less
- -c
- -i
- -s
- -x　
- q　 나가기
- 행번호　지정된 행 다음부터 출력
- ↑　한 행씩 위로
- ↓　한 행씩 아래로
- Page Up　한 화면씩 위로
- Page Down　한 화면씩 아래로
- 엔터　한 행씩 아래로
- 스페이스바　한 화면씩 아래로

grep
> 파일 안에서 검색한 후, 검색된 모든 행을 출력. 디렉토리 안에서 해당 패턴을 포함하는 파일을 출력할 수도 있다.
- grep 다중 패턴 검색 / egrep 정규 표현식 검색 / fgrep 단순 패턴 검색
- -c　일치하는 행의 수 출력
- -i　대소문자 구분 안함
- -l　패턴이 포함된 파일 이름들을 출력
- -n　행 번호 출력
- -v　패턴과 일치하지 않는 행을 출력
- -w　패턴이 전체 문자열과 일치하는 행만 출력

wc
> 파일 안의 행, 단어, 문자 수를 출력하는 명령어
- -l　행 개수 출력
- -w　단어 개수 출력
- -c　문자 개수 출력

sort
> 파일 내용을 정렬
- -b　선행 공백 무시
- -c　정렬 여부 검사
- -f　대소문자 구분 안함
- -m　정렬된 파일 병합
- -n　숫자로 한정하여 정렬
- -o　저장할 파일명 지정
- -r　역순 정렬
- -R　랜덤하게 정렬 (해시값으로)
- -t　필드 구분자 지정
- -u　정렬후 중복 제거

cut
> 파일에서 특정 필드를 추출하여 출력
- -b　바이트 단위
- -c　문자 단위
- -d　
- -f　TAB으로 필드를 구분하여 지정한 필드만 출력
- -s　

split
> 하나의 파일을 여러 파일로 분할
- -a　
- -b　바이트 단위 분할
- -l　행 단위 분할
- --additional-suffix　확장자명을 지정

----
### 파일 비교 명령어

diff
> 차이가 없으면 0, 차이가 있으면 1, 에러는 2를 반환.  
> diff3은 파일을 3개까지 비교
- -b　연결되는 공백을 무시
- -c　차이점 출력
- -d　차이점을 상세히 출력
- -i　대소문자 구분 안함
- -r　하위 디렉토리의 파일도 비교
- -s　두 파일이 같을 경우 알림
- -t　출력 행에 TAB 삽입
- -w　모든 공백 표시

cmp
> 파일을 바이트 단위로 비교
- -b　서로 다른 바이트 수 출력
- -i　최초의 Skip 바이트를 건너 뜀
- -l　서로 다른 문자의 수 출력
- -s　아무것도 출력하지 않고 종료 코드만 출력

comm
> 파일을 행 단위로 비교
- -1　파일1에만 있는 행은 출력하지 않음
- -2　파일2에만 있는 행은 출력하지 않음
- -3　공통으로 있는 행은 출력하지 않음

<br>

## 기타 명령어

리다이렉션 Redirection
- \>
- \>>　명령 실행 결과를 추가하거나 저장
- <
- \>&　명령의 출력을 다른 명령의 입력으로 보냄
- <&

파이프 Pipe
> 두 개의 명령얼르 연결. 프로세스와 프로세스 간의 통로.  
> 명령 출력이 다른 명령의 입력으로 전달
- <명령어> | <명령어> | <명령어>

세미콜론 ;
> 명령 구분. 첫 번째 명령이 실패해도 다음 명령어 실행

----
### 네트워크 명령어

ping
- -c　횟수만큼 패킷 전송
- -d　
- -f　
- -i　패킷 전송 사이의 대기 시간 지정
- -l　
- -n　
- -r　

traceroute
- -m　홉 수 지정
- -n　
- -p　시작 포트 번호 지정
- -q　패킷 수 지정
- -w　타임아웃 시간 지정

nslookup
> 도메인 이름으로 IP 주소를 확인하거나, IP 주소로 도메인 이름을 확인  
> -type=
- a　IPv4
- aaaa　IPv6
- mx　
- ns　
- soa　
- srv　
- txt　
- ptr　
- cname　

dig
> Domain Information Groper 로 nslookup과 유사
- @server
- domain
- type
　
- a
- any
- mx
- ns
- soa
- hinfo
- axft
- txt
- zone transfer

host


hostname


----

date

rdate
> 원격지의 시간 정보를 가져와 동기화시킴
- -4　IPv4
- -6　IPv6
- -p　정보만 출력하고 설정은 안 함
- -s　출력 안 하고 설정만 함
- -o
- -u
- -v

cal
> 달력을 출력
- -j　
- -y　

time
> 프로그램의 실행 시간을 출력

tty
> 현재 사용하고 있는 단말 장치의 경로와 파일명을 출력

clear

wall
> 로그인된 모든 사용자에게 메시지 전송

write
> 지정된 사용자에게 메시지 전송

mesg
> 메시지 수신 여부를 확인하고 제어


<br>
<br>
<br>

# 파일 시스템 관리

## 사용자 권한 및 그룹 설정
    - rw-r--r--. 1 root root 45 10월 11 13:44 linux.txt

파일 유형
- \-　일반파일
- c　문자 파일
- |　심볼릭 링크 파일
- b　블록 장치 파일
- d　장치 파일
- s　소켓 파일
- p　파이프

허가권  
링크 수  
소유자명  
그룹명  
파일 크기  
마지막 변경 시각  
파일명

<br>

### 소유권 관련 명령어

chown
> 파일이나 디렉토리의 사용자 소유권과 그룹 소유권을 변경  
> 구분자는 . 혹은 :
- -c　소유권 변경 정보 출력
- -f　오류 메시지 출력 안함
- -R　하위 디렉토리도 모두 변경

chgrp
> 파일이나 디렉토리의 그룹 소유권을 변경
- -c　소유권 변경 정보 출력
- -f　오류 메시지 출력 안함
- -R　하위 디렉토리도 모두 변경
- -v　verbose

<br>

### 허가권 관련 명령어

chmod
> 파일이나 디렉토리의 허가권을 변경
- -c　소유권 변경 정보 출력
- -R　하위 디렉토리도 모두 변경
- -v　verbose

umask
> 새로 생성되는 파일이나 디렉토리의 기본 허가권을 지정하는 명령  
> umask값이 022이라면, 파일은 644 이고, 디렉토리는 755 다.
- -S　umask 값을 기호로 출력

<br>

### 특수 허가권

프로세스가 실행되는 동안, 해당 파일을 실행한 사용자가 아닌, 해당 파일을 소유한 사용자의 권한으로 실행하도록 만드는 허가권

- 낮은 수준의 사용자가 높은 수준의 자원에 접근할 수 있다.

|   |   |   |
|---|---|---|
| SetUID | s | 4000 |
| SetGID | s | 2000 |
| Sticky | t | 1000 |

<br>

### 디스크 쿼터　Disk Quota

파일 시스템별로 사용자나 그룹의 사용량을 제한
- 블록(block) 단위나 아이노드(I-Node)의 개수를 제한한다.
- 사용자별, 파일 시스템별로 작동

quotaon
> 쿼터를 활성화
- -a　모든 파일 시스템에 대해 쿼터 적용
- -g　그룹 쿼터 적용
- -u　사용자 쿼터 적용
- -v　verbose

quotaoff
> 쿼터를 끔
- -a　모든 파일 시스템에 대해 쿼터 적용
- -g　그룹 쿼터 적용
- -u　사용자 쿼터 적용
- -v　verbose

quotacheck
> 모든 파일 시스템을 점검하고, 쿼터 설정 및 기록 파일을 갱신  
> 갱신 목록: quota.user , quota.group , aquota.user , aquota.group
- -a　모든 파일 시스템을 점검 및 기록 갱신
- -g　그룹 기록 갱신
- -m　파일 시스템을 읽기 전용으로 다시 마운트하지 않음
- -u　사용자 기록 갱신
- -v　verbose

edquota
> 쿼터를 설정하고 변경
- -g　그룹 쿼터 설정 및 변경
- -p　기존 사용자의 할당량 설정을 다른 사용자에게 복사
- -t　유예 기간 확인 및 변경
- -u　사용자 쿼터 설정 및 변경

setquota
> 터미널에서 직접 사용자나 그룹에 쿼터를 적용하는 명령
- -a
- -g
- -u

repquota
> 터미널에서 직접 사용자나 그룹에 적용된 쿼터를 요약하여 출력
- -a
- -g
- -u

xfs_quota
> xfs 파일 시스템에서 quota를 설정하기 위한 명령


## 파일 시스템 관리 유틸리티

### 파일 시스템

### 파일 시스템 명령어

fdisk

mkfs

mke2fs

mkfs.xfs

fsck

e2fsck

xfs_repair

mount, umount

eject

df
> 시스템에 마운트된 하드디스크의 사용량과 남은 용량을 확인  
> 기본적으로 블록 단위(1Kbyte)로 출력

### 파일 시스템 관련 파일

/etc/fstab

    /dev/sdb1 /home ext3 defaults 0 0

<br>
<br>
<br>

# 셸 관리

## 셸　Shell

- 사용자가 입력한 명령어를 해석하여 커널에 전달
- 윈도(도스)에서의 command.com과 유사한 기능을 수행
- 사용자가 로그인 시 실행되어 사용 환경을 제공
- 셸 프로그래밍 언어(스크립트 언어) 이다.
- 리다이렉션과 파이프 기능을 수행
- 사용자 셸 프롬프트 이다. (본 셸 계열: $ , C 셸 계열: %)

본 셸 계열
|   |   |   |
|---|---|---|
| 본 셸 | /bin/sh |
| 콘 셸 | /bin/ksh |
| 배시 셸 | /bin/bash | GNU 프로젝트 |
| 지 셸 | /bin/zsh |

C 셸 계열
|   |   |   |
|---|---|---|
| C 셸 | /bin/csh | 버클리대 빌 조이 |
| TC 셸 | /bin/tcsh |

### 셸 관련 파일

/etc/shells
> 사용자들이 사용 가능한 셸들을 정의해논 파일

/etc/passwd
> 사용자 계정 정보가 저장되는 파일

    test:x:1000:1000:test:/home/test2:/bin/bash

### 셸 관련 명령어

echo $SHELL
> 현재 사용중인 셸 확인

chsh
> 셸 변경
- -s　지정한 셸로 변경
- -l　/etc/shells 파일의 내용을 출력
- -u

usermod
> 사용자의 계정 정보를 직접 수정
```bash
usermod -s /bin/csh test
```

## 환경 설정

### 환경 변수
> 현재 사용하고 있는 셸의 실행 파일에 대한 위치를 저장하는 변수

주요 환경 변수
- DISPLAY
- HOME
- HOSTNAME
- LANG
- PS1
- PS2
- PWD
- SHELL
- TERM　사용자의 터미널 유형
- TMOUT　자동 로그아웃 되는 시간
- USER

export

echo $변수명

export 변수명=변수값

export 변수명=$변수명:변수값
```bash
export PATH=$PATH:/root/linux
```

셸 프롬프트 설정
?

<br>

### 배시 셸 관련 파일

/etc/profile
> 모든 사용자의 셸 환경을 제어하는 전역 설정 파일  
> 환경변수와 배시가 실행하는 프로그램 제어

/etc/bashrc
> 별칭과 배시가 실행하는 함수를 제어 (전역)

~/.bash_profile
> 개별 사용자의 셸 환경을 제어하는 설정 파일

~/.bash_logout
> 로그아웃 직전에 실행되는 설정 파일

~/.bash_history
> 사용자가 입력한 명령어가 저장되는 파일

~/.bashrc
> 별칭과 배시가 실행하는 함수를 제어 (local)

<br>

### 배시 셸의 주요 기능

history 기능
- 사용자가 사용했던 명령어를 저장해서 재사용이 가능하게 함
- 1000개 까지 저장. 사용자 홈에 저장. (~/.bash_history)
```bash
history [옵션]
```
- !!
- !n
- !-n
- !?string　가장 최근에 string으로 시작되는 명령 실행
- !$ , !!\$
- !*
- !?string?
- n
- -c

history 관련 환경변수
- HISTSIZE　
- HISTFILE　히스토리 파일 위치
- HISTFILESIZE　
- HISTCONTROL　중복되는 명령어 기록 유무
- HISTTIMEFORMAT　히스토리 명령어 수행 시간, 출력 형태 지정

alias , unalias
```bash
alias
alias [단축명령어]='명령어'
```

<br>
<br>
<br>


# 프로세스 관리

## 프로세스
- 중앙처리장치(CPU)를 할당받아 실행 중인 프로그램
- 프로세서가 할당되는 실체로서, 디스패치가 가능한 단위
- 비동기적 행위를 일으키는 주체
- 고유의 PID를 갖음
- 최상위 프로세스는 systemd 이며, 가장 먼저 실행되는 프로세스로 PID는 1이다

### 프로세스 유형

포그라운드, 백그라운드　foreground, background


fork() 와 exec()
> 한 프로세스가 다른 프로세스를 실행시키기 위해서 사용하는 시스템 호출

데몬　Daemon
> 리눅스 부팅 시 실행되는 백그라운드 프로세스  
> 사용자의 요청을 기다리고 있다가 요청이 오면 적절히 대응하는 프로세스  
> 독립적으로 수행되며, 서비스 요청에 응답하기 위해 항상 메모리에 상주  
> 대게 d가 붙는다.
- standalone / (x)inetd

시그널
> 운영체제에서 사용하는 제한된 형태의 프로세스 간 통신

<br>

### 프로세스 명령어

ps
> 현재 실행 중인 프로세스의 상태를 출력
- -a　로그인 셸과 터미널에 종속되지 않은 모든 프로세스 출력
- -e　커널 프로세스를 제외한 모든 프로세스 출력
- -f　풀 포맷으로 출력
- -l　자세한 프로세스 목록 출력
- -o　출력 포맷을 지정
- -p　특정 PID를 지정
- -r　현재 실행중인 프로세스 출력
- -u　특정 사용자의 프로세스를 출력
- -x　접속된 터미널뿐만 아니라 사용중인 모든 프로세스 출력

pstree
> 실행 중인 프로세스를 트리 구조로 출력

top
> 프로세스 상태를 실시간으로 확인하거나 모니터링 함  
> 시스템 상태 (CPU, Memory, Process)를 빠르게 파악  
> 옵션 없이 입력하면 Interval 은 3초
- -b
- -d
- -n
- -p

nohup
> 프로세스를 중단하지 않고, 백그라운드 작업을 수행할 수 있게 하는 명령
> 터미널을 종료해도 프로세스는 백그라운드로 계속 실행  
> nohup 으로 실행하면 nohup.out 라는 로그 파일 생성.

jobs
> 백그라운드로 실행 중인 프로세스를 확인하는 명령

fg, bg
> 프로그램을 포그라운드, 백그라운드로 실행
```bash
fg %[작업번호], bg %[작업번호]
```

nice
> nice값으로 우선순위를 지정.  
> 기본 nice 값은 0. -20 ~ 19까지 가능. 수치가 낮을 수록 우선순위가 높다.  
> 일반 사용자는 nice값을 증가시킬 수만 있다.
```bash
nice -n 10 top
```

renice
> 이미 실행 중인 프로세스의 nice값을 변경.  
> root 사용자와 해당 프로세스 소유자만 변경 가능.  
> 일반 사용자는 nice값을 증가시킬 수만 있다.
```bash
renice 10 14177
```

kill
- -1　프로세스 재시작
- -9　프로세스 강제 종료
- -l　Signal의 종류를 출력
- -s　특정 Signal 지정

killall
> PID가 아닌 프로세스 명으로 종료.  
> 여러 프로세스를 한 번에 종료할 때도 씀.
- -i
- -I
- -g
- -o
- -l
- -s
- -u
- -v
- -w

### 작업 스케줄링

cron
> 주기적으로 반복되는 작업을 자동 실행하는 프로그램.  
> 데몬은 crond , 관련 파일은 관리자인 경우 /etc/crontab 이고 사용자는 /var/spool/cron  
> 분　시　일　월　요일　명령

- -e　설정하거나 변경
- -l　목록 출력
- -r　설정 제거
- -u　특정 사용자의 작업 스케줄 수정


<br>
<br>
<br>

# 에디터 관리

### 에디터 종류 및 특징

#### vi
- 1976년 빌 조이, 리눅스와 유닉스에 기본적으로 포함됨.
- 리눅스에서 가장 많이 사용
- 모드(mode)형 편집기로 입력모드, 편집모드 ex모드로 구성.
- 줄 단위 편집기가 아니고, 한 화면씩 편집하는 비주얼 편집기(visual editor)다.
- GUI 와 텍스트 모드에서 모두 사용 가능.

#### vim
- 브람 무레나르, vi와 호환되면서 다양한 기능을 추가.
- vi라고 입력해도 자동으로 vim이 실행됨.
- 다양한 색, 하이라이트 기능
- 실행모드에서 히스토리 기능, 확장된 정규 표현식, 강력한 문법 강조, 다중 되돌리기, 유니코드, 문법 검사 기능

#### pico
- 아보일 카사르, 초기 리눅스 배포판에서 사용. 무료지만 오픈소스는 아니라 수정 불가.
- 메뉴형 편집기. 윈도우의 메모장과 유사하며, 쉽게 사용 가능.
- 모드형 편집기가 아니기 때문에 바로 텍스트 입력 및 수정이 가능.

#### nano
- GNU 프로젝트에서 pico의 복제판인 nano를 개발.
- 텍스트 모드 편집기. Curses Library를 기반으로 화면 친화적인 편집기다.
- pico와 동일한 기능으로 구성.

#### emacs
- 리차드 스톨만. 제임스 고슬링이 LISP 언어를 기반으로 emacs에 다양한 기능 추가.
- 프로그램 소스 코드 작성까지 가능.
- 비모드형 편집기로 여러 개의 키를 조합해서 사용.

#### gedit
- X 윈도에서 사용할 수 있는 오픈 소스 텍스트 편집기.
- GNOME 데스크톱 환경용으로 GTK+ 라이브러리를 이용하여 개발할 수 있다.
- 프로그램 코드, 마크업 언어와 같은 구조화된 텍스트 편집에 용이
- GUI용으로, 텍스트 기반 터미널에서 사용 불가.
- 윈도우, MAC OS X 에서도 사용 가능.

#### X 윈도에서만 사용 가능한 GUI 편집기
- gedit, gvim, xemacs

<br>

### vi

```bash
vi [옵션명] 파일명
```
옵션
- -R　읽기 전용
- +　파일을 열 때, 커서가 마지막 행에 위치
- -n　파일을 열 때, 커서가 n행에 위치
- -r　손상된 파일 복구

모드
- 입력 모드　i, a, o
- 명령 모드　esc
- ex 모드　　esc를 누른 후, :를 입력한 상태

저장 및 종료
- :q
- :q!
- :w
- :wq
- :wq!
- :!bash　편집 상태를 그대로 두고, 배시 셸 실행.
- ZZ　저장 후 나가기
- :x　변경 사항이 있으면 저장하고 나가기

명령 모드에서 입력 모드로 전환
- a　현재 커서 뒤에서 글자 삽입
- A　현재 커서 행의 맨 뒤에서 글자 삽입
- i　현재 커서 위치에서 글자 삽입
- I　현재 커서 행의 맨 앞에서 글자 삽입
- o　현재 커서 다음 행에서 글자 삽입
- O　현재 커서 위 행에서 글자 삽입

커서 이동
- h　←
- l　→
- j　↓
- k　↑
- 엔터　↓

명령 모드에서 복사, 붙여넣기, 삭제, 치환, 되돌리기
- yb　커서 위치에서 왼쪽으로 한 단어 복사
- yw　커서 위치에서 오른쪽으로 한 단어 복사
- yy　한 행 복사 (nyy: n행 복사)
- db　커서 위치에서 왼쪽으로 한 단어 삭제
- dw　커서 위치에서 오른쪽으로 한 단어 삭제
- dd　한 행 삭제 (ndd: n행 삭제)
- x　커서 위치에서 한 문자 삭제
- p　커서가 위차한 다음 행에 붙여넣기
- P　커서가 위치한 위 행에 붙여넣기
- r　커서 위치의 문자 치환
- u　되돌리기

행 추가, 행 합치기
- o　커서 다음 행에 빈 행 추가, 입력모드로 전환
- O　커서 위 행에 빈 행추가, 입력모드로 전환
- J　현재 행에 이어 다음 행 합치기

파일 안 위치 검색
- b　한 단어 앞으로 이동
- w　한 단어 뒤로 이동
- ^　그 행 맨 앞으로 이동
- 0　그 행 맨 앞으로 이동
- $　그 행 맨 뒤로 이동
- G　마지막 행으로 이동
- nG　n번째 행으로 이동

문자 검색
- /linux　linux 문자로 이동
- n　다음 일치 문자로 이동
- N　이전 일치 문자로 이동

문자 치환
- old 라는 단어를 new 라는 단어로 치환하기
- `:%s/old/new/g`


### pico
```bash
pico [옵션] 파일명
```
옵션
- w　긴 행에서 행이 깨지는 경우에 사용
gi
활용
- ctrl + O　저장
- ctrl + X　저장 후 나가기
- ctrl + R　커서 위치에 다른 파일 불러오기
- ctrl + A　그 행 맨 앞으로 이동
- ctrl + E　그 행 맨 뒤로 이동
- ctrl + V　이전 페이지로
- ctrl + Y　다음 페이지로
- ctrl + T　맞춤법 검사
- ctrl + C　현재 행이 몇 번째 행인지, 전체 글자 중 몇 번째 글자인지, 전체에서 몇 퍼센트에 위치하는 지 알려줌.
- ctrl + J　자동으로 정돈함
- ctrl + W　이 키를 누르고 문자열을 입력해서 검색함
- ctrl + K　현재 행 제거
- ctrl + U　제거 된 행 복구
- ctrl + L　화면 갱신
- ctrl + G　도움말

### nano
```bash
nano [옵션] 파일명
```
옵션
- -B
- -m
- +n

ctrl Y, ctrl V 가 반대

활용


### emacs
```bash
emacs 파일명
```


<br>
<br>
<br>

# 소프트웨어 설치 및 관리

## 패키지
바이너리 파일을 설치함.
| 레드햇 계열 | 데비안 계열 |
|---|---|
| Fedora, RHEL, CentOS | Debian, Ubuntu, Xandros, Linspire, Kali Linux |
| rpm, yum | dpkg, apt-get, aptitude |

수세 리눅스: YaST, zypper  
아키텍처 종류: x86_64, alpha, sparc64, ppc64, i686, noarch  
<br>

### rpm　RedHat Package Manager
    name-2.4.6-93.el7.centos.x86_64.rpm
|   |   |
|---|---|
| name | 패키지 이름 |
| 2.4.6 | 버전 |
| 93 | 릴리즈 번호 |
| .el7.centos | CentOS 버전 |
| .x86_64 | 아키텍처 |
| .rpm | 확장자 |

```bash
rpm [옵션] [패키지명]
```
- -a　모든 패키지 검색
- -e　삭제
- -f　패키지에 대해 질의
- -F　비교해서 최신일 때 업그레이드
- -h　설치 시 # 마크 표시
- -i　설치
- -K　
- -V　
- -q　설치 여부 확인
- -U　기존 패키지 업그레이드
- -v　
- -vv
- --force　강제로 덮어 쓰기
- --nodeps
- --oldpackage
- --replacepkgs　재설치
- --replacefiles  
<br>

### yum　Yellow dog Updater Modified
- 레드햇 계열의 네트워크 기반 패키지 관리자
- /etc/yum.repos.d
- 페도라 22부터는 yum의 문제점을 보완한 dnf 를 사용.
```bash
yum [옵션] [명령어] [패키지명]
```
- -y install
- -y update
- localinstall
- groupinstall
- remove
- groupremove
- info
- search
- check update　업데이트 가능한 패키지 출력
- check-update
- list　전체 패키지 정보 출력
- grouplist
- history  
<br>

### dpkg　Debian Package Manager
- 데비안의 저레벨 패키지 관리자
```
name_15.04-32_all.deb
```
|   |   |
|---|---|
| name | 패키지 이름 |
| 15.04 | 버전 |
| 32 | 릴리즈 |
| all | 아키텍처 |
| .deb | 확장자 |
- -c　
- -i　설치
- -I　
- -l　설치된 패키지 목록
- -L　특정 패키지가 설치한 파일 목록
- -P　환경설정 파일도 같이 제거
- -r　제거
- -s　상세 정보 출력  
<br>

### apt-get　Advanced Packaging Tool get
- 데비안 계열의 네트워크 기반 패키지 관리자
- /etc/apt/source.list ← apt-get이 의존성과 충돌성 해결을 위해 참조하는 파일
- GTK+ 기반의 GUI 도구는 synaptic
```bash
apt-get [옵션] [명령어] [패키지명]
```
- -b　소스 패키지를 다운로드한 후 빌드
- -d　다운로드만 
- -f　
- -u　업그레이드 패키지 목록 출력
- -V　
- -y　

- autoremove　
- autoclean　
- build-dep　
- check　
- clean　다운로드한 압축 파일 지우기
- dist-upgrade　
- download　
- install　설치
- purge　환경설정 파일도 같이 제거
- remove　제거
- source　
- update　새로운 패키지 목록 다운로드
- upgrade　업그레이드  
<br>

## 파일 아카이브와 소스 파일

### 파일 아카이브와 압축
- 여러 개의 파일이나 디렉토리를 하나의 파일로 묶는 것
- .tar
```bash
tar [옵션] [아카이브 이름] [묶여질 파일명]
```
- -A　
- -c　아카이브 파일 생성
- -C　디렉토리 경로 지정
- -d　
- -e　
- -f　대상 아카이브 지정 (default)
- -j　bzip2 압축 또는 해제
- -J　xz 압축 또는 해제
- -k　
- -p　
- -P　
- -r　tar 파일 마지막에 파일을 추가
- -t　내용물을 보기만함
- -u　
- -U　
- -v　verbose
- -w　
- -x　아카이브에서 파일 추출 = 압축 해제
- -z　gzip 압축 또는 해제
- -Z　compress 압축 또는 해제  
<br>

### 파일 압축과 해제
- gzip, bzip2, xz, compress, zip, bzcat, zcat  
<br>

gzip　gunzip
> .gz
- -c 
- -d　압축 해제
- -f
- -l　압축 정보 출력
- -n　n은 1~9로, 9는 최대 압축이지만 느리다.
- -r　디렉토리를 지정 시, 디렉토리에 포함된 모든 파일을 압축
- -t
- -v

bzip2　bunzip2
> .bz2
- -c
- -d　압축 해제
- -f
- -k
- -v
- -z　압축
- -1~-9　압축 블록 크기 지정

xz　unxz
> .xz
- -d
- -l
- -t
- -z

compress　uncompress
> .Z
- -b　
- -c　*.Z 파일 이름 대신 다른 이름으로 생성
- -d
- -f
- -r
- -v
- -V

zip　unzip
> .zip
- -e　암호 설정
- -r
- -x
- -1
- -9


### 소스 코드 설치
- 압축 해제된 소스코드는 컴파일해서 설치할 수 있다.
- 리눅스의 소스코드는 대부분 C언어

컴파일 순서
1. ./configure　환경설정 - makefile 생성
2. make　컴파일 - makefile 기반으로 컴파일
3. make install　파일 설치

CMake　Cross Platform Make
- 키트웨어와 컨소시엄에서 개발. 오픈소스
- 기존의 make 과정을 거치지 않고, 운영체제에 맞게 make 파일을 생성하므로, Meta Make 라고도 한다.
- 유닉스 계열, 윈도우 계열의 프로그램도 지원. 멀티 플랫폼 지원
- 소프트웨어 빌드에 특화된 언어로, 독자적인 설정 스크립트를 사용
- C, C++, Java 등에서는 의존관계를 분석할 수 있다.
- MS 비주얼 스튜디오, eclips
- 병렬 빌드와 크로스 컴파일 가능

<br>
<br>
<br>

# 주변 장치 관리
## 장치

### 프린터
LPRng
- 버클리. BSD 계열 유닉스에서 사용
- 초기에 사용된 프린터
- 스풀링, 네트워크 프린터 지원
- 설정 파일: /etc/printcap

CUPS
- 애플. 유닉스 계열에서 사용. 매킨토시나 윈도우 등 대부분의 프린터 지원. 오픈 소스.
- HTTP 기반의 IPP를 사용하여 웹 기반으로 제어
- 사용자 및 호스트 기반의 인증 제공
- 설정 파일 디렉토리: /etc/cups
- 설정 파일: 프린터 데몬 (cupsd.conf), 프린터 큐 (printers.conf), 프린터 데몬의 클래스 (classes.conf), 프린터 데몬 (cupsd)

### 사운드 카드
OSS　Open Sound System
- 1992년 Hannu Sacolainen
- 표준 유닉스 장치 (POSIX) 에 기반한 인터페이스.
- 현재는 ALSA로 대체

ALSA　Advanced Linux Sound Architecture
- 1998년 Jaroslav Kysela
- GPL 및 LGPL 라이선스 기반으로 배포
- 설정 파일: /etc/asound.state

### 스캐너
SANE　Scanner Access Now Easy
- 스캐너, 캠 등 이미지 관련 하드웨어를 제어하는 API
- GPL 라이센스. 유닉스 계열. OS2, 윈도우 지원

XSANE　X based interface for the SANE
- SANE을 이용한 X 윈도 기반 스캐너
- GTK+ 라이브러리로 만들어짐. xsane 명령으로 실행
- 스캔 뿐만 아니라 캡처한 이미지 수정도 가능
- GPL 라이센스. 유닉스 계열. OS2, 윈도우 지원


## 명령어

### BSD 계열 프린터

lpr
> 프린터 작업 요청
- -C
- -h
- -i
- -j
- -l
- -m
- -P
- -r　스풀링 완료 시, 파일 제거
- -T
- -#

lpq
> 프린터 큐에 있는 작업 목록을 출력  
> lpd 데몬 실행 후 프린터 설정이 제대로 됐는지 확인할 때 유용
- -a
- -l
- -P

lprm
> 프린터 큐에 대기 중인 작업을 제거. 작업번호나 파일명으로 제거.
> 작업번호가 지정되지 않았을 경우, 가장 마지막 요청작업을 제거.
- -　모든 작업 취소
- -h
- -P
- -U

lpc
> 프린터나 프린터 큐를 제어 및 상태 확인

lpd
> 프린터 데몬

### System V 계열 프린터

lp
> 프린터 작업 요청
- -d
- -n

lpstat
> 프린터 큐의 상태를 출력
- -a
- -P
- -t

cancel
> 프린터 작업을 취소
- -a

### 사운드 카드

alsactl
> alsa 사운드 카드를 제어
- -d
- -f
- init
- store
- restore

cdparanoia
> CD로부터 음악 파일을 추출
- -a
- -B
- -w

alsamixer
> 커서(ncurses) 라이브러리 기반의 오디오 프로그램

### 스캐너

sane-fine-scanner
> 스캐너 관련 장치 파일을 검색
- -p
- -q
- -v

scanimage
> 이미지를 스캔
- -d
- -L
- --format

scanadf
> 자동 문서 공급 장치가 장착된 스캐너에서 여러 개의 사진을 스캔하는 명령
- -d
- -L

xcam
> GUI 기반으로 평판 스캐너나 카메라로부터 이미지를 스캔



<br>
<br>
<br>
<br>

# X 윈도

플랫폼과 독립적으로 작동하는 그래픽 시스템이다. X11, X 라고도 불린다.

- 네트워크 기반의 그래픽 환경을 지원
- 이기종 시스템 간에도 사용 가능
- 그래픽 환경 자원들이 특정 형태로 정의되어 있지 않아서, 인터페이스를 원하는대로 커스터마이징 가능.
- 프로토콜 기반의 클라이언트/서버 시스템으로 나뉜다.

### 구성 요소

Sever / Client
- 클라이언트와 서버는 다른 시스템에 있거나, 개인 컴퓨터처럼 두 부분이 동일한 시스템에 상주하여 실행될 수 있다.
- 일반적인 관계와 반대다. 클라이언트가 자원을 제공하고, 서버는 응용 프로그램에서 수행된 결과를 출력 장치에 표시함.
- 서버는 클라이언트의 디스플레이에 관한 접근 허용, 클라이언트 간의 자원 공유, 네트워크 메시지 전달, 클라이언트와 입출력 장치와의 중계를 담당.
- 클라이언트는 애플리케이션으로 X 서버가 제공하는 기능을 이용할 수 있다.

X protocal
- 서버와 클라이언트의 상호 작용은 메시지로 이뤄지는데, 이 메시지 형태와 사용법을 X protocol 이라고 함.

Xlib, Xtoolkit
- X 프로토콜은 Xlib 라는 라이브러리 루틴으로부터 생성
- Xlib는 저수준의 인터페이스. 그래서 상위 라이브러리인 Xtoolkit을 사용.
- Xtoolkit: GTK, Qt, Xaw, Xview, Xt Intrinsics, Motif

### X 윈도 실행과 설정
```bash
startx [옵션] [인자값]
```
startx 는 시스템 환경을 초기화하고 xinit을 호출함.

- \--　인자값을 xinit에 전달
- -bpp 8　256 컬러
- -bpp 32　트루 컬러
- ctrl + alt + F1~F4　터미널 전환
- ctrl + alt + F7　상태 전환
- ctrl + alt + Backspace　강제 종료

환경 변수
```bash
export DISPLAY=[IP 주소]:[디스플레이 번호].[스크린 번호]
```
- 환경변수 DISPLAY는 현재 X윈도 출력 장치 위치를 지정.

## 윈도 매니저
- X 윈도의 형태를 갖추는 프로그램
- 메뉴판 구성, 스크롤바, 아이콘, 마우스 등을 제공
- 윈도 매니저마다 서로 다른 모양과 기능
- Mutter, Metacity, KWin, fvwm, twm, mwm. Window Maker, AfterStep

## 데스크탑 환경
- 윈도 매니저, 파일 관리자, 도움말, 제어판 등 다양한 도구를 제공하는 패키지 형태의 프로그램
- 아이콘 창, 도구 모음, 파일 관리자, 배경 화면, 위젯등을 제공
- 드래그 앤 드롭과 프로세스 간 통신을 지원

### GNOME
- GNU Network Object Model Environment
- GNU에서 개발. GTK+ 라이브러리. 데스크톱과 라이브러리는 LGPL 라이센스, 응용 프로그램은 GPL 라이센스.
- 전용 윈도 매니저 없음. (Metacity → Mutter)
- 세션 매니저

### KDE
- Kool Desktop Environment
- 독일. Qt 툴킷. LGPL 라이센스
- UNIX, Linux, Solaris, IRIX, HP-UX, FreeBSD 등의 시스템에서 작동
- 전용 윈도 매니저 없음. (KWin)

### LXDE
- Light X11 Desktop Environment
- GTK 2 툴킷. Openbox 윈도 매니저.
- 가볍고 빠른 데스크톱 환경과 경제성
- 우분투, Peppermint OS, Raspbinan

### Xfce
- XForums Common Environment
- GTK+ 2 툴킷. Xfwm 윈도 매니저.
- 유닉스 계열 플랫폼을 위한 오픈 소스 데스크탑 환경

|   | GNOME | KDE |
|---|---|---|
| 기본 편집기 | gedit | kate |
| 기본 브라우저 | Web | konquerer |
| 파일 관리자 | nautilus | konquerer, dolphin |
| 윈도 매니저 | Metacity → Mutter | KWin |


## 디스플레이 매니저
- X 서버 로그인과 세션을 담당.
- 1988년 X11R3 에서 xdm 디스플레이 매니저를 도입.
- xdm, gdm, kdm, dtlogin(레드햇 리눅스)

## X 윈도 활용
### xhost
- x 서버에 접속할 수 있는 클라이언트를 지정
- 호스트 기반 인증 방식
```bash
xhost [옵션] [IP 주소/도메인명]
```
- \+　모든 클라이언트 접속 허용
- \-　모든 클라이언트 접속 차단
- +[IP 주소]　IP 접속 허용
- -[IP 주소]　IP 접속 차단

### xauth
- .Xauthority 파일의 쿠키 내용을 추가, 삭제
- IP 주소가 아닌 키값으로 인증함.
- MMC 기반 인증 방식
```bash
xauth [옵션]
```
- list　현재 사용되는 모든 쿠키값 출력
- list [출력 장치명]　파일에 추가

### X윈도 응용 프로그램

1. 오피스 프로그램
    - LibreOffice (Write, Impress, Calc, Draw)
    - gedit
    - kwrite
2. 그래픽 프로그램
    - GIMP
    - ImageMagick
    - eog
    - gthumb
    - kolourpaint
    - gwenview
3. 멀티미디어
    - Totem
    - Rhytmbox
    - cheese
    - KMid
4. 개발
    - eclipse
5. 기타
    - ksnapshot
    - evolution
    - kmail
    - evince

<br>
<br>
<br>

# 인터넷 활용

## 통신망의 종류
### LAN
- Local Area Network  

LAN의 종류
- Ethernet　(IEEE802.3)
- Token Ring　(IEEE802.5)
- FDDI　(Fiber Distributed Data Interface)

### MAN
- Metropolitan Area Network
- 같은 도시나 지리적으로 가까운 위치에 있는 LAN을 연결
- 몇 개의 LAN을 연결하여 백본 라인을 구성
- 라우터나 전송 장비 없이도 저렴하게 인터넷 제공

### WAN
WAN 프로토콜
- HDLC
- PPP
- X.25
- Frame-Relay
- ATM

### SAN
- Storage Area Network
- 광섬유 채널로 구성. 시스템 종류에 영향 받지 않음. 저장장치용 고속 네트워크


## 네트워크
### LAN 토폴로지 (topology)
- 스타형 Star
- 버스형 Bus
- 링형 Ring
- 트리형 Tree
- 망형 Mesh

### 매체 접근 방식
공유 매체에서 여러 터미널들의 충돌 및 경합 발생을 제어하는 접근 방식
- CSMA/CD
    - 단말기가 전송로의 신호 유무를 조사하고 전송함.
- Token Passing

## 네트워크 장비
### 케이블
- UTP 케이블
- STP 케이블

### LAN 카드
- 네트워크에 접속할 수 있도록 시스템에 설치하는 인터페이스 장비
- 데이터 신호를 전기 신호로, 전기 신호를 데이터 신호로 변환.
- MAC 주소로 데이터의 수신을 판별.

### 리피터
- 신호 재생 및 증폭

### 허브
- 신호를 노드에 전달해 주는 장비
- 네트워크 확장, 다른 허브와의 연결, 신호 증폭
- 더미 허브, 인탤리전트 허브, 스태커블 허브

### 브리지
- 모든 수신 프레임을 버퍼에 저장하고, 주소에 따라 프레임을 해당 포트로 전송하는 장비
- 큰 네트워크를 작고 관리하기 쉬운 세그먼트로 나눔
- 패킷의 송수신 주소를 분석하여 패킷 통과 여부를 판정

### 스위치
- 브리지와 비슷한 기능을 가진 장비
- 소프트웨어 기반인 브리지보다 빠름.
- MAC 주소 테이블을 기반으로 프레임을 전송.
- 전용 매체 교환 기술을 이용하여 트래픽 병목현상을 제거하고 포트별 속도를 보장

### 라우터
- OSI 계층의 물리 계층, 데이터 링크 계층, 네트워크 계층을 수행함.
- 서로 다른 통신망이나 서로 다른 프로토콜을 사용하는 통신망끼리 연결.
- 통신망에서 데이터를 전송하기 위해 경로를 설정하는 장비
- 최적의 경로 설정 데이터를 목적지까지 전달함

### 게이트웨이
- 서로 다른 통신망이나 서로 다른 프로토콜을 사용하는 통신망끼리 연결.
- 데이터 전송을 위해 두 개의 네트워크 사이에서 중계자 역할을 함.

## 프로토콜
통신을 하기 위한 통신 규약.

### 프로토콜 구성요소
- 구문
- 의미
- 타이밍

### OSI 7 계층 모델과 TCP/IP 모델

- 물리 > 데이터 링크 > 네트워크 > 전송 > 세션 > 표현 > 응용
- 네트워크 인터페이스 > 인터넷 > 전송 > 응용

### 네트워크 계층 프로토콜

IP
- Internet Protocol
- 비연결형, 비신뢰성
- 호스트의 논리 주소 지정

ICMP
- Internet Control Message Protocol
- IP 전달에 대한 다양한 메시지를 전달하기 위한 프로토콜
- 호스트 간 연결 확인. 오류 보고 및 이벤트 알림

IGMP
- Internet Group Management Protocol
- 네트워크에서 장비들이 어느 멀티캐스트 그룹에 속해 있는지 알리기 위한 프로토콜

ARP
- IP 주소를 MAC 주소로 매핑

RARP
- MAC 주소를 IP 주소로 매핑

### 전송 계층 프로토콜

TCP 3-Way Handshake
1. SYN　클라이언트의 접속 요청 플래그
2. SYN + ACK　클라이언트의 접속 요청에 대한 서버의 응답 플래그
3. ACK　서버의 응답에 대한 클라이언트의 응답 플래그

TCP 상태 전이
- CLOSE　포트가 닫힌 상태
- LISTEN　포트가 열린 상태로 요청을 기다리는 상태
- SYN_RCV　SYN 요청을 받고 상대방의 응답을 기다리는 상태
- ESTABLISHED　포트 연결 상태

**TCP　UDP**


### 응용 계층 프로토콜

FTP
- 파일 송수신. 계정 접속과 익명 접속이 있음. 포트 20, 21

Telnet
- 원격 접속. 데이터를 평문으로 전송. 포트 23

SSH
- 원격 접속. Telnet의 보안 취약점을 해결. 파일 전송도 가능. 포트 22

SMTP
- 이메일 송신. 포트 25

DHCP
- IP 주소, 게이트웨이, DNS 주소를 동적으로 할당. 포트 67, 68

TFTP
- FTP보다 단순한 파일 전송. 포트 69

HTTP
- 웹 서버와 클라이언트 간의 통신 프로토콜. 포트 80

POP3
- 전자 우편 수신. 메일 읽은 후 삭제. 포트 110

IMAP
- 전자 우편 수신. 메일 읽은 후 저장. 포트 143

SNMP
- 네트워크 장비들을 관리하고, 감시하기 위한 프로토콜. 포트 161, 162


## IP 주소와 도메인

### IPv4
- 네트워크 주소와 호스트 주소는 서브넷 마스크로 구분.
- 서브넷 마스크: 디폴트 서브넷 마스크, 변형된 서브넷 마스크
- 통신 방식: 유니캐스트, 멀티캐스트, 브로드캐스트

### IPv6
- IPSec 프로토콜이 포함돼서 보안이 향상됨.
- MAC 주소와 Prefix를 통해서 IP 주소를 자동으로 설정.
- 통신 방식: 유니캐스트, 멀티캐스트, 애니캐스트

### 사설 IP 주소　Private IP Address
- 공인 IP 주소가 아닌 사적인 용도로 사용되는 IP 주소. IP 주소 부족을 해결.

### 도메인
- 레이블과 . 으로 구성. 국가 도메인, 국제 도메인.
- co 영리기관, or 비영리 기관 / com 영리기관, org 비영리기관

## 인터넷 서비스 종류

### 웹 서비스
### 메일 서비스
### FTP 서비스
### DNS 서비스
### Telnet 서비스
    telent [옵션] [IP 주소/도메인명] [포트번호]
- -a　자동 로그인 요청
- -d　디버깅
- -l　사용자명 지정
- port　접속 대상의 포트 지정
### SSH 서비스
    ssh [옵션] [IP 주소/도메인명] [포트번호]
    ssh [사용자명]@[IP 주소/도메인명]
- -a　인증 에이전트 사용 불가 지정
- -c　세션 암호화에 사용할 암호 알고리즘 지정
- -l　사용자명 지정
- -p　접속 대상의 포트 지정
### 기타
SAMBA 서비스
- 파일이나 프린터 공유. SMB 프로토콜  

NFS 서비스
- 다른 시스템의 파일 시스템을 마운트하여 내것처럼 사용
- NFS 관련 데몬: nfsd, rpc.mountd, rpc.lockd, rpc.statd

RPC 서비스
- 서비스와 포트를 동적으로 연결
- RPC 데몬: rpcbind

## 인터넷 서비스 설정
### 네트워크 인터페이스 설정
인터페이스 종류
|   |   |
|:---:|:---:|
| lo | 루프백 인터페이스 |
| eth | 이더넷 인터페이스 |
| ppp | PPP 인터페이스 |
| plip | 병렬 인터페이스 |
| sl | 직렬 인터페이스 |

인터페이스 모듈 적재
1. 자동 적재
    - 시스템 부팅시 모듈 정보를 저장한 환경설정 파일을 읽어서 자동으로 적재
    - /etc/modprobe.conf
2. 수동 적재
    - lsmod　적재된 모듈 확인
    - insmod　적재할 모듈 삽입
    - rmmod　적재된 모듈 삭제
    - modprobe　모듈의 적재 및 삭제

### 네트워크 설정 파일

/etc/sysconfig/network
> 네트워크 기본 정보가 설정되어 있는 파일
```
NETWORK=yes
HOSTNAME=localhost.localdomain
GATEWAY=192.168.0.1
GATEWAY DEV=eth0
```

/etc/sysconfig/network-scripts/ifcfg-eth0
> 지정된 인터페이스에 대한 네트워크 설정 정보  
> 첫 번째 이더넷 카드(ifcfg-eth0), 두 번째 이더넷 카드(ifcfg-eth1)
```
DEVICE=eth0
BOOTPROTO=static
BROADCAST=192.168.10.255
IPADDR=192.168.10.100
NETMASK=255.255.255.0
GATEWAY=192.168.10.1
DNS1=168.126.63.1
ONBOOT=yes
TYPE=Ethernet
```

/etc/resolv.conf
> 기본 DNS 서버를 지정
```
search domain.co.kr
nameserver 168.126.63.1
nameserver 168.126.63.2
```

/etc/hosts
> IP 주소와 호스트명 혹은 도메인명을 매핑
```
127.0.0.1   localhost localhost.localdomain
::1         localhost localhost.localdomain
192.168.10.100  domain.co.kr
```

/etc/host.conf
> 도메인 요청 시 DNS 서버 검색 순서를 지정

/etc/protocols
> /etc/services 파일에서 정의되는 프로토콜이 정의되어 있는 파일

/etc/services
> 서비스가 사용하는 포트 번호를 지정

### 네트워크 설정 명령어

ifconfig
> IP 주소를 설정, 활성/비활성, 인터페이스 정보 출력

ip addr show
> 네트워크 정보를 확인하는 명령

route
> 목적지까지 경로를 설정 및 관리하는 명령

ping
> 연결 상태 확인
```bash
ping [옵션] [IP 주소/도메인명]
```
- -c　전송할 패킷의 요청 횟수 지정
- -l　전송할 패킷의 크기를 지정

traceroute
> 경로를 출력
```bash
traceroute [옵션] [IP 주소/도메인명]
```
- -d　호스트 명을 확인하지 않음.
- -m　최대 홉 수를 지정 (기본: 30홉)

netstat
> 현재 시스템의 네트워크 연결 상태를 확인  
> 프로토콜, 라우팅 테이블, 인터페이스 등을 확인할 수 있다
```bash
netstat [옵션]
```
- -a　모든 서비스 및 포트 출력
- -e　이더넷 데이터 전송 통계 출력
- -n　IP주소 형식으로 출력
- -r　라우팅 테이블 출력
- -s　프로토콜 통계 출력

arp
> ARP 테이블을 설정하고 확인
- -a　지정하지 않으면 모든 테이블의 정보 출력. 지정하면 지정한 테이블의 정보 출력
- -s　IP 주소와 MAC 주소를 ARP 테이블에 추가

ethtool
> 네트워크 인터페이스의 물리적 연결 상태를 확인하는 명령  
> mii-tool 보다 상세

mii-tool
> 네트워크 인터페이스의 속도, 전송모드 등을 확인

ss
> 네트워크 상태 확인. netstat을 대체


<br>
<br>
<br>

# 응용분야

## 리눅스 관련 기술
### 클러스터링
구성
- 클러스터 노드, 클러스터 관리자

종류
- HPC = 베어울프
- LVS
- HA

### 임베디드 시스템
- 특정 목적에 부합하는 최적화 설계
- 실시간 처리와 높은 신뢰성

구성
- 하드웨어, 소프트웨어

| 장점 | 단점 |
|---|---|
| 기능성, 확정성 우수 | 많은 메모리 요구 |
| 로열티가 없어 가격 경쟁력 우수 | 텍스트 기반 개발환경으로 불편 |
| 데스크탑 환경과 동일해서 개발용이 | 사용자모드와 커널모드 메모리 접근이 복잡. 솔루션 구성이 어려움 |
| 다양한 플랫폼 지원 | 표준화가 어려움 |


## 서버 분야

### 서버 가상화
- 하나의 물리적인 IT 자원이 다수의 논리적인 IT자원으로 사용될 수 있는 기술

**하이퍼 바이저**
- 가상 머신과 하드웨어 사이에 위치. 다수의 가상 머신이 동작하게 함
- 자원을 각 가상머신에게 논리적으로 할당하고 스케줄링 한다.
- 하드웨어 자원과 가상머신간의 고립화를 보장

하이퍼 바이저 운영 방식
- 네이티브 방식: 하드웨어에 직접 설치 (Xen, KVM)
- 호스티드 방식: 일반 어플리케이션처럼 실행 (Vbox, VMware)

오픈소스 하이퍼 바이저
- Xen
    - 케임브리지대
    - 전가상화, 반가상화 가능. 단, 반가상화 구성 시에는 QEMU 기반
    - 반가상화 시에 호스트와 다른 아키텍처를 게스트로 실행 불가
- KVM
    - Qumranet
    - CPU는 전가상화만 가능. x86 기반
    - RHEV가 대표적
    - QEMU라는 CPU에뮬레이터 사용
- Virtual Box
    - 이노테크 - 오라클
    - 전가상화만 지원 (x86, Intel-64, AMD-64 다 가능)
    - .vdi (vmware는 vmx)

### 클라우드 컴퓨팅
- 네트워크로 자원 혹은 서비스를 제공
- 소프트웨어와 데이터를 통합하여 관리함으로써 유지보수, 효율성, 비용절약의 이점
- 낮은 가격에 높은 가용성

서비스 종류
- IaaS
- SaaS
- PaaS

구축 환경
- 오픈 스택
- 클라우드 스택
- 유칼립투스

### 빅데이터
3V: Volume, Velocity, Variety

하둡
- 대용량 데이터를 분산처리.
- 자바 기반의 오픈 소스 프레임워크
- 복제본을 저장하므로 데이터 복구 가능
- x86 CPU에 리눅스면 됨

## 임베디드 시스템
### 모바일
- 안드로이드
- iOS
    - OS X를 기반
- 타이젠
    - 인텔, 삼성
    - 웹표준, HTML5 지원
    - 리눅스 커널 기반

### 스마트 TV
- 타이젠
- webOS
    - 팜 - LG

### IVI
- In Vehicle Infotainment
- GENIVI
    - 오픈 소스 기반의 차량 멀티미디어 플랫폼 표준화 활동


# 추가

## 23년 12월 기출

### 다음 중 LVM 구성할 때 가장 먼저 생성되는 것은?

     1.	VG(Volume Group)
     2.	LV(Logical Volume)
     3.	PV(Physical Volume)
     4.	PE(Physical Extend)
PV-VG-LV 순서

### 다음은 확장 패키지 관련 저장소를 설치하는 과정이다. (괄호) 안에 들어갈 내용으로 알맞은 것은?

    yum install (괄호)
     1.	epel
     2.	epel-repository
     3.	epel-release
     4.	epel-download
epel-release

### 다음중 vi 편집기의 ex 명령모드에 대한 설명으로 틀린 것은?

     2.	w 파일명 → 지정한 '파일명'으로 저장한다.
위는 맞는 내용

### 다음 중 nano 편집기에서 

     1.	[Ctrl]+[a]  현재 행의 시작 부분으로 커서를 이동
     2.	[Ctrl]+[e]  현재 행의 끝 부분으로 커서를 이동
     3.	[Ctrl]+[o]  파일을 저장하고 나가기 위해 사용
     4.	[Ctrl]+[i]  탭을 삽입합니다.


### 다음 중 작업번호가 2번인 백그라운드 프로세스를 종료시키는 명령으로 알맞은 것은?

     1.	kill 2   PID가 2인 프로세스 종료
     2.	kill %2   정답
     3.	kill -j 2
     4.	kill -b 2

### 다음 중 standalone 방식과 inetd 방식에 대한 비교 설명으로 알맞은 것은?
     
     1.	inetd 방식이 standalone 방식보다 메모리 관리가 더 효율적이다.

### 다음 보기의 시그널을 번호값이 낮은 순부터 높은 순으로 정렬했을 때 세 번째에 해당하는 시그널 이름으로 알맞은 것은?

     1.	SIGTSTP - 20 : Terminal Stop Signal 프로세스를 대기(suspend)로 전환
     2.	SIGKILL - 9 : Kill
     3.	SIGINT - 2 : Terminal Interrupt 
     4.	SIGTERM - 15 : Termination. kill 시스템 호출시, 가능하면 정상종료 시키는 시그널
SIGTERM

### 다음 설명에 해당하는 파일명으로 가장 알맞은 것은?
    모든 사용자에게 적용되는 alias와 함수를 설정하려고 한다.

     1.	/etc/.bashrc
     2.	/etc/.bash_profile
     3.	/etc/bashrc
     4.	/etc/profile
/etc/bashrc

### 다음 중 (괄호) 안에 들어갈 명령의 결과로 알맞은 것은?
    user = kaitman
    echo "$user"

     1.	아무것도 출력되지 않는다.
     2.	$user
     3.	ihduser
     4.	kaitman
kaitman


### 다음은 로그인 셀을 확인하는 과정이다. (괄호) 안에 들어갈 명령어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220231209/r220231209m35.gif?1702544534)

     1.	ps
     2.	chsh
     3.	jobs
     4.	shells
ps

### 다음 설명에 해당하는 파일명으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220231209/r220231209m39.gif?1702544534)

     1.	/etc/fstab   파일 시스템 테이블을 나타내는 파일
     2.	/etc/mtab   현재 마운트된 파일 시스템에 관한 정보
     3.	/etc/mounts   실제로 마운트되어 있는지 여부와 관계없이 보여줍니다.
     4.	/proc/partitions   파티션 정보
/etc/mtab

### 다음 중 /etc/fstab 파일의 첫 번째 필드에 설정할 수 있는 값으로 틀린 것은?

     1.	UUID
     2.	LABEL
     3.	마운트 포인트
     4.	장치 파일명
마운트 포인트  
장치명=/dev=UUID, 라벨명, 네트워크 주소, 파일명

### 다음은 ihduser 사용자의 홈 디렉터리가 차지하고 있는 디스크 용량을 확인하는 과정이다. (괄호) 안에 들어갈 명령어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220231209/r220231209m41.gif?1702544534)

     1.	df -sh ~ihduser
     2.	quota ihduser
     3.	du -sh ~ihduser
     4.	df -sh /home/ihduser
du -sh ~ihduser  
du는 디스크 사용량을 확인. df는 디스크의 남은량을 확인. quota는 디스크 사용량 제한

### 다음 그림에 해당하는 명렁어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220231209/r220231209m44.gif?1702544534)

     1.	quota
     2.	edquota
     3.	repquota
     4.	xfs_quota
repquota - report quota

### 	project 그룹에 속한 사용자들이 /project 디렉터리에서 파일 생성은 자유로우나 삭제는 본인의 생성한 파일만 가능하도록 설정하려고 한다. 또한 파일 생성 시 자동으로 그룹 소유권이 project로 부여되도록 설정하려고 한다. /project 디렉터리의 정보가 다음과 같을 때 관련 명령으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220231209/r220231209m46.gif?1702544534)

     1.	chmod 1770 /project
     2.	chmod 2770 /project
     3.	chmod 3770 /project
     4.	chmod 5770 /project

chmod 3770 /project  
그룹에 속한 사용자들이 디렉터리에서 파일 생성은 자유로우나 삭제는 본인이 생성한 파일만 가능 => Sticky Bit (1)  
파일 생성시 자동으로 그룹 소유건이 Project로 부여 되도록 설정 => Set GID(2)  
Sticky Bit 와 Set GID를 동시에 설정 해야 하므로 1+2 =3

### 다음 명령의 결과로 설정되는 lin.txt 파일의 허가권 값으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220231209/r220231209m47.gif?1702544534)

     1.	----r-----
     2.	-r--r--r--
     3.	-rw-r--r--
     4.	-rw-rw----
3번

### 다음 상황에 적합한 클리스터링 기술로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220231209/r220231209m52.gif?1702544534)

     3.	고가용성 클러스터

### 다음 중 SYN Flooding 공격과 같은 네트워크 상태 정보를 확인하는 명령으로 알맞은 것은?

     1.	ip
     2.	arp
     3.	route
     4.	netstat
netstat

### 다음 설명에 해당하는 파일명으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220231209/r220231209m54.gif?1702544534)

     1.	/etc/hosts
     2.	/etc/resolv.conf
     3.	/etc/sysconfig/network
     4.	/etc/sysconfig/network-scripts
/etc/resolv.conf

### 다음 중 시스템에 설정된 게이트웨이 주소값을 확인하는 명령어로 틀린 것은?
     
     1.	ip
     2.	route
     3.	netstat
     4.	ethtool
ethtool

<br>

## 23년 9월

### 1.	project 그룹에 속한 사용자들이 /project 디렉터리에서 파일 생성은 자유로우나 삭제는 본인이 생성한 파일만 가능하도록 설정하려고 한다. /project 디렉터리의 정보가 다음과 같을 때 관련 명령으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230909/r220230909m1.gif?1694553791)

     1.	chmod g+s /project
     2.	chmod g+t /project
     3.	chmod o+s /project
     4.	chmod o+t /project
4.	chmod o+t /project

### 다음 중 특수 권한을 부여해서 사용하는 경우의 예로 가장 거리가 먼 것은?
     
     1.	Sticky-Bit를 파일에 부여한다.
     2.	Set-UID를 실행 파일에 부여한다.
     3.	Set-GID를 실행 파일에 부여한다.
     4.	Set-GID를 디렉터리에 부여한다.
1.	Sticky-Bit를 파일에 부여한다.

### 다음 결과에 대항하는 명령어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230909/r220230909m7.gif?1694553792)

     1.	lsblk - 트리로 보여줌
     2.	blkid - UUID로 보여줌
     3.	fdisk
     4.	df
lsblk

### 다음 중 최근에 실행한 명령 중에 'al'이라는 문자열을 포함한 명령을 찾아서 실행하는 명령으로 알맞은 것은?

     1.	!?al

### ls 명령으로 에일리어스(alias)가 설정된 상태에서 원래의 ls 명령어를 실행하려고 한다. 다음 중 관련 설명으로 알맞은 것은?

     3.	ls 명령어 앞에 \ 기호를 덧붙여서 실행한다.

### 	다음 (괄호) 안에 들어갈 내용으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230909/r220230909m19.gif?1695071370)

     1.	exec
     2.	fork
     3.	init
     4.	systemd
fork

### 다음 중 kill 명령어를 실행할 때 전달되는 기본 시그널 명칭과 번호의 조합으로 알맞은 것은?
     
     1.	SIGKILL, 9
     2.	SIGKILL, 15
     3.	SIGTERM, 9
     4.	SIGTERM, 15
SIGTERM, 15

### 다음 중 포어그라운드 프로세스를 백그라운드 프로세스로 전환하기 위해 사용하는 키 조합으로 알맞은 것은?
     
     1.	[Ctrl] + [c]
     2.	[Ctrl] + [a]
     3.	[Ctrl] + [z]
     4.	[Ctrl] + [d]
[Ctrl] + [z] 로 작업을 일시중지 하고 bg로 백그라운드 실행하면 된다.


### 다음 명령의 결과에 대한 설명으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230909/r220230909m24.gif?1694553791)

     1.	bash 프로세스의 우선순위를 높인다.
     2.	bash 프로세스의 우선순위를 낮춘다.
     3.	bash 프로세스의 PRI 값을 -10으로 변경한다.
     4.	사용법 오류로 인해 실행되지 않는다.
4.	사용법 오류로 인해 실행되지 않는다.

### 다음은 프로세스 아이디가 513, 514, 515번인 프로세스를 종료시키는 과정이③ (괄호) 안에 들어갈 명령어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230909/r220230909m26.gif?1694553791)

     1.	kill
     2.	pkill
     3.	killall
     4.	pgrep
kill

### 다음 그림에 해당하는 명령어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230909/r220230909m27.gif?1694553791)

     1.	ps
     2.	top
     3.	jobs
     4.	pstree
top

### 다음 중 vi 편집기의 명령 모드에서 바로 직전에 삭제한 줄을 다시 복원하기 위해 실행하는 명령으로 알맞은 것은?

     1.	c   변경 명령을 시작하는데 사용
     2.	r   하나의 문자를 다른 문자로 교체
     3.	u   undo
     4.	dd

### 다음 중 vi 편집기에서 한 줄이 linux인 경우에만 전부 Linux로 치환하는 명령으로 알맞은 것은?


     1.	:% s/^linux$/Linux/g
     2.	:% s/linux/^Linux$/g
     3.	:% s/\<linux\>/Linux/g
     4.	:% s/linux/\<Linux\>/g
1.	:% s/^linux$/Linux/g

### 다음 중 vi 편집기에서 행 번호가 표시되도록 하는 ex 모드 환경설정으로 알맞은 것은?

     1.	set no      = set nonu nu 기능 off
     2.	set ai   자동 들여쓰기
     3.	set sm   괄호 입력시 자동으로 대응되는 괄호 표시
     4.	set number   = set nu

### 	다음 중 현재 디렉터리에 있는 C 언어 파일만을 source.tar로 묶는 명령으로 알맞은 것은?

     2.	tar rvf source.tar *.c   r은 기존 압축파일에 파일 추가
     4.	tar cvf source.tar *.c

### 47.	다음 중 LVM에 대한 설명으로 틀린 것은?
     
     1.	물리적 디스크 2개를 이용해서 하나의 파티션으로 구성할 수 있다.
     2.	파티션의 크기를 확장해도 데이터의 손실이 발생하지 않는다.
     3.	파티션의 크기를 축소해서 데이터의 손실이 발생하지 않는다.
     4.	물리적 디스크 1개를 이용해서 두 개의 파티션을 구성할 수 있다.
정답 3  
LVM = Logical Volume Management - 파티션 관리하며 용량 확장

### 다음 결과에 해당하는 명령으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230909/r220230909m54.gif?1694553791)

     1.	echo $DISPLAY
     2.	xhost list $DISPLAY
     3.	xauth list $DISPLAY
     4.	export DISPLAY
3.	xauth list $DISPLAY  
xhost 뒤에는 ip주소가 와야함.

### 다음 중 패킷 교환 방식에 대한 설명으로 틀린 것은?
     
     1.	패킷별로 우선순위를 부여할 수 있다.
     2.	회선 교환 방식과 비교해서 지연이 적게 발생한다.
     3.	각각의 패킷마다 오버헤드 비트가 존재한다.
     4.	고정 대역을 할당하지 않는 관계로 이론상으로는 무제한 수용이 가능하다.

2.	회선 교환 방식과 비교해서 지연이 적게 발생한다. X 더 발생함.

### 60.	다음 설명에 해당하는 기술로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230909/r220230909m60.gif?1694553791)

     1.	FDDI
     2.	X.25
     3.	Frame Relay
     4.	Cell Relay
1.	FDDI

### 다음 중 시스템에 장착된 이더넷 카드의 MAC 주소를 확인하는 명령으로 알맞은 것은?
     
     1.	ip
     2.	route
     3.	mii-tool
     4.	ethtool
정답은 ip 이나 ethtool도 가능

### 74. 다음 설명에 해당하는 파일명으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230909/r220230909m74.gif?1694553792)

     1.	/etc/hosts
     2.	/etc/resolv.conf
     3.	/etc/sysconfig/network
     4.	/etc/sysconfig/network-scripts
1.	/etc/hosts

### 79.	다음 설명에 해당하는 프로그램으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230909/r220230909m79.gif?1694553792)

     1.	Docker
     2.	OpenStack
     3.	Kubernetes
     4.	Ansible
Kubernetes

<br>

## 23년 6월

### 1.	다음 설명의 상황에 설정해야 하는 작업으로 가장 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230610/r220230610m1.gif?1703227203)

     1.	project 디렉터리에 부여된 w 권한을 제거한다.
     2.	project 디렉터리에 Set-UID를 부여한다.
     3.	project 디렉터리에 Set-GID를 부여한다.
     4.	project 디렉터리에 Sticky-Bit를 부여한다.
4번

### 3.	다음 중 특수 권한이 설정된 파일이나 디렉터리로 알맞은 것은?
     
     1.	/etc
     2.	/etc/shadow
     3.	/etc/passwd
     4.	/usr/bin/passwd
4. /usr/bin/passwd  
/usr/bin/passwd 파일은 사용자의 비밀번호를 변경할 때 사용되는 실행 파일로, 일반 사용자도 자신의 비밀번호를 변경할 수 있도록 setuid 특수 권한이 설정되어 있음.

### 5.	다음은 ihduser 사용자에게 대한 디스크 쿼터를 설정하는 과정이다. ( 괄호 ) 안에 들어갈 명령어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230610/r220230610m5.gif?1703227204)

     1.	quota          디스크 사용량이나 상태정보를 표시
     2.	edquota        텍스트 편집기같은 인터페이스를 제공
     3.	setquota       -u 옵션 사용 시
     4.	xfs_quota      -x -c 옵션 사용 시 xfs_quota 명령어

### 8.	다음 중 파일 시스템이 ext4인 /dev/sdb1 파티션을 /data 디렉터리로 마운트하는 명령으로 알맞은 것은?
     
     1.	mount –o ext4 /data /dev/sdb1
     2.	mount –o ext4 /dev/sdb1 /data
     3.	mount –t ext4 /data /dev/sdb1
     4.	mount –t ext4 /dev/sdb1 /data
정답 4  
-t = 파일 시스템의 유형을 지정하는데 사용  
-o = 마운트할 때 사용할 옵션을 지정하는데 사용

### 24.	다음 중 백그라운드로 실행 중인 데몬을 확인하는 방법으로 알맞은 것은?
     
     1.	jobs 명령어를 사용해서 확인한다.
     2.	fg 명령어를 사용해서 확인한다.
     3.	bg 명령어를 사용해서 확인한다.
     4.	ps 명령어를 사용해서 확인한다.
4번  
1. jobs 명령어는 현재 셸 세션에서 실행된 백그라운드 작업의 상태를 보여주지만,
셸 세션과 관련된 작업에 한정되므로 시스템 전체에서 실행 중인 데몬을 확인하는 데 사용할 수 없습니다.
4. ps 명령어는 현재 시스템에서 실행 중인 모든 프로세스(데몬 포함)의 정보를 제공

### 31.	다음 그림에 해당하는 편집기로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230610/r220230610m31.gif?1703227204)

     1.	pico
     2.	nano
     3.	emacs
     4.	gedit
emacs - File, Edit 이 있음

### 33.	다음 중 vi 편집기에서 단어의 시작이 linux 인 경우에만 전부 Linux로 치환하는 명령으로 알맞은 것은?
     
     1.	:% s/^linux/Linux/g
     2.	:% s/\<linux/Linux/g
     3.	:% s/Linux/^linux/g
     4.	:% s/Linux/\<linux/g
문장의 시작이 linux인 경우라면 1번이 정답이지만,  
linux 단어를 Linux를 치환하기 위한 것이라면 2번이 정답입니다.

### 34.	다음 중 vi 편집기에서 환경 설정한 내용을 계속해서 사용하기 위해 등록하는 파일명으로 알맞은 것은?
     
     1.	.virc      != vim을 위한 설정 파일은 vimrc
     2.	.exrc      = vi 편집기에서 사용자가 환경 설정
     3.	dd
     4.	s

### 36.	다음 설명에 해당하는 패키지 관리 도구로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230610/r220230610m36.gif?1703227204)

     1.	alien
     2.	dselect
     3.	dnf
     4.	apt-get
alien


### 41.	다음 중 rpm 명령의 설치 관련 옵션으로 가장 거리가 먼 것은?
     
     1.	-i        설치
     2.	-U        업그레이드
     3.	-F        freshen, 업그레이드 또는 설치
     4.	-f

### 42.	다음 중 미설치된 sendmail 패키지에 대한 자세한 정보를 확인하는 명령으로 알맞은 것은?
     
     1.	rpm –qi sendmail    이미 설치된 패키지에 대한 정보를 조회
     2.	yum –qi sendmail
     3.	yum list sendmail   설치되어 있는지 여부
     4.	yum info sendmail   정답

### 53.	다음 명령의 결과에 대한 설명으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230610/r220230610m53.gif?1703227204)

     1.	X 클라이언트를 실행하면 권한이 없는 관계로 허가 거부된다.
     2.	X 클라이언트를 실행하면 원격지 시스템의 첫 번째 X 서버에 실행된다.
     3.	X 클라이언트를 실행하면 로컬 시스템의 첫 번째 X 서버에 실행된다.
     4.	X 클라이언트를 실행하면 원격지 시스템에서 허가 거부된다.
정답 3

### 60.	다음 설명에 해당하는 프로그램으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230610/r220230610m60.gif?1703227204)

     1.	Docker         컨테이너, 이미지 형태로 패키지 관리 및 배포 플랫폼
     2.	Openstack      오픈 소스 클라우드컴퓨팅 플랫폼
     3.	Kubernetes     Docker 자동화 플랫폼
     4.	Ansible        오픈 소스 자동화 플랫폼
정답 4

### 70.	다음 중 게이트웨이 주소를 확인하는 명령어로 알맞은 것은?
     
     1.	ifconfig
     2.	ifstat
     3.	ss
     4.	route
4번

### 73.	다음 중 UDP 프로토콜과 가장 관련 있는 서비스로 알맞은 것은?
     
     1.	TELNET
     2.	SMTP
     3.	DNS
     4.	HTTP
DNS

### 77.	다음에서 설명하는 해당하는 명령으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230610/r220230610m77.gif?1707293429)

     1.	telnet www.kait.or.kr@443
     2.	telnet www.kait.or.kr 443
     3.	telnet www.kait.or.kr 21
     4.	telnet www.kait.or.kr 22
SFTP는 (SSH File Transfer Protocol)의 약자임.  
말 그대로 SSH를 사용하기 때문에 22번 포트를 확인해야함.

<br>

## 23년 3월

### 3.	다음 중 파일이나 디렉터리에 부여된 Set-UID나 Set-GID와 같은 특수 권한을 확인하는 명령어로 알맞은 것은?
     
     1.	ls
     2.	chmod
     3.	chown
     4.	umask
1번 ls -l로 확인

### 6.	다음 중 fdisk 실행 상태에서 파티션을 삭제할 때 사용하는 명령으로 알맞은 것은?
     
     1.	d    파티션 삭제
     2.	r    없음
     3.	e    없음
     4.	x    전문가용 추가기능 나열

### 7.	다음 내용이 기록된 파일명으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230311/r220230311m7.gif?1680877130)

     1.	/etc/fstab
     2.	/etc/mtab
     3.	/etc/mounts
     4.	/etc/partitions
2번

### 12.	다음 중 특정 사용자에게 부여된 로그인 셸이 기록된 파일명으로 알맞은 것은?
     
     1.	/etc/shells
     2.	/etc/passwd
     3.	˜/.bashrc
     4.	˜/.bash_profile
/etc/passwd

### 23.	다음 설명에 해당하는 명칭으로 가장 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230311/r220230311m23.gif?1680877130)

     1.	inetd
     2.	xinetd
     3.	standalone
     4.	daemon
daemon


### 26.	프로세스 아이디(PID)가 1222인 bash 프로세스의 우선순위(NI)값이 0이다. 다음 중 이 프로세스의 NI값을 10으로 우선순위를 변경하는 명령으로 알맞은 것은?
     
     1.	nice 10 1222
     2.	nice -10 1222
     3.	nice 10 bash
     4.	nice -10 bash
정답 4번  
양수는 -n  
음수는 --n

### 30.	다음 중 nano 편집기에서 프로그램을 종료하는 키 조합으로 알맞은 것은?
     
     1.	[Ctrl]+[a] : 행의 맨 앞으로 커서 이동
     2.	[Ctrl]+[e] : 행의 맨 끝으로 커서 이동
     3.	[Ctrl]+[c] : 현현재 커서 위치의 줄번호와 열번호를 표시
     4.	[Ctrl]+[x] : 나노 편집기 종료, 변경사항 저장 여부 물어봄

### 41.	다음 결과에 해당하는 명령으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230311/r220230311m41.gif?1680877130)

     1.	rpm –ql vsftpd      패키지가 설치한 설치한 파일목록을 출력.
     2.	rpm –qa vsftpd      시스템에 설치된 모든 패키지 정보를 출력.
     3.	rpm –qV vsftpd      패키지를 검증
     4.	rpm –qip vsftpd-3.0.2-29.el7_9.x86_64.rpm    패키지 파일에 대한 정보를 출력.

### 47.	다음 설명에 해당하는 LVM 용어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230311/r220230311m47.gif?1680877130)

     1.	PV
     2.	PE
     3.	VG
     4.	LV
PE

### 50.	다음 설명에 해당하는 명칭으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230311/r220230311m50.gif?1680877130)

     1.	XFree86
     2.	Wayland
     3.	X.org
     4.	Metacity
1.	XFree86

### 64.	다음 설명에 해당하는 국제기구로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220230311/r220230311m64.gif?1680877130)

     1.	EIA
     2.	IEEE
     3.	ITU
     4.	ANSI
1.	EIA

### 66.	다음 중 OSI 계층 기준으로 가장 많은 계층을 지원하는 장치로 알맞은 것은?
     
     1.	HUB            1계층
     2.	Repeater       1계층
     3.	Bridge         2계층
     4.	Gateway        4계층
4. Gateway

### 71.	다음 중 SSH와 관련된 서비스로 가장 거리가 먼 것은?
     
     1.	nfs            네트워크 파일 시스템
     2.	scp            SSH 기반의 원격 파일 전송 프로토콜
     3.	rsh            원격 명령을 실행하는 프로토콜 SSH로 대체됨
     4.	sftp           SSH 파일 전송 프로토콜 FTP의 SSH버전
1. nfs


### 78.	다음 중 IPv4의 C클래스 대역에 할당된 사설 IP 주소의 네트워크 개수로 알맞은 것은?
     
     1.	32
     2.	64
     3.	128
     4.	256
4.	256

<br>

## 22년 9월

### 3.	다음 설명에 해당하는 LVM 관련 용어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220220903/r220220903m3.gif?1663151727)

     1.	볼륨 그룹(VG)
     2.	논리적 볼륨(LV)
     3.	물리적 볼륨(PV)
     4.	물리적 확장(PE)
2.	논리적 볼륨(LV)  
물리적인 볼륨(PV) (하드)를 하나로 모아 블록단위로 쪼갠것이 (PE),  
이 블록들의 집합이 VG.  
집합에서 필요량 만큼 "할당"받아 만드는 것이 논리적볼륨(LV)

### 5.	다음 중 인터넷상에서 원격으로 인쇄하기 위해 사용되는 프로토콜명으로 알맞은 것은?
     
     1.	IPP
     2.	LPRng
     3.	CUPS
     4.	PPD
1.	IPP - Internet Printing Protocol

### 8.	다음 중 소스 파일을 이용한 설치 방법이 나머지 셋과 다른 것은?
     
     1.	Apache httpd
     2.	MySQL
     3.	PHP
     4.	Nmap
MySQL - cmake 사용. 나머지는 make


### 27.	다음 ( 괄호 ) 안에 들어갈 내용으로 가장 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220220903/r220220903m27.gif?1717711123)

     1.	㉠ standalone, ㉡ foreground
     2.	㉠ standalone, ㉡ background
     3.	㉠ daemon, ㉡ foreground
     4.	㉠ daemon, ㉡ background
4.	㉠ daemon, ㉡ background


### 30.	다음 중 [Ctrl]+[z] 키 조합으로 실행했을 때 발생하는 시그널명과 번호의 조합으로 알맞은 것은?
     
     1.	SIGSTOP, 19
     2.	SIGSTOP, 20
     3.	SIGTSTP, 19
     4.	SIGTSTP, 20
4.	SIGTSTP, 20  
[Ctrl]+[z] 키워드는 SIGTSTP 20  
[Ctrl]+[z] 가 쓰이지않는 SIGSTOP 19

### 35.	다음 설명에 해당하는 파일로 가장 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220220903/r220220903m35.gif?1669582361)

     1.	˜/.bashrc
     2.	˜/.bash_history
     3.	˜/.bash_profile
     4.	˜/.bash_logout
환경변수는 profile / 별칭은 bashrc

### 41.	다음은 /project 디텍터리를 포함해서 하위 디렉터리 및 파일의 그룹 소유권을 project로 변경하는 과정이다. ( 괄호 ) 안에 들어갈 내용으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220220903/r220220903m41.gif?1663151727)

     1.	chgrp -r
     2.	chgrp -R
     3.	chmod -r
     4.	chown -r
2.	chgrp -R

### 43.	다음 결과에 해당하는 명령어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220220903/r220220903m43.gif?1663151727)

     1.	fdisk
     2.	mount
     3.	df
     4.	du
2.	mount

### 47.	다음 중 사용자 디스크 쿼터 설정을 위해 /etc/fstab 파일에 설정하는 옵션 값으로 틀린 것은?
     
     1.	quota          파일 용량 개수 설정
     2.	uquota         xfs파일에 적용
     3.	usrquota       사용자 할당량 사용
     4.	userquota
4.	userquota

### 62.	다음 중 로컬 네트워크상에 있는 다른 호스트의 MAC 주소를 확인할 때 사용하는 명령으로 알맞은 것은?
     
     1.	ip
     2.	ss
     3.	arp
     4.	ifconfig
3.	arp

### 64.	다음 중 CentOS 7 버전에서 이더넷 카드(Ethernet Card)를 장착했을 때 나타나는 장치명의 형식으로 가장 알맞은 것은?
     
     1.	lo
     2.	eth0
     3.	enp0s3
     4.	virbr0
3.	enp0s3

### 70.	다음 설명에 해당하는 명칭으로 가장 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220220903/r220220903m70.gif?1663151728)

     1.	X.25
     2.	ATM
     3.	DQDB
     4.	FDDI
3.	DQDB

<br>

## 22년 6월

### 17.	다음 중 vi 편집기에서 모든 windows라는 문자열을 linux로 치환하는 명령으로 알맞은 것은?
     
     1.	:% s/linux/windows/g
     2.	:% s/windows/linux/g
     3.	:% s/\<linux\>/windows/g
     4.	:% s/\<windows\>/linux/g
2.	:% s/windows/linux/g

### 18.	vim 편집기 실행할 때마다 행 번호가 자동으로 표시되도록 설정하려고 한다. 다음 중 관련 설정을 저장하기 위해 생성해야 할 파일명으로 알맞은 것은?
     
     1.	.virc
     2.	.vimrc
     3.	.viex
     4.	.vimex
2.	.vimrc

###  20.	다음 중 emacs 편집기를 종료하는 조합으로 알맞은 것은?
     
     1.	[Ctrl]+[c] 후에 [Ctrl]+[x]
     2.	[Ctrl]+[x] 후에 [Ctrl]+[c]
     3.	[Ctrl]+[c] 후에 [Ctrl]+[f]
     4.	[Ctrl]+[x] 후에 [Ctrl]+[f]
 2.	[Ctrl]+[x] 후에 [Ctrl]+[c]

### 40.	다음은 마운트된 /backup 영역을 마운트 해제하는 과정이다. ( 괄호 ) 안에 들어갈 명령어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220220611/r220220611m40.gif?1657003192)

     1.	umount
     2.	unmount
     3.	eject
     4.	nohup
1.	umount

### 41.	다음 그림에 해당하는 명령어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220220611/r220220611m41.gif?1657003192)

     1.	du
     2.	df
     3.	mount
     4.	fdisk
2.	df  
df 명령어가 시스템 전체의 디스크 공간을 확인하는 명령어라면, du 명령은 특정 디렉토리를 기준으로 디스크 사용량을 확인할 수 있습니다.

### 44.	다음은 /home 영역에 설정된 사용자 쿼터 정보를 확인하는 과정이다. ( 괄호 ) 안에 들어갈 명령어로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220220611/r220220611m44.gif?1657003192)

     1.	quota
     2.	edquota
     3.	setquota
     4.	repquota
4.	repquota

### 47.	다음은 원격지의 윈도우 시스템에 공유된 폴더를 마운트하는 과정이다. ( 괄호 ) 안에 들어갈 내용으로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220220611/r220220611m47.gif?1657003192)

     1.	ntfs
     2.	cifs
     3.	samba
     4.	xfs
2.	cifs  
윈도우 시스템에 공유된 폴더 마운트 : cifs, smb

### 50.	다음 설명에 해당하는 가상화 기술로 알맞은 것은?
![](https://img.comcbt.com/cbt/data/r2/r220220611/r220220611m50.gif?1657003192)

     1.	KVM
     2.	XEN
     3.	VirtualBox
     4.	Hyper-V
1.	KVM

### 66.	다음 중 게이트웨이(Gateway) 주소를 확인하는 명령어로 알맞은 것은?
     
     1.	nslookup
     2.	ifconfig
     3.	arp
     4.	route
4.	route  
게이트웨이 주소 확인 명령어 : route, netstat -r

ㅁㄴㅇㄹ

