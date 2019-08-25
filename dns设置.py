x=open('/etc/resolv.conf','w')
x.write('nameserver 8.8.8.8\nnameserver 8.8.4.4')
x.close()
