# takes input from the reverse-dns-ip-list.py output

filtered = {}
with open('reversed_ips.txt', 'r') as source:
    for line in source:
        host_piece = line.strip('\r\n').split(',')[1]
        if host_piece == 'N/A':
            continue
        pieces = host_piece.split(':')
        if pieces[0].count('.') <= 3 and 'ip-' not in pieces[0] and pieces[0].count('-') < 4:
            filtered[pieces[0]] = pieces[1]
result = {}
for host in filtered:
    pieces = host.split('.')
    if len(pieces) <= 1:
        continue
    if len(pieces[-1]) + len(pieces[-2]) < 6:
        check = '.'.join(pieces[-3:])
    else:
        check = '.'.join(pieces[-2:])
    add_host = True
    for h in result:
        if check in h:
            add_host = False
    if add_host:
        result[host] = filtered[host]
with open('result.txt', 'a') as save:
    for host in result:
        line = '%s:%s\n' % (host, result[host])
        print(line, end='')
        save.write(line)

print('Completed: %i' % len(result))
