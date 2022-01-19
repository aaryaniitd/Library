def filereader(file):
    f = open(file, 'r')
    t = f.readlines()
    temp = []
    for item in t:
        if item == t[-1]:
            temp.append(item)
        else:    
            temp.append(item[:-1])
    f.close()
    return temp

def fileadder(file, string):
    f = open(file, 'a')
    f.write('\n')
    f.write(string)
    f.close()

def fileremover(file, string):
    with open(file, 'r') as m:
        t = m.readlines()
        n = len(t)
    with open(file, 'w') as f:
        for line in t:
            if line.strip('\n') != string:
                if t.index(line) == n-1: 
                    f.write(line[0:-1])
                else:
                    f.write(line)
