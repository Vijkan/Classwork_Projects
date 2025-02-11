//Mihir Kandlur
//CS114009
import java.util.Iterator;
class SortedList<E extends Comparable<? super E>> extends List<E> {

   
    public void insert(E data) {
        head = insertRecursive(head, data);
    }

    private Node<E> insertRecursive(Node<E> node, E data) {
        if (node == null || data.compareTo(node.data) < 0) {
            Node<E> newNode = new Node<>(data);
            newNode.next = node;
            return newNode;
        }
        node.next = insertRecursive(node.next, data);
        return node;
    }

   
    public void remove(E data) {
        head = removeRecursive(head, data);
    }

    private Node<E> removeRecursive(Node<E> node, E data) {
        if (node == null) return null;
        if (data.compareTo(node.data) == 0) {
            return node.next; 
        }
        node.next = removeRecursive(node.next, data);
        return node;
    }

    
    public E retrieve(int index) {
        return retrieveRecursive(head, index, 0);
    }

    private E retrieveRecursive(Node<E> node, int targetIndex, int currentIndex) {
        if (node == null || targetIndex < 0) return null;
        if (currentIndex == targetIndex) return node.data;
        return retrieveRecursive(node.next, targetIndex, currentIndex + 1);
    }

    
    public boolean search(E data) {
        return searchRecursive(head, data);
    }

    private boolean searchRecursive(Node<E> node, E data) {
        if (node == null) return false;
        if (data.compareTo(node.data) == 0) return true;
        return searchRecursive(node.next, data);
    }

    
    public Iterator<E> iterator() {
        return new SortedListIterator();
    }

    private class SortedListIterator implements Iterator<E> {
        private Node<E> current = head;

        
        public boolean hasNext() {
            return current != null;
        }

        
        public E next() {
            E data = current.data;
            current = current.next;
            return data;
        }
    }
}