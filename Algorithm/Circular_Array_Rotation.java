import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int q = in.nextInt();
        int[] a = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        int temp1;
        
        for(int i=0;i<k;i++)
            {
            int last = a[n-1];
            int temp = a[0];
            for(int j=0;j<a.length-1;j++)
                {
                temp1 = a[j+1];
                a[j+1] = temp;
                temp = temp1;
                }
            a[0] = last;    
          }
        for(int a0 = 0; a0 < q; a0++){
            int m = in.nextInt();
            System.out.println(a[m]);
            
        }
    }
}

