// #include<stdio.h>
// #include<conio.h>
// int main()
// {
// int n = 100200300;
// int b=n;
// int c = n;
// int countn = 0;
// int countz=0;
// while (b!=0)
// {
//    b/=10;
//     countn++;
// }
// for (int i = 0; i <countn; i++)
// {
// if(c%10==0){
// countz++;
// }
// c/=10;
// }
// printf("%d",countz);
//     return 0;
// }
// #include <stdio.h>

// int main() {
//     int n = 100200300;
//     int c = n;
//     int countz = 0;

//     while (c != 0) {
//         if (c % 10 == 0) {
//             countz++;

//         }else
//         {
// printf("%d", c % 10);
//         }

//         c /= 10;
//     }

//     printf("Number of zeros = %d\n", countz);
//     return 0;
// }
// #include <stdio.h>

// int main() {
//     int n = 100200300;
//     int c = n;
//     int countz = 0;
//     int digits[20];  // assuming max 20 digits
//     int idx = 0;

//     while (c != 0) {
//         int d = c % 10;
//         if (d == 0)
//             countz++;
//         else
//             digits[idx++] = d;  // store non-zero digits
//         c /= 10;
//     }

//     // Now print in reverse (left-to-right order)
//     printf("Non-zero digits (L->R): ");
//     for (int i = idx - 1; i >= 0; i--) {
//         printf("%d", digits[i]);
//     }

//     printf("\nNumber of zeros = %d\n", countz);

//     return 0;
// }
#include <stdio.h>

int main()
{
    int n = 100200300;
    int temp = n;
    int rev = 0, countz = 0;

    // Step 1: Reverse the number
    while (temp != 0)
    {
        rev = rev * 10 + temp % 10;
        temp /= 10;
    }

    // Step 2: Process reversed number
    while (rev != 0)
    {
        int digit = rev % 10;
        if (digit != 0)
            printf("%d", digit);
        rev /= 10;
    }

    // printf("\nNumber of zeros = %d\n", countz);
    return 0;
}
