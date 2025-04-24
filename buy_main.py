import streamlit as st

st.set_page_config(page_title="צריך לקנות", page_icon="🛒")

# עיצוב בסיסי עם CSS
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 3em;
        color: #2C3E50;
        margin-bottom: 0.2em;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #7F8C8D;
        margin-bottom: 2em;
    }
    .item-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.5em;
        margin-bottom: 0.3em;
        background-color: #F7F9F9;
        border-radius: 10px;
        border: 1px solid #D5DBDB;
    }
    </style>
""", unsafe_allow_html=True)

# כותרת
st.markdown('<div class="title">צריך לקנות 🛍️</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">רשימת הקניות שלך – פשוטה ונוחה</div>', unsafe_allow_html=True)

# רשימת הקניות
if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = []

# הוספת מוצר
with st.form(key='add_item_form'):
    new_item = st.text_input("הוסיפי מוצר חדש:")
    submitted = st.form_submit_button("הוספה")
    if submitted and new_item:
        st.session_state.shopping_list.append(new_item)

# הצגת הרשימה
st.subheader("📝 הרשימה שלך:")

if st.session_state.shopping_list:
    for i, item in enumerate(st.session_state.shopping_list):
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            st.markdown(f'<div class="item-row">{item}</div>', unsafe_allow_html=True)
        with col2:
            if st.button("❌", key=f"delete_{i}"):
                st.session_state.shopping_list.pop(i)
                st.rerun()
else:
    st.info("הרשימה ריקה כרגע. התחילי להוסיף מוצרים 💡")

