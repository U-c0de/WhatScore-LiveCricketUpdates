import requests
from datetime import datetime



class ScoreGet:


    def __init__(self):
        
        """
        Declaring the endpoints, apikey
        """

        self.url_get_all_matches = "http://cricapi.com/api/matches"
        self.url_get_score="http://cricapi.com/api/cricketScore"
        self.api_key = "************************"
        self.unique_id = ""  # unique to every match


    def get_unique_id(self):

        uri_params = {"apikey": self.api_key}
        resp = requests.get(self.url_get_all_matches, params=uri_params)
        resp_dict = resp.json()
        uid_found=0

        for i in resp_dict['matches']:
            if (i['team-1'] == "Canterbury Women" or i['team-2'] == "India") and i['matchStarted']:
                todays_date = datetime.today().strftime('%Y-%m-%d')
                if todays_date == i['date'].split("T")[0]:
                    uid_found=1
                    self.unique_id=i['unique_id']
                    print(self.unique_id)
                    break

        if not uid_found:
            self.unique_id=-1
        send_data=self.get_score(self.unique_id)
        return send_data


    def get_score(self,unique_id):

        data="" #stores the cricket match data

        if unique_id == -1:
            data="No matches today"

        else:
            uri_params = {"apikey": self.api_key, "unique_id": self.unique_id}
            resp=requests.get(self.url_get_score,params=uri_params)
            data_json=resp.json()
            
            try:
                data="Here's the score : "+ "\n" + data_json['stat'] +'\n' + data_json['score']
            except KeyError as e:
                data="Something went wrong"

        return data



