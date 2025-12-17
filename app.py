import streamlit as st
import pandas as pd


def grade(pct: float) -> str:
    if pct >= 90:
        return "A+"
    if pct >= 80:
        return "A"
    if pct >= 70:
        return "B"
    if pct >= 60:
        return "C"
    if pct >= 50:
        return "D"
    return "F"


st.title("Subject Percentage & Grade Calculator")

num = st.number_input("Number of subjects", min_value=1, max_value=50, value=3, step=1)

with st.form("marks_form"):
    st.write("Enter subject names, obtained marks and maximum marks for each subject.")
    subjects = []
    for i in range(int(num)):
        cols = st.columns([2, 1, 1])
        name = cols[0].text_input(f"Subject {i+1} name", value=f"Subject {i+1}", key=f"name_{i}")
        marks = cols[1].number_input(
            "Marks obtained",
            min_value=0.0,
            value=0.0,
            step=1.0,
            key=f"marks_{i}",
        )
        max_marks = cols[2].number_input(
            "Max marks",
            min_value=1.0,
            value=100.0,
            step=1.0,
            key=f"max_{i}",
        )
        subjects.append((name, marks, max_marks))

    submitted = st.form_submit_button("Calculate")

if submitted:
    rows = []
    total_obtained = 0.0
    total_max = 0.0
    for name, marks, maxm in subjects:
        pct = (marks / maxm) * 100 if maxm > 0 else 0.0
        g = grade(pct)
        rows.append({
            "Subject": name,
            "Marks Obtained": marks,
            "Max Marks": maxm,
            "Percentage": round(pct, 2),
            "Grade": g,
        })
        total_obtained += marks
        total_max += maxm

    df = pd.DataFrame(rows)
    st.subheader("Results")
    st.dataframe(df)

    overall_pct = (total_obtained / total_max) * 100 if total_max > 0 else 0.0
    st.markdown(f"**Total Obtained:** {total_obtained} / {total_max}")
    st.markdown(f"**Overall Percentage:** {round(overall_pct,2)}% — **Grade:** {grade(overall_pct)}")

    st.success("Calculation complete.")
