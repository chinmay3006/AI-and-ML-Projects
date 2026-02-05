import streamlit as st
import pandas as pd
import os
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="YouTube Analytics Pro", layout="wide", page_icon="🎬")

# Modern Dark UI Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stMetricValue"] { color: #ff4b4b !important; font-size: 30px; }
    .stMetric { background-color: #161b22; padding: 20px; border-radius: 12px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# 2. Safety Loading Data
@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "USvideos.csv")
    try:
        # Loading 2000 rows for stability and variety
        df = pd.read_csv(file_path, nrows=2000)
        return df
    except Exception as e:
        return f"Error: {e}"

df = load_data()

# Error Check
if isinstance(df, str):
    st.error(f"🚨 Dataset Load Error: {df}")
    st.stop()

# 3. Dashboard UI starts here
st.title("🔥 YouTube Viral Content Intelligence")
st.markdown("### Deep-dive into trending patterns and channel dominance.")

# --- SIDEBAR FILTERS ---
st.sidebar.header("🎛️ Control Panel")
channels = sorted(df['channel_title'].unique())
selected_channel = st.sidebar.selectbox("Select a Channel", ["All Channels"] + channels)

# Filter Logic
if selected_channel == "All Channels":
    f_df = df
else:
    f_df = df[df['channel_title'] == selected_channel]

# --- TOP METRICS ROW ---
m1, m2, m3 = st.columns(3)
m1.metric("Total Views", f"{f_df['views'].sum():,}")
m2.metric("Total Likes", f"{f_df['likes'].sum():,}")
m3.metric("Video Count", len(f_df))

st.markdown("---")

# --- 🏆 KEY RECORDS SECTION (Update) ---
st.subheader("🏆 Key Records in this Selection")

if not f_df.empty:
    # Saare highest aur lowest points nikalne ke liye
    h_view_idx = f_df['views'].idxmax()
    l_view_idx = f_df['views'].idxmin()
    h_like_idx = f_df['likes'].idxmax()
    l_like_idx = f_df['likes'].idxmin()

    # Row 1: Views ke liye
    r1_col1, r1_col2 = st.columns(2)
    with r1_col1:
        st.success(f"🚀 **Highest Views:** {f_df.loc[h_view_idx, 'views']:,} \n\n Video: *{f_df.loc[h_view_idx, 'title']}*")
    with r1_col2:
        st.warning(f"📉 **Lowest Views:** {f_df.loc[l_view_idx, 'views']:,} \n\n Video: *{f_df.loc[l_view_idx, 'title']}*")

    # Row 2: Likes ke liye
    r2_col1, r2_col2 = st.columns(2)
    with r2_col1:
        st.info(f"❤️ **Highest Likes:** {f_df.loc[h_like_idx, 'likes']:,} \n\n Video: *{f_df.loc[h_like_idx, 'title']}*")
    with r2_col2:
        st.error(f"👎 **Lowest Likes:** {f_df.loc[l_like_idx, 'likes']:,} \n\n Video: *{f_df.loc[l_like_idx, 'title']}*")

st.markdown("---")

# --- VISUAL CHARTS ---
st.subheader("📊 Engagement Trends")
c1, c2 = st.columns(2)

with c1:
    top_10 = f_df.nlargest(10, 'views')
    fig_bar = px.bar(top_10, x='views', y='title', orientation='h', 
                     title="Top 10 Trending Videos", color='views', 
                     color_continuous_scale='Reds', template="plotly_dark")
    st.plotly_chart(fig_bar, use_container_width=True)

with c2:
    fig_scatter = px.scatter(f_df, x="views", y="likes", size="comment_count", 
                             hover_name="title", title="Views vs Likes Analysis",
                             color_discrete_sequence=['#ff4b4b'], template="plotly_dark")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Data Table
with st.expander("👀 View Raw Data Table"):
    st.write(f_df)