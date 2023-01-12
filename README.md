# MarkDown 
* 텍스트 기반의 가벼운 마크업언어(태그를 이용)
* 문서의 구조와 내용을 같이 쉽고 빠르게 적고자 탄생
* README.md 파일을 통해 오픈 소스의 공식 문서 작성
* 개인 프로젝트 소개 문서 작성
* 학습내용 정리
* 블로그 운영 


# 꾸미는 방법 : 
[https://www.markdownguide.org/cheat-sheet/] 참고

1. \# >헤딩 - 문서의 제목이나 소제목으로 사용
		#의 개수에 따라 제목의 수준을 구별(h1~h6)
		문서 구조의 기본, 글자 크기를 키우기 위해서 사용X
	
2.	1.2.3.  and *- > 리스트 순서가 있는 리스트와 없는 리스트
		목록표시

3.	```code black``` or `inline code block` > 코드블럭
		구문 강조!

4.	\[string](url) > 링크 
string은 보여지는 부분 url은 연결할 곳 나타냄
다른 페이지로 이동하는 링크 삽입
파일 경로를 넣어 다운로드 가능한 링크도 가능

4. ![string](img_url) > 이미지
	이미지를 삽입 / 이미지 너비와 높이 조절x / 조절필요하면 html사용

5. \*\*Bold**   \*italic* \~~strikeout~~ > 텍스트 강조
	굵게 , 기울임, 취소선을 이용해 텍스트강조

6. — (마이너스 3개 이상) > 수평선
	가로로 긴 수평선 작성


 # <span style="color:pink"> Git/Github 사용법

**`## Git 기본기`**

* README.md
   * 프로젝트설명 문서


* `repository` : 특정 디렉토리를 버전관리하는저장소
* `git init` : 명령어로 로컬 저장소 생성
- `.git` : 디렉토리 버전관리에 필요한 모든 것이 들어있음

<u>`ls - a > 숨긴파일 볼 수 있다.`</u>


* README.md파일 생성하기
  * 새 폴더 만들고 README.md 파일 생성
  * 파일을 버전관리하며 Git사용하자
    * commit한다 = 특정 버전(3가지 영역을 바탕으로 동작)으로 남긴다
        * 특정버전 3가지
       1. working directory = 작업영역
       2. staging Area  = commit으로 남기고 싶은 내용
          (변경사항을 저장)
       3. repository = commit을 저장 (저장소)


## <span style="color:red">명령어!
* git add 파일명 : working -> staging
* git commit : staging -> repository
* git status : 현재 상태 학인
* git commit - m “메세지” :  "메세지" commit 생성
* git push origin main(master) : 원격 저장소로 파일 저장

![image](https://miro.medium.com/max/640/1*zpvd5fjZAFGsVAEsvMGKxA.webp)
	


# README.md 순서 (local에서 생성해서 github으로 옮기기)
1. mkdir git_test - git_test 디렉토리 생성
2. cd git_test
3. git init (하고나면 master가 뜸)
4. touch README.md (README.md 파일 생성)
5. git status
6. git add README.md (working->staging)
7. git commit -m "Add README.md” (staging->repository commit함)
8. git config --global user.email "siwol406@gmail.com" (내 이메일넣고)
9. git config --global user.name "kdw"	(내 이름 넣고)
10. git remote add origin https://github.com/dongwoo46/git_test.git
11. git branch -M main (master를 main으로 변경)
12. git push -u origin main (너가 git의 주인이 맞는지 확인하는 과정)
13. git add 파일명 
14. git restore - - staged README.md > unstaged
15. git diff README.md >> unstaged 내용확인
16. git push origin main >> 오리진 메인에 올려주겠다. - origin main 원격 저장소
17. git clone 파일을 복사할 주소

` ls -a 모든 파일 보기 숨겨진것도`

`git commit “fqwf” 썻는데 막 이상한 글 나올 때 빠져 나오는 법 : esc ->:q!`

`git에서 다운로드 하면 최종 결과물만 가져옴 .git 안 나온다`


