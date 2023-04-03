# Linked Lists

A linked list is a linear data structure much like an array. A linked list consists of the node's value and the next node's value. This is how they are linked together.

So why use a linked list over an array if they are similar? It mostly has to do with the efficiency of the program. With an array, if you had 500 values in an array, but you wanted to insert a value in the middle of it, it would have to shift everything from the middle over. The same is said if you were to delete a value from an array, every item would have to shift the index down a number. With a linked list deleting takes the next nodes number and changes the previous "next" to that number. this is 2 simple changes rather than 250 changes.

## Types of linked list

- [Single Linear](#single-linear-linked-list)
- [Double Linear](#double-linear-linked-list)

### Single Linear Linked List

Each node in single linked list consists of two values:

- Node value
- Next value

The node value consists of the data you want to store, and the next value is what links that node to the next node. The next value equals the node value of the next node. A simple illustration is given below. 

| ![single linked list](single_linked_list.png) | 
|:--:| 
| *linked list figure 1* |

#### Adding node to a the front of a single linked list

A linked list has a head, and a tail. The head is the node that is the furthest to the right and the tail is the furthest to the left.
When adding to the head, the new node becomes the new head and the old head becomes part of the tail. To add to the head you would simply create a new node that has the next value of the old head.

* [See Example 1 Figure 2](add_single_linked_list.png)

#### Adding into the middle of a single linked list
To add a node into the middle of the linked list, you will need to find the two nodes that you would like to put them in between. In the picture below it shows that we are putting a node value of "Cyan" in between "Yellow" and "Green". We need to create the new node of "Cyan" with a next value of "Green", and then we need to change the next value of "Yellow" to "Cyan". This will create a new node that satisfies the requirement.  

* [See Example 2 Figure 2](add_single_linked_list.png)

| ![single linked list](add_single_linked_list.png) | 
|:--:| 
| *linked list figure 2* |

### Double Linear Linked List

Each node in Double linked list consists of three values:

- Previous value
- Node value
- Next value

Much like a Single linked list, a double linked list contains a "Node value" and a "Next Value". The difference is that we are now adding a "Previous Value" to the node. An example of how this might look is listed in the picture below.

There are a both advantages and disadvantages to using a double linked list versus a single linked list. The main benefit of a double linked list is that because you have a "Previous Value" and a "Next Value", you can traverse the linked list from either direction. With a single linked list you can only traverse in one direction. This can make a double linked list more efficient in the long run. The down side to the double linked list is that because we are storing an extra value per node, it can occupy more memory.

| ![double linked list](double_linked_list.png) | 
|:--:| 
| *linked list figure 1* |

#### Adding node to a the front of a double linked list

| ![double linked list](add_double_linked_list.png) | 
|:--:| 
| *linked list figure 1* |

