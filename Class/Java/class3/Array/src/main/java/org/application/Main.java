package org.application;

import org.application.custom.CustomArray;
import org.application.custom.CustomLinked;
import org.application.custom.CustomList;

public class Main {
    public static void main(String[] args) {
        CustomList<Integer> arr = new CustomArray<>();
        arr.add(3);
        arr.add(5);
        arr.add(7);
        System.out.println(arr.get(2));
    }
}
