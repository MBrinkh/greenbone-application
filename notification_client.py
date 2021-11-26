import requests


#I am not sure its 'pythonic' to create 'hard clients', but from my experience its safer and far easier to maintain in the long run 
class Notification_Client:

    def __init__(self, url):

        self.url = url

    
    def notify(self, employeeAbbreviation, message):

        request_data = {
            'level': 'warning',
            'employeeAbbreviation': employeeAbbreviation,
            'message': message
        }

        print(request_data)

        #Since the docker image isn't actually running this request is just commented out
        #Using the 'json' parameter of requests.post automatically sets neccessary headers for content-type 'application/json'
        #requests.post(self.url, json = requestData)
