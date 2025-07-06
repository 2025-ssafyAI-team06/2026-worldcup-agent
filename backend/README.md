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
