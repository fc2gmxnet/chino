# whatsapp_app.py
# to run in the same browser window as the whatsapp web is running

import streamlit as st
import pywhatkit as kit
import random

st.title("📱 WhatsApp Message Scheduler")

# User inputs
phone_number = st.text_input("Recipient's number (with country code, e.g., +5511900000000)")
message = st.text_area("Your message")
time_input = st.time_input("Send time (hh:mm)")

# Button to send
if st.button("Schedule Message"):
    if phone_number and message:
        hour = time_input.hour
        minute = time_input.minute
        try:
            kit.sendwhatmsg(phone_number, message, hour, minute, 
                # tab_close=True, # it does not work well
                wait_time=random.randint(8, 20)   # optional
                )
            st.success(f"Message scheduled to {phone_number} at {hour:02d}:{minute:02d}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in all fields before scheduling.")
