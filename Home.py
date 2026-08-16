import streamlit as st

st.set_page_config(
    page_title="Real Estate AI",
    page_icon="🏠",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================

st.html("""
<style>

body {
    background-color: #0e1117;
}

.hero {
    background: linear-gradient(135deg, #191e2a, #11151f);
    border: 1px solid #303746;
    border-radius: 24px;
    padding: 45px;
    margin-bottom: 35px;
}

.hero h1 {
    color: white;
    font-size: 48px;
    margin: 0 0 15px 0;
    font-weight: 800;
}

.hero h1 span {
    color: #ff4b4b;
}

.hero p {
    color: #aab2c0;
    font-size: 18px;
    line-height: 1.7;
    max-width: 800px;
}

.section-title {
    color: white;
    font-size: 30px;
    font-weight: 700;
    margin: 35px 0 20px 0;
}

.card {
    background: #171b24;
    border: 1px solid #303746;
    border-radius: 18px;
    padding: 28px;
    min-height: 180px;
    box-sizing: border-box;
}

.card:hover {
    border-color: #ff4b4b;
}

.icon {
    font-size: 36px;
    margin-bottom: 15px;
}

.card h3 {
    color: white;
    font-size: 21px;
    margin: 0 0 10px 0;
}

.card p {
    color: #9da6b5;
    font-size: 15px;
    line-height: 1.6;
    margin: 0;
}

.stat {
    background: #171b24;
    border: 1px solid #303746;
    border-radius: 16px;
    padding: 22px;
    text-align: center;
}

.stat-number {
    color: #ff4b4b;
    font-size: 28px;
    font-weight: 800;
}

.stat-label {
    color: #9da6b5;
    font-size: 14px;
    margin-top: 6px;
}

.cta {
    background: linear-gradient(135deg, #21171b, #171a22);
    border: 1px solid #39252b;
    border-radius: 20px;
    padding: 35px;
    text-align: center;
    margin-top: 35px;
}

.cta h2 {
    color: white;
    font-size: 27px;
    margin: 0 0 10px 0;
}

.cta p {
    color: #aab2c0;
    margin: 0;
}

</style>
""")


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("## 🏠 Real Estate AI")

st.sidebar.caption(
    "Property Intelligence Platform"
)

st.sidebar.divider()

st.sidebar.info(
    "Use the menu to explore property prices, "
    "market analysis, recommendations and insights."
)


# =========================================================
# HERO
# =========================================================

st.html("""
<div class="hero">

    <h1>
        Real Estate <span>Intelligence</span> 🏠
    </h1>

    <p>
        An interactive machine learning platform for exploring
        property prices, analysing real estate trends and finding
        suitable apartments based on your requirements.
    </p>

</div>
""")


# =========================================================
# WHAT YOU CAN DO
# =========================================================

st.html("""
<div class="section-title">
    What You Can Do
</div>
""")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.html("""
    <div class="stat">
        <div class="stat-number">🤖 ML</div>
        <div class="stat-label">Price Prediction</div>
    </div>
    """)

with c2:
    st.html("""
    <div class="stat">
        <div class="stat-number">📊</div>
        <div class="stat-label">Market Analysis</div>
    </div>
    """)

with c3:
    st.html("""
    <div class="stat">
        <div class="stat-number">🏘️</div>
        <div class="stat-label">Property Recommendations</div>
    </div>
    """)

with c4:
    st.html("""
    <div class="stat">
        <div class="stat-number">💡</div>
        <div class="stat-label">Market Insights</div>
    </div>
    """)


# =========================================================
# EXPLORE PLATFORM
# =========================================================

st.html("""
<div class="section-title">
    Explore the Platform
</div>
""")


# Row 1

c1, c2 = st.columns(2)

with c1:
    st.html("""
    <div class="card">

        <div class="icon">💰</div>

        <h3>Price Predictor</h3>

        <p>
            Estimate the expected price of a property using
            machine learning based on location, area,
            bedrooms and other property features.
        </p>

    </div>
    """)

with c2:
    st.html("""
    <div class="card">

        <div class="icon">📊</div>

        <h3>Market Analysis</h3>

        <p>
            Explore property prices, price per square foot,
            popular locations and other patterns in the
            real estate dataset.
        </p>

    </div>
    """)


st.write("")


# Row 2

c1, c2 = st.columns(2)

with c1:
    st.html("""
    <div class="card">

        <div class="icon">🏠</div>

        <h3>Recommend Apartments</h3>

        <p>
            Find apartments that match your preferred
            location, budget and property requirements.
        </p>

    </div>
    """)

with c2:
    st.html("""
    <div class="card">

        <div class="icon">💡</div>

        <h3>Real Estate Insights</h3>

        <p>
            Get useful insights from the dataset through
            visualisations, trends and statistical analysis.
        </p>

    </div>
    """)


# =========================================================
# HOW IT WORKS
# =========================================================

st.html("""
<div class="section-title">
    How It Works
</div>
""")

c1, c2, c3 = st.columns(3)

with c1:
    st.html("""
    <div class="card">

        <div class="icon">1️⃣</div>

        <h3>Enter Property Details</h3>

        <p>
            Provide information such as location,
            property area, bedrooms and other features.
        </p>

    </div>
    """)

with c2:
    st.html("""
    <div class="card">

        <div class="icon">2️⃣</div>

        <h3>ML Model Analysis</h3>

        <p>
            The trained machine learning model processes
            the property information and generates results.
        </p>

    </div>
    """)

with c3:
    st.html("""
    <div class="card">

        <div class="icon">3️⃣</div>

        <h3>Get Insights</h3>

        <p>
            View predicted prices, recommendations
            and useful market insights.
        </p>

    </div>
    """)


# =========================================================
# CTA
# =========================================================

st.html("""
<div class="cta">

    <h2>
        Ready to explore the real estate market? 🏠
    </h2>

    <p>
        Select a section from the sidebar and start
        exploring your property data.
    </p>

</div>
""")


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div style="
    text-align:center;
    color:#697386;
    font-size:13px;
    margin-top:40px;
    padding-top:20px;
    border-top:1px solid #292f3d;
">

    Real Estate Intelligence Platform
    <br>
    Built with Python • Machine Learning • Streamlit

</div>
""")
