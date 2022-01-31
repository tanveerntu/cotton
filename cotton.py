##Environment used for this file
#charts38 ; created using anaconda navigator

####
#Required installtaions#

#pip install plotly
#pip install pandas
#pip install streamlit

######
#Required imports

from turtle import color
import plotly.express as px
from plotly import graph_objs as go
import plotly.graph_objects as go


import pandas as pd
import streamlit as st 
import yfinance as yf 

# Use the full page instead of a narrow central column
st.set_page_config(
    page_title = 'Cotton Production in Pakistan',
    page_icon = '✅',
    layout = 'wide'
)
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.title("Cotton Production in Pakistan")
st.write("Analysis by: National Textile University, Pakistan")

#importing csv file as dataframe
df = pd.read_csv('cotton_districts.csv')


#shorten name of a district for better display on chart
#df['District'] = df['District'].replace('Shaheed Benazirabad', 'Benazirabad')
########################################
########################################
#yearly trend chart
########################################

#creating new colum 'Bales_sum' of yearly sum of bales
df_yearly = df.groupby(['Year']).agg(Bales_sum=('Bales', 'sum')).reset_index()

##############################

##############################
fig_cd = go.Figure()
# Add traces
fig_cd.add_trace(go.Bar(x=df_yearly['Year'], y=df_yearly['Bales_sum'],
                    name='Cotton Bales', 
                    text=df_yearly['Bales_sum'], #text on bars
                    textfont_size=24, #text on bars
                    textfont_family='roboto',
                    textposition='auto',
                    texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
                    marker_color='#006BA2', #bar colors
                    hovertemplate='%{x} <br>Cotton Bales: %{y}'
                    ))
fig_cd.update_layout(
    autosize=False, height=650, width=1050,
    legend_traceorder="reversed",
    margin=dict(t=90, b=40, l=40, r=40),
    #title="Cotton Production in Pakistan",
    #title_font=dict(size=30, color='#111111', family="fjalla one, sans-serif"),
    xaxis_title='', yaxis_title="No. of Bales",
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
)

fig_cd.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig_cd.update_yaxes(showline=True, linewidth=2, linecolor='black')

fig_cd.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig_cd.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig_cd.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

#fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

fig_cd.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')

#title
fig_cd.add_annotation(
            text="Cotton Production",
            font=dict(family='Fjalla one', color='#006BA2', size=36), 
            xref="x domain", yref="y domain",
            x=0, y=1.15, 
            showarrow=False,
            arrowhead=1)

#subtitle
fig_cd.add_annotation(
            text="in Pakistan over the last few years of the closing season",
            font=dict(family='roboto', color='black', size=24), 
            xref="x domain", yref="y domain",
            x=0, y=1.08, 
            showarrow=False,
            arrowhead=1)
#datasource
fig_cd.add_annotation(
            text="Source: Pakinstan Cotton Ginners Association/National Textile University, Pakistan",
            font=dict(family='Roboto', color='#758D99', size=20), 
            xref="x domain", yref="y domain",
            x=0, y=-0.13, 
            showarrow=False,
            arrowhead=1)


st.plotly_chart(fig_cd, use_container_width=True) # to show Figure; container width true makes fig. size responsive

###
#######################################
###############################
#cotton exports and imports
##############################
df_e = pd.read_csv('yearly_cotton_imports_pbs.csv')


##############################

##############################
fig = go.Figure()
# Add traces

fig.add_trace(go.Bar( 
            x=df_e["year"], 
            y=df_e["imp_bales"],
            text=df_e["imp_bales"],
            marker_color='#ff6b6c',
            name='Imports' #name on legend
            ))

fig.add_trace(go.Bar( 
            x=df_e["year"], 
            y=df_e["exp_bales"],
            text=df_e["exp_bales"],
            marker_color='#3ebcd2',
            name='Exports'
            ))


fig.update_traces(texttemplate='%{text:.2s}', textposition='auto', textfont_size=24, textfont_family='roboto', textfont_color="#111111")

fig.update_layout(
    autosize=False, height=650, width=1050,
    legend_traceorder="reversed",
    margin=dict(t=90, b=40, l=40, r=40),
    xaxis_title='', yaxis_title="No. of Bales",
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
)

fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

#fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')

#title
fig.add_annotation(
            text="Cotton Exports & Imports",
            font=dict(family='Fjalla one', color='#006BA2', size=36), 
            xref="x domain", yref="y domain",
            x=0, y=1.15, 
            showarrow=False,
            arrowhead=1)

#subtitle
fig.add_annotation(
            text="in Pakistan over the last few years of the closing season",
            font=dict(family='roboto', color='black', size=24), 
            xref="x domain", yref="y domain",
            x=0, y=1.08, 
            showarrow=False,
            arrowhead=1)
#datasource
fig.add_annotation(
            text="Source: Pakinstan Bureau of Statistics/National Textile University, Pakistan",
            font=dict(family='Roboto', color='#758D99', size=20), 
            xref="x domain", yref="y domain",
            x=0, y=-0.13, 
            showarrow=False,
            arrowhead=1)

fig.update_layout(legend=dict(
    orientation="h",
    font=dict(family='Roboto', color='#758D99', size=16), 
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1))
st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

###############################
################################
#monthly cotton imports
#importing csv file as dataframe
df_m = pd.read_csv('monthly_cotton_imports_pbs.csv')
#calculating year-to-date YTD bales and adding new column for the same
df_m['bales_ytd'] = df_m['bales'].cumsum()
df_m['usd_ytd'] = df_m['USD'].cumsum()


##############
fig = go.Figure()
###############
# Add traces
fig.add_trace(go.Bar(x=df_m['month'], y=df_m['bales_ytd'],
                    name='Cotton Bales', 
                    text=df_m['bales_ytd'], #text on bars
                    textfont_size=24, #text on bars
                    textfont_family='roboto',
                    textposition='auto',
                    texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
                    marker_color='#006BA2', #bar colors
                    ))


