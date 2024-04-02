import streamlit as st


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://repository-images.githubusercontent.com/275336521/20d38e00-6634-11eb-9d1f-6a5232d0f84f");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
st.write("hello")
add_bg_from_url()