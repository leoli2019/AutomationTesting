import requests


def register_user(email, first_name, last_name, password, url_register_user):
    headers = {'Content-Type': "application/json", }
    payload = {"email": email,
               "firstName": first_name,
               "lastName": last_name,
               "credentials": [{"value": password}]}

    response = requests.request("POST", url_register_user, json=payload, headers=headers)

    return response


def activate_account(activate_code, user_id, url):
    querystring = {"activateCode": activate_code, "id": user_id}
    headers = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def get_token(username, password, url_get_token):
    headers = {'Content-Type': "application/json", }
    payload = {"userName": username, "password": password}
    response = requests.request("POST", url_get_token, json=payload, headers=headers)
    # Save it to a list, as the result will included multiple info
    token = response.text
    return token


def get_user_profile(url_user_profile, token):
    headers = {'Content-Type': "application/json", 'Authorization': "Bearer " + token}
    # ========== This payload was used by "Wallet ID" and "Order ID" ==========
    payload = {"order": {
        "lineItemInOrderList": [{
            "product": {"id": 1},
            "quantity": 2,
            "ledgerLineItemOrder": {"id": 1}}],
        "shippingAddress": {
            "province": {"code": "QC"},
            "country": {"code": "CA"},
            "address1": "1625 Maisonneuve",
            "address2": "",
            "city": "Montreal",
            "zip": "H3A",
            "phone": 5141231234,
            "firstName": "Ting",
            "lastName": "Yu",
            "note": "note",
            "isDefault": False}},
        "shopId": 403}
    response = requests.request("GET", url_user_profile, json=payload, headers=headers)
    result = response.text
    return result


def get_order_id(url_order_creat, token):
    headers = {'Content-Type': "application/json", 'Authorization': "Bearer " + token}
    # ========== This payload was used by "Wallet ID" and "Order ID" ==========
    payload = {"order": {
        "lineItemInOrderList": [{
            "product": {"id": 1},
            "quantity": 2,
            "ledgerLineItemOrder": {"id": 1}}],
        "shippingAddress": {
            "province": {"code": "QC"},
            "country": {"code": "CA"},
            "address1": "1625 Maisonneuve",
            "address2": "",
            "city": "Montreal",
            "zip": "H3A",
            "phone": 5141231234,
            "firstName": "Ting",
            "lastName": "Yu",
            "note": "note",
            "isDefault": False}},
        "shopId": 403}
    response = requests.request("POST", url_order_creat, json=payload, headers=headers)
    result = response.text
    return result


def pay_to_ledger(order_id, subtotal, wallet_id, ledger_ip, payment_type, url_pay2ladger, token):
    headers = {'Content-Type': "application/json", 'Authorization': "Bearer " + token}
    payload = {"orderId": order_id,
               "subtotal": subtotal,
               "walletAddress": wallet_id,
               "ledgerIp": ledger_ip,
               "paymentType": payment_type
               }
    response = requests.request("POST", url_pay2ladger, json=payload, headers=headers)
    result = response.text
    return result


def upload_submit_task(web_con, task_file_path, task_name, order_id, ledger_ip, task_id, url, token, boundary):
    headers = {'content-type': "multipart/form-data; boundary=----" + boundary,
               'Authorization': "Bearer " + token}
    payload = (
            "------" + web_con + "name=\"data\"; filename=" + task_file_path +
            "\r\nContent-Type: application/zip\r\n\r\n\r\n"
            "------" + web_con + "name=\"duration\"\r\n\r\n3600\r\n"
                                 "------" + web_con + "name=\"taskName\"\r\n\r\n" + task_name + "\r\n"
                                                                                                "------" + web_con + "name=\"Id\"\r\n\r\n" + order_id + "\r\n"
                                                                                                                                                        "------" + web_con + "name=\"gpu_count\"\r\n\r\n1\r\n"
                                                                                                                                                                             "------" + web_con + "name=\"ledger_ip\"\r\n\r\n" + ledger_ip + "\r\n"
                                                                                                                                                                                                                                             "------" + web_con + "name=\"task_id\"\r\n\r\n" + task_id + "\r\n"
                                                                                                                                                                                                                                                                                                         "------" + web_con + "name=\"unit_fee\"\r\n\r\n500000000000000000\r\n"
                                                                                                                                                                                                                                                                                                                              "------" + boundary + "--")
    response = requests.request("POST", url, data=payload, headers=headers)
    # result = response.text
    # return result

    return response
