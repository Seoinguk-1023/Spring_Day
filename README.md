# 💻 Spring Day 

## 🛠 제작자

## 💡 진행사항

1. 기능 3가지에 따라 App 3가지 생성 [Main / Project / Meeting]
2. URL 각 App 별로 관리 할 수 있게 정리
3. Static File 경로 추가 -> 새로운 파일 추가할 때 마다 `python manage.py collectstatic`

## 🧱 기술 스택

## 📖  사용법

### 1. 깃 클론

- `git clone [url]`

### 2. 가상 환경 생성 및 실행 후, 종속성 다운로드

- `python -m venv [가상환경 명]`
- window : `source [가상환경 명]/Scripts/activate` / mac : `source [가상환경 명]/bin/activate`
- `pip install -r requirements.txt`

## ⚙️ 로컬 서버 실행
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`
