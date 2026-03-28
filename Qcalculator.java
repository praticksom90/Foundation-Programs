import java.util.Scanner;
public class Qcalculator {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int ans = 0;

        while (true) {
            System.out.print("Enter the operator +,-,*,/,%, or 0 to exit: ");
            char op = in.next().trim().charAt(0);

            
            if (op == '0') {
                System.out.println("Calculator Closed :)");
                break;
            }

            
            
            if (op == '+' || op == '-' || op == '*' || op == '/' || op == '%') {

                System.out.print("Enter first number: ");
                int num1 = in.nextInt();
                System.out.print("Enter second number: ");
                int num2 = in.nextInt();

                switch (op) {
                    case '+':
                        ans = num1 + num2;
                        break;
                    case '-':
                        ans = num1 - num2;
                        break;
                    case '*':
                        ans = num1 * num2;
                        break;
                    case '/':
                        if (num2 != 0) {
                            ans = num1 / num2;
                        } else {
                            System.out.println("Cannot divide by zero!");
                            continue; // skip printing ans
                        }   break;
                    case '%':
                        ans = num1 % num2;
                        break;
                    default:
                        break;
                }

                System.out.println("Answer: " + ans);

            } else {
                System.out.println("Invalid operation!!");
            }
        }
        in.close();
    }
}