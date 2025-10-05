import json 
import os 
import pandas as pd
json_files = ["./chatgpt_raw_outputs/"+file for file in os.listdir("./chatgpt_raw_outputs") if file.endswith(".json")]
json_files
row_data_list = []
for json_file in json_files:
    out = json.load(open(json_file,'r'))
    if 'name' not in out['short_answer']:
        out['short_answer']['name'] = out['short_answer']['name_query']
    row_data_list.append(out['short_answer'])
pd.DataFrame.from_dict(row_data_list).to_excel('./test_set_with_chatpgt_output.xlsx',index=False)