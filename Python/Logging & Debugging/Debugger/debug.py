import ipdb

def testbug():
    ipdb.set_trace()
    l=[]
    for i in range(10):
        l.append(i)
        print("we have append your data in list")
    return l

testbug()