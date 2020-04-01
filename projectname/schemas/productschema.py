CREATE_EMPLOYEE_PAYLOAD = {"name": "test", "salary": "123", "age": "23"}


def payload_variable_length_evalutaor(**kwargs):
    count = 0
    for key in kwargs.keys():
        if "var" in key:
            count = count + 1
    return count


def AddInteger_Schema(**kwargs):
    if payload_variable_length_evalutaor(**kwargs) == 2:
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
    if payload_variable_length_evalutaor(**kwargs) == 2:
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
    if payload_variable_length_evalutaor(**kwargs) == 1:
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
