package org.application;

public class Linked<E> implements CustomList<E>, CustomStack<E>, CustomQueue<E> {

    private NodeLink head;
    private NodeLink start;
    private int size = 0;

    static public class NodeLink {
        Object data;
        NodeLink next;
        NodeLink prev;
        NodeLink(Object data) {
            this.data = data;
        }
    }

    @Override
    public void add(E data) {
        NodeLink newNode = new NodeLink(data);
        size++;
        if(start == null) {
            start = newNode;
        } else {
            head.next = newNode;
            newNode.prev = head;
        }
        head = newNode;
    }

    @Override
    public E get(int index) {
        NodeLink current = start;
        for(int i = 0; i < index; i++) {
            current = current.next;
        }
        return (E) current.data;
    }

    @Override
    public void remove(int index) {
        size--;
        if(index == 0) {
            start = start.next;
            return;
        }
        NodeLink current = start;
        for(int i = 0; i < index - 1; i++) {
            current = current.next;
        }
        current.next = current.next.next;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public E pop() {
        size--;
        NodeLink current = head;
        if(current.prev == null) {
            start = null;
            head = null;
        } else {
            head = current.prev;
            head.next = null;
        }
        return (E) current.data;
    }

    @Override
    public E poll() {
        size--;
        NodeLink current = start;
        if(current.next == null) {
            start = null;
            head = null;
        } else {
            start = current.next;
            start.prev = null;
        }
        return (E) current.data;
    }
}
