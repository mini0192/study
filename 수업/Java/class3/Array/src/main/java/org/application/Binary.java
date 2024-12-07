package org.application;

import java.util.Arrays;

public class Binary {
    public void search() {
        int[] data = {30, 20, 10, 50, 70, 80, 10, 60};
        Arrays.sort(data);
        int foundData = 100;

        int top = data.length - 1;
        int bottom = 0;
        while(top >= bottom) {
            int mid = (top + bottom) / 2;
            if(foundData == data[mid]) {
                System.out.println("Found");
                break;
            }
            if(foundData > data[mid]) bottom = mid + 1;
            else top = mid - 1;
        }
    }
}
