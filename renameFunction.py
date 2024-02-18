# import libraries
import os,shutil,re
# TODO: Define The function
namePattern=re.compile(r""" 
            (\d{4})         # the year part
            .
            ([\s\w]+)       # the Movie name     
            """,re.VERBOSE)
def get_address():
    message="Please enter the path: "
    promptRes=input(message)
    return promptRes

def chdir_prompt():
    os.chdir(get_address())

chdir_prompt()
print(os.getcwd())

