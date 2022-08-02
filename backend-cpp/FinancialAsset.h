#include <string>

using std::string;

class FinancialAssets
{
public:
   static const int MAX_SIZE = 30;

   FinancialAssets(int = 0, string = "",
      string = "", double = 0.0);
   ~FinancialAssets();

   void setDate(time_t);
   void setSymbol(string);
   void setHigh(double);
   void setLow(double);
   void setOpen(double);
   void setClose(double);
   void setVolume(long double);

   time_t getDate() const;
   string getSymbol() const;
   double getHigh() const;
   double getLow() const;
   double getOpen() const;
   double getClose() const;
   long double getVolume() const;

private:
   time_t Date;
   string Symbol[MAX_SIZE];
   double Open[MAX_SIZE];
   double High[MAX_SIZE];
   double Low[MAX_SIZE];
   double Close[MAX_SIZE];
   long double Volume[MAX_SIZE];
};
