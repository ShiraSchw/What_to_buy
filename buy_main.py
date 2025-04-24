import streamlit as st

# כותרת
st.title("🛒 צריך לקנות")

# שימוש ב-session_state לשמירת הרשימה
if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = []

# טופס להוספת מוצר
with st.form(key='add_item_form'):
    new_item = st.text_input("הוסיפי מוצר חדש:")
    submitted = st.form_submit_button("הוספה")
    if submitted and new_item:
        st.session_state.shopping_list.append(new_item)

# הצגת הרשימה הנוכחית עם כפתורי מחיקה
st.subheader("רשימת הקניות:")
for i, item in enumerate(st.session_state.shopping_list):
    col1, col2 = st.columns([0.85, 0.15])
    col1.write(f"- {item}")
    if col2.button("❌", key=f"delete_{i}"):
        st.session_state.shopping_list.pop(i)
        st.rerun()