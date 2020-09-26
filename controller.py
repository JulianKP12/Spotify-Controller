import requests
import threading
import time

class Controller:
    def __init__(self, refresh):
        self.refresh_code = refresh
        self.pauseMode = 1 # 0: Paused, 1: Playing
        self.token = None

        self.get_token()
        self.pause()


    def get_token(self):
        data = dict(grant_type="authorization_code", redirect_uri="http://localhost:5000/", code=self.refresh_code)
        headers = {"Authorization": "Basic ZDU1NGQ1OWUwYmE0NDZkOWIyOTdhMzRhZWE4ZDZhYTQ6MDlkZjg2NWFlODc1NDZlNzlmZTc3MDQyMDk5YjMxMWQ="}
        
        r = requests.post("https://accounts.spotify.com/api/token", data=data, headers=headers)
        jsonified = r.json()

        self.token = jsonified["access_token"]

        threading.Thread(target=self.handle_refresh, args=(jsonified,)).start()

    def handle_refresh(self, json_data):
        time.sleep(json_data["expires_in"])
        self.get_token(json_data["refresh_token"])



    def getDevice(self):
        url = f"https://api.spotify.com/v1/me/player/devices"
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}

        r = requests.get(url, headers=headers)

        return r.json()["devices"][0]["id"]

    def previous(self):
        url = f"https://api.spotify.com/v1/me/player/previous"
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}

        r = requests.post(url, headers=headers)

    def next(self):
        url = f"https://api.spotify.com/v1/me/player/next"
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}

        r = requests.post(url, headers=headers)

    def pause(self):
        url = f"https://api.spotify.com/v1/me/player/pause"
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}

        r = requests.put(url, headers=headers)
        self.pauseMode = 0

    def play(self):
        url = f"https://api.spotify.com/v1/me/player/play"
        headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}

        r = requests.put(url, headers=headers)
        self.pauseMode = 1