class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.store={}
        self.head=Node(0,0)
        self.tail=Node(0,0)

        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        else:
            value=self.store[key].val
            curr=self.store[key]
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

            last=self.tail.prev
            last.next=curr
            curr.prev=last
            curr.next=self.tail
            self.tail.prev=curr
            return value

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            curr=self.store[key]
            curr.val=value

            curr.prev.next = curr.next
            curr.next.prev = curr.prev

            last=self.tail.prev
            last.next=curr
            curr.prev=last
            curr.next=self.tail
            self.tail.prev=curr
        else:
            if self.cap>len(self.store):
                new=Node(key,value)
                last=self.tail.prev
                new.next=self.tail
                new.prev=last
                last.next=new
                self.tail.prev=new
                self.store[key]=new
            else:
                rem=self.head.next
                rem.prev.next = rem.next
                rem.next.prev = rem.prev
                del self.store[rem.key]

                new=Node(key,value)
                last=self.tail.prev
                new.next=self.tail
                new.prev=last
                last.next=new
                self.tail.prev=new
                self.store[key]=new



                
                






        
