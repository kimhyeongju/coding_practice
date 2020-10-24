# 함수 선언부
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNode(current):
    # current = node1
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory,head, current, pre
    if findData == head.data:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node


def deleteNode(deleteData):
    global memory, head, current, pre
    if deleteData == head.data:
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

# 전역 변수부
memory = []     # 노드가 저장될 공간(무한 크기)
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효']


# 메인 코드부
if __name__ == '__main__':
    # 첫 노드
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    # 두번째 노드 이후
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNode(head)

    insertNode('다현', '모모')
    printNode(head)
    insertNode('사나','미나')
    printNode(head)

    deleteNode('모모')
    printNode(head)
    deleteNode('정연')
    printNode(head)
    

