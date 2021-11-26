import requests


#I am not sure its 'pythonic' to create 'hard clients', but from my experience its safer and far easier to maintain in the long run 
class Api_Client:

    def __init__(self, baseUrl):

        self.baseUrl = baseUrl


    def check_response(self, response, acceptedResponseCode = 200):

        return response.status_code == acceptedResponseCode and 'application/json' in response.headers.get('Content-Type','')

    
    def get(self, employee = None):

        success = False
        data = None
        url = self.baseUrl if not employee else f'{self.baseUrl}?employee={employee}'

        response = requests.get(url)
    
        if self.check_response(response):
            success = True
            data = response.json()

        return { 'success': success, 'data': data }


    def get_by_id(self, id):

        success = False
        data = None

        response = requests.get(f'{self.baseUrl}/{id}')

        if self.check_response(response):
            success = True
            data = response.json()

        return { 'success': success, 'data': data }


    def post(self, formdata):

        success = False
        data = None

        response = requests.post(self.baseUrl, formdata)

        if self.check_response(response, 201):
            success = True
            data = response.json()

        return { 'success': success, 'data': data }

    
    def put(self, id, formdata):

        success = False
        data = None

        response = requests.put(f'{self.baseUrl}/{id}', formdata)

        if self.check_response(response):
            success = True
            data = response.json()

        return { 'success': success, 'data': data }

    
    def delete(self, id):

        success = False
        data = None

        response = requests.delete(f'{self.baseUrl}/{id}')

        if self.check_response(response):
            success = True
            data = response.json()

        return { 'success': success, 'data': data }
