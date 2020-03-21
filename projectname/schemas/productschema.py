CREATE_EMPLOYEE_PAYLOAD = {"name": "test", "salary": "123", "age": "23"}


def wrapper_payload():
    def modified_payload(payload, updatepayloaddict):
        if updatepayloaddict:
            for key in updatepayloaddict.keys():
                if key in payload.keys():
                    payload[key] = updatepayloaddict.get(key)
            return payload
        else:
            return payload
    return modified_payload
