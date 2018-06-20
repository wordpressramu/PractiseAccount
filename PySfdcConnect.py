import beatbox
import codecs
sf = beatbox._tPartnerNS
svc = beatbox.Client()
svc.login(username, passwordToken)


dg = svc.describeGlobal()
for t in dg[sf.sobjects:]:
    print(str(t[sf.name]) + " \t " + str(t[sf.label]))

qr = svc.query("select Id, Name from Account")
print("query size = " + str(qr[sf.size]))
for rec in qr[sf.records:]:
    print(str(rec[2]) + " : " + str(rec[3]))


a = { 'type': 'Account',
    'Name': 'Python Account',
    'Website': 'http://www.pocketsoap.com/' }
sr = svc.create(a)
if str(sr[sf.success]) == 'true':
    print("id " + str(sr[sf.id]))

'''
a = {
	'type': 'Task',
	'OwnerID' : '0057F000000VqS9',
	'Priority' : 'High',
	'Subject' : 'Demo task 2',
	'Status' : 'In Progress',
	'WhatID' : '0017F00000pjxikQAA',
	
}

message = "this is my first file attachement"
a = {
	'type': 'Attachment',
	#'OwnerID' : '0057F000000VqS9',
	#'Priority' : 'High',
	#'Subject' : 'Demo task 2',
	#'Status' : 'In Progress',
	#'WhatID' : '0017F00000pjxikQAA',
	'Name': "FirstFile2.txt",
	'ParentId ': "00T7F00000jAkhOUAS",
	'Body  ': message
}


sr = svc.create(a)
if str(sr[sf.success]) == 'true':
    print("id " + str(sr[sf.id]))
'''
