import frappe
import requests
import json

@frappe.whitelist()
def make_payment():
    api_url = "https://api.flutterwave.com/v3/payments"
    secret_key = "FLWSECK_TEST-589bade24114ff287746782b71b2b9db-X"
    headers = {"Authorization": f"Bearer {secret_key}"}
    payload = {
        "tx_ref": "hooli-tx-1920bbtytty",
        "amount": "1",
        "currency": "ZMW",
        "redirect_url": "https://webhook.site/9d0b00ba-9a69-44fa-a43d-a82c33c36fdc",
        "meta": {
            "consumer_id": 23,
            "consumer_mac": "92a3-912ba-1192a"
        },
        "customer": {
            "email": "chipohameja@gmail.com",
            "phonenumber": "+260770993633",
            "name": "Chipo Hameja"
        },
        "custo/home/frappe/frappe-bench/apps/hrmsmizations": {
            "title": "Pied Piper Payments",
            "logo": "http://www.piedpiper.com/app/themes/joystick-v27/images/logo.png"
        }
    }

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()
    #frappe.errprint(json.dumps(payload))
    #frappe.errprint(payload)
    #return payload