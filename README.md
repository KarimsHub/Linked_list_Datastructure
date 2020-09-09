# Main Concept of linked list

Each Element of a linked list is called a node, and every node has two different fields:
1. Data contains the value to be stored in the node
2. Next contains a reference to the next node on the list

A linked list is a collection of nodes. 
First node is called head, and it's used as the starting point for any iteration through the list.
Last node must have it's next reference pointing to None to determine the end of the list


## Linked Lists vs. Python Lists:

### Memory usage 
- Normally we have clear differences in the way linked lists and arrays are stored in memory. In Python, however, lists are dynamic arrays. That means that the memory usage of both lists and liked lists is very similar.

### Insertion & Deletion of Elements
- In Python you can use .insert() and .remove() to insert or remove elements at a specific position in a list, but you use .append() and .pop() only to insert or remove elements at the end of a list.
- So even though inserting elements at the end of a list using .append() or .insert() will have a constant time of O(1), when you try inserting an element closer to or at the beginning of the list, the average time complexity will grow to O(n).
- Linked lists are much more straightforward when it comes to insertion and deletion of elements at the beginning or end of a list, where their time complexity is always constant O(1).
- For this reason, linked lists are faster than normal lists when implementing a queue (FIFO), in which elements are continiously inserted an removed at the beginning of the list. But they perform similar to a list when implementing a stack(LIFO), in which elements are inserted and removed at the end of the list

### Retrieval of Elements
- When it comes to element lookup, lists perform much better than linked lists. When you know, which element you want to access, lists can perform this operation in O(1).
- Trying to do the same with a linked list would take O(n) because you need to traverse/iterate through the whole list to find the element.
- When searching for a specific element, however, both lists and linked lists perform very similar with a time complexity of O(n).



