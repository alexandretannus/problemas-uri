import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    
    public static void main(String[] args) throws IOException {
        
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);
        
        int  num;
        long result;
        
        num = Integer.parseInt(in.readLine());
        for (int i = 2; i <= num; i++) {
            if(i % 2 == 0) {
                result = i * i;
                System.out.printf("%d^2 = %d\n", i, result);
            }
        }
    }
}