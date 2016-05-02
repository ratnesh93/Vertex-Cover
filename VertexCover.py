'''
Author : Ratnesh Chandak
Roll No: CS12b1030
Assignment 3: Vertex-Cover using primal dual algorithm
'''

def minimum(a,b):
	if(a<=b):
		return a
	else:
		return b

#to check the number in present in the list
def ispresent(a,S):
	for i in range(len(S)):
		if(S[i]==a):
			return 1
	return 0

numstring = input('Enter n: ')
n=int(numstring)

#getting weight of vertex
w= [0 for i in range(n)]
for i in range(n):
	numstring = input ('Enter weight of vertex ' )
	w[i]=int(numstring)

s= [0 for i in range(n)]	#value of the weight which has been used
S=[]						#set for vertex-cover

#creating graph
a=[]
for i in range(n):
	b=[]
	print 'enter number of edges of',i+1,'th vertex'
	numstring=input('Enter how many edges: ')
	p=int(numstring)
	for j in range(p):
		numstring=input('Enter vertex number: ')
		q=int(numstring)
		b.append(q-1)
	a.append(b)

edges=[]
y=0					#cost
for i in range(n):
	t=len(a[i])
	for k in range(t):
		j=a[i].pop()
		d=minimum(w[i]-s[i],w[j]-s[j])
		s[i]=s[i]+d
		s[j]=s[j]+d
		if(s[i]==w[i]):
			if(ispresent(i+1,S)==0):
				y=y+w[i]
				S.append(i+1)
				temp=[]
				temp.append(i+1)
				temp.append(j+1)
				edges.append(temp)
		elif(s[j]==w[j]):
			if(ispresent(j+1,S)==0):
				y=y+w[j]
				S.append(j+1)
				temp=[]
				temp.append(i+1)
				temp.append(j+1)
				edges.append(temp)

print '\nEdge Sequence : '
while(1):
 	print edges.pop()
 	if not edges:
 		break		
print '\nthe vertex cover is : ',
print S
print 'cost = ',y

