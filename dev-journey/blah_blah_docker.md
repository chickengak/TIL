### 도커 개념이 궁금하다면?
유튜브로


## 내가 겪은 Docker 문제점들

### 의외로 용량을 많이 먹는다.
우습게 보고 10기가면 충분하겠지? 했다가 이미지 빌드 중에 용량이 꽉 차서 몇 번을 재시작했는지 모르겠다. 최소 50기가는 여유로운 상태로 시작하자  
&nbsp;

### 죄송해요 도커님 어디 계세요?
리눅스와 MacOS는 인터넷에서 검색해서 나오는 경로에 모든 파일과 캐시파일까지 있는 모양이다. 
- Linux:  /var/lib/docker/
- MacOS: ~/Library/Containers/com.docker.docker/Data/vms/0/

하지만 윈도우 경로에는 캐시파일이 읎다!
- C:\ProgramData\DockerDesktop
- C:\Program Files\Docker\Docker  

이 경로들은 가봐도 Docker파일만 있고 용량부족으로 중단된 후 버려진 작업하던 파일(내 c드라이브 수기가바이트!)은 아무리 찾아봐도 없다.

```
docker images
```
로 중단된 이미지가 보이는 경우도 있다던데 난 없었다. 보이면 image 없애면 된다고 하더라.  
결국 파일을 찾아낸 경로는  
C:\Users\YourName\AppData\Local\Docker  
여기였다. 드디어 찾았다 내 c드라이브 도둑놈!  
&nbsp;

### 파이썬 requirements.txt 작성 시 주의사항
내가 현재 쓰는 라이브러리들을 requirements.txt로 뽑고 싶다면?
```
pip freeze > requirements.txt
```
경로는 알잘딱으로 주길 바란다.  
```
아래와 같이 작성되어 나올거다.

absl-py==2.1.0
asgiref==3.7.2
astunparse==1.6.3
beautifulsoup4==4.12.3
...
```

다만, 내가 아나콘다로 파이썬을 사용중이라면?  
pip freeze를 했을 때, 
```
absl-py=2.1.0@머시기
...
```
이런 식으로 나올거다. 이건 하나하나 수정하거나 정규식으로 바꾸면 된다.  
그런데 추가로 검색하다가 아래 명령을 찾아냈다.
```
pip list --format=freeze > requirements.txt
```
이거로 가능하다는데 실행은 안해봤다.

하지만, conda 환경은 갓만든 환경도 이거저거 몇가지가 설치되어 있고, base환경에 있는 라이브러리도 가져오는 것도 있어서 꽤나 힘들거로 예상한다.

**conda일 경우엔 conda로 개발환경 공유하는게 더 빠르고 깔끔할거다!**  
&nbsp;

### 도커 이미지 빌드 중에 pip 버전 오류 발생 시
```
[notice] A new release of pip is available: 23.0.1 -> 23.3.2
[notice] To update, run: pip install --upgrade pip
```
이런 오류가 발생할 때는
```
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
``` 
이렇게 requirements.txt를 install 하기 전에 upgrade pip를 먼저 하면 된다.  
&nbsp;

### 도커 허브 오류 -왜 아무도 안 알려줌?
이거 진짜 검색해도 내용이 잘 안나와서 빡친 부분이다.
이미지 빌드해서 도커 허브에 올리려고 했는데
```
denied: requested access to the resource is denied
```
이런 오류가 발생하더라. 오류명도 참고사항도 없고 구글링해도 뭔가 원하는 내용이 잘 안나왔다.
