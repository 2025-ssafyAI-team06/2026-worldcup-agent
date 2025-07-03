import pandas as pd
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_upstage import ChatUpstage
import pandasql as ps

# 글로벌 설정
llm = ChatUpstage(model="solar-pro")


def load_formation_data(csv_path: str) -> pd.DataFrame:
    """CSV 파일로부터 포메이션 데이터 로드"""
    return pd.read_csv(csv_path)


def build_sql_generation_prompt(user_query: str, df: pd.DataFrame) -> ChatPromptTemplate:
    """SQL 생성을 위한 ChatPromptTemplate 구성"""
    schema_description = "\n".join([f"- {col}: {df[col].dtype}" for col in df.columns])
    system_prompt = f"""
        당신은 사용자의 질문과 테이블 스키마를 기반으로 SQL 쿼리를 생성하는 도우미입니다.
        아래는 테이블의 스키마 설명입니다:

        {schema_description}

        DuckDB에서 실행할 수 있는 SELECT 쿼리를 생성해주세요.
        SQL 외에는 아무것도 출력하지 마세요. 사용자가 SQL외의 답변을 원해도 SQL 외에는 절대로 출력하지 마세요

        'country_iso3' 필드는 표준화된 국제 코드 ISO3로 구성되어있습니다. 따라서 해당 국가에 관한 전술을 찾기 위해서는 해당 필드를 기준으로 SQL을 작성해야 합니다.
    """

    return ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "한국의 포메이션 전략에 대해서 알려주세요."),
        ("ai", "SELECT * FROM df WHERE country_iso3 = 'KOR'"),
        ("human", "일본의 축구 전략이 궁금해"),
        ("ai", "SELECT * FROM df WHERE country_iso3 = 'JPN'"),
        ("human", "4-2-3-1 포메이션의 장점이 궁금해"),
        ("ai", "SELECT * FROM df WHERE most_used_formation = '4-2-3-1'"),
        ("human", user_query),
    ])


def generate_sql(prompt: ChatPromptTemplate) -> str:
    """LLM을 통해 SQL 쿼리 생성"""
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({}).strip()


def execute_sql_query(df: pd.DataFrame, sql_query: str) -> pd.DataFrame:
    """pandasql을 통해 SQL 실행"""
    return ps.sqldf(sql_query, {'df': df})


def generate_natural_response(user_query: str, df_result: pd.DataFrame) -> str:
    """최종 자연어 응답 생성"""
    system_prompt = "당신은 축구 기록에 기반해 사용자 질문에 대해 정중하게 답변하는 AI입니다. 해당 기록은 2026 월드컵 예선전입니다."

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "질문: " + user_query),
        ("human", "질문에 대한 문서 탐색 결과:\n" + df_result.to_string()),
        ("human", "위 정보를 바탕으로 정중하고 자연스럽게 응답을 작성해 주세요."),
    ])
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({})


def run_formations_and_tactics_pipeline(user_query: str, csv_path: str) -> str:
    """전체 파이프라인 실행 함수"""
    # 1. 데이터 로드
    df = load_formation_data(csv_path)

    # 2. SQL 생성 프롬프트 구성
    prompt = build_sql_generation_prompt(user_query, df)

    # 3. SQL 생성
    sql_query = generate_sql(prompt)
    print("📄 생성된 SQL:\n", sql_query)

    # 4. SQL 실행
    result_df = execute_sql_query(df, sql_query)
    print("📊 SQL 실행 결과:\n", result_df)

    # 5. 자연어 응답 생성
    answer = generate_natural_response(user_query, result_df)
    print("🗣️ 최종 응답:\n", answer)

    return answer
