import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="영화 데이터 그래프 도감 2 - 분포와 관계", layout="wide")
st.title("영화 데이터 그래프 도감 2 - 분포와 관계")

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"


@st.cache_data
def load_data():
    # 1년간 박스오피스 10위권에 든 영화 216편의 요약표를 불러옵니다
    df = pd.read_csv(DATA_URL)
    # 장르가 세로막대 기호(|)로 여러 개 적힌 영화는 첫 번째 장르만 씁니다
    df["장르"] = df["genre"].str.split("|").str[0]
    return df


df = load_data()

# ── 그래프 1. 장르별 영화 편수 도넛 ──
st.header("1. 장르별 영화 편수 (도넛)")
genre_count = df["장르"].value_counts().reset_index()
genre_count.columns = ["장르", "편수"]

fig = px.pie(
    genre_count,
    names="장르",
    values="편수",
    hole=0.45,  # 가운데 구멍을 뚫어 도넛 모양으로
)
# 조각에 마우스를 올리면 편수와 비율이 보이게 합니다
fig.update_traces(hovertemplate="%{label}<br>%{value}편 (%{percent})<extra></extra>")
st.plotly_chart(fig, width="stretch")

# '이 그래프로 알 수 있는 것' 한 문장을 적는 자리
st.text_input("이 그래프로 알 수 있는 것", key="note1")

