import json
import pandas as pd

class Print():
    def xlsx(data,path):
        try:
            data_json = json.dumps(data)
            df_json = pd.read_json(data_json)
            df_json.to_excel(path)
            return True
        except:
            return False
        