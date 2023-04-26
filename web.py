import streamlit as st

st.title("Movie Recommendation")
st.write("This is demo of Movie Recommendation, Made by mr.kumbhaniii")
st.subheader("Avatar: The Way of Water (2022)")
st.image("https://lumiere-a.akamaihd.net/v1/images/p_20cs_avatarwayofwater_1710_4025feea.jpeg", width=200)
col1, col2, col3 = st.columns([1, 1, 5])
with col1:
    st.button("Dislike")
with col2:
    st.button("Not sure")
with col3:
    st.button("Like")
