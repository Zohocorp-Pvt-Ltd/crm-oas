import requests
import logging
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.api.default_api import DefaultApi

# Use this file for sample testing in your generated SDK file.

# Configure logging
logging.basicConfig(
    filename='access_token.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Zoho token functions
def get_zoho_crm_access_token(client_id, client_secret, refresh_token):
    payload = {
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "refresh_token"
    }
    url = "https://accounts.zoho.com/oauth/v2/token"
    response = requests.post(url, data=payload)
    logging.debug("Response body: %s", response.text)
    response.raise_for_status()
    return response.json().get("access_token")

def create_refresh_token(client_id, client_secret, code, redirect_uri):
    payload = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }
    url = "https://accounts.zoho.com/oauth/v2/token"
    response = requests.post(url, data=payload)
    logging.debug("Create refresh token response: %s", response.text)
    response.raise_for_status()
    return response.json()

def fetch_record(api_instance, module_api_name, record_id):
    try:
        response = api_instance.get_record(module_api_name, record_id)
        print("API response:", response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_record: %s" % e)

def create_new_record(api_instance, module_api_name, body):
    try:
        response = api_instance.create_records(body, module_api_name)
        print("Record created:", response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_records: %s" % e)

def main():
    # Zoho CRM token retrieval
    CLIENT_ID = "FAKE_VLAUE" # replace with your client_id
    CLIENT_SECRET = "FAKE_VLAUE" # replace with your client_secret
    REFRESH_TOKEN = "FAKE_VLAUE" # create_refresh_token(client_id, client_secret, code, redirect_uri) can be used to generate this
    
    token = "FAKE_VLAUE" #get_zoho_crm_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
    print("Zoho Access Token:", token)
    
    # Swagger API configuration using the token (or a placeholder)
    configuration = Configuration()
    configuration.access_token = token
    
    api_client = ApiClient(configuration)
    api_instance = DefaultApi(api_client)
    
    # Demonstrate API calls
    # GET Record
  
    module_api_name = 'Leads'
    record_id = 'FAKE_VLAUE'

    fetch_record(api_instance, module_api_name, record_id)

    #POST Record
  
    body = swagger_client.BodyWrapper(
        data=[
            swagger_client.Record(
                Last_Name="Sample Lead - 01"
            )
        ]
    )
  
    create_new_record(api_instance, module_api_name, body)

if __name__ == "__main__":
    main()
