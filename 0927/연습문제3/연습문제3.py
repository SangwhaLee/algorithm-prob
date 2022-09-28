import sys
sys.stdin = open('sample_input.txt','r')


def preorder(idx):
    if idx != 0:
        pre_node.append(idx)
        preorder(ch1[idx])
        preorder(ch2[idx])


def inorder(idx):
    if idx != 0:
        inorder(ch1[idx])
        in_node.append(idx)
        inorder(ch2[idx])


def postorder(idx):
    if idx != 0:
        postorder(ch1[idx])
        postorder(ch2[idx])
        po_node.append(idx)


V, E = map(int, input().split())

arrs = list(map(int,input().split()))
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

pre_node = []
in_node = []
po_node = []

for i in range(0,2*E,2):
    if ch1[arrs[i]] == 0:
        ch1[arrs[i]] = arrs[i+1]
    else:
        ch2[arrs[i]] = arrs[i+1]

preorder(1)
inorder(1)
postorder(1)

print("전위 순회 :", end=' ')
for i in pre_node:
    print(i, end=' ')
print()

print("중위 순회 :", end=' ')
for i in in_node:
    print(i, end=' ')
print()

print("후위 순회 :", end=' ')
for i in po_node:
    print(i, end=' ')
print()