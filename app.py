import streamlit as st 
from PIL import Image
from pathlib import Path
from utils import social_icons


st.set_page_config(page_title="DHARUN Portfolio",  
                   layout="wide",
)
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / 'assets' /"Dharun_ds.pdf"
css_file = current_dir / 'styles'/'homepage.css'

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    
    
st.markdown("<marquee behavior='scroll' direction='left' style='font-size:30px;'>Welcome to my portfolio</marquee>", unsafe_allow_html=True)

img = Image.open("assets\WhatsApp Image 2024-09-10 at 2.32.55 PM.jpeg")


with st.container():
    left_column, middle_column, right_column = st.columns((1,0.2,0.6))
    with left_column:
        st.header("About Me", divider='red')
        st.subheader("Aspiring Data Scientist")
        st.write("-Hi, I'm Dharun! a Recent graduate with a strong foundation in data science and a deep enthusiasm for leveraging data to drive impactful business decisions. My academic journey has equipped me with robust analytical skills and hands-on experience in machine learning, statistical analysis, and data visualization.")
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

