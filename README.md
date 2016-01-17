# paypal_flask_payment

A PayPal payment example using Flask and PayPal sdk for Python.

First, you'll need to register your PayPal app on (https://developer.paypal.com/). Sign up, log in and navigate to Dashboard->My apps & credentials. Create an app and get your client ID and secret. Copy these and update the payment_vars.sh file.
In payment.py, modify the 'return_url' and 'cancel_url' to include domain or IP of your server. Now run payment_vars.sh.

In a browser, initiate payment procedure with '/pay' link. This should create a test payment and redirect you to PayPal for confirmation. After a successful payment, you will be redirected to 'return_url', which is set to '/success'. In case of failure you will be redirected to '/failure'.
