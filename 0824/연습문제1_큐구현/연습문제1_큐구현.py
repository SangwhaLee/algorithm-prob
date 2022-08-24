def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear += 1
        Q[rear] = item
    
def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front += 1
        return Q[front]
    
def isEmpty():
    return front == rear

def isFull():
    rear == len(Q) - 1

def Qpeek():
    if isEmpty():
        print("Queue_Empty")
    else:
        return Q[front+1]
    
Q = [0]*5
front = -1
rear = -1
print(Q)
enQueue(1)
enQueue(2)
enQueue(3)

print(Q)
print(deQueue())
print(deQueue())
print(deQueue())