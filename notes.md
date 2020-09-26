# Spotify Authorization

---
## Access Token

### Url
```
https://accounts.spotify.com/authorize/
```

### Parameters
```
?response_type=code
&client_id=d554d59e0ba446d9b297a34aea8d6aa4
&scope=user-read-playback-state%20user-modify-playback-state
&redirect_uri=https%3A%2F%2Fgoogle.nl%2F
```

### Scopes
```
user-read-playback-state
user-modify-playback-state
```

### Finished Authorization Url
```
https://accounts.spotify.com/authorize/?response_type=code&client_id=d554d59e0ba446d9b297a34aea8d6aa4&scope=user-read-playback-state%20user-modify-playback-state&redirect_uri=https%3A%2F%2Fgoogle.nl%2F
```

---
## Refresh Token

### Base64 Encoded ClientID + ClientSecret
```
ZDU1NGQ1OWUwYmE0NDZkOWIyOTdhMzRhZWE4ZDZhYTQ6MDlkZjg2NWFlODc1NDZlNzlmZTc3MDQyMDk5YjMxMWQ=
```

### Final cURL
```
curl -H "Authorization: Basic ZDU1NGQ1OWUwYmE0NDZkOWIyOTdhMzRhZWE4ZDZhYTQ6MDlkZjg2NWFlODc1NDZlNzlmZTc3MDQyMDk5YjMxMWQ=" -d grant_type=authorization_code -d code=<insert refresh token here> -d redirect_uri=https%3A%2F%2Fgoogle.nl%2F https://accounts.spotify.com/api/token
```

### Returned JSON Data
```
{
	'access_token': 'BQCUaOdPyIDjc-mArAE3qqrsXXe3cSCRIxF3YwLtM_vqYzGsoXTYYfuZeki599zpVKVn7DpIvnzRmGVOefNWdbQWzRQEv1EjHuRzID4N2ZaMU2-6MMeBGGak4bGp-JXZZz32eHyE6gGETp5R_jageFfx29Jvk4E0', 
	'token_type': 'Bearer', 
	'expires_in': 3600, 
	'refresh_token': 'AQDUj9DyuIjAwA1JcIClmrVlaa5pS6JA6S0zMMQsB5k234cKY8u9FXT5i2b5XNW_6gVR7ZNE23dCc7R0wuvvIJxeWY9HL-QZ0hQTuX3oa1z3ni6_AhQ3h0MVYFKikxE9QMg', 
	'scope': 'user-modify-playback-state user-read-playback-state'
}
```