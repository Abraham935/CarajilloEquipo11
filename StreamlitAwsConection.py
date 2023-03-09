import streamlit as st
import pandas as pd
from io import StringIO
import boto3

config = {
    'aws_access_key_id': '',
    'aws_secret_access_key': '',
    'region_name': 'us-east-1'
}

client = boto3.client('s3', aws_access_key_id=config['aws_access_key_id'], 
                      aws_secret_access_key=config['aws_secret_access_key'], 
                      region_name=config['region_name'])

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

    file_name = uploaded_file.name

    #ACL='public-read' makes the file public
    client.put_object(Bucket='autentico-corajillo', Key=file_name, Body=bytes_data)
    st.write(f"{file_name} uploaded to S3 bucket!")