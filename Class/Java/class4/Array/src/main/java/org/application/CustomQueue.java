package org.application;

public interface CustomQueue<E> extends CustomCollection<E> {
    E poll();
}
