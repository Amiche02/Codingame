import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int initialTx = in.nextInt(); // Thor's starting X position
        int initialTy = in.nextInt(); // Thor's starting Y position

        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); // The remaining amount of turns Thor can move. Do not remove this line.

            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");
            String actionX = "";
            String actionY = "";
            String action;
            if (lightX < initialTx){
                actionX = "W";
                lightX += 1;
            }else if(lightX > initialTx){
                actionX = "E";
                lightX -= 1;
            }

            if (lightY < initialTy){
                actionY = "N";
                lightY += 1;
            }else if(lightY > initialTy){
                actionY = "S";
                lightY -= 1;
            }


            if ((lightX < initialTx) &  (lightY < initialTy)){
                action = actionX + actionY;
            }else {
                action = actionY + actionX;
            }

            // A single line providing the move to be made: N NE E SE S SW W or NW
            System.out.println(action);
        }
    }
}