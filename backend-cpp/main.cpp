#include <iostream>
#include <sstream>
#include <iomanip>

#include <cstdlib>
#include <mysql.h>

#include "FinancialAssets.h"

using namespace std;

int optionalOperations();

int main(int argc, char** argv)
{
    FinancialAssets* bt =
        new FinancialAssets("1970-1-1", "ABC",
                            "1.0", "1.0", "1.0", "1.0", "10.0");

    int input;
    time_t Date;
    string Symbol;
    double Open;
    double High;
    double Low;
    double Close;
    double Volume;

    while(1) {
        input = mainMenu();
        if(input == END)
            break;
        switch(input) {
        case LIST:
            bt->listFinancialAssets(); // to be included in FinancialAssets.cpp
            break;
        case INSERT:
            cout << "\nEnter date, symbol, Open, High, Low, Close, Volume: " << endl;
            cin >> Date;
            cin >> Symbol;
            cin >> Open;
            cin >> High;
            cin >> Low;
            cin >> Close;
            cin >> Volume;
            bt->insertFinancialAssets(new FinancialAssets(date, symbol, open, high, low, close, volume)); // to be included in FinancialAssets.cpp
            break;
        case DELETE:
            cout << "\nEnter date and symbol to delete a record: " << endl;
            cin >> Date;
            cin >> Symbol;
            bt->deleteFinancialAsset(acno); // to be included in FinancialAssets.cpp
            break;
        default:
            cerr << "Invalid input!" << endl;
            break;
        }
    }
    return 0;
}

int optionalOperations()
{
    cout << "\nOptional Operations" << endl
         << "1. List all financial assets" << endl 
         << "2. Insert a new financial asset" << endl
         << "3. Delete an existing financial asset" << endl;
    int ch;
    cin >> ch;
    return ch;
}
