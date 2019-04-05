from mytree import MaxHeap

def heapsort (tree):
  l = []
  while tree.len() != 0:
    l.append(tree.extract())
  return l[::-1] 

t = MaxHeap()
with open("words_27.txt","r") as f:
    lines = f.readlines()
    for word in lines:
      t.add(word[:-1])
        
    array = heapsort(t)
    
for word in array:
  print(word)    


