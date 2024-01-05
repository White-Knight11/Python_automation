from requests_oauthlib import OAuth1Session
import urllib.parse

# Replace 'YOUR_CONSUMER_KEY' and 'YOUR_CONSUMER_SECRET' with your Flickr API key and secret
consumer_key = '4e3a11513b7038875db9dd861929821c'
consumer_secret = 'afc396e44c0e4437'

# Step 1: Get Request Token
request_token_url = 'https://www.flickr.com/services/oauth/request_token'
callback_url = 'https://www.flickr.com/photos/199812832@N05/'  # Replace with your desired callback URL

# Provided OAuth parameters
oauth_nonce = '95613465'
oauth_timestamp = '1305586162'
oauth_consumer_key = '653e7a6ecc1d528c516cc8f92cf98611'
oauth_signature_method = 'HMAC-SHA1'
oauth_version = '1.0'
oauth_signature = '7w18YS2bONDPL%2FzgyzP5XTr5af4%3D'

# Set up OAuth1 session with the provided parameters
flickr = OAuth1Session(
    client_key=consumer_key,
    client_secret=consumer_secret,
    resource_owner_key='',
    resource_owner_secret='',
    callback_uri=callback_url,
    nonce=oauth_nonce,
    timestamp=oauth_timestamp,
    signature_method=oauth_signature_method
)

fetch_response = flickr.fetch_request_token(request_token_url)

resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

# Print the obtained request token and secret
print("Request Token:", resource_owner_key)
print("Request Token Secret:", resource_owner_secret)
