#comment

def search(a,b):
	list = a
	return b in a
	
def binarysearch(a,b):
	list = a
	low = 0
	hi = len(a)
	while(low<hi):
		mid = (low+hi)//2
		num = list[mid]
		if num==b:
			return "found in list"
		elif num>b:
			low = mid
		else:
			hi = mid
	return "not found in list"
		
		
	
list1 = [2,5,6,8,10,12]

print(binarysearch(list1,8))
	
