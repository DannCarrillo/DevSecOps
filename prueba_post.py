from numpy import True_
import requests
import json

from sympy import true
 
url_api = "http://18.218.244.166:8080/api/v2/{method}"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"
 

# Set up headers and authentication if required

headers = {

    'Authorization': api_key,  # Replace with your authentication method

    'Content-Type': 'application/json',  # Adjust the content type as needed
    'accept' : 'application/json' 
}

# Define the data for the new product

new_product_data = {
  "tags": [
    "string"
  ],
  "name": "string",
  "description": "string",
  "prod_numeric_grade": 2147483647,
  "business_criticality": "very high",
  "platform": "web service",
  "lifecycle": "construction",
  "origin": "third party library",
  "user_records": 2147483647,
  "revenue": "7220042.43",
  "external_audience": True,
  "internet_accessible": True,
  "enable_product_tag_inheritance": True,
  "enable_simple_risk_acceptance": True,
  "enable_full_risk_acceptance": True,
  "disable_sla_breach_notifications": True,
  "product_manager": 0,
  "technical_contact": 0,
  "team_manager": 0,
  "prod_type": 0,
  "sla_configuration": 0,
  "regulations": [
    0
  ]
}
def get_products ():
    headers = {
        'accept' : 'application/json',
        'Authorization' : api_key
    }
 
    r = requests.get(url_api.format(method = 'products'), headers = headers, verify = False)
 
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=4))
 
if __name__== '__main__':
    get_products()