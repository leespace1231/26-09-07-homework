import streamlit as st

st.title("🚀 GitHub Actions + Hugging Face Spaces CI/CD")
st.write("GitHub에 코드를 푸시하면 Hugging Face Space에 자동 배포됩니다.")

name = st.text_input("이름을 입력하세요:", "방문자")
if st.button("인사하기"):
    st.success(f"안녕하세요, {name}님! CI/CD 파이프라인 구축에 성공하셨습니다.")