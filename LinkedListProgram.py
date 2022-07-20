#-------------------------------------------------------------------------------
# Name:        LinkedListProgram
# Purpose:
#
# Author:      Rani Sweta
#
# Created:     16-07-2022
# Copyright:   (c) Sweta 2022
# Licence:
#-------------------------------------------------------------------------------
'''
class Node:
    def __init__(self,data):
        self.val = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None


    def Printlinklist(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next

    def InsertInStart(self, nn):
        nn.next = self.head
        self.head = nn

    def AddNewNodeInEnd(self,endnn):
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = endnn

if __name__=='__main__':


    Llist = LinkedList()


    Llist.head = Node(1)
    Second = Node(2)
    Third = Node(3)

    Llist.head.next = Second
    Second.next = Third

    Llist.Printlinklist()
    A = Node("sweta")
    B = Node("Mukesh")

    Llist.AddNewNodeInEnd(B)
    Llist.InsertInStart(A)

    Llist.Printlinklist()
'''


class Node:
    def __init__(self,data):
        self.val = data
        self.next = None


class MylinkList:
    def __init__(self):
        self.head = None



    def ShowMyLinkList(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next


    def AddElmntInFirstOfList(self,NewNodeS):
        NewNodeS.next = self.head
        self.head = NewNodeS


    def AddElmntInEndOfList(self,NewNodeE):
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = NewNodeE

    def AddElementAfterCount(self,count,NewNode):
        Tempcount = 0
        temp = self.head
        while temp:
            Tempcount = Tempcount + 1
            if Tempcount == count:
                NewNode.next = temp.next
                temp.next = NewNode
                break
            temp = temp.next


    def get_length(self):
        temp = self.head
        count = 0
        while (temp):
            count = count + 1
            temp = temp.next

        return count


    def deleteNode(self, key):

        temp = self.head

        if (temp is not None):
            if (temp.val == key):
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.val == key:
                break
            prev = temp
            temp = temp.next

        if(temp == None):
            return

        prev.next = temp.next

        temp = None


if __name__=='__main__':


    showonj = MylinkList()
    showonj.head = Node(10)
    second = Node(20)
    third = Node(30)
    First = Node('00')
    Last = Node(40)
    Aftrcunt = Node('Mynewnode')

    showonj.head.next = second
    second.next = third


    showonj.AddElmntInFirstOfList(First)
    showonj.AddElmntInEndOfList(Last)

    showonj.ShowMyLinkList()
    showonj.deleteNode(20)
    print("After deletion of key node")
    showonj.ShowMyLinkList()

    newListObj = MylinkList()
    print("After count insert:")
    showonj.AddElementAfterCount(3,Aftrcunt)
    showonj.ShowMyLinkList()

    print("lenoflst =",showonj.get_length())
