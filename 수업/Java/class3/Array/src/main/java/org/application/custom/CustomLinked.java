package org.application.custom;

public class CustomLinked<E> implements CustomList<E> {

    private NodeLink head;
    private NodeLink start;

    static public class NodeLink {
        Object data;
        NodeLink next;
        NodeLink(Object data) {
            this.data = data;
        }
    }

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

    public E get(int index) {
        NodeLink current = start;
        for(int i = 0; i < index; i++) {
            if(current == null) {
                System.out.println("길이 초과");
                return null;
            }
            current = current.next;
        }
        if(current == null) {
            System.out.println("길이 초과");
            return null;
        }
        return (E) current.data;
    }
}
