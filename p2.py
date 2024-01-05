from requests_oauthlib import OAuth1Session
import requests

### Replace 'YOUR_CONSUMER_KEY' and 'YOUR_CONSUMER_SECRET' with your Flickr API key and secret
consumer_key = '4e3a11513b7038875db9dd861929821c'
consumer_secret = 'afc396e44c0e4437'
##
##
##
##from requests_oauthlib import OAuth1Session
##
### Replace 'YOUR_CONSUMER_KEY' and 'YOUR_CONSUMER_SECRET' with your Flickr API key and secret
##consumer_key = 'YOUR_CONSUMER_KEY'
##consumer_secret = 'YOUR_CONSUMER_SECRET'
##
### Step 1: Get Request Token
##request_token_url = 'https://www.flickr.com/services/oauth/request_token'
##callback_url = 'http%3A%2F%2Fexample.com%2Fcallback'  # URL-encoded callback URL # Replace with your desired callback URL
##flickr = OAuth1Session(
##    client_key=consumer_key,
##    client_secret=consumer_secret,
##    callback_uri=callback_url
##)
##fetch_response = flickr.fetch_request_token(request_token_url)
##
##Request Token: 72157720905662281-d2a11074c8f943c9
##Request Token Secret: 1d5a25c058e69e54
resource_owner_key = '72157720905662281-d2a11074c8f943c9'
resource_owner_secret = '1d5a25c058e69e54'

# Step 2: Authorize the Request Token
authorize_url = 'https://www.flickr.com/services/oauth/authorize?oauth_token=72157720905662281-d2a11074c8f943c9'
print('Please go to the following link in your browser:', authorize_url + resource_owner_key)


# Step 3: Get Access Token
access_token_url = 'https://www.flickr.com/services/oauth/access_token'
flickr = OAuth1Session(
    client_key=consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier='199812832@N05'
)

access_token = flickr.fetch_access_token(access_token_url)

# Print the obtained access token and secret
print("Access Token:", access_token.get('oauth_token'))
print("Access Token Secret:", access_token.get('oauth_token_secret'))







# Replace 'YOUR_ACCESS_TOKEN' and 'YOUR_ACCESS_TOKEN_SECRET' with the obtained access token and secret
access_token = access_token.get('oauth_token')
access_token_secret = access_token.get('oauth_token_secret')

# Print the obtained access token and secret
print("Access Token:", access_token)
print("Access Token Secret:", access_token_secret)

# Step 4: Upload a Photo
upload_url = 'https://up.flickr.com/services/upload/'
photo_path = 'path/to/your/photo.jpg'  # Replace with the actual path to your photo

# Set up OAuth1 session with the access token and secret
flickr = OAuth1Session(
    client_key=consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret
)

# Prepare the parameters for the upload
upload_params = {
    'oauth_consumer_key': consumer_key,
    'oauth_token': access_token,
    'oauth_signature_method': 'HMAC-SHA1',
    'oauth_timestamp': flickr.timestamp(),
    'oauth_nonce': flickr.nonce(),
    'oauth_version': '1.0',
    'title': 'Your Photo Title',  # Replace with your desired title
    'description': 'Your Photo Description',  # Replace with your desired description
    'tags': 'tag1 tag2',  # Replace with your desired tags
}

# Upload the photo using requests
with open(photo_path, 'rb') as photo_file:
    files = {'photo': ('photo.jpg', photo_file)}
    response = requests.post(upload_url, params=upload_params, files=files)

print("Photo uploaded successfully!")
