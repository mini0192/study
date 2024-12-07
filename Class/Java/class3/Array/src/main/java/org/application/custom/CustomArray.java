package org.application.custom;

import java.util.Arrays;

public class CustomArray<E> implements CustomList<E> {
    private int index = -1;
    private int size = 10;
    private Object[] arr = {};

    public CustomArray() {
        arr = new Object[size];
    }

    @Override
    public void add(E data) {
        if(index == size - 1)
            resize();
        arr[++index] = data;
    }

    @Override
    public E get(int index) {
        return (E) arr[index];
    }

    private void resize() {
        size *= 2;
        arr = Arrays.copyOf(arr, size);
    }
}
