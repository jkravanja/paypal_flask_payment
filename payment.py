#!/usr/bin/python

from flask import Flask, redirect, request
import paypalrestsdk

app = Flask(__name__)

@app.route("/test")
def test():
	return "Test"

@app.route("/pay")
def pay():

	payment = paypalrestsdk.Payment({
	  "intent": "sale",
	  "payer": {
	    "payment_method": "paypal" },
	  "redirect_urls": {
	    "return_url": "http://<YOUR_DOMAIN_OR_IP>:5050/success",
	    "cancel_url": "http://<YOUR_DOMAIN_OR_IP>:5050/failure" },

	  "transactions": [ {
	    "amount": {
	      "total": "12",
	      "currency": "USD" },
	    "description": "creating a payment" } ] } )

	payment.create()
	return redirect(payment['links'][1]['href'])


@app.route("/success")
def success():

	paymentId = request.args.get('paymentId')
	PayerID = request.args.get('PayerID')
	token = request.args.get('token')

	payment = paypalrestsdk.Payment.find(paymentId)
	if payment.execute({"payer_id": PayerID}):
		return "OK <br/> paymentId: {} <br/> PayerID: {} <br/>".format(
					            	     paymentId,PayerID)
	else:
		return(payment.error) # Error Hash
	

@app.route("/failure")
def failure():

	token = request.args.get('token')
	return "Failed"


if __name__ == "__main__":
    app.run(port=5050,host="0.0.0.0",debug=True)
