#include "FinancialAsset.h"
#include <string>
#include <cstring>

using std::string;

FinancialAsset::FinancialAsset(time_t date, string symbol, double open, double high, double low, double close, long double volume)
{
    setDate(date);
    setSymbol(symbol);
    setHigh(price);
    setLow(price);
    setOpen(price);
    setClose(price);
    setVolume(volume);
}

void FinancialAsset::setDate(time_t date)
{
    Date = date;
}

void FinancialAsset::setSymbol(string symbol)
{
    Symbol = symbol;
}

void FinancialAsset::setHigh(double price)
{
    High = price;
}

void FinancialAsset::setLow(double price)
{
    Low = price;
}

void FinancialAsset::setOpen(double price)
{
    Open = price;
}

void FinancialAsset::setClose(double price)
{
    Close = price;
}

FinancialAsset::~FinancialAsset()
{
}