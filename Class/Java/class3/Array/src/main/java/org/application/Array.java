package org.application;

import java.util.Arrays;

public class Array<E> implements CustomList<E> {
    private int index = -1;
    private int size = 10;
    private Object[] arr = {};

    public Array() {
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

    @Override
    public void remove(int index) {

    }

    private void resize() {
        size *= 2;
        arr = Arrays.copyOf(arr, size);
    }
}
