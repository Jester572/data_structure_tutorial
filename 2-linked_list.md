# Linked Lists

A linked list is a linear data structure much like an array. A linked list consists of the node's value and the next node's value. This is how they are linked together.

So why use a linked list over an array if they are similar? It mostly has to do with the efficiency of the program. With an array, if you had 500 values in an array, but you wanted to insert a value in the middle of it, it would have to shift everything from the middle over. The same is said if you were to delete a value from an array, every item would have to shift the index down a number. With a linked list deleting takes the next nodes number and changes the previous "next" to that number. this is 2 simple changes rather than 250 changes. 

## Types of linked list
* [Single Linear](#single-linear-linked-list)
* [Double Linear](#double-linear-linked-list)

### Single Linear Linked List
![single linked list](single_linked_list.png)

### Double Linear Linked List
![double linked list](double_linked_list.png)