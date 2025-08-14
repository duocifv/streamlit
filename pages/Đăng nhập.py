import streamlit as st
from services.auth_service import login_user
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.theme import apply_white_theme

# Áp dụng theme trắng
apply_white_theme()

st.title("🔐 Đăng nhập")

username = st.text_input("Tên đăng nhập")
password = st.text_input("Mật khẩu", type="password")

if st.button("Đăng nhập"):
    if login_user(username, password):
        st.session_state.user = username
        # <-- Dùng API chính thức
        st.switch_page("pages/Cá nhân.py")
    else:
        st.error("Sai tên đăng nhập hoặc mật khẩu")
