import time,webbrowser
total_breaks=3
print('take a brak statrte on ',time.ctime())
for m in range(total_breaks+1):
     time.sleep(2)
     if m==1:
          print(m,'break started at',time.ctime())
          webbrowser.open('https://www.duckduckgo.com')
     elif m==2:
          print(m,'break started at',time.ctime())
          webbrowser.open('https://www.gmail.com')
     elif m==3:
          print(m,'break started at',time.ctime())
          webbrowser.open('https://www.facebook.com')
