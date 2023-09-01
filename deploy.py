import streamlit as st
import requests
import streamlit_lottie as stl
import joblib
import numpy as np

st.set_page_config(page_title='Mall Customer Segmentation', page_icon='::magnifying_glass::',
    layout="wide",
    initial_sidebar_state="expanded")




def get_values(age,income,score):
    list = [age,income,score]
    vals = np.array(list).reshape(-1,len(list))
    return vals


def clusterDef(pred,Age):
    

     if pred[0] == 0:
          st.write('''These customers are likely to be middle-class families with a moderate income. They may be looking for a good value for their money. Here are some marketing ideas for this class:

* Offer a variety of products and services to meet their needs.
* Provide clear and concise information about your products and services.
* Offer competitive prices and discounts.
* Make it easy for customers to find what they are looking for.''')
     if pred[0] == 1:
          st.write('''These customers are likely to be affluent individuals who are willing to spend money on luxury items. They may be looking for the latest trends and the best quality products. Here are some marketing ideas for this class:

* Offer high-end products and services.
* Create a sense of exclusivity by offering limited-edition items or VIP treatment.
* Partner with luxury brands or retailers.
* Host events and experiences that appeal to this group.''')
     if pred[0] == 2:
            if Age < 27:
                st.write('''These customers are likely to be young and just starting out in their careers. They may be on a tight budget and not have a lot of disposable income. Here are some marketing ideas for this class:

* Offer discounts and promotions on affordable items.
* Host events and workshops that are free or low-cost.
* Partner with local businesses to offer discounts or special offers.
* Create a loyalty program that rewards customers for their spending.''')
            else:
                st.write('''These customers are likely to be lower class individuals with a poor financial status. They may be on a tight budget and not have a lot of disposable income. Here are some marketing ideas for this class:

* Offer discounts and promotions on affordable items.
* Host events and workshops that are free or low-cost.
* Partner with local businesses to offer discounts or special offers.
* Create a loyalty program that rewards customers for their spending.''')
                

     if pred[0] == 3:
        if Age < 27:
            st.write('''These customers may be students or young professionals who are passionate about fashion or beauty. They may be willing to spend more money on items that they love. Here are some marketing ideas for this class:

* Create a sense of urgency by offering limited-time sales and promotions.
* Highlight the unique features and benefits of your products.
* Use social media to connect with this group and share fashion and beauty inspiration.
* Partner with influencers who are popular with this demographic.''')
        else:
            st.write('''These customers may be someone who is generous with their time and money. They may be willing to spend more money on items that they love. Here are some marketing ideas for this class:

* Create a sense of urgency by offering limited-time sales and promotions.
* Highlight the unique features and benefits of your products.
* Use social media to connect with this group and share fashion and beauty inspiration.
* Partner with influencers who are popular with this demographic.''')
     if pred[0] == 4:
          st.write('''These customers may be wealthy individuals who are not interested in spending a lot of money on clothes or beauty products. They may be more interested in experiences or services. Here are some marketing ideas for this class:

* Offer exclusive experiences or services.
* Personalize your marketing messages to appeal to this group.
* Focus on the quality and craftsmanship of your products.
* Highlight the benefits of your products and services, such as convenience or time savings.''')



loaded_model = joblib.load(open("Mall Customer Segmentation Model", 'rb'))

 
with st.container():
    
    left_column,right_column = st.columns(2)


    with left_column:
         
                    st.markdown("<h1 style='text-align: center;'>Understand Your Customers Better</h1>", unsafe_allow_html=True)
##st.markdown("<h3 style='text-align: center:'> By understanding your customer's needs and preferences, you can create a more personalized and relevant customer experience.</h3>", unsafe_allow_html=True)
                    st.write('''
                                 By understanding your customer's needs and preferences, you can create a more personalized and relevant customer experience.
                 ''')

         
    
    with right_column:
         lottie_url = "https://lottie.host/42dcafd6-714f-4406-9398-f1d5704f33ba/Y7reWlNnWr.json"

         stl.st_lottie(lottie_url)
        
        



st.write('---')
st.subheader('Enter Customer Details : ')

with st.container():
    
    right_column, left_column = st.columns(2)


    with left_column:
        Score = st.slider('Select Spending Score', 1, 100)
        AnnualIncome = st.number_input('Annual Income (k$)', 1, 5000)

        
         
    
    with right_column:
        
        gender = st.radio('Gender : ', ['Female', 'Male'])
        Age = st.number_input('Age : ', min_value=18, max_value=100, value=18, step=1)

        

        
        








data = get_values(Age,AnnualIncome,Score)


if st.button('Discover the insights'):
            pred_Y = loaded_model.predict(data)

            
            clusterDef(pred_Y,Age)







