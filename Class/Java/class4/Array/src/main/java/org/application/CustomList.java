package org.application;

public interface CustomList<E> extends CustomCollection<E> {
    E get(int index);
    void remove(int index);
}