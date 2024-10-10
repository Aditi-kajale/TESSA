import streamlit as st
from PIL import Image
import data
from data import NER, SENTIMENT_ANALYSIS, SUMMARIZATION, TOPIC_IDENTIFICATION


def set_techniques(ner, sentiment, summary, topic):
    if ner:
        NER.selected=True
    if sentiment:
        SENTIMENT_ANALYSIS.selected=True
    if summary:
        SUMMARIZATION.selected=True
    if topic:
        TOPIC_IDENTIFICATION.selected=True   

def run_analysis(input):
    data.INPUT_TEXT= input
    if NER.selected==True:
        NER.compute()
    if SENTIMENT_ANALYSIS.selected==True:
        SENTIMENT_ANALYSIS.compute()
    if SUMMARIZATION.selected==True:
        SUMMARIZATION.compute()
    if TOPIC_IDENTIFICATION.selected==True:
        TOPIC_IDENTIFICATION.compute()      

# Main page
def main():
    # Set page title and favicon
    st.set_page_config(page_title="TESSA: 4-in-1 Text Analytics Engine", page_icon="🔢", layout="wide")

    # Sidebar with options
    st.title("TESSA: 4-in-1 Text Analytics Engine")
    st.write("")
    st.sidebar.title("Select analysis techniques:")
    ner = st.sidebar.checkbox("NER")
    sentiment = st.sidebar.checkbox("Sentiment Analysis")
    summarization = st.sidebar.checkbox("Summarization")
    topic_identification = st.sidebar.checkbox("Topic Identification")

    img, inputs = st.columns([2,3],gap="medium")
    with img:
        image = Image.open('./text_analysis.jpg')
        st.image(image, use_column_width=True)
    with inputs:
        # Text input field
        st.markdown("<span style='font-size: 24px; font-weight: bold' >Type/paste your text:</span>",unsafe_allow_html=True)
        text_input = st.text_area("", label_visibility="collapsed", height=180)

        # File upload option
        st.markdown("<span style='font-size: 24px; font-weight: bold' >OR, upload a file:</span>",unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Choose a file", type=["txt"])
        if uploaded_file is not None:
            file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
            # st.write(file_details)

        if st.button("Analyse", type="primary"):
            
            set_techniques(ner, sentiment, summarization, topic_identification)
            run_analysis(text_input)

            url = "http://localhost:8501/Analysis"
            st.markdown(f"<meta http-equiv='refresh' content='0; URL={url}' />", unsafe_allow_html=True)
        st.markdown("<style>div.row-widget.stButton > button:first-child {margin: 0 auto; margin-top: 20px; display: block; width: 200px; height: 60px; border-radius: 15px;}</style>", unsafe_allow_html=True)    

   
       
# Run main function
if __name__ == "__main__":
    main()