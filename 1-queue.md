# Queues


In terms of programming a queue is a list of data that exits or runs in the order in which it entered the queue. A queue is also used in daily life in determining who may recieve service next.  

## Queue Types

The Following are the various types of queues that will be covered in this tutorial

* <p>Standard Queue</p>
* <p>Circular Queue</p>
* <p>Priority Queue</p>

### Standard Queue
```mermaid
graph LR;

    enter[Enter queue] --> C([Customer 3]) --> B([Customer 2]) --> A([Customer 1]) --> exit[Exit queue]; 
```

### Circular Queue

```mermaid
graph LR;
    A([Kid 1]) --> B([Kid 2]) --> C([Kid 3]) --> D([Kid 4]) --> slide[Slide]
    slide --> A
```

### Priority Queue
```mermaid
graph LR;;

    regular[Regular Priority] --> C([Customer 3]) --> B([Customer 2]) --> A([Customer 1]) --> exit[Car Wash];

    high[High Priority] ---> D([Customer 4]) --Washed before customer 1---> exit;
```