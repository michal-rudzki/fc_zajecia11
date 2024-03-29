import sys
import csv
import json
import pickle

class ChangeFile():

    def __init__(self, data_to_save, output_file, input_file):
        self.data_to_save = data_to_save
        self.output_file = output_file
        self.input_file = input_file
        
    def normalize_output_data(self):
        normalize_output_data = []
        if self.input_file.split('.')[1] in ['json']:
            for val in self.data_to_save.values():
                normalize_output_data.append(val)
        
        elif self.input_file.split('.')[1] in ['csv', 'pickle']:
            normalize_output_data = self.data_to_save

        elif self.input_file.split('.')[1] in ['txt']:
            while len(self.data_to_save) != 0:
                normalize_output_data.append(self.data_to_save[0:4])
                self.data_to_save = self.data_to_save[4:]
        
        return normalize_output_data
            
    def ChangeFile_export_convert(self, data_to_save, output_file, input_file):
        self.data_to_save = data_to_save
        self.output_file = output_file
        self.input_file = input_file
        
        formated_data = self.normalize_output_data()
        print(formated_data)

        if output_file.split('.')[1] in ['csv']:
            csv_output = formated_data
            with open(output_file, mode='w', newline='') as csvfile:
                csvfile = csv.writer(csvfile)
                csvfile.writerows(csv_output)

        elif output_file.split('.')[1] in ['json']:
            json_output = {}
            for counter in range(len(formated_data)):
                json_output.update({counter:formated_data[counter]})
            
            with open(output_file, mode='w') as jsonfile:
                json.dump(json_output, jsonfile, indent=4)
        
        elif output_file.split('.')[1] in ['txt']:
            txt_output = formated_data
            with open(output_file, mode='w') as txtfile:
                for data in txt_output:
                    for read_data in data:
                        txtfile.write(read_data+"\n")
        
        elif output_file.split('.')[1] in ['pickle']:
            pickle_output = formated_data
            with open(output_file, mode='wb') as picklefile:
                pickle.dump(pickle_output, picklefile)