st.divider()
# 앞으로 그래프를 계속 추가할 구역
st.header("2. (import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="영화 데이터 그래프 도감 2 - 분포와 관계", layout="wide")
st.title("영화 데이터 그래프 도감 2 - 분포와 관계")

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"


@st.cache_data
def load_data():
    # 1년간 박스오피스 10위권에 든 영화 216편의 요약표를 불러옵니다
    df = pd.read_csv(DATA_URL)

    # 장르가 세로막대 기호(|)로 여러 개 적힌 영화는 첫 번째 장르만 씁니다
    df["장르"] = df["genre"].str.split("|").str[0]

    # 총 관객 수를 숫자로 변환합니다
    df["total_audi"] = pd.to_numeric(df["total_audi"], errors="coerce")

    return df


df = load_data()

# ── 그래프 1. 장르별 영화 편수 도넛 ──
st.header("1. 장르별 영화 편수 (도넛)")

genre_count = df["장르"].value_counts().reset_index()
genre_count.columns = ["장르", "편수"]

fig = px.pie(
    genre_count,
    names="장르",
    values="편수",
    hole=0.45,
)

# 조각에 마우스를 올리면 편수와 비율이 보이게 합니다
fig.update_traces(
    hovertemplate="%{label}<br>%{value}편 (%{percent})<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)

# '이 그래프로 알 수 있는 것' 한 문장을 적는 자리
st.text_input("이 그래프로 알 수 있는 것", key="note1")

st.divider()


# ── 그래프 2. 장르별 영화 총 관객 트리맵 ──
st.header("2. 장르별 영화 총 관객 (트리맵)")

fig = px.treemap(
    df,
    path=["장르", "movieNm"],
    values="total_audi",
)

# 마우스를 올렸을 때 영화명과 총 관객이 보이게 합니다
fig.update_traces(
    hovertemplate="<b>%{label}</b><br>총 관객: %{value:,}명<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)

# '이 그래프로 알 수 있는 것' 한 문장을 적는 자리
st.text_input("이 그래프로 알 수 있는 것", key="note2")

st.divider()


# 앞으로 그래프를 계속 추가할 구역
st.header("3. (
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    layout="wide"
)

st.title("영화 데이터 그래프 도감 2 - 분포와 관계")

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"


@st.cache_data
def load_data():
    # 1년간 박스오피스 10위권에 든 영화 216편의 요약표를 불러옵니다
    df = pd.read_csv(DATA_URL)

    # 여러 장르가 적힌 영화는 첫 번째 장르만 사용합니다
    df["장르"] = df["genre"].fillna("기타").str.split("|").str[0].str.strip()

    # 총 관객 수를 숫자로 변환합니다
    df["total_audi"] = pd.to_numeric(df["total_audi"], errors="coerce")

    return df


df = load_data()


# ── 그래프 1. 장르별 영화 편수 도넛 ──
st.header("1. 장르별 영화 편수 (도넛)")

genre_count = df["장르"].value_counts().reset_index()
genre_count.columns = ["장르", "편수"]

fig = px.pie(
    genre_count,
    names="장르",
    values="편수",
    hole=0.45,
)

fig.update_traces(
    hovertemplate="%{label}<br>%{value}편 (%{percent})<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)

st.text_input("이 그래프로 알 수 있는 것", key="note1")


st.divider()


# ── 그래프 2. 장르별 영화 총 관객 트리맵 ──
st.header("2. 장르별 영화 총 관객 (트리맵)")

treemap_df = df.dropna(subset=["total_audi", "movieNm"]).copy()
treemap_df = treemap_df[treemap_df["total_audi"] >= 0]

fig = px.treemap(
    treemap_df,
    path=["장르", "movieNm"],
    values="total_audi",
)

fig.update_traces(
    hovertemplate="<b>%{label}</b><br>총 관객: %{value:,.0f}명<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)

st.text_input("이 그래프로 알 수 있는 것", key="note2")


st.divider()


# ── 그래프 3. 총 관객 수 히스토그램 ──
st.header("3. 영화별 총 관객 수 분포 (히스토그램)")

hist_df = df.dropna(subset=["total_audi", "movieNm"]).copy()
hist_df = hist_df[hist_df["total_audi"] >= 0]

if not hist_df.empty:
    fig = px.histogram(
        hist_df,
        x="total_audi",
        nbins=15,
        labels={"total_audi": "총 관객 수 (명)", "count": "영화 편수"},
    )

    fig.update_layout(
        xaxis_title="총 관객 수 (명)",
        yaxis_title="영화 편수",
        bargap=0.08,
    )

    fig.update_traces(
        hovertemplate="총 관객 수 구간: %{x:,.0f}명<br>영화 편수: %{y}편<extra></extra>"
    )

    st.plotly_chart(fig, use_container_width=True)

    # 영화가 가장 많이 몰린 구간 계산
    counts, edges = __import__("numpy").histogram(
        hist_df["total_audi"],
        bins=15
    )

    most_common_bin = counts.argmax()
    lower = edges[most_common_bin]
    upper = edges[most_common_bin + 1]
    most_common_count = counts[most_common_bin]

    # 총 관객 수가 가장 많은 영화 찾기
    top_movie = hist_df.loc[hist_df["total_audi"].idxmax()]
    top_movie_name = top_movie["movieNm"]
    top_movie_audience = top_movie["total_audi"]

    st.markdown("### 이 그래프로 알 수 있는 것")

    st.write(
        f"📊 **영화가 가장 많이 몰린 구간:** "
        f"{lower:,.0f}명 이상 ~ {upper:,.0f}명 미만 "
        f"(총 {most_common_count}편)"
    )

    st.write(
        f"🏆 **총 관객 수가 가장 많은 영화:** "
        f"{top_movie_name} "
        f"({top_movie_audience:,.0f}명)"
    )

else:
    st.info("총 관객 수 데이터가 없습니다.")


st.divider()


# 앞으로 그래프를 계속 추가할 구역
st.header("4. (# ── 그래프 4. 개봉일 스크린 수와 총 관객의 관계 ──
st.header("4. 개봉일 스크린 수와 총 관객의 관계 (산점도)")

scatter_df = df.dropna(
    subset=["first_scrn", "total_audi", "movieNm", "장르"]
).copy()

# 숫자로 변환
scatter_df["first_scrn"] = pd.to_numeric(
    scatter_df["first_scrn"], errors="coerce"
)
scatter_df["total_audi"] = pd.to_numeric(
    scatter_df["total_audi"], errors="coerce"
)

scatter_df = scatter_df.dropna(
    subset=["first_scrn", "total_audi"]
)

fig = px.scatter(
    scatter_df,
    x="first_scrn",
    y="total_audi",
    color="장르",
    hover_name="movieNm",
    labels={
        "first_scrn": "개봉일 스크린 수",
        "total_audi": "총 관객 수",
        "장르": "장르"
    },
)

fig.update_traces(
    hovertemplate="<b>%{hovertext}</b><br>"
                  "개봉일 스크린 수: %{x:,.0f}개<br>"
                  "총 관객 수: %{y:,.0f}명"
                  "<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)

st.text_input("이 그래프로 알 수 있는 것", key="note4")

st.divider()

# 앞으로 그래프를 계속 추가할 구역
st.header("5. (# ── 그래프 5. 장르별 총 관객 수 상자 그림 ──
st.header("5. 장르별 총 관객 수 (상자 그림)")

box_df = df.dropna(
    subset=["장르", "total_audi", "movieNm"]
).copy()

# 영화가 10편 이상인 장르만 선택
genre_counts = box_df["장르"].value_counts()
selected_genres = genre_counts[genre_counts >= 10].index

box_df = box_df[box_df["장르"].isin(selected_genres)]

fig = px.box(
    box_df,
    x="장르",
    y="total_audi",
    points="outliers",
    labels={
        "장르": "장르",
        "total_audi": "총 관객 수"
    },
)

# 이상치 점에 마우스를 올리면 영화명이 보이게 합니다
fig.update_traces(
    customdata=box_df[["movieNm"]].values,
    hovertemplate="<b>%{customdata[0]}</b><br>"
                  "총 관객 수: %{y:,.0f}명"
                  "<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)

st.text_input("이 그래프로 알 수 있는 것", key="note5")

st.divider()

# 앞으로 그래프를 계속 추가할 구역
st.header("6. (# ── 그래프 6. 개봉일 스크린 수와 총 관객의 관계 (버블 그래프) ──
st.header("6. 개봉일 스크린 수와 총 관객의 관계 (버블 그래프)")

bubble_df = df.dropna(
    subset=[
        "first_scrn",
        "total_audi",
        "first_week_audi",
        "movieNm",
        "장르"
    ]
).copy()

# 숫자로 변환
bubble_df["first_scrn"] = pd.to_numeric(
    bubble_df["first_scrn"], errors="coerce"
)
bubble_df["total_audi"] = pd.to_numeric(
    bubble_df["total_audi"], errors="coerce"
)
bubble_df["first_week_audi"] = pd.to_numeric(
    bubble_df["first_week_audi"], errors="coerce"
)

bubble_df = bubble_df.dropna(
    subset=["first_scrn", "total_audi", "first_week_audi"]
)

fig = px.scatter(
    bubble_df,
    x="first_scrn",
    y="total_audi",
    size="first_week_audi",
    color="장르",
    hover_name="movieNm",
    labels={
        "first_scrn": "개봉일 스크린 수",
        "total_audi": "총 관객 수",
        "first_week_audi": "첫 주 관객",
        "장르": "장르"
    },
    size_max=50
)

# 마우스를 올리면 영화명과 주요 수치가 보이게 합니다
fig.update_traces(
    hovertemplate="<b>%{hovertext}</b><br>"
                  "개봉일 스크린 수: %{x:,.0f}개<br>"
                  "총 관객 수: %{y:,.0f}명<br>"
                  "첫 주 관객: %{marker.size:,.0f}명"
                  "<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)

st.text_input("이 그래프로 알 수 있는 것", key="note6")

st.divider()

st.header("7. (# ── 그래프 7. 제작 국가 → 장르 선버스트 ──
st.header("7. 제작 국가와 장르별 영화 분포 (선버스트)")

sunburst_df = df.dropna(
    subset=["nation", "장르"]
).copy()

# 제작 국가와 장르별 영화 편수를 계산합니다
sunburst_count = (
    sunburst_df
    .groupby(["nation", "장르"])
    .size()
    .reset_index(name="편수")
)

fig = px.sunburst(
    sunburst_count,
    path=["nation", "장르"],
    values="편수",
)

fig.update_traces(
    hovertemplate="<b>%{label}</b><br>"
                  "영화 편수: %{value}편"
                  "<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)

st.text_input("이 그래프로 알 수 있는 것", key="note7")

st.divider()

st.header("8. (# ── 그래프 8. 10위권 체류 기간과 총 관객의 관계 ──
st.header("8. 10위권에 오래 머문 영화는 총 관객도 많은가")

scatter2_df = df.dropna(
    subset=["days_in_top10", "total_audi", "movieNm"]
).copy()

# 숫자로 변환
scatter2_df["days_in_top10"] = pd.to_numeric(
    scatter2_df["days_in_top10"], errors="coerce"
)
scatter2_df["total_audi"] = pd.to_numeric(
    scatter2_df["total_audi"], errors="coerce"
)

scatter2_df = scatter2_df.dropna(
    subset=["days_in_top10", "total_audi"]
)

fig = px.scatter(
    scatter2_df,
    x="days_in_top10",
    y="total_audi",
    hover_name="movieNm",
    labels={
        "days_in_top10": "10위권에 머문 날수",
        "total_audi": "총 관객 수",
    },
)

fig.update_traces(
    hovertemplate="<b>%{hovertext}</b><br>"
                  "10위권에 머문 날수: %{x:,.0f}일<br>"
                  "총 관객 수: %{y:,.0f}명"
                  "<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)

st.text_input("이 그래프로 알 수 있는 것", key="note8")

st.divider()

st.header("9. (다음 그래프를 여기에 추가)"))"))"))"))"))"))"))")
