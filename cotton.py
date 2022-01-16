##Environment used for this file
#charts38 ; created using anaconda navigator

####
#Required installtaions#

#pip install plotly
#pip install pandas
#pip install streamlit

######
#Required imports

import plotly.express as px
from plotly import graph_objs as go

import pandas as pd
import streamlit as st 

st.set_page_config(layout='wide')

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Use the full page instead of a narrow central column
st.title("Cotton Production in Pakistan")
st.write("Data Source: Pakistan Cotton Ginners Association; Analysis by: National Textile University")

#importing csv file as dataframe
df = pd.read_csv('cotton_districts.csv')
########################
#creating new colum 'Bales_sum' of yearly sum of bales

df_yearly = df.groupby(['Year']).agg(Bales_sum=('Bales', 'sum')).reset_index()


fig_cd = go.Figure()
# Add traces
fig_cd.add_trace(go.Bar(x=df_yearly['Year'], y=df_yearly['Bales_sum'],
                    name='Cotton Bales', 
                    text=df_yearly['Bales_sum'],
                    textposition='auto',
                    texttemplate='%{text:,}',
                    hovertemplate='%{x} <br>Cotton Bales: %{y}'
                    ))
fig_cd.update_layout(
    autosize=True, height=700, width=1100,
    legend_traceorder="reversed",
    margin=dict(t=80, b=0, l=40, r=40),
    title="Cotton Production in Pakistan",
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    xaxis_title='', yaxis_title="Bales",
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
)
fig_cd.add_annotation(
            text="Source: PCGA/NTU",
            xref="x domain", yref="y domain",
            x=1, y=1.1, 
            showarrow=False,
            arrowhead=1)
fig_cd.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=0.7
))
st.plotly_chart(fig_cd, use_container_width=True) # to show Figure; container width true makes fig. size responsive


####################

########################
#grouping by province

###############################

df_province = df.groupby(['Year', 'Province']).agg(Bales_province=('Bales', 'sum')).reset_index()

fig = px.bar(df_province, 
            x="Year", 
            y="Bales_province", 
            color="Province", 
            barmode='group', 
            text=df_province["Bales_province"],
            title="Cotton Production in Pakistan")
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

fig.update_layout(
    autosize=True, height=700, width=1100,
    legend_traceorder="reversed",
    margin=dict(t=80, b=0, l=40, r=40),
    title="Province-wise Cotton Production in Pakistan",
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    xaxis_title='', yaxis_title="Bales",
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises

)

fig.add_annotation(
            text="Source: PCGA/NTU",
            xref="x domain", yref="y domain",
            x=1, y=1.1, 
            showarrow=False,
            arrowhead=1)

st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive




#######################################
##############################

####################
#################
fig = px.bar(df_province, x='Province', y="Bales_province", range_y=[0, 8000000], text=df_province['Bales_province'], 
  animation_frame="Year")  

fig.update_layout(
    autosize=True, height=700, width=1100,
    title="Province-wise Cotton Production in Pakistan",
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=18, family="roboto, sans-serif"),
)    #font of lablels of axises
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

