import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")

st.title('Analytics')

new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl','rb'))


group_df = (
    new_df
    .groupby('sector')[[
        'price',
        'price_per_sqft',
        'built_up_area',
        'latitude',
        'longitude'
    ]]
    .mean()
    .reset_index()
)
st.header('Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig, use_container_width=True)

st.header('Features Wordcloud')

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='black',
    stopwords=set(['s']),
    min_font_size=10
).generate(feature_text)

fig_wc, ax = plt.subplots(figsize=(8, 8))

ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
fig_wc.tight_layout(pad=0)

st.pyplot(fig_wc)

st.header('Area Vs Price')

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)

st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)

st.header('Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)


st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)



st.header('Price Distribution')

fig4 = px.histogram(
    new_df,
    x='price',
    nbins=50,
    title='Property Price Distribution'
)

st.plotly_chart(fig4, use_container_width=True)


st.header('BHK Vs Built-up Area')

fig5 = px.scatter(
    new_df,
    x='built_up_area',
    y='bedRoom',
    color='property_type',
    title='BHK Vs Built-up Area'
)

st.plotly_chart(fig5, use_container_width=True)



st.header('Price Per Sqft by Property Type')

fig6 = px.box(
    new_df,
    x='property_type',
    y='price_per_sqft',
    title='Price Per Sqft Comparison'
)

st.plotly_chart(fig6, use_container_width=True)


st.header('Top 15 Expensive Sectors')

top_sectors = (
    new_df.groupby('sector')['price_per_sqft']
    .mean()
    .sort_values(ascending=False)
    .head(15)
    .reset_index()
)

fig7 = px.bar(
    top_sectors,
    x='price_per_sqft',
    y='sector',
    orientation='h',
    title='Top 15 Sectors by Average Price Per Sqft'
)

st.plotly_chart(fig7, use_container_width=True)

st.header('Average Price by BHK')

bhk_price = (
    new_df.groupby('bedRoom')['price']
    .mean()
    .reset_index()
)

fig8 = px.bar(
    bhk_price,
    x='bedRoom',
    y='price',
    title='Average Property Price by BHK'
)

st.plotly_chart(fig8, use_container_width=True)


st.header('Average Built-up Area by BHK')

bhk_area = (
    new_df.groupby('bedRoom')['built_up_area']
    .mean()
    .reset_index()
)

fig9 = px.bar(
    bhk_area,
    x='bedRoom',
    y='built_up_area',
    title='Average Built-up Area by BHK'
)

st.plotly_chart(fig9, use_container_width=True)

st.header('Furnishing Type Vs Price')

fig10 = px.box(
    new_df,
    x='furnishing_type',
    y='price',
    title='Price by Furnishing Type'
)

st.plotly_chart(fig10, use_container_width=True)

st.header('Property Type Distribution')

property_count = new_df['property_type'].value_counts().reset_index()

fig11 = px.pie(
    property_count,
    names='property_type',
    values='count',
    title='Flat Vs House'
)

st.plotly_chart(fig11, use_container_width=True)


st.header('Bathrooms Vs Price')

fig12 = px.box(
    new_df,
    x='bathroom',
    y='price',
    title='Bathrooms Vs Property Price'
)

st.plotly_chart(fig12, use_container_width=True)


st.header('Sector Analysis')

selected_sector = st.selectbox(
    'Choose Sector',
    ['Overall'] + sorted(new_df['sector'].dropna().unique().tolist())
)

if selected_sector == 'Overall':
    temp_df = new_df
else:
    temp_df = new_df[new_df['sector'] == selected_sector]

st.metric(
    'Average Price',
    f"₹{temp_df['price'].mean():.2f} Cr"
)

st.metric(
    'Average Price Per Sqft',
    f"₹{temp_df['price_per_sqft'].mean():.0f}"
)

st.metric(
    'Average Built-up Area',
    f"{temp_df['built_up_area'].mean():.0f} sqft"
)