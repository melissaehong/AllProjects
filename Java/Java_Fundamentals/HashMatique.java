import java.util.HashMap;

public class HashMatique{

    public static void main(String[] args){
        HashMap<String, String> trackList = new HashMap<>();
        trackList.put("Song1", "Lyrics");
        trackList.put("Song2", "Lyrics");
        trackList.put("Song3", "Lyrics");
        trackList.put("Song4", "Lyrics");

        String track = trackList.get("Song1");
        System.out.println(track);

        for (String key : trackList.keySet()){
            System.out.println(key + " : " + trackList.get(key));
        }
    }
}