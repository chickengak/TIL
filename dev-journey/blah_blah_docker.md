### 도커 개념이 궁금하다면?
유튜브로. 그림도 없이 글로 배우는 것보다 유튜브영상 하나 보는게 나음.


## 내가 겪은 Docker 문제점들

### 1. 의외로 용량을 많이 먹는다.
우습게 보고 10기가면 충분하겠지? 했다가 이미지 빌드 중에 용량이 꽉 차서 몇 번을 재시작했는지 모르겠다. WSL이 골치아프게 할 수도 있으니 최소 50기가는 여유로운 상태로 시작하자.   
&nbsp;

### 2. 죄송한데 도커님 왤케 크세요?
리눅스와 MacOS는 인터넷에서 검색해서 나오는 경로에 모든 파일이 있는 모양이다. 무슨 문제가 발생하더라도 저 안에서 해결되는 모양.
- Linux:  /var/lib/docker/
- MacOS: ~/Library/Containers/com.docker.docker/Data/vms/0/

하지만 윈도우는 다르다!
- C:\ProgramData\DockerDesktop
- C:\Program Files\Docker\Docker  

이 경로들은 가봐도 Docker 프로그램 파일만 있고 용량부족으로 중단된 후 복구 안 된 버려진 내 c드라이브 십수기가바이트!는 아무리 찾아봐도 없었다.  
결국 파일을 찾아낸 경로는  
C:\Users\YourName\AppData\Local\Docker  
여기였다. 드디어 찾았다 내 c드라이브 도둑놈!  
원인은 WSL ext4.vhdx 였다. 이런 현상의 자세한 발생원인까진 못 찾았지만, 도커 이미지를 빌드할 때 그냥 빌드 뿅!하고 되는게 아니라 WSL을 이용해야 하는 모양이다. 아래에 링크로 해결법 적어 놓겠다.  
https://stackoverflow.com/questions/70946140/docker-desktop-wsl-ext4-vhdx-too-large
&nbsp;

### 3. 파이썬 requirements.txt 작성 시 주의사항
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

### 4. 도커 이미지 빌드 중에 pip 버전 오류 발생 시
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

### 5. 도커 허브 오류 -왜 제대로 안 알려줌?
이거 진짜 검색해도 내용이 잘 안나와서 빡친 부분이다.
이미지 빌드해서 도커 허브에 올리려고 했는데
```
denied: requested access to the resource is denied
```
이런 오류가 발생하더라. 오류명도 참고사항도 없고 구글링해도 뭔가 제대로 된 내용이 잘 안 나왔다.

일단 도커 허브 홈페이지로 가서 내 repository를 만들어야 한다.  
https://hub.docker.com/  
repository를 만들고 들어가보면 도커 push 명령어가 있을거다.  
하지만 신나서 따라 치면 오류는 여전할거다. 다만, No such image라고 오류가 바뀔거다.  
그렇다면 우리가 만들었던 이미지 이름을 바꿔야할 때가 온거다.  
뭣도 모르고 대충 만들었던 이름으로는 도커허브에 안 올라간다.
```
docker tag aaaa:bbbb cccc/dddd
```
이런 식으로 쳐야 한다. `docker images` 명령으로 현 이미지들 확인해서, aaaa는 님들 로컬에 있는 이미지 repository를 적고, bbbb에는 tag를 쓰고, cccc에는 님들 도커 허브 이름을 적고 dddd는 방금 도커 허브에서 만든 원격 repository를 적으면 된다.

이제 아까 도커 허브에서 봤던 명령어를 치면 된다.
```
docker push cccc/dddd:tagname
```
따라 치면 바보죠? 빨리 도커허브가서 명령어 다시 보던가 도커이름/리포지토리명 으로 바꿔서 치면 된다.  

고로 이미지 빌드할 때 처음부터 이름 잘 주는게 중요했다라는게 키포인트.




