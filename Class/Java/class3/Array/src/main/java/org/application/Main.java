package org.application;

public class Main {
    public static void main(String[] args) {
        CustomList<String> arr = new Array<>();
        arr.add("Test");
        arr.add("Good");

        System.out.println(arr.get(0));
        System.out.println(arr.get(1));
    }
}
