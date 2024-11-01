import os

from dotenv import load_dotenv

load_dotenv()

login = os.getenv('login')
password = os.getenv('password')

api_username = os.getenv('api_username')
api_appkid = os.getenv('api_appkid')

url_balancer_ural = 'http://***'
