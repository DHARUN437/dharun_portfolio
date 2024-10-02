import matplotlib
from matplotlib import style
import streamlit as st
from PIL import Image, ImageDraw
from pathlib import Path
from streamlit_extras.mention import mention
from utils import social_icons

st.set_page_config(page_title="DHARUN Portfolio",  
                   layout="wide",
)
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / 'assets' /"Dharun_ds.pdf"
css_file = current_dir / 'styles\homepage.css'

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    
st.markdown("<marquee behavior='scroll' direction='left' style='font-size:30px;'>Welcome to my portfolio</marquee><br><br><br>", unsafe_allow_html=True)

img = Image.open("assets\WhatsApp Image 2024-09-10 at 2.32.55 PM.jpeg")

with st.container():
    left_column, middle_column, right_column = st.columns((1,0.2,0.6))
    with left_column:
        st.header("About Me", divider='red')
        st.subheader("Aspiring Data Scientist")
        st.write("-Hi, I'm Dharun! As a recent graduate with a solid background in data science, I am passionate about utilizing data to facilitate impactful business decisions. My academic pursuits have honed my analytical abilities and provided me with hands-on experience in machine learning, statistical analysis, and data visualization. I am eager to bring my skills and enthusiasm to your team, contributing to innovative data-driven solutions")
        st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream")
        st.markdown(social_icons(32, 32, LinkedIn="https://www.linkedin.com/in/bdharun19/", 
                                         GitHub="https://github.com/DHARUN437", 
                                         ),
                                         unsafe_allow_html=True)
    with middle_column:
        st.empty()
    with right_column:
        st.image(img)


st.subheader("Education", divider="red")

