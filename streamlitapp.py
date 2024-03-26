#import libraries
import streamlit as st
#import cv2
#from cvzone.HandTrackingModule import HandDetector
#from cvzone.ClassificationModule import Classifier
#import numpy as np
#import math

#setup theside bar
with st.sidebar:
    st.image('https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png')
    st.title('BUC SIGN Language')
    st.info('This Application was deevloped by Kipsang Mutai Nicholas')
   #generating a list of options 
options = ("ASL to Alphabets", "KSL to Words")
selected_translation = st.selectbox('choose Translation', options)

#generate two columns 
col1, col2 =st.columns(2)

if options:

    with col1:
        st.text('ASL TO LETTERS')
        st.camera_input("Capture_Image")
 
    with col2:
         st.text('KSL TO WORDS')
