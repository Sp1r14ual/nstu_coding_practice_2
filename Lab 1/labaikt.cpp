#include <iostream>
#include <windows.h>
#include <locale.h>
using namespace std;

char int_symbol(int num)
{
    switch(num)
    {
        case 0: return '0';
        case 1: return '1';
        case 2: return '2';
        case 3: return '3';
        case 4: return '4';
        case 5: return '5';
        case 6: return '6';
        case 7: return '7';
        case 8: return '8';
        case 9: return '9';
        case 10: return 'A';
        case 11: return 'B';
        case 12: return 'C';
        case 13: return 'D';
        case 14: return 'E';
        case 15: return 'F';
    }
}

int symbol_int(char sym)
{
    switch(sym)
    {
        case '0': return 0;
        case '1': return 1;
        case '2': return 2;
        case '3': return 3;
        case '4': return 4;
        case '5': return 5;
        case '6': return 6;
        case '7': return 7;
        case '8': return 8;
        case '9': return 9;
        case 'A': return 10;
        case 'B': return 11;
        case 'C': return 12;
        case 'D': return 13;
        case 'E': return 14;
        case 'F': return 15;
    }
}


void to_kth_base(int number, int base) 
{
    if (number < base) 
    {
        cout << int_symbol(number);
        return;
    }
    to_kth_base(number / base, base);
    cout << int_symbol(number % base);
}

void to_tenth_base(int number, int k)
{
    //To do
    return;
}


int main() 
{
    setlocale(LC_ALL, "rus");
    int number, base;
    cout << "Введите число и систему счисления" << endl;
    cin >> number >> base;
    to_kth_base(number, base);
    return 0;
}
