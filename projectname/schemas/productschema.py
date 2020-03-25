CREATE_EMPLOYEE_PAYLOAD = {"name": "test", "salary": "123", "age": "23"}

# def wrapper_payload():
#     def modified_payload(payload, updatepayloaddict):
#         if updatepayloaddict:
#             for key in updatepayloaddict.keys():
#                 if key in payload.keys():
#                     payload[key] = updatepayloaddict.get(key)
#             return payload
#         else:
#             return payload
#     return modified_payload


def AddInteger_Schema(**kwargs):
    if len(kwargs) == 2:
        return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:AddInteger>
         <tem:Arg1>{kwargs.get('var1')}</tem:Arg1>
         <tem:Arg2>{kwargs.get('var2')}</tem:Arg2>
      </tem:AddInteger>
   </soapenv:Body>
</soapenv:Envelope>"""
    else:
        assert kwargs, "required 2 variable but passed {}".format(len(kwargs))


def DivideInteger_Schema(**kwargs):
    if len(kwargs) == 2:
        return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:DivideInteger>
         <tem:Arg1>{kwargs.get('var1')}</tem:Arg1>
         <tem:Arg2>{kwargs.get('var2')}</tem:Arg2>
      </tem:DivideInteger>
   </soapenv:Body>
</soapenv:Envelope>"""
    else:
        assert kwargs, "required 2 variable but passed {}".format(len(kwargs))


def FindPerson_Schema(**kwargs):
    if len(kwargs) == 1:
        return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:FindPerson>
         <tem:id>{kwargs.get('var1')}</tem:id>
      </tem:FindPerson>
   </soapenv:Body>
</soapenv:Envelope>"""
    else:
        assert kwargs, "required 1 variable but passed {}".format(len(kwargs))
