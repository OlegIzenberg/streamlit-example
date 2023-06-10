import pickle
import streamlit as st
import pandas as pd
from PIL import Image
model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


def main():

	image = Image.open('images/icone.png')
	image2 = Image.open('images/image.png')
	st.image(image,use_column_width=False)
	add_selectbox = st.sidebar.selectbox(
	"How would you like to predict?",
	("Online", "Batch"))
	st.sidebar.info('This app is created to predict Churn')
	st.sidebar.image(image2)
	st.title("Predicting Churn")
	if add_selectbox == 'Online':
		gender = st.selectbox('Gender:', ['male', 'female'])
		seniorcitizen= st.selectbox(' Customer is a senior citizen:', [0, 1])
		status = st.selectbox(' Customer has a partner:', ['yes', 'no'])
		dependents = st.selectbox(' Customer has  dependents:', ['yes', 'no'])
		phoneservice = st.selectbox(' Customer has phoneservice:', ['yes', 'no'])
		multiplelines = st.selectbox(' Customer has multiplelines:', ['yes', 'no', 'no_phone_service'])
		internetservice= st.selectbox(' Customer has internetservice:', ['dsl', 'no', 'fiber_optic'])
		security = st.selectbox(' Customer has onlinesecurity:', ['yes', 'no', 'no_internet_service'])
		backup = st.selectbox(' Customer has onlinebackup:', ['yes', 'no', 'no_internet_service'])
		protection = st.selectbox(' Customer has deviceprotection:', ['yes', 'no', 'no_internet_service'])
		support = st.selectbox(' Customer has techsupport:', ['yes', 'no', 'no_internet_service'])
		streamingtv = st.selectbox(' Customer has streamingtv:', ['yes', 'no', 'no_internet_service'])
		streamingmovies = st.selectbox(' Customer has streamingmovies:', ['yes', 'no', 'no_internet_service'])
		contracttype = st.selectbox(' Customer has a contract:', ['month-to-month', 'one_year', 'two_year'])
		emailbilling  = st.selectbox(' Customer has a paperlessbilling:', ['yes', 'no'])
		paymentmethod = st.selectbox('Payment Option:', ['bank_transfer_(automatic)', 'credit_card_(automatic)', 'electronic_check' ,'mailed_check'])
		loyaltyperiod = st.number_input('Number of months the customer has been with the current telco provider :', min_value=0, max_value=240, value=0)
		monthlycharges= st.number_input('Monthly charges :', min_value=0, max_value=240, value=0)
		totalcharges = loyaltyperiod*monthlycharges
		numadmintickets = st.number_input('Number of admin tickets opened:', min_value=0, max_value=5, value=0)
		numtechtickets = st.number_input('Number of tech tickets opened:', min_value=0, max_value=9, value=0)
		output= ""
		output_prob = ""
		input_dict={
				"gender":gender ,
				"seniorcitizen": seniorcitizen,
				"status": partner,
				"dependents": dependents,
				"phoneservice": phoneservice,
				"multiplelines": multiplelines,
				"internetservice": internetservice,
				"security": onlinesecurity,
				"backup": onlinebackup,
				"protection": deviceprotection,
				"support": techsupport,
				"streamingtv": streamingtv,
				"streamingmovies": streamingmovies,
				"contracttype": contract,
				"emailbilling": paperlessbilling,
				"paymentmethod": paymentmethod,
				"loyaltyperiod": tenure,
				"monthlycharges": monthlycharges,
				"totalcharges": totalcharges,
			    "numadmintickets": numadmintickets,
			    "numtechtickets": numtechtickets

			}

		if st.button("Predict"):
			X = dv.transform([input_dict])
			y_pred = model.predict_proba(X)[0, 1]
			churn = y_pred >= 0.5
			output_prob = float(y_pred)
			output = bool(churn)
		st.success('Churn: {0}, Risk Score: {1}'.format(output, output_prob))
	if add_selectbox == 'Batch':
		file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
		if file_upload is not None:
			data = pd.read_csv(file_upload)
			X = dv.transform([data])
			y_pred = model.predict_proba(X)[0, 1]
			churn = y_pred >= 0.5
			churn = bool(churn)
			st.write(churn)

if __name__ == '__main__':
	main()