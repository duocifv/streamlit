import streamlit as st
from services.auth_service import register_user
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.theme import apply_white_theme

# Áp dụng theme trắng
apply_white_theme()

st.title("📝 Đăng ký tài khoản")

username = st.text_input("Tên đăng ký")
password = st.text_input("Mật khẩu", type="password")

if st.button("Đăng ký"):
    success, message = register_user(username, password)
    if success:
        st.success(message)
    else:
        st.error(message)
