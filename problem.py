import string
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import shutil
import sys
hostname="localhost"
dir_path = sys.argv[1]

class colors:
    HEADER = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    ENDC = '\033[0m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'

class Problem(BaseHTTPRequestHandler):
    def do_POST(self):
        json_data = None
        json_data = json.load(self.rfile)
        if json_data is not None:
            json.dumps(json_data)
        else:
            ("Got no data")
        # (json_data)
        problem_name = json_data['name']
        print(colors.GREEN+"Coloning Problem"+colors.ENDC)
        problem_name.translate({ord(c): None for c in string.whitespace})
        #making folder in current directory
        path_for_problem = os.path.join(dir_path, problem_name)
        path_for_problem = path_for_problem.replace(' ','_')
        path_for_problem = path_for_problem.replace('.','')
        path_for_problem = path_for_problem.replace('\'','')
        path_for_problem = path_for_problem.replace('(','_')
        path_for_problem = path_for_problem.replace(')', '_')
        # (path_for_problem)
        if os.path.exists(path_for_problem) and os.path.isdir(path_for_problem):
            shutil.rmtree(path_for_problem)
        os.mkdir(path_for_problem)

        input_data = json_data['tests']
        # (input_data)
        #saving the samples in diff folders.
        #making the seperate folders for each Test

        os.mkdir(os.path.join(path_for_problem,"test_cases"))
        for idx, u in enumerate(input_data):
            # (u['input'],"\n", u['output'],"\n")
            name = os.path.join(path_for_problem,"test_cases",str(idx))
            os.mkdir(name)
            with open(os.path.join(name,"input.txt"),'w') as f:
                f.write(u['input'])
            with open(os.path.join(name,"output.txt"),'w') as f:
                f.write(u['output'])
        print(colors.BOLD+problem_name+colors.ENDC)
        sys.exit()

def run():
   port = 5001
   server = HTTPServer((hostname, port), Problem)
   server.serve_forever()

if __name__ == '__main__':
    run()
