import streamlit as st

st.set_page_config(page_title="צריך לקנות", layout="centered", page_icon="🛒")

# --- עיצוב כללי ---
st.markdown("""
    <style>
        body {
            background-color: #0f172a;
            color: #f8fafc;
            font-family: 'Varela Round', sans-serif;
        }
        .title {
            font-size: 3em;
            margin-bottom: 0.5em;
            text-align: center;
            color: #facc15;
        }
        .logo {
            position: absolute;
            top: 1rem;
            right: 1.5rem;
            font-size: 1.5rem;
            font-weight: bold;
            color: #38bdf8;
        }
        .product-card {
            background-color: #1e293b;
            padding: 1rem;
            border-radius: 1rem;
            margin-bottom: 0.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .add-form input, .add-form button {
            border-radius: 1rem;
            padding: 0.75rem;
            font-size: 1rem;
            margin: 0.25rem;
        }
        .add-form button {
            background-color: #22c55e;
            color: white;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='logo'>צריך לקנות</div>", unsafe_allow_html=True)
st.markdown("<div class='title'>🛒 רשימת הקניות</div>", unsafe_allow_html=True)

# --- רשימת קניות התחלתית ---
if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = [
        {"item": "עגבניות", "qty": 2},
        {"item": "עוף", "qty": 1},
        {"item": "פלפלים", "qty": 3},
    ]

# --- הצגת פריטים ---
for i, entry in enumerate(st.session_state.shopping_list):
    with st.container():
        st.markdown(f"""
            <div class='product-card'>
                <span>{entry['qty']} × {entry['item']}</span>
                <form action="" method="post">
                    <button name="remove" type="submit" formaction="/?remove={i}" style="background: none; border: none; color: #f87171; font-size: 1rem;">❌</button>
                </form>
            </div>
        """, unsafe_allow_html=True)

# --- מחיקת פריט דרך קישור ---
query_params = st.query_params
remove_index = query_params.get("remove")
if remove_index:
    try:
        del st.session_state.shopping_list[int(remove_index[0])]
        st.query_params.clear()  # מחיקת הפרמטר מה-URL
        st.rerun()
    except:
        pass

# --- טופס הוספה ---
st.markdown("<div class='add-form'>", unsafe_allow_html=True)
with st.form(key="add_form"):
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        item = st.text_input("שם המוצר", label_visibility="collapsed")
    with col2:
        qty = st.number_input("כמות", min_value=1, step=1, label_visibility="collapsed")
    with col3:
        submitted = st.form_submit_button("הוסף")
    if submitted and item:
        st.session_state.shopping_list.append({"item": item.strip(), "qty": qty})
        st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# --- לינק לפונט ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Varela+Round&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)
