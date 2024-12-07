package org.application;

import java.util.Arrays;

public class Array{
    private int index = -1;
    private int size = 10;
    private int[] arr = {};

    public Array() {
        arr = new int[size];
    }

    public void add(int data) {
        if(index == size - 1)
            resize();
        arr[++index] = data;
    }

    public int get(int index) {
        return arr[index];
    }

    private void resize() {
        size *= 2;
        arr = Arrays.copyOf(arr, size);
    }
}
