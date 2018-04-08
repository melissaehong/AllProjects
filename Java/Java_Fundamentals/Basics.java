import java.util.ArrayList;
import java.util.Arrays;

public class Basics {

    public void print1to255(){
        for (int i = 0; i <= 255; i++){
            System.out.println(i);
        }
    }

    public void print1to255odd(){
        for (int i = 0; i <= 255; i++){
            if(i%2 == 1){
                System.out.println(i);
            }
        }
    }

    public void printSum(){
        int sum = 0;
        for (int i = 0; i <= 255; i++){
            sum += i;
            System.out.println("New number: " + i + "Sum: " + sum);
        }
    }

    public void iterateArray(int[] arr){
        for (int i = 0; i < arr.length; i++){
            System.out.println(arr[i]);
        }
    }

    public void findMax(int[] arr){
        int max = 0;
        for (int i = 0; i < arr.length; i++){
            if (arr[i] > max){
                max = arr[i];
            }
        }
        System.out.println(max);
    }

    public void getAverage(int[] arr){
        double sum = 0;
        for (int i = 0; i < arr.length; i++){
            sum += arr[i];
        }
        System.out.println(sum/arr.length);
    }

    public void arrayOdd(){
        ArrayList<Integer> arrList = new ArrayList<Integer>();
        for (int i = 0; i <= 255; i ++){
            arrList.add(i);
        }
        System.out.println(arrList);
    }

    public void greaterThanY(int[] arr, int y){
        int count = 0;
        for (int i = 0; i < arr.length; i++){
            if (arr[i] > y){
                count++;
            }
        }
        System.out.println(count);
    }

    public void squareValues(int[] arr){
        int length = arr.length;
        System.out.println("hi!" + arr);
    }

    public void eliminateNeg(int[] arr){
        ArrayList<  Integer> arrList = new ArrayList<Integer>();
        for (int i = 0; i < arr.length; i++){
            if (arr[i] < 0){
                arrList.add(0);
            } else{
                arrList.add(arr[i]);
            }
        }
        System.out.println(arrList);
    }

    public void maxMinAvg(int[] arr){
        int max = arr[0];
        int min = arr[0];
        double sum = 0;
        for (int i = 0; i < arr.length; i++){
            if(arr[i] > max){
                max = arr[i];
            }
            if(arr[i] < min){
                min = arr[i];
            }
            sum += arr[i];
        }
        System.out.println("Max: " + max);
        System.out.println("Min: " + min);
        System.out.println("Avg: " + (sum/arr.length));
    }

    public void shiftArray(int[] arr){
        int length = arr.length - 1; 
        for  (int i = 0; i < length; i++){
            arr[i] = arr[i+1];
        }
        arr[length] = 0;
        System.out.println(arr);
    }

}