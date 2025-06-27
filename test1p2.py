import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Applications, Admissions, and Enrollment KPIs", layout="wide")
st.title("Applications, Admissions, and Enrollment KPIs")

# -- Data --
data = {
    "Metric"      : ["Total Increase", "Average YoY", "Compound Annual Growth Rate"],
    "Applications": [40.0, 1.8, 3.8],
    "Admissions"  : [40.0, 1.8, 3.8],
    "Enrollments" : [33.3, 1.5, 3.2],
}

df_long = (
    pd.DataFrame(data)
      .melt(id_vars="Metric", var_name="Category", value_name="Percent")
)

# -- Sidebar --
st.sidebar.header("Options")
metric = st.sidebar.radio(
    "Choose statistic to view:",
    options=df_long["Metric"].unique()
)

# -- Filter for chosen metric --
sub = df_long[df_long["Metric"] == metric]

# -- Build Plotly figure --
palette = ["#1f77b4", "#2ca02c", "#d62728"]
fig = go.Figure()

fig.add_bar(
    x=sub[""],
    y=sub["%"],
    marker_color=palette[: len(sub)],
    text=[f"{v:.1f}%" for v in sub["Percent"]],
    textposition="outside",
    name=metric,
)

# adjust y-axis to have a bit of headroom
ymax = sub["Percent"].max() * 1.1
fig.update_layout(
    title=f"{metric}",
    xaxis_title="Category",
    yaxis_title="Percent",
    yaxis=dict(range=[0, ymax]),
    template="plotly_white",
    bargap=0.3,
    height=450,
)

# -- Render --
st.plotly_chart(fig, use_container_width=True)
