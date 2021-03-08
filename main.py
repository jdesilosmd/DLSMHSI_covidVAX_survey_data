import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from nltk.corpus import stopwords
nltk.download(...)


stop = stopwords.words('english')
#df = pd.read_csv("C://Users//jdesilosmd//Documents//DLSHSI//COVID-19 Vax Team//survey result.csv")
df = pd.read_csv('survey result.csv')

st.markdown("# DLSMHSI COVID-19 Vaccination Survey Data")
st.empty()
st.empty()

# Analysis of the survey population:
st.markdown("## **1. Analysis of the survey respondents as to age:**")
age_hist = px.histogram(df, x='Age', nbins=20, template='seaborn',
                        marginal='box',
                        title='Age Distribution of Respondents (Histogram)')
st.plotly_chart(age_hist,use_container_width=True)

st.empty()
st.markdown("### ")
st.empty()
st.empty()

st.markdown("## **2. Analysis of survey question responses:**")
st.markdown("### ")
st.markdown("## _Survey data code sheet:_")
st.empty()
st.empty()

st.markdown("### ***Q1:*** Are you working within the premises of DLSUMC or the COVID-19 Molecular Laboratory (CDCDC)?")

df_q1 = df['Q1'].value_counts()
df_q1 = df_q1.rename_axis('Q1 Response').reset_index(name='Frequency')

q1_plot = px.bar(df_q1, x='Frequency', y='Q1 Response', orientation='h',
                 title='Frequency of YES and NO Answers in Q1',
                 template='seaborn', color='Q1 Response')

q1_plot.update_layout(showlegend=False)

st.plotly_chart(q1_plot, use_container_width=True)

st.markdown("### **Q2:** Once COVID-19 vaccines become available here at DLSMHSI, would you...?")
df_q2 = df['Q2'].value_counts()
df_q2 = df_q2.rename_axis('Q2 Response').reset_index(name='Frequency')

q2_plot = px.bar(df_q2, x='Frequency', y='Q2 Response', orientation='h',
                 title='Frequency of All Answers in Q2',
                 template='seaborn', color='Q2 Response')

q2_plot.update_layout(showlegend=False)

st.plotly_chart(q2_plot, use_container_width=True)

st.markdown("### **Q3:** What is the reason for your hesitancy? (May choose multiple answers)")
df_q3 = df['Q3'].value_counts()
df_q3 = df_q3.rename_axis('Q3 Response').reset_index(name='Frequency')
df_q3.index += 1

q3_plot = go.Figure(data=[go.Table(
    header=dict(values=list(df_q3.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_q3['Q3 Response'], df_q3['Frequency']],
               fill_color='lavender',
               align='left')
)])

q3_plot.update_layout(showlegend=False)
st.plotly_chart(q3_plot, use_container_width=True)

st.markdown("### **Q4:** What would definitely make you agree to getting vaccinated?")
df['Q4'] = df['Q4'].fillna('None')
q4_common = df['Q4'].apply(lambda words: ' '.join(word.lower() for word in words.split() if word not in stop)).value_counts()[:100]
st.write(q4_common)

st.markdown("### **Q5:** Do you agree that COVID-19 vaccination should be compulsory at work?")
df_q5 = df['Q5'].value_counts()
df_q5 = df_q5.rename_axis('Q5 Response').reset_index(name='Frequency')

q5_plot = px.bar(df_q5, x='Frequency', y='Q5 Response', orientation='h',
                 title='Frequency of YES and NO Answers in Q5',
                 template='seaborn', color='Q5 Response')

q5_plot.update_layout(showlegend=False)
st.plotly_chart(q5_plot, use_container_width=True)


st.markdown("### **Q6:** Who do you trust most to give you the vaccine? (May choose multiple answers)")
df_q6 = df['Q6'].value_counts()
df_q6 = df_q6.rename_axis('Q6 Response').reset_index(name='Frequency')
df_q6.index += 1

q6_plot = go.Figure(data=[go.Table(
    header=dict(values=list(df_q6.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_q6['Q6 Response'], df_q6['Frequency']],
               fill_color='lavender',
               align='left')
)])

q6_plot.update_layout(showlegend=False)
st.plotly_chart(q6_plot, use_container_width=True)


st.write("**Q7:** Who is your most trusted source of reliable information about the COVID-19 vaccine? (May choose multiple answers)")
df_q7 = df['Q7'].value_counts()
df_q7 = df_q7.rename_axis('Q7 Response').reset_index(name='Frequency')
df_q7.index += 1

q7_plot = go.Figure(data=[go.Table(
    header=dict(values=list(df_q7.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_q7['Q7 Response'], df_q7['Frequency']],
               fill_color='lavender',
               align='left')
)])

q7_plot.update_layout(showlegend=False)
st.plotly_chart(q7_plot, use_container_width=True)


st.write("**Q8:** What information would you like to know BEFORE vaccination?")
df['Q8'] = df['Q8'].fillna('None')
q8_common = df['Q8'].apply(lambda words: ' '.join(word.lower() for word in words.split() if word not in stop)).value_counts()[:100]
st.write(q8_common)


st.markdown("### **Q9:** What information would you like to be given to you AFTER vaccination?")
df['Q9'] = df['Q9'].fillna('None')
q9_common = df['Q9'].apply(lambda words: ' '.join(word.lower() for word in words.split() if word not in stop)).value_counts()[:100]
st.write(q9_common)


st.markdown("### **Q10:** What is/are your expectation/s in terms of getting infected once you have been vaccinated? (May choose multiple answers)")
df_q10 = df['Q10'].value_counts()
df_q10 = df_q10.rename_axis('Q10 Response').reset_index(name='Frequency')
df_q10.index += 1

q10_plot = go.Figure(data=[go.Table(
    header=dict(values=list(df_q10.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_q10['Q10 Response'], df_q10['Frequency']],
               fill_color='lavender',
               align='left')
)])

q10_plot.update_layout(showlegend=False)
st.plotly_chart(q10_plot, use_container_width=True)


st.markdown("### **Q11:** If there is an opportunity, would you like to have other members of your family to be vaccinated as well?")
df_q11 = df['Q11'].value_counts()
df_q11 = df_q11.rename_axis('Q11 Response').reset_index(name='Frequency')

q11_plot = px.bar(df_q11, x='Frequency', y='Q11 Response', orientation='h',
                 title='Frequency of YES and NO Answers in Q11',
                 template='seaborn', color='Q11 Response')

q11_plot.update_layout(showlegend=False)
st.plotly_chart(q11_plot, use_container_width=True)


st.empty()
st.empty()

