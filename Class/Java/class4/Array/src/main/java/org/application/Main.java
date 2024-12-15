package org.application;

public class Main {
    public static void main(String[] args) {
        CustomQueue<Integer> arr = new Linked<>();

        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.add(4);

        System.out.println(arr.poll());
        System.out.println(arr.poll());
        System.out.println(arr.poll());
        System.out.println(arr.poll());
    }
}

