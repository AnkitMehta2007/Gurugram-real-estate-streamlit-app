import streamlit as st
import pandas as pd
import pickle
import plotly.express as px


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Property Insights",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Property Insights")
st.write("Understand how different property features affect prices.")


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    df = pd.read_csv("datasets/data_viz1.csv")

    return df


df = load_data()


# =========================================================
# BASIC CLEANING
# =========================================================

if "price" in df.columns:
    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

if "price_per_sqft" in df.columns:
    df["price_per_sqft"] = pd.to_numeric(
        df["price_per_sqft"],
        errors="coerce"
    )

if "built_up_area" in df.columns:
    df["built_up_area"] = pd.to_numeric(
        df["built_up_area"],
        errors="coerce"
    )

df = df.dropna(subset=["price"])


# =========================================================
# HELPER FUNCTION
# =========================================================

def percentage_change(old, new):

    if old == 0:
        return 0

    return ((new - old) / old) * 100


# =========================================================
# 1. BHK INSIGHT
# =========================================================

st.header("1️⃣ BHK Impact on Price")

if "bedRoom" in df.columns:

    bhk_df = (
        df.groupby("bedRoom")["price"]
        .mean()
        .reset_index()
    )

    bhk_df = bhk_df.sort_values("bedRoom")

    bhk_df["percentage_change"] = (
        bhk_df["price"].pct_change() * 100
    )

    # Display table

    st.dataframe(
        bhk_df,
        use_container_width=True,
        hide_index=True
    )

    # Generate insights

    st.subheader("💡 Insights")

    for i in range(1, len(bhk_df)):

        previous = bhk_df.iloc[i - 1]
        current = bhk_df.iloc[i]

        old_bhk = previous["bedRoom"]
        new_bhk = current["bedRoom"]

        old_price = previous["price"]
        new_price = current["price"]

        change = percentage_change(
            old_price,
            new_price
        )

        if change >= 0:

            st.success(
                f"Moving from {old_bhk:g} BHK to "
                f"{new_bhk:g} BHK increases the "
                f"average price by {change:.2f}%."
            )

        else:

            st.warning(
                f"Moving from {old_bhk:g} BHK to "
                f"{new_bhk:g} BHK decreases the "
                f"average price by {abs(change):.2f}%."
            )

    # Chart

    fig = px.bar(
        bhk_df,
        x="bedRoom",
        y="price",
        text="price",
        title="Average Property Price by BHK"
    )

    fig.update_traces(
        texttemplate="₹%{text:.2f} Cr",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.warning("bedRoom column not found.")


# =========================================================
# 2. BATHROOM INSIGHT
# =========================================================

st.header("2️⃣ Bathroom Impact on Price")

if "bathroom" in df.columns:

    bathroom_df = (
        df.groupby("bathroom")["price"]
        .mean()
        .reset_index()
        .sort_values("bathroom")
    )

    bathroom_df["percentage_change"] = (
        bathroom_df["price"].pct_change() * 100
    )

    st.dataframe(
        bathroom_df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("💡 Insights")

    for i in range(1, len(bathroom_df)):

        previous = bathroom_df.iloc[i - 1]
        current = bathroom_df.iloc[i]

        change = percentage_change(
            previous["price"],
            current["price"]
        )

        st.info(
            f"{int(previous['bathroom'])} bathrooms → "
            f"{int(current['bathroom'])} bathrooms: "
            f"{change:.2f}% change in average price."
        )

    fig = px.bar(
        bathroom_df,
        x="bathroom",
        y="price",
        text="price",
        title="Average Price by Number of Bathrooms"
    )

    fig.update_traces(
        texttemplate="₹%{text:.2f} Cr",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# 3. PROPERTY TYPE
# =========================================================

st.header("3️⃣ Flat vs House")

if "property_type" in df.columns:

    type_df = (
        df.groupby("property_type")["price"]
        .mean()
        .reset_index()
        .sort_values("price", ascending=False)
    )

    st.dataframe(
        type_df,
        use_container_width=True,
        hide_index=True
    )

    if len(type_df) >= 2:

        expensive = type_df.iloc[0]
        cheaper = type_df.iloc[-1]

        change = percentage_change(
            cheaper["price"],
            expensive["price"]
        )

        st.success(
            f"{expensive['property_type'].title()} properties "
            f"have {change:.2f}% higher average prices "
            f"than {cheaper['property_type'].title()} properties."
        )

    fig = px.bar(
        type_df,
        x="property_type",
        y="price",
        text="price",
        title="Average Price: Flat vs House"
    )

    fig.update_traces(
        texttemplate="₹%{text:.2f} Cr",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# 4. FURNISHING
# =========================================================

st.header("4️⃣ Furnishing Impact")

if "furnishing_type" in df.columns:

    furnishing_df = (
        df.groupby("furnishing_type")["price"]
        .mean()
        .reset_index()
        .sort_values("price", ascending=False)
    )

    st.dataframe(
        furnishing_df,
        use_container_width=True,
        hide_index=True
    )

    fig = px.bar(
        furnishing_df,
        x="furnishing_type",
        y="price",
        text="price",
        title="Average Price by Furnishing Type"
    )

    fig.update_traces(
        texttemplate="₹%{text:.2f} Cr",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# 5. LUXURY CATEGORY
# =========================================================

if "luxury_category" in df.columns:

    st.header("5️⃣ Luxury Category Impact")

    luxury_df = (
        df.groupby("luxury_category")["price"]
        .mean()
        .reset_index()
        .sort_values("price", ascending=False)
    )

    st.dataframe(
        luxury_df,
        use_container_width=True,
        hide_index=True
    )

    fig = px.bar(
        luxury_df,
        x="luxury_category",
        y="price",
        text="price",
        title="Average Price by Luxury Category"
    )

    fig.update_traces(
        texttemplate="₹%{text:.2f} Cr",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# 6. FLOOR CATEGORY
# =========================================================

if "floor_category" in df.columns:

    st.header("6️⃣ Floor Category Impact")

    floor_df = (
        df.groupby("floor_category")["price"]
        .mean()
        .reset_index()
        .sort_values("price", ascending=False)
    )

    st.dataframe(
        floor_df,
        use_container_width=True,
        hide_index=True
    )

    fig = px.bar(
        floor_df,
        x="floor_category",
        y="price",
        text="price",
        title="Average Price by Floor Category"
    )

    fig.update_traces(
        texttemplate="₹%{text:.2f} Cr",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# 7. BUILT-UP AREA
# =========================================================

st.header("7️⃣ Built-up Area vs Price")

if "built_up_area" in df.columns:

    area_df = df[
        ["built_up_area", "price"]
    ].dropna()

    fig = px.scatter(
        area_df,
        x="built_up_area",
        y="price",
        title="Built-up Area vs Property Price"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# 8. PRICE PER SQFT
# =========================================================

st.header("8️⃣ Price Per Sqft")

if "price_per_sqft" in df.columns:

    average_price_sqft = df[
        "price_per_sqft"
    ].mean()

    st.metric(
        "Average Price Per Sqft",
        f"₹{average_price_sqft:,.0f}"
    )

    fig = px.histogram(
        df,
        x="price_per_sqft",
        nbins=40,
        title="Price Per Sqft Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# 9. TOP SECTORS
# =========================================================

st.header("9️⃣ Most Expensive Sectors")

if "sector" in df.columns:

    sector_df = (
        df.groupby("sector")["price"]
        .mean()
        .reset_index()
        .sort_values("price", ascending=False)
        .head(10)
    )

    st.dataframe(
        sector_df,
        use_container_width=True,
        hide_index=True
    )

    fig = px.bar(
        sector_df.sort_values("price"),
        x="price",
        y="sector",
        orientation="h",
        text="price",
        title="Top 10 Most Expensive Sectors"
    )

    fig.update_traces(
        texttemplate="₹%{text:.2f} Cr",
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# 10. QUICK SUMMARY
# =========================================================

st.header("🔎 Quick Market Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Properties",
        len(df)
    )

with col2:

    st.metric(
        "Average Price",
        f"₹{df['price'].mean():.2f} Cr"
    )

with col3:

    if "built_up_area" in df.columns:

        st.metric(
            "Average Area",
            f"{df['built_up_area'].mean():,.0f} sqft"
        )

with col4:

    if "price_per_sqft" in df.columns:

        st.metric(
            "Avg Price / Sqft",
            f"₹{df['price_per_sqft'].mean():,.0f}"
        )


# =========================================================
# FINAL NOTE
# =========================================================

st.caption(
    "Insights are calculated from average prices in the available dataset. "
    "They show relationships in the data and do not imply causation."
)