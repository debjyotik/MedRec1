import google.auth.transport.requests
from google.oauth2 import id_token

class Google:
    @staticmethod
    def validate(auth_token):
        try:
            idinfo = id.token.verify_oauth2_token(auth_token, request.Request())

            if 'accounts.google.com' in idinfo['iss']:
                return idinfo
            
        except:
            return "This token is either invalid or expired!!! "