###############
#layout
fig.update_layout(
    autosize=False, height=650, width=1050,
    legend_traceorder="reversed",
    margin=dict(t=90, b=90, l=90, r=40),
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
)
###############
#updates axes
fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(title='Cumulative No. of Bales', title_font=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
###############
#title
fig.add_annotation(
            text="Cotton Imports",
            font=dict(family='Fjalla one', color='#006BA2', size=36), 
            xref="x domain", yref="y domain",
            x=0, y=1.18, 
            showarrow=False,
            arrowhead=1)

#subtitle
fig.add_annotation(
            text="in Pakistan in the current financial year 2021-22 (Cumulative No. of Bales imported till recent month)",
            font=dict(family='roboto', color='black', size=24), 
            xref="x domain", yref="y domain",
            x=0, y=1.10, 
            showarrow=False,
            arrowhead=1)
#data reference
fig.add_annotation(
            text="Source: Pakinstan Bureau of Statistics/National Textile University, Pakistan",
            font=dict(family='Roboto', color='#758D99', size=20), 
            xref="x domain", yref="y domain",
            x=0, y=-0.18, 
            showarrow=False,
            arrowhead=1)
######################
#show figure in streamlit web app
st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive
##############################
##############################
##############
fig = go.Figure()
###############
# Add traces

fig.add_trace(go.Bar(x=df_m['month'], y=df_m['usd_ytd'],
                    name='Cotton Bales', 
                    text=df_m['usd_ytd'], #text on bars
                    textfont_size=24, #text on bars
                    textfont_family='roboto',
                    textposition='auto',
                    texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
                    marker_color='#ff6b6c', #bar colors
                    ))

###############
#layout
fig.update_layout(
    autosize=False, height=650, width=1050,
    legend_traceorder="reversed",
    margin=dict(t=90, b=90, l=90, r=40),
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
)
###############
#updates axes
fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(title='Cumulative US$', title_font=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
###############
#title
fig.add_annotation(
            text="Cost of Cotton Imports",
            font=dict(family='Fjalla one', color='#006BA2', size=36), 
            xref="x domain", yref="y domain",
            x=0, y=1.18, 
            showarrow=False,
            arrowhead=1)

#subtitle
fig.add_annotation(
            text="Cumulative price paid for cotton imports till recent month)",
            font=dict(family='roboto', color='black', size=24), 
            xref="x domain", yref="y domain",
            x=0, y=1.10, 
            showarrow=False,
            arrowhead=1)
#data reference
fig.add_annotation(
            text="Source: Pakinstan Bureau of Statistics/National Textile University, Pakistan",
            font=dict(family='Roboto', color='#758D99', size=20), 
            xref="x domain", yref="y domain",
            x=0, y=-0.18, 
            showarrow=False,
            arrowhead=1)
######################
#show figure in streamlit web app
st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive
##############################
##############################

##############################
#grouping by province

###############################

df_punjab = df[df['Province'] == 'Punjab']
df_punjab = df_punjab.groupby(['Year']).agg({'Bales':'sum'}).reset_index()

df_sindh = df[df['Province'] == 'Sindh']
df_sindh = df_sindh.groupby(['Year']).agg({'Bales':'sum'}).reset_index()

df_baluchistan = df[df['Province'] == 'Baluchistan']
df_baluchistan = df_baluchistan.groupby(['Year']).agg({'Bales':'sum'}).reset_index()


fig = go.Figure()


fig.add_trace(go.Bar( 
            x=df_punjab["Year"], 
            y=df_punjab["Bales"],
            text=df_punjab["Bales"],
            marker_color='#ff6b6c',
            name='Punjab' #name on legend
            ))

fig.add_trace(go.Bar( 
            x=df_sindh["Year"], 
            y=df_sindh["Bales"],
            text=df_sindh["Bales"],
            marker_color='#3ebcd2',
            name='Sindh'
            ))

fig.add_trace(go.Bar( 
            x=df_baluchistan["Year"], 
            y=df_baluchistan["Bales"],
            text=df_baluchistan["Bales"],
            marker_color='#006BA2',
            name='Baluchistan'
            ))

fig.update_traces(texttemplate='%{text:.2s}', textposition='auto', textfont_size=24, textfont_family='roboto', textfont_color="#111111")

fig.update_layout(
    autosize=True, height=650, width=1050,
    margin=dict(t=100, b=120, l=40, r=40),
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
    bargap=0.2,                             #value can be An int or float in the interval [0, 1]
)

fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

#fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
fig.update_yaxes(title="No. of Bales",
    title_font=dict(size=25, color='#111111', family="roboto"),
    )


#title
fig.add_annotation(
            text="Cotton Production",
            font=dict(family='Fjalla one', color='#006BA2', size=36), 
            xref="x domain", yref="y domain",
            x=0, y=1.19, 
            showarrow=False,
            arrowhead=1)

#subtitle
fig.add_annotation(
            text=f"in different Pakistani provinces over the last few years of the closing season",
            font=dict(family='roboto', color='black', size=24), 
            xref="x domain", yref="y domain",
            x=0, y=1.11, 
            showarrow=False,
            arrowhead=1)

fig.add_annotation(
            text="Source: Pakinstan Cotton Ginners Association/National Textile University, Pakistan",
            font=dict(family='Roboto', color='#758D99', size=20), 
            xref="x domain", yref="y domain",
            x=0, y=-0.24, 
            showarrow=False,
            arrowhead=1)
fig.update_layout(legend=dict(
    orientation="h",
    font=dict(family='Roboto', color='#758D99', size=16), 
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1))
st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive


############################
############################
# district-wise chart
###########################
#year = df["Year"]
#latest_year = year.max()
#filter data for latest_year

df_latest_year = df[df['Period'] == '2021-22']



fig = go.Figure()
# Add traces
fig.add_trace(go.Bar(x=df_latest_year['District'], y=df_latest_year['Bales'],
                    name='Cotton Bales', 
                    text=df_latest_year['Bales'], #text on bars
                    textfont_size=24, #text on bars
                    textfont_family='roboto',
                    texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
                    marker_color='#006BA2', #bar colors
                    ))
fig.update_layout(
    autosize=False, height=650, width=1050,
    legend_traceorder="reversed",
    margin=dict(t=90, b=40, l=40, r=40),
    #title="Cotton Production in Pakistan",
    #title_font=dict(size=30, color='#111111', family="fjalla one, sans-serif"),
    xaxis_title='', yaxis_title="No. of Bales",
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
)

fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

fig.update_xaxes(tickangle=90, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

#fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
fig.update_xaxes({'categoryorder':'total descending'})


#title
fig.add_annotation(
            text="Cotton Production",
            font=dict(family='Fjalla one', color='#006BA2', size=36), 
            xref="x domain", yref="y domain",
            x=0, y=1.22, 
            showarrow=False,
            arrowhead=1)

#subtitle
fig.add_annotation(
            text=f"in different Pakistani districts during 2020-21 season",
            font=dict(family='roboto', color='black', size=24), 
            xref="x domain", yref="y domain",
            x=0, y=1.11, 
            showarrow=False,
            arrowhead=1)

fig.add_annotation(
            text="Source: Pakinstan Cotton Ginners Association/National Textile University, Pakistan",
            font=dict(family='Roboto', color='#758D99', size=20), 
            xref="x domain", yref="y domain",
            x=0, y=-0.75, 
            showarrow=False,
            arrowhead=1)


st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

########################
########################
# montlhy cotton arrivals chart
###########################
#################
df_cotton_arrivals = pd.read_csv('cotton_arrivals.csv')

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_cotton_arrivals["Date"], 
    y=df_cotton_arrivals["2018-19"], 
    name="2018-19", 
    text=df_cotton_arrivals['2018-19'],
    texttemplate='%{text:.3s}', #text shorten into 3 digits
    mode="markers+lines",
    textposition="bottom right",
    textfont=dict(family="roboto, sans-serif", size=18, color="#eca220"),
    marker=dict(size=8, color="#eca220"),
    line=dict(width=2, color="#eca220"),
))

fig.add_trace(go.Scatter(
    x=df_cotton_arrivals["Date"], 
    y=df_cotton_arrivals["2019-20"], 
    name="2019-20", 
    text=df_cotton_arrivals['2019-20'],
    texttemplate='%{text:.3s}', #text shorten into 3 digits
    mode="markers+lines",
    textposition="bottom right",
    textfont=dict(family="roboto, sans-serif", size=18, color="#b4bb3b"),
    marker=dict(size=8, color="#b4bb3b"),
    line=dict(width=2, color="#b4bb3b"),
))

fig.add_trace(go.Scatter(
    x=df_cotton_arrivals["Date"], 
    y=df_cotton_arrivals["2020-21"], 
    name="2020-21", 
    text=df_cotton_arrivals['2020-21'],
    texttemplate='%{text:.3s}', #text shorten into 3 digits
    mode="markers+lines",
    textposition="bottom right",
    textfont=dict(family="roboto, sans-serif", color="#963c4c", size=18),
    marker=dict(size=8, color="#963c4c"),
    line=dict(width=2, color="#963c4c"),
))

fig.add_trace(go.Scatter(
    x=df_cotton_arrivals["Date"], 
    y=df_cotton_arrivals["2021-22"], 
    name="2021-22", 
    text=df_cotton_arrivals['2021-22'],
    texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
    mode="markers+lines+text",
    textposition="bottom right",
    textfont=dict(family="fjalla one, sans-serif", color="#106ea0", size=20),
    marker=dict(size=12, color="#106ea0"),
    line=dict(width=5, color="#106ea0")
))

fig.update_layout(
    autosize=True, height=650, width=1050,
    margin=dict(t=90, b=120, l=40, r=40),
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
    bargap=0.2,                             #value can be An int or float in the interval [0, 1]
)

fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

fig.update_xaxes(tickangle=90, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

#fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
fig.update_yaxes(title="Cumulative number of bales",
    title_font=dict(size=25, color='#111111', family="roboto"),
    )


#title
fig.add_annotation(
            text="Monthly Cotton Arrival",
            font=dict(family='Fjalla one', color='#006BA2', size=36), 
            xref="x domain", yref="y domain",
            x=0, y=1.19, 
            showarrow=False,
            arrowhead=1)

#subtitle
fig.add_annotation(
            text=f"in Pakistani factories during the last few years",
            font=dict(family='roboto', color='black', size=24), 
            xref="x domain", yref="y domain",
            x=0, y=1.11, 
            showarrow=False,
            arrowhead=1)

fig.add_annotation(
            text="Source: Pakinstan Cotton Ginners Association/National Textile University, Pakistan",
            font=dict(family='Roboto', color='#758D99', size=20), 
            xref="x domain", yref="y domain",
            x=0, y=-0.24, 
            showarrow=False,
            arrowhead=1)
fig.update_layout(legend=dict(
    orientation="h",
    font=dict(family='Roboto', color='#758D99', size=16), 
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1))
st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

###############################
##############################
#Historical cotton data
#########################

##############################
df_h = pd.read_csv('cotton_historical.csv')

fig = go.Figure()
# Add traces

#fig.add_trace(go.Bar(x=df_h['Year'], y=df_h['Bales'],
#                    name='', 
#                    text=df_h['Bales'], #text on bars
#                    textfont_size=24, #text on bars
#                    textfont_family='roboto',
#                    textposition='auto',
#                    texttemplate='%{text:,}',
#                    marker_color='#006BA2', #bar colors
#                    hovertemplate='%{x} <br>Cotton Bales: %{y}'
#                    ))

fig.add_trace(go.Scatter(
    x=df_h["Year"], 
    y=df_h["Bales"], 
    name="", 
    #text=df_cotton_arrivals['2021-22'],
    #texttemplate='%{text:.3s}', # to text shorten into 3 digits, use '%{text:.3s}'
    mode="markers+lines",
    #textposition="bottom right",
    #textfont=dict(family="fjalla one, sans-serif", color="#106ea0", size=20),
    marker=dict(size=12, color="#106ea0"),
    line=dict(width=5, color="#106ea0"),
    showlegend=False
))
fig.update_layout(
    autosize=False, height=650, width=1050,
    legend_traceorder="reversed",
    margin=dict(t=90, b=40, l=40, r=40),
    #title="Cotton Production in Pakistan",
    #title_font=dict(size=30, color='#111111', family="fjalla one, sans-serif"),
    xaxis_title='', yaxis_title="No. of Bales",
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
)

fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

#fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
#adding range buttons

fig.update_xaxes(
rangeslider_visible = False, 
    rangeselector = dict(
    buttons = list([
    dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
    dict(count = 2, label = '2Y', step = 'year', stepmode = 'backward'),
    dict(count = 5, label = '5Y', step = 'year', stepmode = 'backward'),
    #dict(step = 'all')
    ])))



#title
fig.add_annotation(
            text="Cotton Production in Pakistan",
            font=dict(family='Fjalla one', color='#006BA2', size=36), 
            xref="x domain", yref="y domain",
            x=0, y=1.15, 
            showarrow=False,
            arrowhead=1)

#subtitle
fig.add_annotation(
            text="since 1947-48 season",
            font=dict(family='roboto', color='black', size=24), 
            xref="x domain", yref="y domain",
            x=0, y=1.08, 
            showarrow=False,
            arrowhead=1)
#datasource
fig.add_annotation(
            text="Source: Pakinstan Cotton Ginners Association/Karachi Cotton Association/National Textile University, Pakistan",
            font=dict(family='Roboto', color='#758D99', size=20), 
            xref="x domain", yref="y domain",
            x=0, y=-0.13, 
            showarrow=False,
            arrowhead=1)
#Adding only the last date point value/text
fig.add_trace(go.Scatter(x=[df_h['Year'].iloc[-1]],
                         y=[df_h['Bales'].iloc[-1]],
                         text=[df_h['Bales'].iloc[-1]],
                         name='',
                         mode='markers+text',
                         marker=dict(color='red', size=14),
                         textposition='top right',
                         textfont=dict(family="fjalla one, sans-serif", color="#006BA2", size=24),
                         texttemplate='%{text:.3s}', #text shorten into 3 digits
                         showlegend=False))

#Adding value/text at year 2005, which is at index number 57
fig.add_trace(go.Scatter(x=[df_h['Year'].iloc[57]],
                         y=[df_h['Bales'].iloc[57]],
                         text=[df_h['Bales'].iloc[57]],
                         name='',
                         mode='markers+text',
                         marker=dict(color='red', size=14),
                         textposition='middle right',
                         textfont=dict(family="fjalla one, sans-serif", color="#006BA2", size=24),
                         texttemplate='%{text:.3s}', #text shorten into 3 digits
                         showlegend=False))


st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive

###########################
###########################
#cotton map of Pakistan
###########################
import json
pak_districts = json.load(open("pakistan_districts.geojson", 'r'))

district_id_map = {}
for feature in pak_districts["features"]:
  feature["id"] = feature["properties"]["objectid"]
  district_id_map[feature['properties']['districts']] = feature['id']

df['id']=df['District'].apply(lambda x:district_id_map[x])
#st.title("Cotton Map of Pakistan")

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
#st.plotly_chart(fig)

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
    autosize=True, height=700, width=1400,
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

###########################
########################
#monthly cotton imports




##############################
#Cotton prices
#############################
import yfinance as yf

from datetime import datetime, timedelta

#data = yf.download(tickers=stock_price, period = ‘how_many_days’, interval = ‘how_long_between_each_check’, rounding= bool)
#data = yf.download(tickers='CT=F', period = '5Y', interval = '1D', rounding= True)
data = yf.download(tickers='CT=F', start = '2017-01-01', end = datetime.now().date(), rounding= True)

#data 
data= data.reset_index() # to show date as column header
#data 

## getting the live ticker price

# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si

#to get live price of ticker/cotton CT=F
price = si.get_live_price('CT=F')
prev_close = data.Close.iloc[-2] #iloc[-2] is second last row of res_df ; iloc[0] is first row 


##

fig = go.Figure()

fig.add_trace(go.Scatter(x=data['Date'], 
                        y=data['Close'], 
                        name = '',
                        texttemplate='%{text:.2s}', # to  shorten text into 3 digits, use '%{text:.3s}'
                        ))
fig.update_traces(hovertemplate='Date: %{x} <br>Price: %{y} cents per pound') #<br> adds space or shifts to next line; x & y is repected axis value; 

fig.add_trace(go.Indicator(
            domain={"x": [0, 1], "y": [0.98, 1]},
            value=price,
            mode="number+delta",
            number={"font":{"size":50, "color":'#111111', "family":"roboto"}},
            title={"text": "Current Price in cents per pound"},
            title_font=dict(size=25, color='#111111', family="roboto"),
            delta={"reference": prev_close},
        ))



fig.update_yaxes(title_text = 'Cents Per Pound', tickprefix = '')
#fig.update_xaxes(showspikes=True, spikecolor="red", spikesnap="cursor", spikemode="across", spikethickness=3) #xaxis spike on hover
#fig.update_yaxes(showspikes=True, spikecolor="red", spikesnap="cursor", spikemode="across", spikethickness=3) #yais spike on hover

fig.update_layout(
    autosize=True, height=650, width=1050,
    margin=dict(t=90, b=120, l=40, r=40),
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
    font=dict(color='#111111', size=20, family="roboto, sans-serif"), 
    bargap=0.2,                             #value can be An int or float in the interval [0, 1]
)

fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

fig.update_xaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(tickangle=0, tickfont=dict(family='Roboto', color='black', size=24))
fig.update_yaxes(title_font=dict(family='Roboto', color='black', size=24))

#fig_cd.update_xaxes(font=dict(color='#111111', size=24, family="roboto, sans-serif"))

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#758D99')
fig.update_yaxes(title="Cents Per Pound",
    title_font=dict(size=25, color='#111111', family="roboto"),
    )

fig.update_xaxes(
rangeslider_visible = False, 
    rangeselector = dict(
    buttons = list([
    dict(count = 1, label = '1W', step = 'day', stepmode = 'backward'),
    dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
    dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
    dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
    dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
    dict(count = 2, label = '2Y', step = 'year', stepmode = 'backward'),
    dict(count = 5, label = '5Y', step = 'year', stepmode = 'backward'),
    #dict(step = 'all')
    ])))
#title
fig.add_annotation(
            text="Cotton Rates/ICE Futures",
            font=dict(family='Fjalla one', color='#006BA2', size=36), 
            xref="x domain", yref="y domain",
            x=0, y=1.19, 
            showarrow=False,
            arrowhead=1)


fig.add_annotation(
            text="Source: Yahoo Finance/National Textile University",
            font=dict(family='Roboto', color='#111111', size=20), 
            xref="x domain", yref="y domain",
            x=0, y=-0.24, 
            showarrow=False,
            arrowhead=1)

st.plotly_chart(fig, use_container_width=True) # to show Figure; container width true makes fig. size responsive


