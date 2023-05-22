import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(layout='wide')

st.title('Loan Application Modelling')

df_bernoulli = pd.read_csv("bernoulli-accuracy.csv")  
df_rf = pd.read_csv("rf-accuracy.csv")  
df_bernoulli_tuned = pd.read_csv("bernoulli-accuracy-tuned.csv")  
df_rf_tuned = pd.read_csv("rf-accuracy-tuned.csv")  
df_tuned = pd.read_csv("tuned-results.csv")  

st.write('For the Loan Application Modelling, we have used Clustering and Classification to predict the approval of the loan application. For the prediction, we have used K-Means Clustering and incorporated the results with either one of the classification model which is Bernoulli Naive Bayes and Random Forest.')

st.markdown('#')
st.markdown('**Before Hyperparameter Tuning**')

st.write('Choose the preferred k-value and classification model to assess the efficacy of the models.')

k_val = st.selectbox("Select a k-value for K-Means Clustering", options=[2, 3, 4])

class_choice = st.selectbox("Select a classification model for Classification", ['Bernoulli Naive Bayes', 'Random Forest'])

if st.button('Submit'):
    if class_choice == 'Bernoulli Naive Bayes':
        if k_val == df_bernoulli['k-value'][0]: 
            st.write('Accuracy: ', df_bernoulli['accuracy'][0])
        if k_val == df_bernoulli['k-value'][1]: 
            st.write('Accuracy: ', df_bernoulli['accuracy'][1])
        if k_val == df_bernoulli['k-value'][2]: 
            st.write('Accuracy: ', df_bernoulli['accuracy'][2])
    else:
        if k_val == df_rf['k-value'][0]: 
            st.write('Accuracy: ', df_rf['accuracy'][0])
        if k_val == df_rf['k-value'][1]: 
            st.write('Accuracy: ', df_rf['accuracy'][1])
        if k_val == df_rf['k-value'][2]: 
            st.write('Accuracy: ', df_rf['accuracy'][2])

st.markdown('#')
st.markdown('**After Hyperparameter Tuning**')

st.write('Choose the preferred k-value and classification model to assess the efficacy of the models.')

k_val_tuned = st.selectbox("Select a k-value for K-Means Clustering", options=[2, 3, 4], key=2)

class_choice_tuned = st.selectbox("Select a classification model for Classification", ['Bernoulli Naive Bayes', 'Random Forest'], key=2)

if st.button('Submit', key=2):
    if class_choice_tuned == 'Bernoulli Naive Bayes':
        if k_val_tuned == df_bernoulli_tuned['k-value'][0]: 
            st.write('Accuracy: ', df_bernoulli_tuned['accuracy'][0])
        if k_val_tuned == df_bernoulli_tuned['k-value'][1]: 
            st.write('Accuracy: ', df_bernoulli_tuned['accuracy'][1])
        if k_val_tuned == df_bernoulli_tuned['k-value'][2]: 
            st.write('Accuracy: ', df_bernoulli_tuned['accuracy'][2])
    else:
        if k_val_tuned == df_rf_tuned['k-value'][0]: 
            st.write('Accuracy: ', df_rf_tuned['accuracy'][0])
        if k_val_tuned == df_rf_tuned['k-value'][1]: 
            st.write('Accuracy: ', df_rf_tuned['accuracy'][1])
        if k_val_tuned == df_rf_tuned['k-value'][2]: 
            st.write('Accuracy: ', df_rf_tuned['accuracy'][2])

st.markdown('#')
st.markdown('**Data Visualization for Model Before Hyperparameter Tuning**')

st.write('Summary of Bernoulli Naive Bayes with different k-values for K-Means Clustering:')
st.write(df_bernoulli)
st.bar_chart(df_bernoulli['accuracy'])

st.write('Summary of Random Forest with different k-values for K-Means Clustering:')
st.write(df_rf)
st.bar_chart(df_rf['accuracy'])

st.write('Based on the results above, we can conclude that Bernoulli Naive Bayes with k-value of 3 performs the best overall with an accuracy of 78%.')

st.markdown('#')
st.markdown('**Data Visualization for Model After Hyperparameter Tuning**')

st.write(df_tuned)
st.bar_chart(df_tuned['accuracy'])

st.write('Overall, it can be seen that K-Means Clustering with a k-value of 3 and Bernoulli Naive Bayes classifier with alpha value of 10 produces the highest accuracy of 78%.')