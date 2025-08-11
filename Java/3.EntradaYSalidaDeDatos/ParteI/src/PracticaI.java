import java.util.Scanner;

public class PracticaI {
    public static void main(String[] args) {
        
        Scanner nuevoScanner;
        nuevoScanner = new Scanner(System.in);
        
        System.out.println("introduce tu edad: ");

        int edad =  nuevoScanner.nextInt();

        System.out.println( "El año que viene cumpliras: " +  (edad + 1) );
        
        nuevoScanner.close();
        
    }
}
