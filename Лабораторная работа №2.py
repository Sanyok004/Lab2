arr=[1,2,3,0]
def Min(arr):
	cont=arr[0]
	for i in arr:
		if i<cont:
			cont=i
	print('минимум в массиве =',cont)
Min(arr)

def Arif(arr):
	sum=0
	count=len(arr)
	for i in arr:
		sum+=i
	sr=sum/count
	print('среднее арифметическое в массиве =',sr)
Arif(arr)

string='hello, world'
def Swap(string):
	c=len(string)-1
	arr2=''
	for i in string:
		arr2+=string[c]
		c-=1
	print(arr2)
Swap(string)



ivan={
	"name":"ivan",
	"age":34,
	"children":[{
		"name":"vasja",
		"age":15,
	},{
		"name":"petja",
		"age":10,
	}],
}
darja={
	"name":"darja",
	"age":41,
	"children":[{
		"name":"kirill",
		"age":21,
	},{
		"name":"pavel",
		"age":19,
	}],
}
emps=[ivan,darja]

for i in emps:
	a=i.get('children')
	for q in a:
		if q.get('age')>18:
			print(i.get('name'))
		break
