# import streamlit as st
# from auth_utils import register_user, login_user
# from models import get_all_products
# from cart import initialize_cart, add_to_cart, view_cart
# from admin import admin_panel
# from history import view_order_history

# import base64
# st.set_page_config(page_title="MyShop", layout="wide")
# initialize_cart()

# # Scrolling banner
# st.markdown(
    # """
    # <style>
    # .marquee {
      # width: 100%;
      # overflow: hidden;
      # white-space: nowrap;
      # box-sizing: border-box;
      # animation: marquee 10s linear infinite;
      # font-size: 24px;
      # font-weight: bold;
      # color: #007BFF;
      # padding: 10px 0;
      # background-color: #f0f2f6;
    # }

    # @keyframes marquee {
      # 0%   { transform: translateX(100%); }
      # 100% { transform: translateX(-100%); }
    # }
    # </style>

    # <div class="marquee">
      # Welcome to Online Shopping
    # </div>
    # """,
    # unsafe_allow_html=True
# )

# # Background color
# def set_bg_color(color_hex="#f0f2f6"):
    # st.markdown(
        # f"""
        # <style>
        # .stApp {{
            # background-color: {color_hex};
        # }}
        # </style>
        # """,
        # unsafe_allow_html=True
    # )

# set_bg_color("#D5D6EA") 

# # Session state setup
# if "user" not in st.session_state:
    # st.session_state.user = None

# def logout():
    # st.session_state.user = None
    # st.success("Logged out successfully!")

# # Sidebar menu
# if st.session_state.user:
    # options = ["Shop", "Cart", "Logout"]
    # if st.session_state.user.get("is_admin"):
        # options.append("Admin")
    # menu = st.sidebar.selectbox("Menu", options)
# else:
    # menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

# # User auth pages
# if menu == "Register":
    # st.subheader("📝 Create New Account")
    # with st.form("register_form"):
        # uname = st.text_input("Username")
        # pwd = st.text_input("Password", type="password")
        # submit = st.form_submit_button("Register")
        # if submit:
            # msg = register_user(uname, pwd)
            # if msg == "Success":
                # st.success("Account created! Please login.")
            # else:
                # st.error(msg)

# elif menu == "Login":
    # st.subheader("🔐 Login to Your Account")
    # with st.form("login_form"):
        # uname = st.text_input("Username")
        # pwd = st.text_input("Password", type="password")
        # submit = st.form_submit_button("Login")
        # if submit:
            # user = login_user(uname, pwd)
            # if user:
                # st.session_state.user = user
                # st.success(f"Welcome, {user['username']}!")
                # st.rerun()
            # else:
                # st.error("Incorrect Username or Password")

# elif menu == "Logout":
    # logout()
    # st.experimental_rerun()

# # Shop Page
# elif menu == "Shop":
    # st.title("🛒 Shop Now")
    # col1, col2 = st.columns([2, 3])

    # with col1:
        # keyword = st.text_input("🔍 Search by product name", key="search_keyword")

    # with col2:
        # st.write("📂 Category")
        # category_options = ["All", "Electronics", "Fashion", "Books", "Home"]
        # selected_category = st.radio("", category_options, horizontal=True, key="selected_category")

    # category_filter = None if selected_category == "All" else selected_category
    # products = get_all_products(category_filter, keyword if keyword else None)

    # for product in products:
        # col_img, col_info, col_btn = st.columns([1, 3, 1])
        # with col_img:
            # if product['image_url']:
                # st.image(product['image_url'], width=100)
        # with col_info:
            # st.subheader(product['name'])
            # st.write(f"Category: {product['category']}")
            # st.write(f"Price: ₹{product['price']}")
            # st.write(f"Stock: {product['stock']}")
        # with col_btn:
            # if st.button(f"Add to Cart", key=product['product_id']):
                # add_to_cart(product)

# # Cart Page
# elif menu == "Cart":
    # if not st.session_state.user:
        # st.warning("Please login to view your cart.")
    # else:
        # view_cart()

# # Admin Page
# elif menu == "Admin":
    # if st.session_state.user and st.session_state.user.get("is_admin"):
        # admin_panel()
    # else:
        # st.error("Admin access only. Please login as admin.")

# # Order History
# if st.sidebar.button("📜 Order History"):
    # view_order_history()
    
    
    
import streamlit as st
from auth_utils import register_user, login_user

st.title("🛍️ Shop Login System")

menu = st.sidebar.selectbox("Choose Action", ["Login", "Register"])

if menu == "Register":
    st.header("📝 Create New Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        result = register_user(username, password)
        st.success(result) if result == "Success" else st.error(result)

elif menu == "Login":
    st.header("🔐 Login to Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.success(f"Welcome {user['username']} (Admin: {user['is_admin']})")
        else:
            st.error("Invalid credentials")


