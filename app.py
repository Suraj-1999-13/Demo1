import streamlit as st
import numpy as np
import cv2
import time
from collections import Counter
from streamlit_webrtc import (
    WebRtcMode,
    webrtc_streamer,
)
def emotion_find():
    
    webrtc_ctx = webrtc_streamer(
            key="loopback",
            mode=WebRtcMode.SENDONLY
        )
    st.markdown("## Click here to activate me")
    if(st.button("Activate EMP")):
        progress = st.progress(0)
        i=0
        while ( int(time.time() - start_time) < capture_duration and i<100):
            progress.progress(i+1)
            i=i+1
                # Find haar cascade to draw bounding box around face
            if webrtc_ctx.video_receiver:
                try:
                    video_frame = webrtc_ctx.video_receiver.get_frame(timeout=10)
                    facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                    gray = cv2.cvtColor(video_frame.to_ndarray(format="bgr24"), cv2.COLOR_BGR2GRAY)
                    faces = facecasc.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)

                    for (x, y, w, h) in faces:
                        #cv2.rectangle(video_frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
                        roi_gray = gray[y:y + h, x:x + w]
                        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
                        cv2.imshow('image',roi_gray)
                    
                except:
                    time.sleep(0.1)
                    continue
nav = st.sidebar.radio("", ["Play Emotify"])
if nav == "Play Emotify":
    emotion_find()

