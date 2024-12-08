package org.application;

public interface CustomList<E> {
    void add(E e);
    E get(int index);
    void remove(int index);
}