import streamlit as st

st.set_page_config(
    page_title="CRUD App",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Theme trắng toàn bộ ứng dụng
st.markdown("""
    <style>
        /* Reset và thiết lập nền trắng cho toàn bộ ứng dụng */
        .stApp {
            background-color: white !important;
            color: black !important;
        }
        
        /* Main content area */
        .main .block-container {
            background-color: white !important;
            color: black !important;
        }
        
        /* Sidebar styling */
        .css-1d391kg, .css-1lcbmhc, .css-17eq0hr, section[data-testid="stSidebar"] {
            background-color: white !important;
            color: black !important;
        }
        
        /* Header và toolbar */
        header[data-testid="stHeader"], .css-18e3th9, .css-1dp5vir {
            background-color: white !important;
            color: black !important;
        }
        
        /* Tất cả các widget inputs */
        .stSelectbox > div > div, .stTextInput > div > div > input, 
        .stTextArea > div > div > textarea, .stNumberInput > div > div > input,
        .stDateInput > div > div > input, .stTimeInput > div > div > input {
            background-color: white !important;
            color: black !important;
            border: 1px solid #ddd !important;
        }
        
        /* Buttons */
        .stButton > button, button[kind="primary"], button[kind="secondary"] {
            background-color: white !important;
            color: black !important;
            border: 1px solid #ddd !important;
        }
        
        .stButton > button:hover {
            background-color: #f0f0f0 !important;
            color: black !important;
        }
        
        /* Dataframes và tables */
        .stDataFrame, .stTable, .dataframe {
            background-color: white !important;
            color: black !important;
        }
        
        /* Metrics và info boxes */
        .metric-container, .stMetric, .stInfo, .stSuccess, .stWarning, .stError {
            background-color: white !important;
            color: black !important;
        }
        
        /* Expander */
        .streamlit-expanderHeader, .streamlit-expanderContent {
            background-color: white !important;
            color: black !important;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"], .stTabs [data-baseweb="tab"] {
            background-color: white !important;
            color: black !important;
        }
        
        /* Columns và containers */
        .element-container, .stColumn, .stContainer {
            background-color: white !important;
            color: black !important;
        }
        
        /* Plotly charts background */
        .js-plotly-plot .plotly .modebar {
            background-color: white !important;
        }
        
        /* Aggrid tables */
        .ag-theme-streamlit, .ag-root-wrapper {
            background-color: white !important;
            color: black !important;
        }
        
        /* Footer */
        .css-1rs6os, .css-17ziqus {
            background-color: white !important;
            color: black !important;
        }
        
        /* Scrollbars */
        ::-webkit-scrollbar {
            background-color: white !important;
        }
        
        ::-webkit-scrollbar-thumb {
            background-color: #ddd !important;
        }
        
        /* Đảm bảo tất cả text đều màu đen */
        * {
            color: black !important;
        }
        
        /* Override dark mode nếu có */
        @media (prefers-color-scheme: dark) {
            .stApp {
                background-color: white !important;
                color: black !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.title("📋 CRUD App Demo")
st.write("Chào mừng bạn đến với ứng dụng CRUD!")
st.write("Sử dụng sidebar để điều hướng giữa các trang.")

st.info("💡 **Hướng dẫn sử dụng:**")
st.markdown("""
- Trang này là **Trang chủ** của ứng dụng CRUD
- Sử dụng **sidebar bên trái** để điều hướng đến các trang khác
- **🏥 Y tế**: Quản lý hồ sơ bệnh án, thuốc và lịch khám
- Các trang khác: Quản lý, Cá nhân, Đăng ký, Đăng nhập
""")
