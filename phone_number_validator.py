import streamlit as st
import requests

st.set_page_config(page_title="Phone Number Validator", layout="centered")
st.title("📱 Phone Number Validator with NumVerify")

# Input: API Key and Phone Number
api_key = st.text_input("Enter your NumVerify API Key", type="password")
phone_number = st.text_input("Enter a phone number (e.g. +14158586273)")

if st.button("Validate"):
    if not api_key or not phone_number:
        st.warning("Please provide both an API key and a phone number.")
    else:
        with st.spinner("Validating..."):
            url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
            try:
                response = requests.get(url)
                data = response.json()

                if "error" in data:
                    st.error(f"API Error: {data['error']['info']}")
                else:
                    st.success("Phone number validated successfully!")
                    st.write("### Result:")
                    st.write({
                        "Valid": data.get("valid"),
                        "Country": data.get("country_name"),
                        "Carrier": data.get("carrier"),
                        "Line Type": data.get("line_type"),
                        "Location": data.get("location")
                    })
            except Exception as e:
                st.error(f"Request failed: {e}")
