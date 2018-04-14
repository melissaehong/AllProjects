//create SinglyLinkedList class with the head attribute
class SinglyLinkedList{
    public Node head;

    //create a constructor method that sets the head to null of your SinglyLinkedList objects
    public SinglyLinkedList(){
        this.head = null;
    }

    //create add(int) method that will add a node to the end of your list with the value in the parameter
    public void add(int value){
        Node newNode = new Node(value);

        if(head == null){
            head = newNode;
        } else {
            Node runner = head;
            while(runner.next != null){
                runner = runner.next;
            }
            runner.next = newNode;
        }
    }

    //Create a remove() method that will remove a node from the end of your list
    public void remove(){
        Node runner = this.head;

        if(head == null){
            System.out.println("There are no nodes in the SLL");
        } else if(head.next == null){
            head = null;
        } else {
            while(runner.next.next != null){
                runner = runner.next;
            }
            runner.next = null;
        }

    }

    //Create printValues() method that will print all the values of each node in the list in order
    public void printValues(){
        Node runner = this.head;

        if(runner == null){
            System.out.println("There are no nodes in the SLL");
        } else {
            while(runner != null){
                System.out.println(runner.value);
                runner = runner.next;
            }
        }
    }

    //Implement find(int) method that will return the first node with the value in the parameter
    public Node find(int val){
        if(head == null){
            return null;
        }

        Node runner = this.head;

        while(runner != null){
            if(runner.value == val){
                return runner;
            }
            runner = runner.next;
        }
        return null;
    }

    //Implement removeAt(int) method that will remove the node after n nodes, where n is the parameter.  
    //For example, if n is 0, remove the first node.  If n is 1, remove the second node.  Similar to Arrays.
    public void removeAt(int index){
        Node previous = head;
        int count = 0;

        if (head == null){
            System.out.println("There are no nodes in the SLL");
        } else if (index == 0){
            head = head.next;
        } else{
            while(count < index - 1){
                if(previous.next == null){
                    return;
                }
                previous = previous.next;
                count++;
            }
            Node current = previous.next;
            previous.next = current.next;
            current.next = null;
        }
    }

}