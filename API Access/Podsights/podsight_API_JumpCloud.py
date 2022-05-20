#key: 734cd4ba79cd49f891556054e23fd3bc
#secret: wiy9wwahcam82vgwobre2tpvwobul7nm2tbae37v02opvhvj9kmvi0l6hp4vzg7c
import requests
import json
import pandas as pd
from io import BytesIO, StringIO
import numpy as np
from datetime import datetime

params = dict(key="734cd4ba79cd49f891556054e23fd3bc", secret='wiy9wwahcam82vgwobre2tpvwobul7nm2tbae37v02opvhvj9kmvi0l6hp4vzg7c')

today = datetime.today().strftime('%Y-%m-%d')


#campaign_placement
Download_url= f"https://api.pdst.fm/broker?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl9pZCI6ImE2OGUxYjdlZmY1MTQxODdiMzk3ZTg4MzUyNTIwM2JhIn0.7Alvs6h9dFOkSNsJq-kHETlZu_dFXI0wkVL0CbdpmJ8&kind=daily&pk=9ffdceaae0854d33a0c20921e73f40f2&object_type=organization&after=2022-03-15&before={today}&modelled=true&spend_by_impressions=true"
Podsight_req = requests.get(Download_url, params)


result = str(Podsight_req.content, 'utf-8')
data = StringIO(result)
df = pd.read_csv(data)

df2 = df.groupby(["publisher_name",'line_item_name']).sum().reset_index()

df2["CPM"] = (df2["visitors_modeled"]/df2["reach"])

df2["Detected_On_Site"] = df2["CPM"]*df2["impressions"]


newdf = pd.DataFrame([df2["publisher_name"], df2["line_item_name"],df2["impressions"], df2["CPM"], df2["Detected_On_Site"]]).transpose()
newdf.to_excel('/Users/hamza.ahmed/Coding Projects/Data/Podsight Data/Podsight_JumpCloud.xlsx', 'openpyxl')

