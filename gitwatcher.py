#!/usr/bin/python
import os
import pathlib
import json
import sys
""" 
                        !! CAUTIONS !!

Please make sure all extension are in lower case sensive.
Please make sure you have all extension in your data set json file .
Please don't abuse/delete json structure gaven in this this root folder.
Please make sure your have languages.json file in your root directory .

IMPORTTANT!! --  DONT'T RUN THIS SCRIPT UNDER DIFFERENT USER SESSIONS ( ONLY ADMIN ) .
IMPORTANT !! --  JSON DATA SET FILE HAVE A STRICT STRUCTURE AND DATA , DON'T TOUCH IT IF YOU DON'T KNOW WHAT'S JSON .

                            ABOUT
Python version 3.6
Author : MAAROUF Med Mahdi
email  : admin@agilsoft.net
version: 0.0
liscence:None
"""

def main(directory):
    extensions = []
    languages = []
    analyses = []
    with open('./languages.json', 'r') as j:
        languages = json_data = json.load(j)

    for root, subdirectories, files in os.walk(directory):
        for file in files:
            extensions.append(pathlib.Path(os.path.join(root, file)).suffix.split('.')[1]) 
    for language in languages:
        usage = 0
        for alisas_extension in language['extensions']:
            usage += extensions.count(alisas_extension)
        analyses.append(dict(label=language['label'],rank=language['rank'],extensions=language['extensions'],usage=usage))
    analyses.sort(key=lambda a: a['usage'],reverse=True)    
    for analyse in analyses:
        print(analyse['label'] , "\t\t used ",analyse['usage'],' times (', analyse['usage'] * 100 / len(extensions) ,'%)' ) ;
    if(len(analyses)):
        print('Most used lenguage is : ',analyses[0]['label'],' with usage : ', analyses[0]['usage'] , 'files (' ,analyses[0]['usage'] *100 / len(extensions) ,'%).')

if __name__ == "__main__":
    if len(sys.argv) == 1:
        
        print('Invalid directory')
        print('if you need help , just use option help , syntax gitwatcher --help / --h')
        exit()
    if sys.argv[1] in ['--help','--h']:
        print('gitwatcher analyse git languages usage .\nsyntax\n \t\t gitwatcher <git-directory> : analysing git directory\n\t\t gitwatcher --help or --h : showing help ')
        exit()
    directory = sys.argv[1];
    if os.path.exists(directory) is not True:
        print('Oops, given directory is not exists,Please make sure it is an existing directory path !')
        print('if you need help , just use option help , syntax gitwatcher --help / --h')
        exit()
    elif os.access(os.path.dirname(directory), os.W_OK) is not True:
        print('Oops,You have permission to use that directory !, try open me in administration mode :))')
        print('if you need help , just use option help , syntax gitwatcher --help / --h')
        exit()
    main(directory)
