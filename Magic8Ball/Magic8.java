import java.util.concurrent.ThreadLocalRandom;

class Magic8 {

    static void magic8Ball() {
        int randomNum = ThreadLocalRandom.current().nextInt(0, 20);
        switch (randomNum) {
            case 0:
            System.out.println("Today it will rain.");
            break;
            case 1:
            System.out.println("You will meet a stranger today.");
            break;
            case 2:
            System.out.println("Today you will eat ice-cream.");
            break;
            case 3:
            System.out.println( "You will find £5 where you least expected to.");
            break;
            case 4:
            System.out.println( "You will argue with someone.");
            break;
            case 5:
            System.out.println( "You will get kissed today.");
            break;
            default : System.out.println( "invalid");
            }
            }
  public static void main(String[] args) {
    magic8Ball();
  }
    
};


