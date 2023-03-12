import csv
import json
import pickle
import os

class FileExport:
    
    def __init__(self, dataToSave):
        self.dataToSave = dataToSave
        
    def save_file(self, out_file, output_content):
        if out_file.split('.')[1] in ['csv']:
            self.exportToCsv(out_file, output_content)
        elif out_file.split('.')[1] in ['json']:
            json_file = self.listToJson(output_content)
            self.exportToJson(out_file, json_file)
            
    def exportToCsv(self, csv_file, output_content):
        with open(csv_file, mode = 'w', newline = '') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(output_content)

    def listToJson(self, output_content):
        listToJson = {}
        for li in range(len(output_content)):
            listToJson.update({li:output_content[li]})
        return listToJson
        
    def exportToJson(self, json_file, output_content):
        with open(json_file, mode = 'w') as jsonFile:
            json.dump(output_content, jsonFile, indent = 4)
    
    def exportToTxt(self):
        pass
    
    def exportToPickle(self):
        pass