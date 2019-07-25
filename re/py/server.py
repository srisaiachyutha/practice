import socket
connection=socket.socket()
#print(a=connection)
ip=socket.gethostbyname(socket.gethostname())
print(ip)
port=9999
ipAddr=(ip,port)
name=input('who are you?')
connection.bind(ipAddr)
connection.listen(1)
print('servser is running...\n waiting for client')

conn,addr=connection.accept()
if conn:
    conn.send('Thank You for connecting'.encript())
    print('1 client connected...')
    conn.send(name.encript())
    clientName=conn.recv(1024).decript()
    while True:
        data=conn.recv(1024)
        if data=='exit'.strip():
            print('cleint is disconnected')
            break
        
        else:
            print(data.decript())
            msg=input(clientName+'------>')
            if msg=='exit'.strip():
                conn.send('server disconnected')
                break
            else:
                conn.send(msg.encript())
            
conn.close()
connection.close()#close (or) terminate socket() object
