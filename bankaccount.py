import streamlit as st
from accounts import SavingsAccount, CurrentAccount

st.set_page_config(page_title="Bank Account App", page_icon="🏦", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #b0e2ff;  /* LightSkyBlue1 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style=' color: blue;'>🏦 Bank Account</h1>" ,
    unsafe_allow_html=True
)
st.write("Manage your **Savings** or **Current** account interactively.")




# Session state setup
if "account" not in st.session_state:
    st.session_state.account = None
if "account_type" not in st.session_state:
    st.session_state.account_type = None

# Account creation
with st.form("account_form"):
    st.markdown(
        "<h2 style=' color: blue;'>Create or Load Account</h2>",
        unsafe_allow_html=True
    )
    account_type = st.selectbox("Select account type", ["SavingsAccount", "CurrentAccount"])
    name = st.text_input("Enter your name")
    initial_balance = st.number_input("Initial deposit", min_value=0.0, step=100.0)
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #007bff;
            color: white;
            height: 3em;
            width: 10em;
            border-radius: 10px;
            font-size: 16px;
        }
        </style>
    """, unsafe_allow_html=True)
    submitted = st.form_submit_button("Create Account")

    if submitted:
        if account_type == "SavingsAccount":
            st.session_state.account = SavingsAccount(name, initial_balance)
        else:
            st.session_state.account = CurrentAccount(name, initial_balance)
        st.session_state.account_type = account_type
        st.success(f"{account_type} created for {name} with ₦{initial_balance:.2f}")

# Show account operations if account exists
if st.session_state.account:
    st.divider()
    st.header(f"{st.session_state.account_type} - {st.session_state.account.name}")
    st.subheader(f"💼 Current Balance: ₦{st.session_state.account.balance:.2f}")

    # Deposit➕
    st.subheader("Deposit Funds")
    deposit_amount = st.number_input("Deposit amount", min_value=0.0, step=100.0, key="deposit")
    if st.button("Deposit"):
        result = st.session_state.account.deposit(deposit_amount)
        st.info(result)

    # Withdraw
    st.subheader("➖ Withdraw Funds")
    withdraw_amount = st.number_input("Withdraw amount", min_value=0.0, step=100.0, key="withdraw")
    if st.button("Withdraw"):
        result = st.session_state.account.withdraw(withdraw_amount)
        st.info(result)

    # Refresh balance display
    st.subheader(f"📊 Updated Balance: ₦{st.session_state.account.balance:.2f}")
