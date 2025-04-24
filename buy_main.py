import streamlit as st

st.set_page_config(page_title="צריך לקנות", page_icon="🛒", layout="centered")

# עיצוב כהה עם גופן יפה
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;600&display=swap');

    html, body, [class*="css"]  {
        background-color: #121212;
        color: #ffffff;
        font-family: 'Assistant', sans-serif;
    }

    .title {
        text-align: center;
        font-size: 3em;
        color: #FFB74D;
        margin-top: 0.5em;
        margin-bottom: 0.2em;
    }

    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #B0BEC5;
        margin-bottom: 2em;
    }

    .item-row {
        background-color: #1E1E1E;
        padding: 0.6em 1em;
        border-radius: 10px;
        margin-bottom: 0.4em;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid #333;
    }

    .stTextInput > div > input {
        background-color: #2C2C2C;
        color: white;
    }

    .stButton button {
        background-color: #FFB74D;
        color: black;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# כותרות
st.markdown('<div class="title">צריך לקנות 🛍️</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">רשימת קניות יפיפייה באווירה לילית</div>', unsafe_allow_html=True)

# התחלת רשימה
if "shopping_list" not in st.session_state:
    st.session_state.shopping_list = []

# טופס להוספת מוצר
with st.form(key="add_form"):
    new_item = st.text_input("הוסיפי מוצר חדש:")
    add_btn = st.form_submit_button("הוספה")
    if add_btn and new_item.strip():
        st.session_state.shopping_list.append(new_item.strip())
        st.rerun()

# רשימת קניות
st.subheader("📋 הרשימה שלך:")
if st.session_state.shopping_list:
    for i, item in enumerate(st.session_state.shopping_list):
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            st.markdown(f'<div class="item-row">{item}</div>', unsafe_allow_html=True)
        with col2:
            if st.button("🗑️", key=f"delete_{i}"):
                st.session_state.shopping_list.pop(i)
                st.rerun()
else:
    st.info("הרשימה ריקה כרגע. הוסיפי משהו 😊")

