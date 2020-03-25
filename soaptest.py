# from zeep import Client
# from zeep.plugins import HistoryPlugin
# from lxml import etree
#
# history = HistoryPlugin()
# client = Client('https://www.crcind.com/csp/samples/SOAP.Demo.cls?wsdl', plugins=[history])
#
# import ipdb
# ipdb.set_trace()
# response = client.service
# response = response.AddInteger(6,3)
# print(response)
#
# print(etree.tostring(history.last_sent.get("envelope"), pretty_print=True, encoding='utf-8').decode())
# print(etree.tostring(history.last_received.get("envelope"), pretty_print=True, encoding='utf-8').decode())


###################################################################################
# import ipdb
# ipdb.set_trace()
import requests
url="https://www.crcind.com:443/csp/samples/SOAP.Demo.cls"
headers = {'SOAPAction': 'http://tempuri.org/SOAP.Demo.AddInteger', 'Content-Type': 'text/xml; charset=utf-8'}

def generate_body(arg1, arg2):
    return f'''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:AddInteger>
         <tem:Arg1>{arg1}</tem:Arg1>
         <tem:Arg2>{arg2}</tem:Arg2>
      </tem:AddInteger>
   </soapenv:Body>
</soapenv:Envelope>'''

body = generate_body(2,3)
response = requests.post(url,data=body,headers=headers)
# print(body)
print("Status Code -->> "+str(response.status_code))
print("Response Header -->> "+str(response.headers))
print("Response output -->> "+str(response.content))

import xml.dom.minidom
uglyxml = response.content
xml = xml.dom.minidom.parseString(uglyxml)
xml_pretty_str = xml.toprettyxml()

print(xml_pretty_str)




