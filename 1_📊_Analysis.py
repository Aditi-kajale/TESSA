import streamlit as st
import sys
sys.path.append('../')
from data import NER, SENTIMENT_ANALYSIS, SUMMARIZATION, TOPIC_IDENTIFICATION

# Second page with analysis results
st.set_page_config(page_title="TESSA: 4-in-1 Text Analytics Engine", page_icon="🔢", layout="wide")
st.title("Analysis Results")

# Add back button to sidebar
st.sidebar.button("Download Report 📩", type="primary")
st.sidebar.button("Back to Home page", type="secondary")
st.markdown("<style>div.row-widget.stButton > button:first-child {margin: 0 auto; margin-top: 20px; display: block; border-radius: 15px;}</style>", unsafe_allow_html=True)

# Set container style
container_style = {"border": "2px solid grey", "padding": "10px"}

st.write("")
col1, col2 = st.columns(2)
with col1:
    con1=st.container()
    # Add title
    title1="Entities recognized"
    result1=""
    if NER.selected:
        result1+=NER.output
    con1.markdown(f"<div style='text-align: center; border: 2px solid grey; padding: 10px; padding-bottom: 30px; margin: 10px; border-radius: 15px; background-color: #ffe6e6'><h1 style='font-size: 30px; font-weight: bold; margin-bottom: 20px;'>{title1}</h1>{result1}</div>", unsafe_allow_html=True)

    con2=st.container()
    title2="Summary"
    result2=""
    if SUMMARIZATION.selected:
        result2+=SUMMARIZATION.output
    con2.markdown(f"<div style='text-align: center; border: 2px solid grey; padding: 10px; padding-bottom: 30px; margin: 10px; border-radius: 15px; background-color: #ffe6e6'><h1 style='font-size: 30px; font-weight: bold; margin-bottom: 20px;'>{title2}</h1>{result2}</div>", unsafe_allow_html=True)
    
   
with col2:
    con3=st.container()
    title3="Sentiment"
    result3=""
    if SENTIMENT_ANALYSIS.selected:
        result3+=SENTIMENT_ANALYSIS.output
    con3.markdown(f"<div style='text-align: center; border: 2px solid grey; padding: 10px; padding-bottom: 30px; margin: 10px; border-radius: 15px; background-color: #ffe6e6'><h1 style='font-size: 30px; font-weight: bold; margin-bottom: 20px;'>{title3}</h1>{result3}</div>", unsafe_allow_html=True)    

   
    con4=st.container()
    title4="Topics Identified"
    result4=["","",""]
    if TOPIC_IDENTIFICATION.selected:
        result4=TOPIC_IDENTIFICATION.output
    con4.markdown(f"<div style='text-align: center; border: 2px solid grey; padding: 10px; padding-bottom: 30px; margin: 10px; border-radius: 15px; background-color: #ffe6e6'><h1 style='font-size: 30px; font-weight: bold; margin-bottom: 20px;'>{title4}</h1><span style='color: white; font-size: 20px; font-weight: bold; text-align: center; padding: 10px; margin: 5px; border-radius: 10px; background-color: brown'>{result4[0]}</span> <span style='color: white; font-size: 20px; font-weight: bold; text-align: center; padding: 10px; margin: 5px; border-radius: 10px; background-color: brown'>{result4[1]}</span> <span style='color: white; font-size: 20px; font-weight: bold; text-align: center; padding: 10px; margin: 5px; border-radius: 10px; background-color: brown'>{result4[2]}</span></div>", unsafe_allow_html=True)    


        
    
