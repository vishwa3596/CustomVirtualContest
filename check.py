import json

import requests

URL='https://codeforces.com/api/user.status?handle=T_Wzgp_Ctjl_dtyrs&from=1&count=2'

def run():
    data = requests.get(URL)
    json_data = data.json()
    json.dumps(json_data)
    value = json_data['result'][1]
    status = value['verdict']
    problem_name = value['problem']['index']+'-'+value['problem']['name']
    problem_rating = "NA"
    rating_in_dict = 'raing' in value['problem']
    print(rating_in_dict)
    problem_rating=value['problem']['rating']
    if rating_in_dict:
        problem_rating = value['problem']['rating']
    return (status, " " , problem_name, " ", problem_rating)

