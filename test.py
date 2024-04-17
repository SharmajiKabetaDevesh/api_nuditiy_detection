# import requests
# import base64

# # API endpoint URL
# url = "http://localhost:3001/analyze"

# # Path to the image file you want to test
# image_path = "0001.jpg"

# # Read the image file
# with open(image_path, "rb") as f:
#     image_data = f.read()

# # Prepare payload
# payload = {'image':image_data}

# # Send POST request to the API endpoint
# response = requests.post(url, files=payload)

# # Print the response
# print(response.text)
import requests

url = 'http://192.168.194.19:3001/print_phone_number'
data = {'phone_number': '+1234567890'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
print(response.text)
