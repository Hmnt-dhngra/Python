import streamlit as st

st.title('Streamlit text input ')

name=st.text_input('Enter your name : ')
if name: 
    st.write(f"Hello {name}")

age = st.slider('Select your age', 0,100,25) ## here 25 is used to indicative what the predefined input will be on the slider. 
st.write(f"Your age is  {age}")

options = ['Python', 'SQL', 'PyQt5', 'AWS']
choice = st.selectbox(f'Choose what you are most confident in:' , options)
st.write(f"Interesting, you are most confident in {choice} !")


uploaded_file = st.file_uploader('Choose a csv file', type ='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

## streamlit.io