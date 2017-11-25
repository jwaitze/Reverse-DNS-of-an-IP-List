import socket

with open('ips.txt', 'r') as ips:
    for ip in ips:
        with open('reversed_ips.txt', 'a') as result:
            pieces = ip.strip('\r\n').split(':')
            i = pieces[0]
            try:
                host = socket.gethostbyaddr(i)[0]
                print('%s -> %s' % (i, host))
                if ':' in ip:
                    result.write('%s:%s,%s:%s\n' % (i, pieces[1], host, pieces[1]))
                else:
                    result.write('%s,%s\n' % (i, host))
            except Exception as e:
                print('%s -> N/A' % i)
                if ':' in ip:
                    result.write('%s:%s,N/A\n' % (i, pieces[1]))
                else:
                    result.write('%s,N/A\n' % i)

print('Completed')
