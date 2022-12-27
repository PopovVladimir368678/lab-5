from suds.client import Client

url = 'https://tracking.russianpost.ru/rtm34?wsdl'
client = Client(url,headers={'Content-Type': 'application/soap+xml; charset=utf-8'})

barcode = input('Введите код отправления: ')
my_login = input('Введите логин: ')
my_password = input('Введите пороль: ')
message = \
"""<?xml version="1.0" encoding="UTF-8"?>
                <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:oper="http://russianpost.org/operationhistory" xmlns:data="http://russianpost.org/operationhistory/data" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Header/>
                <soap:Body>
                   <oper:getOperationHistory>
                      <data:OperationHistoryRequest>
                         <data:Barcode>""" + barcode+ """</data:Barcode>  
                         <data:MessageType>0</data:MessageType>
                         <data:Language>RUS</data:Language>
                      </data:OperationHistoryRequest>
                      <data:AuthorizationHeader soapenv:mustUnderstand="1">
                         <data:login>"""+ my_login +"""</data:login>
                         <data:password>""" + my_password + """</data:password>
                      </data:AuthorizationHeader>
                   </oper:getOperationHistory>
                </soap:Body>
             </soap:Envelope>"""

result = client.service.getOperationHistory(__inject={'msg':message})   # ответ в формате xml

