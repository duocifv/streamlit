"""
📊 Products AI Analysis - Streamlit Page
========================================
Fetch products from DummyJSON API and analyze them using Groq AI

Features:
- Fetch product data from https://dummyjson.com/products
- AI analysis using Groq API for each product
- Interactive table with filters
- Category filtering
- Refresh AI Analysis functionality
- Streamlit best practices implementation

Requirements:
pip install streamlit requests pandas
"""

import streamlit as st
import requests
import pandas as pd
import json
import time
from typing import Dict, List, Optional

# Page configuration
st.set_page_config(
    page_title="📊 Products AI Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4ECDC4;
        margin: 0.5rem 0;
    }
    .ai-insight {
        background-color: #e3f2fd;
        padding: 0.8rem;
        border-radius: 6px;
        border-left: 3px solid #2196f3;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    .product-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
    .status-success {
        color: #28a745;
        font-weight: bold;
    }
    .status-error {
        color: #dc3545;
        font-weight: bold;
    }
    .status-processing {
        color: #ffc107;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Groq AI API configuration
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

# Initialize session state
if 'products_data' not in st.session_state:
    st.session_state.products_data = None
if 'ai_analysis_cache' not in st.session_state:
    st.session_state.ai_analysis_cache = {}
if 'analysis_status' not in st.session_state:
    st.session_state.analysis_status = {}

def fetch_products() -> Optional[Dict]:
    """
    Fetch products from DummyJSON API
    
    Returns:
        Dict containing products data or None if failed
    """
    try:
        with st.spinner("🔄 Fetching products from DummyJSON API..."):
            response = requests.get("https://dummyjson.com/products", timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if 'products' in data:
                st.success(f"✅ Successfully fetched {len(data['products'])} products!")
                return data
            else:
                st.error("❌ Invalid response format from API")
                return None
                
    except requests.exceptions.Timeout:
        st.error("⏰ Request timeout. Please try again.")
        return None
    except requests.exceptions.ConnectionError:
        st.error("🌐 Connection error. Check your internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching products: {str(e)}")
        return None
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")
        return None

def analyze_product_with_ai(title: str, description: str, product_id: int) -> str:
    """
    Analyze a product using Groq AI API
    
    Args:
        title: Product title
        description: Product description
        product_id: Product ID for caching
        
    Returns:
        AI analysis result or error message
    """
    # Check cache first
    cache_key = f"{product_id}_{hash(title + description)}"
    if cache_key in st.session_state.ai_analysis_cache:
        return st.session_state.ai_analysis_cache[cache_key]
    
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}"
        }
        
        payload = {
            "model": GROQ_MODEL,
            "messages": [{
                "role": "user",
                "content": f"Analyze this product briefly (2-3 sentences): {title} - {description}"
            }],
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                analysis = result['choices'][0]['message']['content'].strip()
                # Cache the result
                st.session_state.ai_analysis_cache[cache_key] = analysis
                return analysis
            else:
                return "❌ Invalid AI response format"
        else:
            return f"❌ AI API Error: {response.status_code}"
            
    except requests.exceptions.Timeout:
        return "⏰ AI analysis timeout"
    except requests.exceptions.RequestException as e:
        return f"❌ AI API Error: {str(e)}"
    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"

def process_products_with_ai(products: List[Dict], progress_bar, status_text) -> pd.DataFrame:
    """
    Process all products with AI analysis
    
    Args:
        products: List of product dictionaries
        progress_bar: Streamlit progress bar
        status_text: Streamlit status text element
        
    Returns:
        DataFrame with products and AI analysis
    """
    processed_products = []
    total_products = len(products)
    
    for i, product in enumerate(products):
        # Update progress
        progress = (i + 1) / total_products
        progress_bar.progress(progress)
        status_text.text(f"🤖 Analyzing product {i + 1}/{total_products}: {product.get('title', 'Unknown')[:30]}...")
        
        # Get AI analysis
        ai_insight = analyze_product_with_ai(
            product.get('title', ''),
            product.get('description', ''),
            product.get('id', 0)
        )
        
        # Prepare product data
        processed_product = {
            'ID': product.get('id', 0),
            'Title': product.get('title', 'N/A'),
            'Price': f"${product.get('price', 0):.2f}",
            'Category': product.get('category', 'N/A').title(),
            'Rating': f"{product.get('rating', 0):.1f}⭐",
            'Brand': product.get('brand', 'N/A'),
            'Stock': product.get('stock', 0),
            'Discount': f"{product.get('discountPercentage', 0):.1f}%",
            'AI Insight': ai_insight,
            'Description': product.get('description', 'N/A')[:100] + "..." if len(product.get('description', '')) > 100 else product.get('description', 'N/A')
        }
        
        processed_products.append(processed_product)
        
        # Small delay to avoid rate limiting
        time.sleep(0.1)
    
    return pd.DataFrame(processed_products)

def display_product_metrics(df: pd.DataFrame):
    """Display key metrics about the products"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>📦 Total Products</h4>
            <h2>{}</h2>
        </div>
        """.format(len(df)), unsafe_allow_html=True)
    
    with col2:
        avg_price = df['Price'].str.replace('$', '').astype(float).mean()
        st.markdown("""
        <div class="metric-card">
            <h4>💰 Avg Price</h4>
            <h2>${:.2f}</h2>
        </div>
        """.format(avg_price), unsafe_allow_html=True)
    
    with col3:
        categories = df['Category'].nunique()
        st.markdown("""
        <div class="metric-card">
            <h4>🏷️ Categories</h4>
            <h2>{}</h2>
        </div>
        """.format(categories), unsafe_allow_html=True)
    
    with col4:
        avg_rating = df['Rating'].str.replace('⭐', '').astype(float).mean()
        st.markdown("""
        <div class="metric-card">
            <h4>⭐ Avg Rating</h4>
            <h2>{:.1f}</h2>
        </div>
        """.format(avg_rating), unsafe_allow_html=True)

def main():
    """Main application function"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>📊 Products AI Analysis</h1>
        <p>Intelligent product analysis powered by Groq AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar controls
    with st.sidebar:
        st.header("🎛️ Controls")
        
        # Fetch products button
        if st.button("🔄 Fetch Products", type="primary"):
            st.session_state.products_data = fetch_products()
            if st.session_state.products_data:
                st.session_state.ai_analysis_cache = {}  # Clear cache when fetching new data
        
        st.markdown("---")
        
        # AI Analysis controls
        st.header("🤖 AI Analysis")
        
        if st.session_state.products_data:
            if st.button("🚀 Refresh AI Analysis", type="secondary"):
                st.session_state.ai_analysis_cache = {}  # Clear cache to force refresh
                st.rerun()
        
        st.markdown("---")
        
        # Info section
        st.header("ℹ️ Information")
        st.info("""
        **Data Source:** DummyJSON API
        **AI Model:** Llama-4 Scout 17B
        **Features:**
        - Real-time product fetching
        - AI-powered insights
        - Interactive filtering
        - Caching for performance
        """)
        
        # API Status
        st.header("🔌 API Status")
        if st.button("🔍 Check APIs"):
            with st.spinner("Checking..."):
                # Check DummyJSON API
                try:
                    response = requests.get("https://dummyjson.com/products?limit=1", timeout=5)
                    if response.status_code == 200:
                        st.success("✅ DummyJSON API: Online")
                    else:
                        st.error("❌ DummyJSON API: Issues")
                except:
                    st.error("❌ DummyJSON API: Offline")
                
                # Check Groq API
                try:
                    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
                    response = requests.get("https://api.groq.com/openai/v1/models", headers=headers, timeout=5)
                    if response.status_code == 200:
                        st.success("✅ Groq AI API: Online")
                    else:
                        st.error("❌ Groq AI API: Issues")
                except:
                    st.error("❌ Groq AI API: Offline")
    
    # Main content area
    if not st.session_state.products_data:
        # Welcome screen
        st.markdown("""
        ### 👋 Welcome to Products AI Analysis!
        
        **Get started by clicking "🔄 Fetch Products" in the sidebar.**
        
        This application will:
        1. 📥 Fetch product data from DummyJSON API
        2. 🤖 Analyze each product using Groq AI
        3. 📊 Display results in an interactive table
        4. 🔍 Allow filtering by category
        5. ⚡ Cache results for better performance
        """)
        
        # Show sample of what to expect
        st.markdown("### 🎯 What you'll see:")
        sample_data = {
            'ID': [1, 2, 3],
            'Title': ['iPhone 9', 'iPhone X', 'Samsung Universe 9'],
            'Price': ['$549.00', '$899.00', '$1249.00'],
            'Category': ['Smartphones', 'Smartphones', 'Smartphones'],
            'Rating': ['4.7⭐', '4.4⭐', '4.3⭐'],
            'AI Insight': [
                'Premium smartphone with excellent camera...',
                'High-end device with advanced features...',
                'Latest technology with superior performance...'
            ]
        }
        st.dataframe(pd.DataFrame(sample_data), use_container_width=True)
        
    else:
        # Process products with AI analysis
        products = st.session_state.products_data.get('products', [])
        
        if not products:
            st.error("❌ No products found in the data")
            return
        
        # Check if we need to run AI analysis
        needs_analysis = len(st.session_state.ai_analysis_cache) == 0
        
        if needs_analysis:
            st.info("🤖 Running AI analysis on products. This may take a few minutes...")
            
            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Process products
            df = process_products_with_ai(products, progress_bar, status_text)
            
            # Clean up progress indicators
            progress_bar.empty()
            status_text.empty()
            
        else:
            # Use cached data
            st.success("⚡ Using cached AI analysis results")
            df = process_products_with_ai(products, st.empty(), st.empty())
        
        # Display metrics
        display_product_metrics(df)
        
        st.markdown("---")
        
        # Filters
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            # Category filter
            categories = ['All'] + sorted(df['Category'].unique().tolist())
            selected_category = st.selectbox("🏷️ Filter by Category", categories)
        
        with col2:
            # Price range filter
            min_price = float(df['Price'].str.replace('$', '').min())
            max_price = float(df['Price'].str.replace('$', '').max())
            price_range = st.slider(
                "💰 Price Range", 
                min_value=min_price, 
                max_value=max_price, 
                value=(min_price, max_price),
                format="$%.2f"
            )
        
        with col3:
            # Display options
            show_description = st.checkbox("📝 Show Description", value=False)
        
        # Apply filters
        filtered_df = df.copy()
        
        if selected_category != 'All':
            filtered_df = filtered_df[filtered_df['Category'] == selected_category]
        
        # Apply price filter
        prices = filtered_df['Price'].str.replace('$', '').astype(float)
        filtered_df = filtered_df[(prices >= price_range[0]) & (prices <= price_range[1])]
        
        # Select columns to display
        display_columns = ['ID', 'Title', 'Price', 'Category', 'Rating', 'Brand', 'Stock', 'Discount', 'AI Insight']
        if show_description:
            display_columns.append('Description')
        
        # Display results
        st.markdown(f"### 📊 Products Analysis Results ({len(filtered_df)} products)")
        
        if len(filtered_df) > 0:
            # Configure column widths for better display
            column_config = {
                'AI Insight': st.column_config.TextColumn(
                    'AI Insight',
                    width='large',
                    help='AI-generated product analysis'
                ),
                'Title': st.column_config.TextColumn(
                    'Title',
                    width='medium'
                ),
                'Price': st.column_config.TextColumn(
                    'Price',
                    width='small'
                ),
                'Rating': st.column_config.TextColumn(
                    'Rating',
                    width='small'
                )
            }
            
            # Display the dataframe with custom styling
            st.dataframe(
                filtered_df[display_columns],
                use_container_width=True,
                column_config=column_config,
                hide_index=True
            )
            
            # Export options
            st.markdown("### 📥 Export Options")
            col1, col2 = st.columns(2)
            
            with col1:
                csv = filtered_df.to_csv(index=False)
                st.download_button(
                    label="📄 Download as CSV",
                    data=csv,
                    file_name=f"products_ai_analysis_{time.strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
            
            with col2:
                json_data = filtered_df.to_json(orient='records', indent=2)
                st.download_button(
                    label="📋 Download as JSON",
                    data=json_data,
                    file_name=f"products_ai_analysis_{time.strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
        
        else:
            st.warning("⚠️ No products match the current filters")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em;">
        📊 Products AI Analysis | Powered by DummyJSON API & Groq AI | 
        Built with ❤️ using Streamlit
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
