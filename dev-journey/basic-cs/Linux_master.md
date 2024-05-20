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
- Boot Loader. Bootstrap Loader의 약자

`