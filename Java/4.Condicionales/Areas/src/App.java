import java.util.*;
import javax.swing.*;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner lectura = new Scanner(System.in);
        System.out.println("Elige una figura a revisar: \n1. Cuadrado\n2. Triangulo");
        int figura = lectura.nextInt();

        switch (figura) {
            case 1:
                int lado = Integer.parseInt(JOptionPane.showInputDialog("Introduce el número de lados"));
                System.out.println("El area del cuadrado: " + Math.pow(lado, 2));
                break;
        
            default:
                break;
        }
        lectura.close();
    }
}
