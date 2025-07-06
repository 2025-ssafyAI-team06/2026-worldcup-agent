
## ⚽ 2026 북중미 월드컵 통합 정보 챗봇 

![image](https://github.com/user-attachments/assets/0b643c1e-e330-4f1c-b8b4-740aa42751dc)

## 👨‍👦‍👦 Team

| 김승민(팀장) | 성수린 | 김광현 | 서보혁 | 지준오 |
| :---: | :---: | :---: | :---: | :---: |
|  <img width="160px" src="https://avatars.githubusercontent.com/u/195266142?v=4" /> | <img width="160px" src="https://avatars.githubusercontent.com/u/166473769?v=4"/> |  <img width="160px" src="https://avatars.githubusercontent.com/u/54222988?v=4" /> |  <img width="160px" src="https://avatars.githubusercontent.com/u/123562354?v=4" /> |  <img width="160px" src="https://avatars.githubusercontent.com/u/105596059?v=4" /> |
| AI, FE | AI, FE | AI, FE | AI, BE | AI, BE |
| [@seungminkimkim](https://github.com/seungminkimkim)| [@SurinSeong](https://github.com/SurinSeong) | [@kimgwang-hyeon](https://github.com/kimgwang-hyeon) | [@Seo-b-h](https://github.com/Seo-b-h)    | [@MegaZizon](https://github.com/MegaZizon) |

## 🌈 Service Introduce
#### 축구팬과 여행객을 위한 정보형 AI 챗봇 서비스

기존 웹 검색이나 뉴스 기사는 정보가 분산돼 있고 맥락이 부족해, 사용자가 원하는 정보를 빠르게 찾기 어렵습니다.

본 챗봇은 다음과 같은 주제를 중심으로 다양한 정보를 제공합니다:
- 2026년 월드컵 경기장 주변 관광지
- 변경된 월드컵 규정 및 축구 룰
- 역대 월드컵 경기 기록
- 지난 월드컵의 역사적 사건·사고 및 징크스
- 2026년 월드컵 출전 팀의 포메이션 및 전술 정보

사용자는 단순한 질문만으로도 월드컵에 관련된 정확한 정보를 손쉽게 얻을 수 있으며,
축구에 익숙하지 않은 팬들도 직관적인 UI를 통해 더 풍부한 월드컵 경험을 누릴 수 있습니다.

## 🧫 데이터 수집 및 처리방법
#### 데이터 수집
크롤링 : FIFA 공식 자료, 위키백과 및 통계 사이트, TripAdvisor 및 현지 관광청 API, 뉴스 및 기사
- BeautifulSoup
- Selenium

#### 데이터 전처리 방법
- Pandas
- TextSplitter

## 📚 Skills
**Frontend**

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![ES6](https://img.shields.io/badge/ES6-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

**Backend**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

**AI**

![Solar](https://img.shields.io/badge/Solar-DC322F?style=for-the-badge&logo=&logoColor=white)
![Upstage](https://img.shields.io/badge/Upstage-4B0082?style=for-the-badge&logo=&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-000000?style=for-the-badge&logo=LangChain&logoColor=white)

**database**

![ChromaDB](https://img.shields.io/badge/Chroma_DB-9D4EDD?style=for-the-badge&logo=database&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

**Infrastructure & Deployment**

![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![RDS](https://img.shields.io/badge/AWS_RDS-527FFF?style=for-the-badge&logo=amazonaws&logoColor=white)

## 🧬 System Archetacture
![sysarc](https://github.com/user-attachments/assets/7575e631-bb6c-4edb-9bec-a64469b8a638)

## ⛓️ RAG Pipeline
![llmarc](https://github.com/user-attachments/assets/a5d5b06b-4ed3-40b6-b7b4-a1767f2cc467)

## 🎬 Production Video
![productionvideo](https://github.com/user-attachments/assets/05deffa2-864b-431a-9141-fcec5cd556c1)

## 🚀 Backend Configuration
```
cd backend
```
#### 1. 벡터 데이터베이스 및  SQL 다운로드

Chroma 벡터 데이터베이스를 다운로드하여 프로젝트 루트에 배치합니다:

https://drive.google.com/file/d/1d3_UZLVLeyyox6CxBPrKFvnOo5IPGeav/view?usp=sharing

다운로드 후 압축을 해제하여 프로젝트 루트 폴더에 배치하세요.

---
PostgreSQL 데이터베이스 초기 설정을 위해 아래 SQL 파일을 다운로드합니다:

https://drive.google.com/file/d/1iPpchJEP-YvjEGctyG-bauBizR9zHkZ0/view?usp=sharing


---

다운로드한 `.sql` 파일을 원하는 데이터베이스에 import 하여 초기 데이터를 구성할 수 있습니다:

```bash
psql -U {your_rdb_user} -d {your_rdb_name} -f {download_files}.sql
```
---

#### 2. 환경 변수 설정

`.env` 파일을 생성하고 다음 내용을 작성합니다:

```env
# 🔑 Upstage LLM API 키
UPSTAGE_API_KEY={your_upstage_api_key}

# 🔍 Tavily 검색 API 키
TAVILY_API_KEY={your_tavily_api_key}

# 📦 Chroma Vector DB 설정
DB_NAME=spot_collection_2           # Chroma DB 이름
DB_PATH=./chroma_spot_v2            # 로컬 벡터 DB 저장 경로

# 🌐 Papago 번역 API 설정
CLIENT_ID={your_papago_client_id}           # Naver Papago 애플리케이션 Client ID
CLIENT_SECRET={your_papago_client_secret}   # Client Secret
TEXT_TRANSLATION_URL=https://papago.apigw.ntruss.com/nmt/v1/translation  # 번역 API URL

# 🗄️ RDB (PostgreSQL) 설정
RDB_HOST={your_rdb_host}             # 데이터베이스 호스트 주소
RDB_PORT={your_rdb_port}             # 데이터베이스 포트 (예: 5432)
RDB_NAME={your_rdb_name}             # 데이터베이스 이름
RDB_USER={your_rdb_user}             # DB 사용자 이름
RDB_PASSWORD={your_rdb_password}     # DB 비밀번호
```

#### 3. 애플리케이션 실행

Docker Compose를 사용하여 애플리케이션을 빌드하고 실행합니다:

```bash
docker-compose up --build
```

#### 📁 프로젝트 구조

```
backend/
├── chroma_jinxes/                      # 벡터 DB - jinxes
├── chroma_rules/                       # 벡터 DB - rules
├── chroma_spot_v2/                     # 벡터 DB - spot
├── .env                                # 환경 변수 설정 파일
├── Dockerfile                          # 도커 이미지 빌드 정의
├── docker-compose.yml                  # 도커 컴포즈 설정
├── requirements.txt                    # Python 패키지 목록
├── main.py                             # FastAPI 앱 실행
├── prompts.py                          # 정적 프롬프트
└── src/                                
    ├── util/                           # DB, API 요청 등 각종 유틸
    └── worldcup_bot/
        ├── country_statistics/         # 역대 월드컵 경기 기록 QA 로직
        ├── formations_and_tactics/     # 국가별 포메이션 QA 로직
        ├── jinxes_and_incidents/       # 지난 월드컵 징크스 QA 로직
        ├── rules_and_regulations/      # 2026년 월드컵 변경점 QA 로직
        └── stadium_attractions/        # 경기장 주변 관광지 및 맛집 QA 로직
```


## 🚀 Frontend Configuration
```
cd frontend
```


1. Install dependencies:
```bash
npm install
```

2. Create environment files:

- `.env.development`
```env
API_ENDPOINT=http://localhost:8000
```

- `.env.production`
```env
API_ENDPOINT=https://your-production-api.com
```

---

#### 🧪 Local Development

```bash
npm start
```

---

#### 🚀 Production Build

```bash
npm run build
```
