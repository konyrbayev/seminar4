class MaxHeap:
  def __init__( self):
    self._count = 0
    self._elements = []

  def len( self ):
    return self._count

  def capacity( self ):
    return len( self._elements )

  def add(self, data):
    self._elements.append(data)
    self._count += 1
    self._siftUp(self._count - 1)
    
  def extract( self ):
    value = self._elements[0]
    self._count -= 1
    self._elements[0] = self._elements[ self._count ]
    self._siftDown( 0 )

  def _siftUp( self, ndx ):
    if ndx > 0 :
        parent = ndx // 2
        if self._elements[ndx] > self._elements[parent] : # swap elements
          tmp = self._elements[ndx]
          self._elements[ndx] = self._elements[parent]
          self._elements[parent] = tmp
          self._siftUp( parent )

  def _siftDown( self, ndx ):
    left = 2 * ndx + 1
    right = 2 * ndx + 2
    largest = ndx
    if left < self._count and self._elements[left] >= self._elements[largest] :
      largest = left
    elif right < self._count and self._elements[right] >= self._elements[largest]:
      largest = right
      if largest != ndx :
        swap( self._elements[ndx], self._elements[largest] )
        _siftDown( largest )
