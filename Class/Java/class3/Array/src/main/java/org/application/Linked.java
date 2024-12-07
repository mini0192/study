package org.application;

public class Linked {

    private NodeLink head;
    private NodeLink start;

    static public class NodeLink {
        int data;
        NodeLink next;
        NodeLink(int data) {
            this.data = data;
        }
    }

    public void add(int data) {
        NodeLink newNode = new NodeLink(data);
        if(start == null) {
            start = newNode;
            head = newNode;
            return;
        }
        head.next = newNode;
        head = newNode;
    }

    public int get(int index) {
        NodeLink current = start;
        for(int i = 0; i < index; i++) {
            if(current == null) {
                System.out.println("길이 초과");
                return -1;
            }
            current = current.next;
        }
        if(current == null) {
            System.out.println("길이 초과");
            return -1;
        }
        return current.data;
    }
}