fig.update_layout(margin=dict(l=20, r=20, t=70, b=100))
fig['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 150)
fig['layout']['sliders'][0]['pad']=dict(r= 10, t= 50,)
fig.update_xaxes({'categoryorder':'total descending'})
fig.add_annotation(
            text="Source: PCGA/NTU",
            xref="x domain", yref="y domain",
            x=1, y=1.1, 
            showarrow=False,
            arrowhead=1)
st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive
####################
#################
fig = px.bar(df, 
            x='District', 
            y="Bales", 
            range_y=[0, 1500000], 
            text=df['Bales'], 
            color='Bales',
            animation_frame="Year"
            )  

fig.update_layout(
    autosize=True, height=700, width=1100,
    title="District-wise Cotton Production in Pakistan",
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    xaxis_title='', yaxis_title="Bales",
    font=dict(color='#111111', size=18, family="roboto, sans-serif"),
)    #font of lablels of axises
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

fig.update_layout(margin=dict(l=20, r=20, t=60, b=200))
fig['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 150)
fig['layout']['sliders'][0]['pad']=dict(r= 10, t= 150,)
fig.update_xaxes({'categoryorder':'total descending'})
fig.add_annotation(
            text="Source: PCGA/NTU",
            xref="x domain", yref="y domain",
            x=1, y=1.1, 
            showarrow=False,
            arrowhead=1)
st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

##########################
fig = px.bar(df, x="Period", y="Bales", color="District", title="Cotton Production in Pakistan")

fig.update_layout(
    autosize=True, height=700, width=1100,
    legend_traceorder="reversed",
    margin=dict(t=80, b=0, l=40, r=40),
    title="District-wise Cotton Production in Pakistan",
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    xaxis_title='', yaxis_title="Bales",
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
)
fig.add_annotation(
            text="Source: PCGA/NTU",
            xref="x domain", yref="y domain",
            x=1, y=1.1, 
            showarrow=False,
            arrowhead=1)

st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

###########################

df_punjab = df.loc[df['Province'].isin(['Punjab'])]
df_sindh = df.loc[df['Province'].isin(['Sindh'])]


fig = px.bar(df_punjab, x='District', y="Bales", range_y=[0, 1500000], text=df_punjab['Bales'], 
  animation_frame="Year")  

fig.update_layout(
    autosize=True, height=700, width=1100,
    title="District-wise Cotton Production in Punjab",
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=18, family="roboto, sans-serif"),
)    #font of lablels of axises
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

fig.update_layout(margin=dict(l=20, r=20, t=60, b=200))
fig['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 150)
fig['layout']['sliders'][0]['pad']=dict(r= 10, t= 150,)
fig.update_xaxes({'categoryorder':'total descending'})
fig.update_xaxes(tickangle = 90)

fig.add_annotation(
            text="Source: PCGA/NTU",
            xref="x domain", yref="y domain",
            x=1, y=1.1, 
            showarrow=False,
            arrowhead=1)
#st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

###################
fig = px.bar(df_sindh, x='District', y="Bales", range_y=[0, 1500000], text=df_sindh['Bales'], 
  animation_frame="Year")  

fig.update_layout(
    autosize=True, height=700, width=1100,
    title="District-wise Cotton Production in Sindh",
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=18, family="roboto, sans-serif"),
)    #font of lablels of axises
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

fig.update_layout(margin=dict(l=20, r=20, t=60, b=200))
fig['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 150)
fig['layout']['sliders'][0]['pad']=dict(r= 10, t= 150,)
fig.update_xaxes({'categoryorder':'total descending'})
fig.update_xaxes(tickangle = 90)
fig.add_annotation(
            text="Source: PCGA/NTU",
            xref="x domain", yref="y domain",
            x=1, y=1.1, 
            showarrow=False,
            arrowhead=1)
#st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

##############
##########################
fig = px.line(df, x="Year", y="Bales", color="District", markers=True)

fig.update_layout(
    autosize=True, height=700, width=1100,
    legend_traceorder="reversed",
    margin=dict(t=80, b=0, l=40, r=40),
    title="District-wise Cotton Production in Pakistan",
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    xaxis_title='', yaxis_title="Bales",
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
)
fig.add_annotation(
            text="Source: PCGA/NTU",
            xref="x domain", yref="y domain",
            x=1, y=1.1, 
            showarrow=False,
            arrowhead=1)

st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

###############
fig = px.line(df_sindh, x="Year", y="Bales", color="District", markers=True)

fig.update_layout(
    autosize=True, height=700, width=1100,
    legend_traceorder="reversed",
    margin=dict(t=80, b=0, l=40, r=40),
    title="District-wise Cotton Production in Sindh",
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    xaxis_title='', yaxis_title="Bales",
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=18, family="roboto, sans-serif"),    #font of lablels of axises
)
fig.add_annotation(
            text="Source: PCGA/NTU",
            xref="x domain", yref="y domain",
            x=1, y=1.1, 
            showarrow=False,
            arrowhead=1)

#st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

#################
df_cotton_arrivals = pd.read_csv('cotton_arrivals.csv')
#df # to see dataframe
#df_cotton_arrivals
#conver date colums into datetime format
#df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
#df 


import plotly.graph_objects as go

fig_cotton_arrivals = go.Figure()

fig_cotton_arrivals.add_trace(go.Scatter(
    x=df_cotton_arrivals["Date"], 
    y=df_cotton_arrivals["2018-19"], 
    name="2018-19", 
    text=df_cotton_arrivals['2018-19'],
    texttemplate='%{text:.3s}', #text shorten into 3 digits
    mode="markers+lines",
    textposition="bottom right",
    textfont=dict(family="roboto, sans-serif", size=18, color="Purple"),
    marker=dict(size=12, color="Purple"),
    line=dict(width=2.5, color="Purple"),
))

fig_cotton_arrivals.add_trace(go.Scatter(
    x=df_cotton_arrivals["Date"], 
    y=df_cotton_arrivals["2019-20"], 
    name="2019-20", 
    text=df_cotton_arrivals['2019-20'],
    texttemplate='%{text:.3s}', #text shorten into 3 digits
    mode="markers+lines",
    textposition="bottom right",
    textfont=dict(family="roboto, sans-serif", size=18, color="Green"),
    marker=dict(size=12, color="Green"),
    line=dict(width=2.5, color="Green"),
))

fig_cotton_arrivals.add_trace(go.Scatter(
    x=df_cotton_arrivals["Date"], 
    y=df_cotton_arrivals["2020-21"], 
    name="2020-21", 
    text=df_cotton_arrivals['2020-21'],
    texttemplate='%{text:.3s}', #text shorten into 3 digits
    mode="markers+lines",
    textposition="bottom right",
    textfont=dict(family="roboto, sans-serif", color="Blue", size=18),
    marker=dict(size=12, color="Blue"),
    line=dict(width=2.5, color="Blue"),
))

fig_cotton_arrivals.add_trace(go.Scatter(
    x=df_cotton_arrivals["Date"], 
    y=df_cotton_arrivals["2021-22"], 
    name="2021-22", 
    text=df_cotton_arrivals['2021-22'],
    texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
    mode="markers+lines+text",
    textposition="bottom right",
    textfont=dict(family="fjalla one, sans-serif", color="Red", size=20),
    marker=dict(size=12, color="Red"),
    line=dict(width=2.5, color="Red")
))

fig_cotton_arrivals.update_layout(
    autosize=True, height=700, width=1100,
    title="Cotton Arrivals in Pakistani Factories",
    #margin=dict(t=60, b=0, l=40, r=40),
    title_font=dict(size=25, color='#111111', family="fjalla one, sans-serif"),
    xaxis_title='', yaxis_title="Cumulative No. of Cotton Bales",
    plot_bgcolor='#ededed',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=20, family="roboto, sans-serif"),    #font of lablels of axises
    bargap=0.2,                             #value can be An int or float in the interval [0, 1]
    #legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
fig_cotton_arrivals.add_annotation(
            text="Source: PCGA/NTU",
            xref="x domain", yref="y domain",
            x=1, y=1.1, 
            showarrow=False,
            arrowhead=1)
st.plotly_chart(fig_cotton_arrivals, use_container_width=True) # to show Figure; container width true makes fig. size responsive

##################
import json
pak_districts = json.load(open("pakistan_districts.geojson", 'r'))

district_id_map = {}
for feature in pak_districts["features"]:
  feature["id"] = feature["properties"]["objectid"]
  district_id_map[feature['properties']['districts']] = feature['id']

df['id']=df['District'].apply(lambda x:district_id_map[x])
st.title("Cotton Map of Pakistan")

fig = go.Figure(go.Choroplethmapbox(geojson=pak_districts, locations=df.id, z=df.Bales,
                                    text= df['District'], 
                                    hoverinfo= 'text+z',
                                    reversescale=True,
                                                                        ))
fig.update_layout(mapbox_style="stamen-terrain",
                  mapbox_zoom=5.0, mapbox_center = {"lat": 30.3753, "lon": 69.3451})
fig.update_traces(text=df['District'])

fig.update_layout(
    autosize=True, height=650, width=1400,
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#####
st.plotly_chart(fig)

######################
#######################
st.title("Cotton Map of Pakistan")

#satellite-streets
#############

fig = px.scatter_mapbox(df, 
                    lat="Lat", 
                    lon="Long", 
                    hover_name="District", 
                    hover_data=["District", "Bales"],
                    color_discrete_sequence=["Red"], 
                    size="Bales",
                    animation_frame="Year",
                    zoom=5,
                    height=300
                    )



fig.update_layout(mapbox_style="open-street-map")


fig.update_layout(
    autosize=True, height=650, width=1400,
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)
