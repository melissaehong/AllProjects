import java.util.*;

public class PuzzleJavaTest{
    public static void main(String[] args){
        PuzzleJava pz = new PuzzleJava();
        int[] arr1 = {3,5,1,2,7,9,8,13,25,32};
        //ArrayList<Integer> givenArr = pz.greaterThan10(arr1);
        System.out.println("Greater than 10: " + pz.greaterThan10(arr1));
        String[] arr2 = {"Nancy", "Jinchi", "Fujibayashi", "Momochi", "ishikawa"};
        System.out.println("Long names: " + pz.longNames(arr2));
        pz.isVowel();
        ArrayList<Integer> arr3 = pz.genTen();
        System.out.println("Generating 10 random numbers: " + arr3);
        ArrayList<Integer> listed = pz.getTenSorted(arr3);
        System.out.println(pz.genRandomString());
        System.out.println(pz.gen10RandString());
    }
}