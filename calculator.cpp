#include <iostream>
using namespace std;

int main()
{
    char op;
    int fn, sn;
    float ans;

    while (true)
    {
        cout << "\nEnter operator (+, -, *, /, %) or 0 to exit: ";
        cin >> op;

        if (op == '0')
        {
            cout << "Exiting calculator. Bye!\n";
            break;
        }

        if (op == '+' || op == '-' || op == '*' || op == '/' || op == '%')
        {
            cout << "Enter first number: ";
            cin >> fn;
            cout << "Enter second number: ";
            cin >> sn;

            switch (op)
            {
            case '+':
                ans = fn + sn;
                cout << "Addition: " << ans << endl;
                break;
            case '-':
                ans = fn - sn;
                cout << "Subtraction: " << ans << endl;
                break;
            case '*':
                ans = fn * sn;
                cout << "Multiplication: " << ans << endl;
                break;
            case '/':
                if (sn != 0)
                {
                    ans = (float)fn / sn;
                    cout << "Division: " << ans << endl;
                }
                else
                {
                    cout << "Error: Divide by zero!" << endl;
                }
                break;
            case '%':
                if (sn != 0)
                {
                    cout << "Remainder: " << fn % sn << endl;
                }
                else
                {
                    cout << "Error: Divide by zero!" << endl;
                }
                break;
            }
        }
        else
        {
            cout << "Invalid operator! Try again!" << endl;
        }
    }

    return 0;
}