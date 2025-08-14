import streamlit as st

def apply_white_theme():
    """Áp dụng theme trắng toàn bộ cho ứng dụng Streamlit với độ ưu tiên cao nhất"""
    st.markdown("""
        <style>
            /* FORCE WHITE THEME - Độ ưu tiên cao nhất */
            html, body, #root, .stApp, [data-testid="stAppViewContainer"] {
                background-color: white !important;
                color: black !important;
                background: white !important;
            }
            
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
            
            /* Đảm bảo tất cả text đều màu đen - FORCE OVERRIDE */
            *, *::before, *::after, div, span, p, h1, h2, h3, h4, h5, h6, 
            .stMarkdown, .stText, .element-container * {
                color: black !important;
                background-color: inherit !important;
            }
            
            /* FORCE OVERRIDE cho tất cả containers */
            [data-testid="stAppViewContainer"], 
            [data-testid="stHeader"], 
            [data-testid="stToolbar"],
            [data-testid="stDecoration"],
            [data-testid="stSidebar"],
            .main, .block-container {
                background-color: white !important;
                background: white !important;
                color: black !important;
            }
            
            /* Override dark mode nếu có - FORCE */
            @media (prefers-color-scheme: dark) {
                html, body, .stApp, * {
                    background-color: white !important;
                    color: black !important;
                    background: white !important;
                }
            }
            
            /* CSS Variables Override */
            :root {
                --background-color: white !important;
                --text-color: black !important;
                --primary-color: black !important;
                --secondary-background-color: white !important;
            }
            
            /* Specific styling cho các trang Y tế */
            .medical-card, .patient-info, .medicine-info {
                background-color: white !important;
                color: black !important;
                border: 1px solid #ddd !important;
                border-radius: 5px !important;
                padding: 10px !important;
                margin: 5px 0 !important;
            }
            
            /* Form styling */
            .stForm {
                background-color: white !important;
                border: 1px solid #ddd !important;
                border-radius: 5px !important;
                padding: 20px !important;
            }
            
            /* Radio buttons và checkboxes */
            .stRadio > div, .stCheckbox > div {
                background-color: white !important;
                color: black !important;
            }
            
            /* File uploader */
            .stFileUploader > div {
                background-color: white !important;
                color: black !important;
                border: 1px solid #ddd !important;
            }
            
            /* Progress bars */
            .stProgress > div > div {
                background-color: #f0f0f0 !important;
            }
            
            /* Alerts và notifications */
            .stAlert {
                background-color: white !important;
                color: black !important;
                border: 1px solid #ddd !important;
            }
        </style>
    """, unsafe_allow_html=True)
