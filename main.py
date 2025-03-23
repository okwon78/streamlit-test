import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import folium
from streamlit_folium import folium_static


@st.cache_data
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data


def main():
    st.set_page_config(layout="wide")
    st.title("과천중앙고 권혁조")

    df = load_data("data/2024.csv")
    info_df = load_data("data/school.csv")

    # data_load_state.text("Done! (using st.cache_data)")
    st.subheader("2024년 경기도 고등학교 현황")
    st.dataframe(df)
    # hist_values = np.histogram(
    # data['1학년 학생수'].dt.hour, bins=24, range=(0,24))[0]

    # print(data['1학년 학생수'])
    # 총 학생 수 계산
    df["총 학생수"] = df["1학년 학생수"] + df["2학년 학생수"] + df["3학년 학생수"]
    df = df.sort_values(by="학교명", ascending=True)
    # st.bar_chart(df.set_index('학교명')['총 학생수'])
    # Plotly를 사용하여 바 차트 생성
    fig = px.bar(
        df,
        x="학교명",
        y="총 학생수",
        color="총 학생수",
        color_continuous_scale="Viridis",
        title="학교별 총 학생 수",
    )

    # 차트 표시
    st.plotly_chart(fig)

    info_df = (
        load_data("data/school.csv")
        .dropna(subset=["위도", "경도"])
        .rename(columns={"위도": "lat", "경도": "lon"})
    )

    lat = info_df["lat"].mean()
    lon = info_df["lon"].mean()

    map_center = [lat, lon]  # 서울 중심 좌표
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=9.5)

    for idx, row in info_df.iterrows():

        html = f"""
        <div style="width:200px;">
            <b>{row['학교명']}</b><br>
            설립유형: {row['설립유형']}<br>
            설립구분: {row['설립구분']}<br>
            학교특성: {row['학교특성']}<br>
            남녀공학: {row['남녀공학 구분']}<br>
            주소: {row['주소내역']}<br>
            전화번호: {row['전화번호']}<br>
            홈페이지: {row['홈페이지 주소']}
        </div>
        """
        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=folium.Popup(html, max_width=150),
            tooltip=row["학교명"],
        ).add_to(m)

    folium_static(m, width=2000, height=1300)
    # st.map(info_df, latitude="lat", longitude="lon", size=20, zoom=10)
    # latitude, longitude=


if __name__ == "__main__":
    main()
