import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

dir = input("Enter Directory to search:")

Files = os.listdir(dir)

match_score = int(input("How Close of a Match You are looking :[100]") or "100")

for file_ in Files:
       nFiles = Files
       if file_ in Files:
              nFiles.remove(file_)

       match,score = process.extractOne(file_,nFiles,scorer=fuzz.token_set_ratio)
       if score >= match_score:
              print(match +  "," + str(score))

pass