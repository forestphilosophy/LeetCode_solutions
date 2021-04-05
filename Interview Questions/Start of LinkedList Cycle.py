def find_cycle_start(head):
  # TODO: Write your code here
  pointer_fast = head
  pointer_slow = head

  while pointer_fast:
    pointer_fast = pointer_fast.next.next
    pointer_slow = pointer_slow.next

    if pointer_fast == pointer_slow:
      K = calculate_cycle_length(pointer_slow)
      break
  
  for i in range(K):
    pointer_fast = pointer_fast.next

  pointer_slow = head

  if pointer_slow == pointer_fast:
    return pointer_fast
    
  while pointer_fast:
    pointer_slow = pointer_slow.next
    pointer_fast = pointer_fast.next

    if pointer_fast == pointer_slow:
      return pointer_fast

  return head

def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length
