import streamlit as st
import joblib
import pandas as pd
clf = joblib.load('recommendation_model.pkl')
# Define the manual encoding mapping
replace_dict = {"Vanilla": 0,"Chocolate": 1,"Lemon": 2,"Strawberry": 3
               ,"Butterscotch":4,"Blackcurrent":5,"Mango":6,"American Nuts":7,"Lemon":8,"Mint":9,
               "Sprinkles":11,"Chocolate syrup":22,"Nuts (lol)":33,"Fruits":44,"Others":55,
               "Aries":501,"Taurus":502,"Gemini":503,"Cancer":504,"Leo":505,"Virgo":506,"Libra":507,"Scorpio":508,"Sagittarius":509,"Capricorn":510,"Aquarius":511,"Pisces":512,"idk my zodiac sign bro":513
}
# Inverse the replace_dict for decoding
inverse_replace_dict = {v: k for k, v in replace_dict.items()}
st.markdown(
        f"""
        <style>
        .stApp {{ 
            background-image:url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGtO9p_I5nuUVMBkNfnL-1SOpDCySSI6a7tA&usqp=CAU");
            background-attachment: fixed;
            background-size: cover
        }}
        .sidebar {{
            background-image: linear-gradient(#2e7bcf,#2e7bcf);
        }}    
        </style>
        """,
        unsafe_allow_html=True
)
st.title("Ice Cream Flavor Recommender") 
# User inputs
user_age = st.number_input("Enter your age", min_value=1)
user_gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])  # Use actual labels here
user_topping = st.selectbox("Which ice cream topping do you enjoy the most?", list(inverse_replace_dict.values())[10:15])  # Topping options from the inverse mapping
user_zodiac = st.selectbox("What's your zodiac sign?", list(inverse_replace_dict.values())[14:26])  # Zodiac options from the inverse mapping

st.sidebar.title("Ice Cream")
st.sidebar.title("Menu")
st.sidebar.write("Welcome to the Ice Cream Flavor Recommender.")
st.sidebar.write("Age:" ) 
st.sidebar.write("0-10: 0")
st.sidebar.write ("10-15: 1")
st.sidebar.write("15-20: 2")
st.sidebar.write("20-25: 3")
st.sidebar.write("25-30: 4")
st.sidebar.write( "35+: 5")
                  
                 

# Recommendation function
def get_recommendation(age, gender, topping, zodiac, model):
    encoded_topping = replace_dict[topping]
    encoded_zodiac = replace_dict[zodiac]
    gender_mapping = {"Male": 0, "Female": 1, "Other": 2}
    encoded_gender = gender_mapping[gender]
    
    user_data = [age, encoded_gender, encoded_topping, encoded_zodiac]  
    

    recommended_flavor_encoded = model.predict([user_data])[0]
    recommended_flavor = inverse_replace_dict[recommended_flavor_encoded]
    return recommended_flavor

if st.button("Get Ice Cream Recommendation"):
    recommendation=get_recommendation(user_age,user_gender,user_topping,user_zodiac,clf)
    
    st.write(f"Recommended Ice Cream Flavor: {recommendation}")