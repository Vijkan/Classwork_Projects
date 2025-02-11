import java.util.Iterator;
import java.util.Stack;

public class BinarySearchTree<E extends Comparable<? super E>> extends BinaryTree<E> {

    
    public void insert(E data) {
        root = insertRecursively(root, data);
    }

    private Node<E> insertRecursively(Node<E> node, E data) {
        if (node == null) {
            return new Node<>(data);
        }
        if (data.compareTo(node.data) < 0) {
            node.left = insertRecursively(node.left, data);
        } else if (data.compareTo(node.data) > 0) {
            node.right = insertRecursively(node.right, data);
        }
        return node;
    }

    
    public void remove(E data) {
        root = removeRecursively(root, data);
    }

    private Node<E> removeRecursively(Node<E> node, E data) {
        if (node == null) {
            return null;
        }
        if (data.compareTo(node.data) < 0) {
            node.left = removeRecursively(node.left, data);
        } else if (data.compareTo(node.data) > 0) {
            node.right = removeRecursively(node.right, data);
        } else {
            if (node.left == null) {
                return node.right;
            } else if (node.right == null) {
                return node.left;
            }
            Node<E> smallestNode = findMin(node.right);
            node.data = smallestNode.data;
            node.right = removeRecursively(node.right, smallestNode.data);
        }
        return node;
    }

    private Node<E> findMin(Node<E> node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    
    public boolean search(E data) {
        return searchRecursively(root, data);
    }

    private boolean searchRecursively(Node<E> node, E data) {
        if (node == null) {
            return false;
        }
        if (data.compareTo(node.data) == 0) {
            return true;
        } else if (data.compareTo(node.data) < 0) {
            return searchRecursively(node.left, data);
        } else {
            return searchRecursively(node.right, data);
        }
    }

    
    public Iterator<E> iterator() {
        return new InOrderIterator();
    }

    private class InOrderIterator implements Iterator<E> {

        private final Stack<Node<E>> stack = new Stack<>();
        private Node<E> current = root;

        public InOrderIterator() {
            pushLeft(current);
        }

        private void pushLeft(Node<E> node) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
        }

        
        public boolean hasNext() {
            return !stack.isEmpty();
        }

        
        public E next() {
            Node<E> node = stack.pop();
            if (node.right != null) {
                pushLeft(node.right);
            }
            return node.data;
        }
    }
}
