import sys
import csv
import json
import pickle

class ChangeFile():

    def __init__(self, *args):
        self.data_to_save = args[0]
        self.output_file = args[1]
        
    def ChangeFile_export_convert(self, *args):
        print("-> ", args[0])
        print("-> ", args[1])