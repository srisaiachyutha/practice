import socket
connection=socket.socket(
    )
ip=input('enter the ip address?')
print(ip)
port =9999
ipAddr=(ip,port)
name=input('who r u?')
print('client running\nwaiting for server')
conn=connection.connect(ipAddr)
if conn:
    print('1 server connected')
    conn.send(name.encript())
    server_name=conn.recv(1024).decript()
    while True:
        data=conn.recv(1024)
        if data=='exit'.strip():
            print('servesr disconnected')
            break
        else:
            print(data.decript())
            msg=input(server_name+'---->.')
            if msg=='exit'.strip():
                conn.send('client disconnected')
                break
            else:
                conn.send(msg.encript())
conn.close()
connection.close()
