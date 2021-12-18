from PIL import Image
import streamlit as st
from PIL import Image
import pandas as pd
import os
add_selectbox = st.sidebar.radio(
    "Select the type of SEARCH METHOD",
    ("SIMILARITY SEARCH Method", "FAISS Method","UPLOAD")
)


if add_selectbox == 'SIMILARITY SEARCH Method' :
	st.title("Similarity Search Method")
	st.write("-------------------------------------------------------------------------------------------------")
	 
	def get_data():
		    return pd.read_csv('/home/mohit/Downloads/Similarity.csv')
	
	n = 1
	df = get_data()
	images = df['0'].unique()
	
	st.subheader("Choose an product from the below dropdown")
	pic = st.selectbox('',images)

	st.image(pic, width=None)

	st.subheader('Choose the number of products to be recomended')
	z = st.slider('', 1, 5, 1)

	st.subheader("Similar Products")
	for index, row in df.iterrows():
		if row['0'] == pic:
			while n < z + 1:
				st.image(row[str(n)], width=100, caption=row[str(n)])
				n += 1



if add_selectbox == 'FAISS Method' :
	st.title("FAISS Method")
	st.write("-------------------------------------------------------------------------------------------------")
		
	def get_data():
		return pd.read_csv('/home/mohit/Downloads/Faiss.csv')
		
	n = 1
	df = get_data()
	images = df['0'].unique()
	
	st.subheader("Choose an product from the below dropdown")
	pic = st.selectbox('',images)

	st.image(pic, width=None)
	

	st.subheader('Choose the number of products to be recomended')
	z = st.slider('', 1, 5, 1)
	print(pic)
	st.subheader("Similar Products")
	for index, row in df.iterrows():
		if row['0'] == pic:
			while n < z + 1:
				st.image(row[str(n)], width=100, caption=row[str(n)])
				n += 1


if add_selectbox == 'UPLOAD' :
    st.title("Upload Image")
    st.write("-------------------------------------------------------------------------------------------------")
    def get_data():
        return pd.read_csv('/home/mohit/Downloads/Faiss.csv')
    n = 1
    df = get_data()
    images = df['0'].unique()
    st.subheader("Upload an image  ")
    try:
        pic = st.file_uploader("Upload file", ["png", "jpg"])
        st.image(pic, width=None)
        
        st.subheader("Choose the number of products to be recomended")
        z = st.slider('', 1, 5, 1)
        
        st.subheader("Similar Products")
        for index, row in df.iterrows():
            if os.path.basename(str(row['0'])) == str(pic.name):         
                while n < z + 1:
                    st.image(row[str(n)], width=100, caption=row[str(n)])
                    n += 1
    except:
        print("Empty File!")
