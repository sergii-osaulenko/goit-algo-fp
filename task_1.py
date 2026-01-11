class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# 1. Реверсування списку
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# 2. Сортування (Merge Sort)
def sorted_merge(a, b):
    result = None
    if a is None: return b
    if b is None: return a

    if a.value <= b.value:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result

def get_middle(head):
    if head is None: return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_sort(head):
    if head is None or head.next is None:
        return head
    
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None
    
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    
    return sorted_merge(left, right)

# 3. Об'єднання двох відсортованих списків
def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
        
    if l1: tail.next = l1
    elif l2: tail.next = l2
    
    return dummy.next

# --- Перевірка ---
if __name__ == "__main__":
    # Створення списку: 3 -> 1 -> 4 -> 2
    head = ListNode(3, ListNode(1, ListNode(4, ListNode(2))))
    print("Оригінал:")
    print_list(head)

    # Реверс
    head = reverse_list(head)
    print("Реверс:")
    print_list(head)

    # Сортування
    head = merge_sort(head)
    print("Відсортований:")
    print_list(head)
    
    # Об'єднання
    l2 = ListNode(0, ListNode(5)) # 0 -> 5
    merged = merge_two_sorted_lists(head, l2)
    print("Об'єднаний:")
    print_list(merged)