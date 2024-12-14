package org.application;

public class Main {
    public static void main(String[] args) {
        CustomStack<Integer> arr = new Linked<>();

        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.add(4);
        arr.add(5);

        System.out.println(arr.pop());
        System.out.println(arr.pop());
        System.out.println(arr.pop());
        System.out.println(arr.pop());
        System.out.println(arr.pop());
    }
}
