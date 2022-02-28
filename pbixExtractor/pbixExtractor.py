import json
from zipfile import ZipFile
import shutil
import pandas as pd

class ReportExtractor():

    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.result = []

    def extract(self):
        pathFolder = f'{self.path}/temp_{self.name[:-5]}'
        try: shutil.rmtree(pathFolder)
        except:
            print(f'folder {pathFolder} not present')
        f = ZipFile(f'{self.path}/{self.name}', 'r')
        f.extractall(pathFolder)
        report_layout = json.loads(
            open(f'{pathFolder}/Report/Layout', 'r', encoding='utf-16 le').read()
        )

        f.close()
        fields = []
        for s in report_layout['sections']: 
            for vc in s['visualContainers']:       
                try:
                    query_dict = json.loads(vc['config'])
                    for command in query_dict['singleVisual']['prototypeQuery']['Select']:

                        if 'Measure' in command.keys():
                            #- MEASURES
                            name = command['Name'].split('.')[1]
                            table = command['Name'].split('.')[0]
                            fields.append([s['displayName'], query_dict['name'], table, name, 'Measure'])

                        elif 'Column' in command.keys():
                            # COLUMNS
                            name = command['Name'].split('.')[1]
                            table = command['Name'].split('.')[0]
                            fields.append([s['displayName'], query_dict['name'], table, name, 'Column'])

                        elif 'Aggregation' in command.keys():
                            # AGGREGATIONS
                            if ( ( '(' in command['Name'] ) & ( ')' in command['Name'] ) ): 
                                txt_extraction = command['Name'][command['Name'].find('(') + 1: command['Name'].find(')') ]
                            name  = txt_extraction.split('.')[1]
                            table = txt_extraction.split('.')[0]
                            fields.append([s['displayName'], query_dict['name'], table, name, 'Aggregation'])

                except: 
                    pass
        self.result =  fields
        shutil.rmtree(pathFolder)

re = ReportExtractor("CHANGEWITHPATH", "CHANGEWITHFILENAME.pbix")
re.extract()

df = pd.DataFrame(re.result, columns=['Page', 'Visual ID', 'Table', 'Name', 'Type'])
print(df)