st.write("###  [_Sri Ramakrishna College Of Arts and Science_](https://www.srcas.ac.in/) (2021-2024)")
st.write("### Bacholer of Science")
st.write("##### Major: Information Technology")
st.write("**Relevant Coursework:** Data Science,Machine learning, Deep Learning, Natural Language Processing....")
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Experience", divider="red")
st.write("### Data Scientist Intern - Qtree technologies, Coimbatore")
st.write("##### Key Responsiblities:")
st.markdown("""
            -> Gained hands-on experience in data manipulation, data analysis, and statistical modeling using Python and SQL.<br>
            -> Developed machine learning models, including regression, classification, and clustering techniques.
<br>-> Performed data preprocessing tasks such as data cleaning, feature engineering, and handling missing values. Built and deployed interactive dashboards for data visualization using **Seaborn** and __Matplotlib__.<br>
""", unsafe_allow_html=True)
st.write("##### Key Achievements:")
st.markdown("""
            -> Created a predictive model for Cyberbullying detection, achieving an accuracy of __90%__ using [ML techniques like LinearSVC, TF-IDF vectorizer].<br>
            -> Developed a data pipeline to automate the collection, cleaning, and analysis of data, reducing processing time by
__65%__.
<br>-> Presented a final capstone project on Cyberbullying, demonstrating proficiency in machine learning algorithms and data storytelling.
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.subheader ("Technical skills", divider="red")

# Custom CSS for square-shaped cards with icons and text directly below each card
st.markdown(
    """
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css');

    .card-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    .card-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 30%;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        height: 250px;
        width: 75%;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .card-icon {
        font-size: 80px;
        color: #00001F;
    }
    .card-description {
        font-size: 18px;
        color: #FFFFFF;
        text-align: center;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for three square-shaped cards with icons and descriptions below each
st.markdown(
    """
    <div class="card-container">
        <div class="card-item">
            <div class="card">
                <i class="fa fa-code card-icon"></i>
            </div>
            <div class="card-description">Programming language : Python <br> Database : MySQL Database</div>
        </div>
        <div class="card-item">
            <div class="card">
                <i class="fa fas fa-rocket card-icon"></i>
            </div>
            <div class="card-description">Machine Learning Frameworks : Scikit Learn, XGBoost, AdaBoost, MultinomialNB</div>
        </div>
        <div class="card-item">
            <div class="card">
                <i class="fa fas fa-gears card-icon"></i>
            </div>
            <div class="card-description">Data science Libraries & Frameworks : Pandas, NumPy, Streamlit, Matplotlib, Seaborn, Pillow</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Major Projects", divider='red')

cyber = Image.open('assets\cyber_bully.png')
canc = Image.open(r"assets\brest_cancer.png")
res = Image.open(r"assets\res_review.png")

with st.container():
    image_column, text_column = st.columns((1.3,3))
    with text_column:
        st.subheader("Cyberbullying Detection System ", divider="blue")
        #st.write("*Self-initiated project*")
        st.markdown("""
            __Tools/Technologies__ : <br>
                      
                       Python, Streamlit, Scikit-learn, Natural Language Processing (NLP), TF-IDF Vectorizer, LinearSVC, Joblib
__Description__ : <br>
 -> Developed a machine learning-based web application to detect cyberbullying in text data.<br>
 -> Implemented data preprocessing techniques, including stopword removal and text vectorization using TF-IDF.<br>
 -> Built an interactive Streamlit web app to provide real-time feedback on user-submitted text.<br>
 -> The system uses a pre-trained LinearSVC model and TF-IDF Vectorizer to classify input text as either "bullying" or "not bullying"<br>
            """, unsafe_allow_html=True)       
        mention(label="Streamlit App", icon="streamlit", url="https://cyberbullyingdetection-dharun.streamlit.app/")
        mention(label="Github Repo", icon="github", url="https://github.com/DHARUN437/cyberbullying_detection")
    with image_column:
        st.markdown("<br>  </br>",unsafe_allow_html=True)
        st.image(cyber)
        st.markdown("<br>",unsafe_allow_html=True)

with st.container():
    image_column, text_column = st.columns((1.3,3))
    with text_column:
        st.subheader("Brest Cancer Prediction System", divider="blue")
        #st.write("*Self-initiated project*")
        st.markdown("""
            __Tools/Technologies__ : <br>
                      
                       Python, Streamlit, Logistic regression, Scikit-learn, Pandas, Numpy, Joblib
__Description__ : <br>
 ->  Developed an interactive web application using Streamlit to predict the nature of breast tumors based on patient data.<br>
 -> The app utilizes a trained Logistic Regression model to classify tumors as either malignant or benign, providing critical insights for early detection<br>
 -> Designed and implemented a user-friendly interface to allow input of patient ID and display relevant medical parameters.<br>
 -> Integrated a trained machine learning model using joblib, enabling real-time predictions based on user-provided data.<br>
            """ , unsafe_allow_html=True)       
        mention(label="Streamlit App", icon="streamlit", url="https://breastcancer-classification-dharun.streamlit.app/")
        mention(label="Github Repo", icon="github", url="https://github.com/DHARUN437/breast_cancer-classification")
    with image_column:
        st.markdown("<br>  </br>",unsafe_allow_html=True)
        st.image(canc)
        st.markdown("<br>",unsafe_allow_html=True)

with st.container():
    image_column, text_column = st.columns((1.3,3))
    with text_column:
        st.subheader("Restaurant review  sentiment analysis", divider="blue")

        #st.write("*Self-initiated project*")
        st.markdown("""
            __Tools/Technologies__ : <br>
                      
                       Python, Streamlit, Scikit-learn, Natural Language Processing (NLP), Textblob, Vender, XGBoost, Joblib
__Description__ : <br>
 -> This project focuses on building a Natural Language Processing (NLP) model to classify customer reviews of restaurants into positive or negative sentiment.<br>
 -> Preprocessing of text data using tokenization, removal of stopwords, stemming, and lemmatization.<br>
 -> Real-time sentiment analysis using both TextBlob and VADER models.<br>
 -> The application is deployed using Streamlit, allowing users to interact with the model in real-time.<br>
            """ , unsafe_allow_html=True)       
        mention(label="Streamlit App", icon="streamlit", url="https://restaurant-sentiment-dharun.streamlit.app/")
        mention(label="Github Repo", icon="github", url="https://github.com/DHARUN437/NLP_projects")
    with image_column:
        st.markdown("<br>  </br>",unsafe_allow_html=True)
        st.image(res)
        st.markdown("<br>",unsafe_allow_html=True)
        
st.subheader("Minor Projects", divider= 'red')

col1, col2, col3 = st.columns(3)

with col1:
    st.image(r"assets\salary.png", caption="Software developer salary prediction", use_column_width=True)

with col2:
    st.image(r"assets\cyber_bully.png", caption="Description for Image 2", use_column_width=True)

with col3:
    st.image(r"assets\res_review.png", caption="Description for Image 3", use_column_width=True)
    

col1, col2, col3 = st.columns(3)

with col1:
    st.image(r"assets\brest_cancer.png", caption="Description for Image 1", use_column_width=True)

with col2:
    st.image(r"assets\cyber_bully.png", caption="Description for Image 2", use_column_width=True)

with col3:
    st.image(r"assets\res_review.png", caption="Description for Image 3", use_column_width=True)