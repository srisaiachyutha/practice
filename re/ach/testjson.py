import json
#f=open('raw.json','r')
data='''[{"name":"xgirl friend",
       "rollno":"17121a05h3",
       "status":true},
       {"name":"xgirl friend",
       "rollno":"17121a05h3",
       "status":true},
       {"name":"xgirl friend",
       "rollno":"17121a05h3",
       "status":true}
      ]'''
s=json.loads(data)
print(s)


     


     
