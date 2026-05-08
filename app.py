import streamlit as st
import time

st.title("🦈 Sharky Focus Timer")

st.write("Sharky says: small progress is still progress.")

# Work inputs
work_hours = st.number_input(
    "Enter work hours",
    min_value=0,
    max_value=24,
    value=0
)

work_minutes = st.number_input(
    "Enter work minutes",
    min_value=0,
    max_value=59,
    value=25
)

# Break inputs
break_hours = st.number_input(
    "Enter break hours",
    min_value=0,
    max_value=24,
    value=0
)

break_minutes = st.number_input(
    "Enter break minutes",
    min_value=0,
    max_value=59,
    value=5
)

# Convert to seconds
work_time = (work_hours * 3600) + (work_minutes * 60)
break_time = (break_hours * 3600) + (break_minutes * 60)

if st.button("Start Sharky Timer"):

    st.subheader("💻 Work Time!")

    timer = st.empty()

    for i in range(work_time, 0, -1):
        hours = i // 3600
        minutes = (i % 3600) // 60
        seconds = i % 60

        timer.write(f"⏳ {hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    st.success("🎉 Work session complete!")

    st.subheader("☕ Break Time!")

    break_timer = st.empty()

    for i in range(break_time, 0, -1):
        hours = i // 3600
        minutes = (i % 3600) // 60
        seconds = i % 60

        break_timer.write(f"🛌 {hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    st.success("🦈 Sharky is proud of you.")
