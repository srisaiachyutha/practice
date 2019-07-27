import json
data=[
     {"name":"achyutha",
      "rollno":"51466",
      "xgirlfriend":"zeta",
      "value":None},
     {"name":"achyutha",
      "rollno":"51466",
      "xgirlfriend":"zeta",
      "value":None},
     {"name":"achyutha",
      "rollno":"51466",
      "xgirlfriend":"zeta",
      "value":True},

     ]
with open('output.json','w') as f:
     datas=json.dumps(data)
     print(data)
     
     print('success')

