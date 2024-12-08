package org.application;

public class Linked<E> implements CustomList<E> {

    private NodeLink head;
    private NodeLink start;

    static public class NodeLink {
        Object data;
        NodeLink next;
        NodeLink(Object data) {
            this.data = data;
        }
    }

    @Override
    public void add(E data) {
        NodeLink newNode = new NodeLink(data);
        if(start == null) {
            start = newNode;
            head = newNode;
            return;
        }
        head.next = newNode;
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

    }
}
