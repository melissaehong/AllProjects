
public class PuzzleJava {

public void greaterThan10(int[] arr){
    int sum = 0;
    for (int i = 0; i < arr.length; i++){
        sum+=i;
        if (arr[i] > 10){
            System.out.println(arr[i]);
        }
    }
}

}