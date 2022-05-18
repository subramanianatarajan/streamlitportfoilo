#Sri ganasha
from cgitb import html
#From email.mime import image
from PIL import Image
from tkinter import image_names
import streamlit as st
import requests
from streamlit_lottie import st_lottie

##Style function
def local_css(filename):
        with open(filename) as f:
           st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
        local_css("style/style.css")



#st.set_page_config(page_title ="My Web pages", page_icon=":tada", layout="wide")
st.set_page_config(page_title="Subramani PyDev",page_icon=":tada", layout="centered", initial_sidebar_state="auto", menu_items=None)
###

def load_lotteiurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

lotting_image = load_lotteiurl("https://assets1.lottiefiles.com/packages/lf20_tfb3estd.json")
image_webscrap = Image.open("Images/web scriping.png")
image_profile = Image.open("Images/profile.png")

#Header Section
with st.container():
        #left_column, right_column= st.columns(2)
#with left_column:
     #   st.write(image_profile)
        #Function signature

        st.image(image_profile, caption="Subramanian Natarajan", width=180, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
      #  st.image(image_profile, width=300, caption="Subramanian Natarajan")
with st.container():
#with right_column:

        st.subheader("Hi, I am Subramanian :wave:")
        st.title("A Python developer from Germany, Berlin")
        st.write("I am passionate about finding ways to use python Scripting  with cloud services to more efficent in business settings.")

## Header section What i do
with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
with left_column:
        st.header("what I am doing ")
        st.write("##")
        st.write(
            """
            Currently attending Masters in Computer science program in IU hotschedule Berlin from oct 2021 to Oct 2023.Previous I am having experience as a Computer Engineer, Dubai,UAE. 

            I have gained vast knowledge in IT Support, Software implementation, Data Analysis and Customer Services .I have handled various responsibilities in my past solution developer position and quickly established talents in prioritizing tasks, meeting deadlines and finding solutions to eliminate obstacles.

            More interested working on Cloud technology , I have been completed cloud computing course having more knowledge of AWS services , in programming currently learning Python, MySQL with different framework.

            """
        )   

with right_column:

        st_lottie(lotting_image, height=350, key="coding")

with st.container():
        st.write("---")

with st.container():
        st.header("My Current Project")
        st.write("##")
        image_column, text_column = st.columns((1, 2))

with image_column:

        st.image(image_webscrap)
            #insert image
with text_column:
            
        st.subheader("Python for Web scriping ")
        st.write(
            """
            Collecting data from websites using an automated process as web scraping. Some websites explicitly forbid users from scraping their data with automated tools like the ones you ll create in this tutorial. Websites do this for two possible reasons:

            The site has a good reason to protect its data. For instance, Google Maps doesnt let you request too many results too quickly.

            Making many repeated requests to a websites server may use up bandwidth, slowing down the website for other users and potentially overloading the server such that the website stops responding entirely.)
            """
        )
with st.container():
        st.write("---")


#---------------Contact Form----------------
with st.container():
      #  st.write("----")
        st.header("Get touch with me.")
        st.write("##")


        #####Contact form with massage

        contact_form= """<form action="https://formsubmit.co/Subramanian.natarajan@yahoo.com" method="POST">
                         <input type = "hidden" name="_captcha" value="false">
                         <input type="text" name="Please enter your name" required>
                         <input type="email" name="Please enter your email" required>
                         <textarea name="Message" placeholder="Your message here" required></textarea>
                          <button type="submit">Send</button>
                        </form>
                        """
        left_column, right_column = st.columns(2)

        with left_column:
                st.markdown(contact_form, unsafe_allow_html= True)

        with right_column:
                st.empty()
