# import packages
from tokenize import group
import streamlit as st
import pandas as pd
import string
import re
import os
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

def clean_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

# Helper function to get dataset path
def get_dataset_path():
    # Get the current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the CSV file
    csv_path = os.path.join(current_dir, "..", "..", "data", "customer_reviews.csv")
    return csv_path


# Set page config with OG image
st.set_page_config(
    page_title="GenAI Data Processing App",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.streamlit.io',
        'Report a bug': None,
        'About': "# GenAI-powered data processing app"
    }
)

# Add meta tags for Open Graph
st.markdown("""
    <meta property="og:title" content="GenAI Data Processing App" />
    <meta property="og:description" content="AI-powered customer reviews sentiment analysis" />
    <meta property="og:image" content="https://raw.githubusercontent.com/souljazzfunk/fast-prototyping-of-genai-apps-with-streamlit/refs/heads/main/chart-viz-og.png" />
    <meta property="og:type" content="website" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:image" content="https://raw.githubusercontent.com/souljazzfunk/fast-prototyping-of-genai-apps-with-streamlit/refs/heads/main/chart-viz-og.png" />
""", unsafe_allow_html=True)

st.title("Hello, GenAI!")
st.write("This is your GenAI-powered data processing app.")

col1, col2 = st.columns(2)

with col1:
        if st.button("ingest dataset"):
            try:
                csv_path = get_dataset_path()
                st.session_state["df"] = pd.read_csv(csv_path)
                st.success("Dataset loaded successfully!")
            except FileNotFoundError:
                st.error("Dataset not found. Please check the file path.")

with col2:
        if st.button("parse reviews"):
            if "df" in st.session_state:
                st.session_state["df"]["CLEANED_SUMMARY"] = st.session_state["df"]["SUMMARY"].apply(clean_text)
                st.success("Reviews parsed and cleaned!")
            else:
                st.warning("Please ingest the dataset first.")

if "df" in st.session_state:
    st.subheader("Filter by Product")

    # Get all unique products
    all_products = list(st.session_state["df"]["PRODUCT"].unique())

    # Create checkboxes for each product
    st.write("Select products to display:")

    # "Select All" checkbox
    select_all = st.checkbox("Select All Products", value=True)

    # Individual product checkboxes
    selected_products = []
    if select_all:
        selected_products = all_products
    else:
        cols = st.columns(3)  # Create 3 columns for better layout
        for idx, product in enumerate(all_products):
            with cols[idx % 3]:
                if st.checkbox(product, value=False, key=f"product_{product}"):
                    selected_products.append(product)

    # Filter dataframe based on selected products
    if selected_products:
        filtered_df = st.session_state["df"][st.session_state["df"]["PRODUCT"].isin(selected_products)]
        st.subheader(f"Reviews for {len(selected_products)} product(s)")
    else:
        filtered_df = pd.DataFrame()  # Empty dataframe if nothing selected
        st.warning("Please select at least one product to display data.")

    if not filtered_df.empty:
        st.dataframe(filtered_df)

    # Only show charts if there's data
    if not filtered_df.empty:
        # streamlit chart - use filtered_df for all charts
        st.subheader("Sentiment Score by Product (Altair)")
        grouped = filtered_df.groupby(["PRODUCT"])["SENTIMENT_SCORE"].mean().sort_values(ascending=False)
        grouped_df = pd.DataFrame({"Product": grouped.index, "Score": grouped.values})

        # Vertical bar chart with Altair
        chart = alt.Chart(grouped_df).mark_bar().encode(
            x=alt.X("Product:N", sort=None, axis=alt.Axis(labelAngle=-45, labelLimit=200, labelOverlap=False)),
            y=alt.Y("Score:Q", title="Average Sentiment Score")
        ).properties(height=400)
        st.altair_chart(chart, use_container_width=True)

        # Horizontal bar chart with Altair
        chart_h = alt.Chart(grouped_df).mark_bar().encode(
            x=alt.X("Score:Q", title="Average Sentiment Score"),
            y=alt.Y("Product:N", sort=None, axis=alt.Axis(labelLimit=200))
        ).properties(height=400)
        st.altair_chart(chart_h, use_container_width=True)

        # matplotlib bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(grouped.index, grouped.values, edgecolor='black', alpha=0.7)
        ax.set_xlabel('Product')
        ax.set_ylabel('Average Sentiment Score')
        ax.set_title('Sentiment Score by Product (Matplotlib)')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

        # plotly bar chart
        fig = px.bar(
            x=grouped.index,
            y=grouped.values,
            title="Sentiment Score by Product (Plotly)",
            labels={"x": "Product", "y": "Average Sentiment Score"}
        )
        st.plotly_chart(fig, use_container_width=True)

        # plotly horizontal bar chart
        fig = px.bar(
            x=grouped.values[::-1],
            y=grouped.index[::-1],
            title="Sentiment Score by Product (Plotly - Horizontal)",
            labels={"x": "Average Sentiment Score", "y": "Product"},
            orientation='h'
        )
        st.plotly_chart(fig, use_container_width=True)

        # matplotlib histogram
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(filtered_df["SENTIMENT_SCORE"], bins=10, edgecolor='black', alpha=0.7)
        ax.set_xlabel('Sentiment Score')
        ax.set_ylabel('Frequency')
        ax.set_title('Distribution of Sentiment Scores (Matplotlib)')
        st.pyplot(fig)

        # plotly histogram
        fig = px.histogram(
            filtered_df,
            x="SENTIMENT_SCORE",
            nbins=10,
            title="Distribution of Sentiment Scores (Plotly)",
            labels={"SENTIMENT_SCORE": "Sentiment Score", "count": "Frequency"}
        )
        fig.update_layout()
        st.plotly_chart(fig, use_container_width=True)