import streamlit as st
import time

st.title("🦈 Sharky Focus Timer")

minutes = st.number_input("Focus Time", 1, 120, 25)

if st.button("Start Timer"):
    placeholder = st.empty()

    for i in range(minutes * 60, 0, -1):
        mins, secs = divmod(i, 60)
        placeholder.write(f"{mins:02d}:{secs:02d}")
        time.sleep(1)

    st.success("Session Complete!")
