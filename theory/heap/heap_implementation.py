# Representing trees using arrays
# - parent_idx is node_idx // 2
# - left_child_idx is node_idx * 2
# - right_child_idx is node_idx * 2 + 1

# Min Heap
class MinHeap:
  def __init__(self, size):
    self.max_size = size
    self.min_heap = [0] * (size + 1)
    self.real_size = 0
    
  def add(self, element):
    self.real_size += 1
    
    if self.real_size > self.max_size:
      self.real_size -= 1
      return
    
    self.min_heap[self.real_size] = element
    
    idx = self.real_size
    parent_idx = idx // 2
    
    while self.min_heap[idx] < self.min_heap[parent_idx] and idx > 1:
      self.min_heap[parent_idx], self.min_heap[idx] = self.min_heap[idx], self.min_heap[parent_idx]
      idx = parent_idx
      parent_idx = idx // 2

  def peek(self):
    return self.min_heap[1]
  
  def pop(self):
    if self.real_size == 0:
      return
    
    remove_element = self.min_heap[1]
    
    self.min_heap[1] = self.min_heap[self.real_size]
    self.real_size -= 1
    idx = 1
    
    while (idx <= self.real_size // 2):
      left_idx = idx * 2
      right_idx = idx * 2 + 1
      
      if self.min_heap[idx] > self.min_heap[left_idx] or self.min_heap[idx] > self.min_heap[right_idx]:
        if self.min_heap[left_idx] < self.min_heap[right_idx]:
          self.min_heap[left_idx], self.min_heap[idx] = self.min_heap[idx], self.min_heap[left_idx]
          idx = left_idx
        else:
          self.min_heap[right_idx], self.min_heap[idx] = self.min_heap[idx], self.min_heap[right_idx]
          idx = right_idx
      else:
        break
      
    return remove_element
  
  def size(self):
    return self.real_size
  
  def __str__(self):
    return str(self.min_heap[1 : self.real_size + 1])
      