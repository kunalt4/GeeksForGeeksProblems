import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class pn {
    

/*
 * Complete the function below.
 */

    static String FormatString(String S) {
        StringBuilder R = new StringBuilder("");
        S = S.replaceAll("[^a-zA-Z0-9]", "");
        for(int i=0;i<S.length();i=i+3){
            R.append(S.substring(0,3));
            R.append(" ");
            S = S.substring(3);
        }
        if(S.length() > 0){
            R.append(S);
        }

        return R.toString();
    }

    public static void main(String[] args) throws IOException{
        Scanner in = new Scanner(System.in);
        // final String fileName = System.getenv("OUTPUT_PATH");
        // BufferedWriter bw = new BufferedWriter(new FileWriter(fileName));
        String res;
        String _S;
        try {
            _S = in.nextLine();
        } catch (Exception e) {
            _S = null;
        }
        
        res = FormatString(_S);
        // bw.write(String.format("\"%s\"", res));
        System.out.println(res);
        // bw.close();
    }
}