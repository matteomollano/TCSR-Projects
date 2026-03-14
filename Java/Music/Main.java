import java.io.File;
import java.util.Scanner;
import javax.sound.sampled.*;

public class Main {
    public static void main(String[] args) throws Exception {

        File wav = new File("car-horn.wav");
        AudioInputStream audioStream = AudioSystem.getAudioInputStream(wav);
        Clip player = AudioSystem.getClip();

        player.addLineListener(event -> {
            if (event.getType() == LineEvent.Type.STOP) {
                synchronized (player) { player.notify(); }
            }
        });

        player.open(audioStream);

        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("Enter command (p=play, q=stop, r=reset, exit=exit program): ");
            String input = scanner.nextLine().trim().toLowerCase();

            switch (input) {
                case "p":
                    player.start();
                    break;
                case "q":
                    player.stop();
                    break;
                case "r":
                    player.setMicrosecondPosition(0);
                    break;
                case "exit":
                    running = false;
                    break;
            }
        }

        player.close();
        scanner.close();
    }
}
