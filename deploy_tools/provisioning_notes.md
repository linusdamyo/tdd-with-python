신규 사이트 프로비저닝
=====================

## 필요패키지

* nginx
* Python 3
* Git
* pip
* virtualenv

Ubuntu에서 실행방법 예:

	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv

## Nginx 가상 호스트 설정

* nginx.template.conf 참고
* SITENAME 부분을 다음과 같이 수정 staging.my-domain.com

## 폴더구조:
사용자 계정의 홈 폴더가 /home/username 이라고 가정

/home/username
--- sites
    +--- SITENAME
         +--- database
         +--- source
         +--- static
         +--- virtualenv
