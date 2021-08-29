import os
import string
import shutil
import argparse
import json
from requests.api import request

URL='https://codeforces.com/api/user.status?handle=T_Wzgp_Ctjl_dtyrs&from=1&count=1'

parser = argparse.ArgumentParser(description="Enter Contest Name and Duration in Hrs")
parser.add_argument('Contest_Name', metavar='Contest_Name', type=str, help="Enter the Contest Name")
parser.add_argument('Problems', metavar='Problems', type=int, help="Enter the number of problems")
parser.add_argument('Duration', metavar='Duration', type=int, help="Enter the Contest Duration")
arguments = parser.parse_args()
CONTEST_NAME = arguments.Contest_Name
Number_Of_Problems = arguments.Problems
DURATION = arguments.Duration

class StartContest():
    def Check(self):
        data = request.get(URL)
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
        ProblemDone={"problem_name": problem_name, "status": status, "problem_rating": problem_rating}
        return ProblemDone

    def Post(self):
        dir_path = os.getcwd()
        CONTEST_DIRECTORY = os.path.join(dir_path, CONTEST_NAME)
        if os.path.exists(CONTEST_DIRECTORY) and os.path.isdir(CONTEST_DIRECTORY):
            shutil.rmtree(CONTEST_DIRECTORY)
        os.mkdir(CONTEST_DIRECTORY)
        os.chdir(CONTEST_DIRECTORY)
        cur_cnt = 1

        cmd = "python3 /mnt/f/dev/parser/problem.py {}".format(os.getcwd())

        while cur_cnt <= Number_Of_Problems:
            os.system(cmd)
            cur_cnt += 1

        # getting all the file names in the directory
        doneproblem = 0
        Problem = []
        result = os.listdir(os.getcwd())

        for i in result:
            res={   "problem_name": i,
                    "done": False,
                    "time_done": 0
                }
            Problem.append(res.copy())

        print(Problem)
        res = self.Check()
        problem_name = res["problem_name"]
        problem_name.translate({ord(c): None for c in string.whitespace})
        problem_name = problem_name.replace(' ','_')
        problem_name = problem_name.replace('.','')
        problem_name = problem_name.replace('\'','')
        problem_name = problem_name.replace('(','_')
        problem_name = problem_name.replace(')', '_')

        if res["problem_name"] in result:
            doneproblem+=1;
            print("Total Problem Solved ", doneproblem)










def main():
    a = StartContest()
    a.Post()

if __name__ == '__main__':
    main()
