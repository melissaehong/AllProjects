import java.util.*;

public class PuzzleJava {

    public ArrayList<Integer> greaterThan10(int[] arr){
        System.out.println("Array: " + java.util.Arrays.toString(arr));
        ArrayList<Integer> filteredList = new ArrayList<Integer>();
        int sum = 0;
        for (int val : arr){
            sum+=val;
            if (val > 10){
                filteredList.add(Integer.valueOf(val));
            }
        }
        System.out.println("Sum: " + sum);
        return filteredList;
    }

    public ArrayList<String> longNames(String[] givenArray){
        ArrayList<String> longNamesArray = new ArrayList<String>(Arrays.asList(givenArray));
        ArrayList<String> copyArray = new ArrayList<String>(longNamesArray);
        Collections.shuffle(longNamesArray);
        for (String val : longNamesArray){
            System.out.println(val);
            if (val.length() <= 5){
                copyArray.remove(val);
            }
        }
        return copyArray;
    }

    public void isVowel(){
        String [] alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
        String [] vowels = {"a", "e", "i", "o", "u"};
        ArrayList<String> listAlphabet = new ArrayList<String>(Arrays.asList(alphabet));
        ArrayList<String> listVowels = new ArrayList<String>(Arrays.asList(vowels));
        Collections.shuffle(listAlphabet);
        String first = listAlphabet.get(0);
        String last = listAlphabet.get(listAlphabet.size() - 1);

        if(Arrays.asList(vowels).contains(first)){
            System.out.println("The first letter is a vowel!");
        }
        System.out.println("First letter: " + first);
        System.out.println("Last letter: " + last);
    }

    public ArrayList<Integer> genTen(){
        ArrayList<Integer> resultArray = new ArrayList<Integer>();
        Random randomGenerator = new Random();
        for (int i = 0; i < 10; i++){
            resultArray.add(randomGenerator.nextInt(101-55) + 55);
        }
        return resultArray;
    }

    public ArrayList<Integer> getTenSorted(ArrayList<Integer> list){
        ArrayList<Integer> copyArray = new ArrayList<Integer>(list);
        Collections.sort(copyArray);
        System.out.println("Generating 10 sorted numbers: " + copyArray);
        System.out.println("First sorted number: " + copyArray.get(0));
        System.out.println("Last sorted number: " + copyArray.get(copyArray.size()-1));
        return list;
    }

    public static String randomStringHelper(){
        String[] alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
        ArrayList<String> listAlphabet = new ArrayList<String>(Arrays.asList(alphabet));
        Random randomGenerator = new Random();
        String randomString = "";
        for (int i = 0; i < 5; i++){
            randomString = randomString.concat(listAlphabet.get(randomGenerator.nextInt(listAlphabet.size())));
        }
        return randomString;
    }

    public String genRandomString(){
        return PuzzleJava.randomStringHelper();
    }

   public ArrayList<String> gen10RandString(){
       ArrayList<String> resultArray = new ArrayList<String>();
       for (int i = 0; i < 10; i++){
           resultArray.add(PuzzleJava.randomStringHelper());
       }
       return resultArray;
   }

}