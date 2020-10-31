from __future__ import print_function, unicode_literals
import argparse
import os
import sys
import VT
import PEA
import APK_A
import imaging

import regex
from pyfiglet import Figlet
from PyInquirer import prompt
from PyInquirer import Validator, ValidationError
from pprint import pprint

banner = Figlet(font='slant')
print(banner.renderText('GUMMYBEAR WORLD'))

print("HELLO to our tool.\nThis tool aims to automate imaging of evidence disk(s). \nAND\nperform malware scan and analysis for Portable Executable(PE) file as well as Android Application Package(APK) file.\n\n")
print("You may enter:")
print("1 - Specify disk image location to find the file")
print("2 - (NO DISK IMAGE) Create disk image of unmounted evidence disk")
print("3 - Conduct finding of potential malware & produce analysis report")


class ChoiceValidator(Validator):
    def validate(self, document):
        ok = regex.match('^[1-3]$', document.text)
        if not ok:
            raise ValidationError(
                message = 'Please input a valid choice', cursor_position=len(document.text)
            )


questions = [
    {
        'type': 'input',
        'name': 'CHOICE',
        'message': 'Which action would you like to perform?',
        'validate': ChoiceValidator
     }
]
answer = prompt(questions)
if (answer.get('CHOICE') == '1'):
    imaging.with_image()
elif (answer.get('CHOICE') == '2'):
    imaging.no_image()
elif (answer.get('CHOICE') == '3'):
    VT.get_path()


