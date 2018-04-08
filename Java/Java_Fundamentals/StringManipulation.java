public class StringManipulation{

    public String trimAndConcat(String string1, String string2){
        return string1.trim() + string2.trim();
    }

    public Integer getIndexOrNull(String string1, char char1){
        int idx = string1.indexOf(char1);
        return idx == -1 ? null: idx;
    }

    public Integer getIndexOrNull(String string1, String string2){
        int idx = string1.indexOf(string2);
        return idx == -1 ? null: idx;
    }

    public String concatSubstring(String string1, int int1, int int2, String string2){
        String substring = string1.substring(int1, int2);
        return substring + string2;
    }

}