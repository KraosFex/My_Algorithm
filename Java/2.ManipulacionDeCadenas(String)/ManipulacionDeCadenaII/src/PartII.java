// para terminar este ejercicio aun me falta un poco mas de conocimiento.
public class PartII {
    public static void main(String[] args) {
        String Frase;
        Frase = "Hola persona del mundo, ¿como estas?";
         
        String palabra;

        byte count;
        count = 0;

        for (byte i = 0; i <= Frase.length() - 1 ; i++) {
            if(Frase.charAt(i) == ' ' || i == Frase.length() - 1) {
                if(Frase.charAt(i - 1) == ',') {
                    palabra = Frase.substring( i - count , i - 1);
                } else {
                    palabra = Frase.substring( i - count , i);
                }
                System.out.println("Esta es una palabra: " + palabra);   
                count = 0;
            }
            count++;
        }

    }
}
