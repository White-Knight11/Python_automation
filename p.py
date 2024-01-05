import requests

# Replace 'YOUR_API_KEY' with your actual Flickr API key
api_key = '4e3a11513b7038875db9dd861929821c'
base_url = 'https://api.flickr.com/services/rest/'

# Example for flickr.photos.getPopular
popular_photos_params = {
    'method': 'flickr.photos.getPopular',
    'api_key': api_key,
    'user_id': '199812832@N05',
}

response = requests.get(base_url, params=popular_photos_params)
print(response)
data = response.text
print(data)


   
