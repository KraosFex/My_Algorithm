import javax.swing.JOptionPane;

public class App {
    public static void main(String[] args) throws Exception {
        String Nombre_Usuario = JOptionPane.showInputDialog("Introduce tu nombre de usuario");
        String edad = JOptionPane.showInputDialog("Introduce tu edad");
        int Edad_Usuario = Integer.parseInt(edad);
        System.out.println(Nombre_Usuario + ", Pronto va a cumplir: " + (Edad_Usuario + 1) + "Años");
    }
}
