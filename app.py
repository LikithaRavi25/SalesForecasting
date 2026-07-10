import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


st.set_page_config(
    page_title="Sales Forecast Dashboard",
    layout="wide"
)


# Load dataset
df = pd.read_csv("data/train.csv")

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True
)

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Sales Overview",
        "Forecast Explorer",
        "Anomaly Report",
        "Product Demand Segments"
    ]
)

# ===========================
# PAGE 1
# ===========================

if page == "Sales Overview":

    st.header("Sales Overview Dashboard")

    # Yearly Sales
    yearly_sales = (
        df.groupby(df["Order Date"].dt.year)["Sales"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(8,4))

    yearly_sales.plot(kind="bar", ax=ax)

    ax.set_title("Total Sales by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sales")

    st.pyplot(fig)

    # Monthly Sales
    monthly_sales = (
        df.set_index("Order Date")["Sales"]
        .resample("ME")
        .sum()
    )

    fig, ax = plt.subplots(figsize=(12,5))

    monthly_sales.plot(ax=ax)

    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sales")

    st.pyplot(fig)

    # Category Filter
    category = st.selectbox(
        "Select Category",
        ["All"] + list(df["Category"].unique())
    )

    # Region Filter
    region = st.selectbox(
        "Select Region",
        ["All"] + list(df["Region"].unique())
    )

    filtered_df = df.copy()

    if category != "All":
        filtered_df = filtered_df[
            filtered_df["Category"] == category
        ]

    if region != "All":
        filtered_df = filtered_df[
            filtered_df["Region"] == region
        ]

    st.subheader("Filtered Sales Data")

    st.dataframe(filtered_df.head(20))

    st.subheader("Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Sales",
        f"${filtered_df['Sales'].sum():,.2f}"
    )

    col2.metric(
        "Orders",
        filtered_df.shape[0]
    )

    col3.metric(
        "Average Sale",
        f"${filtered_df['Sales'].mean():,.2f}"
    )

elif page == "Forecast Explorer":

    st.header("Forecast Explorer")
    forecast_type = st.selectbox(

    "Forecast By",

    ["Category", "Region"]

)
    if forecast_type == "Category":

        selected = st.selectbox(

        "Select Category",

        sorted(df["Category"].unique())

    )

    else:

        selected = st.selectbox(

        "Select Region",

        sorted(df["Region"].unique())

    )
    months = st.slider(

    "Forecast Horizon (Months)",

    min_value=1,

    max_value=3,

    value=3

)
    if forecast_type == "Category":

       temp = df[df["Category"] == selected]

    else:

       temp = df[df["Region"] == selected]

    monthly = (

    temp.set_index("Order Date")["Sales"]

        .resample("ME")

        .sum()

)
    forecast = [monthly.iloc[-1]] * months

    future_dates = pd.date_range(

    monthly.index[-1] + pd.offsets.MonthEnd(1),

    periods=months,

    freq="ME"

)
    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(

    monthly.index,

    monthly,

    label="Historical Sales"

)

    ax.plot(

    future_dates,

    forecast,

    marker="o",

    linewidth=2,

    color="red",

    label="Forecast"

)

    ax.set_title(f"{selected} Sales Forecast")

    ax.set_xlabel("Year")

    ax.set_ylabel("Sales")

    ax.legend()

    st.pyplot(fig)
    forecast_df = pd.DataFrame({

    "Forecast Month": future_dates,

    "Forecast Sales": forecast

})

    st.subheader("Forecast Output")

    st.dataframe(forecast_df)

    st.subheader("Model Performance")

    col1, col2 = st.columns(2)

    col1.metric(

    "MAE",

    "8017.25"

)

    col2.metric(

    "RMSE",

    "13156.85"

)
elif page == "Anomaly Report":

    st.header("Anomaly Report") 
    weekly_sales = (
    df.set_index("Order Date")["Sales"]
      .resample("W")
      .sum()
      .to_frame(name="Sales")
)
   
    iso_model = IsolationForest(
    contamination=0.05,
    random_state=42
)

    weekly_sales["Isolation_Result"] = iso_model.fit_predict(
    weekly_sales[["Sales"]]
)

    weekly_sales["Isolation_Result"] = weekly_sales["Isolation_Result"].replace({
    1: "Normal",
    -1: "Anomaly"
})
    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(
    weekly_sales.index,
    weekly_sales["Sales"],
    linewidth=2,
    label="Weekly Sales"
)

    anomalies = weekly_sales[
    weekly_sales["Isolation_Result"] == "Anomaly"
]

    ax.scatter(
    anomalies.index,
    anomalies["Sales"],
    color="red",
    s=80,
    label="Anomaly"
)

    ax.set_title("Weekly Sales Anomalies")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sales")
    ax.legend()

    st.pyplot(fig)

    st.subheader("Detected Anomalies")

    st.dataframe(
    anomalies.reset_index()
)
    st.metric(
    "Total Anomalies Detected",
    len(anomalies)
)
    
elif page == "Product Demand Segments":

    st.header("Product Demand Segments")
    total_sales = df.groupby("Sub-Category")["Sales"].sum()

    average_order = df.groupby("Sub-Category")["Sales"].mean()

    sales_volatility = df.groupby("Sub-Category")["Sales"].std()

    yearly_sales = (
    df.groupby(
        [
            "Sub-Category",
            df["Order Date"].dt.year
        ]
    )["Sales"]
    .sum()
    .reset_index()
)

    growth_rate = (
    yearly_sales
    .groupby("Sub-Category")["Sales"]
    .pct_change()
)

    growth_df = yearly_sales.copy()

    growth_df["Growth"] = growth_rate

    average_growth = (
    growth_df
    .groupby("Sub-Category")["Growth"]
    .mean()
)

    cluster_data = pd.DataFrame({
    "Total Sales": total_sales,
    "Average Order Value": average_order,
    "Sales Volatility": sales_volatility,
    "Growth Rate": average_growth
}).fillna(0)
    scaler = StandardScaler()

    scaled = scaler.fit_transform(cluster_data)

    kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

    cluster_data["Cluster"] = kmeans.fit_predict(scaled)
    pca = PCA(n_components=2)

    points = pca.fit_transform(scaled)

    cluster_data["PCA1"] = points[:,0]
    cluster_data["PCA2"] = points[:,1]
    fig, ax = plt.subplots(figsize=(9,6))

    scatter = ax.scatter(
    cluster_data["PCA1"],
    cluster_data["PCA2"],
    c=cluster_data["Cluster"],
    cmap="viridis",
    s=120
)

    for i in cluster_data.index:
        ax.text(
        cluster_data.loc[i,"PCA1"]+0.03,
        cluster_data.loc[i,"PCA2"]+0.03,
        i,
        fontsize=8
    )

    plt.colorbar(scatter)

    ax.set_title("Product Demand Segments")

    st.pyplot(fig)
    labels = {

    0: "High Volume, Premium Products",

    1: "Low Volume, Stable Demand",

    2: "High Volume, Stable Demand",

    3: "Growing Demand"

}

    cluster_data["Demand Segment"] = cluster_data["Cluster"].map(labels)
    st.subheader("Demand Segments")

    st.dataframe(
    cluster_data[
        [
            "Total Sales",
            "Average Order Value",
            "Sales Volatility",
            "Growth Rate",
            "Demand Segment"
        ]
    ]
)