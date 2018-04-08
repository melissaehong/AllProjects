public class BasicsTest{

    public static void main(String[] args){
        Basics basics = new Basics();

        basics.print1to255();
        basics.print1to255odd();
        basics.printSum();
        int[] myArr = {1, 3, 5, 7, 9, 13};
        System.out.println("array" + myArr);
        basics.iterateArray(myArr);
        basics.findMax(myArr);
        basics.getAverage(myArr);
        basics.arrayOdd();
        basics.greaterThanY(myArr, 5);
        basics.squareValues(myArr);
        System.out.println("array" + myArr);
        int[] arr2 = {1, 5, 10, -2};
        basics.eliminateNeg(arr2);
        basics.maxMinAvg(arr2);
        int[] arr3 = {1, 5, 10, 7, -2};
        basics.shiftArray(arr3);
        int[] test = {0, 4, 10};
        System.out.println(java.util.Arrays.toString(test));
    }

}