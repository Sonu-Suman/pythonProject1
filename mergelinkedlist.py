# Merge two linked list in sorted manner

# This is the first approach
# This is iterative method

def mergetwolist(l1, l2):
    p1, p2, res = l1, l2, ListNode()
    p3 = res

    while p1 and p2:
        if p1.val<p2.val:
            p3.next = p1
            p1 = p1.next
        else:
            p3.next = p2
            p2 = p2.next

        p3 = p3.next
    
    p3.next = p1 if p1 else p2

    return res.next

# This is the second approach
# This is iterative method

def mergetwolist(l1, l2):
    res = ListNode()
    p = res
    
    while l1 and l2:
        if l1.val<l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next

        p = p.next

    p.next = l1 if l1 else l2
    return res.next


# This is third approach 
# And this is recursive method

def mergetwolist(l1, l2):
    if l1 is None:
        return l2
    
    if l2 is None:
        return l1

    if l1.val<=l2.val:
        l1.next = mergetwolist(l1.next, l2)
        return l1
    else:
        l2.next = mergetwolist(l2.next, l1)
        return l2
    

# This is forsth approach
# And this is recursive methode

def mergetwolist(l1, l2):
    if l1 is None:
        return l2
    
    if l2 is None:
        return l1

    res = ListNode(0)
    if l1.val <= l2.val:
        res.next = l1
        res.next.next = mergetwolist(l1.next, l2)
    else:
        res.next = l2
        res.next.next = mergetwolist(l2.next, l1)
        
    return res.next