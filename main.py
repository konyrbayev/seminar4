from mytree import MaxHeap 
f=open('words_27.txt','r')
lines=f.readlines()
for i in lines:
	print (i)

f=open('sorted.txt', 'w')
def simpleHeapSort( lines ):
    n = len(lines)
    heap = MaxHeap(n)

    for item in lines :
        heap.add( item )

    for i in range( n, 0, -1 ) :
        lines[i] = heap.extract()
        print(lines[i])


