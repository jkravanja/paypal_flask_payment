#!/bin/sh

export PAYPAL_MODE=sandbox   # sandbox or live
export PAYPAL_CLIENT_ID=<YOUR_CLIENT_ID>
export PAYPAL_CLIENT_SECRET=<YOUR_CLIENT_SECRET>

./payment.py
