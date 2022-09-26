import requests
import json
import os

path = r"C:\sandbox"


class TestAPIResponse:





    def test_upload_file(self):
        data = {
            'file_id': "trial_20220317_163009.csv",
        }
        req_json = {
            "json_data": "string"
        }
        response = requests.post('http://127.0.0.1:5000/uploadfile', params=data, json=req_json)
        # print(response)
        assert response.status_code == 200
        result = response.text
        res = json.loads(result)
        # print(res)
        assert response.headers["Content-Type"] == "application/json"



# response = TestAPIResponse()
# response.test_upload_file()
# response.test_upload_non_existing_file()
# # response.test_upload_id()
# response.test_download_api()
# response.test_download_id()
