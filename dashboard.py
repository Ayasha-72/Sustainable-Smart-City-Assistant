import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_dashboard():
    st.title("📊 Urban Data Analytics Dashboard")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel file",
        type=["csv", "xlsx"]
    )

    if uploaded_file is None:
        st.info("Please upload a dataset to view analysis.")
        return

    # Load data
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📋 Dataset Preview")
    st.dataframe(df)

    # Select numeric column
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    if not numeric_cols:
        st.warning("No numeric columns found for analysis.")
        return

    col = st.selectbox("Select a numeric column to analyze", numeric_cols)

    st.subheader("📈 Data Visualization")

    chart_type = st.radio(
        "Choose chart type",
        ["Bar Chart", "Line Chart", "Histogram"]
    )

    fig, ax = plt.subplots()

    if chart_type == "Bar Chart":
        ax.bar(df.index, df[col])
        ax.set_ylabel(col)

    elif chart_type == "Line Chart":
        ax.plot(df[col])
        ax.set_ylabel(col)

    elif chart_type == "Histogram":
        ax.hist(df[col], bins=10)
        ax.set_xlabel(col)

    st.pyplot(fig)

    # Basic stats
    st.subheader("📊 Statistical Summary")
    st.write(df[col].describe())


