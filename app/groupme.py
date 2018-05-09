from groupy.client import Client
import datetime

def makeGroup(n, usrList):
    client = Client.from_token('jI9arGAkDrtNWAhKdKLnjaj182R2L7RLV7q9odFj')
    now=datetime.datetime.now()
    nDate = n+now.strftime()
    new_group = client.groups.create(name=nDate)
    for i in usrList:
        new_group.memberships.add(i[0], None, i[1], None)

testList=[['aaron', '8583533185'], ['ranga', '7329978242']]
makeGroup('test', testList)