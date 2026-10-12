### Week 04 Lab Notes

- **Test Run:** Tested with starting balance 1000 TRY, monthly deposit 500 TRY, monthly interest rate 1%, and savings goal 3000 TRY. The output matched the expected goal reached in 4 months with a final balance of 3070.80 TRY and total interest earned of 70.80 TRY.
- **Change After Testing:** Initially, interest was calculated after adding the monthly deposit. Corrected the order so that interest is calculated on the current balance first, then the deposit is added, matching the required monthly logic.
- **Input Types:** `input()` returns a string by default, so inputs were validated using a `while` loop and converted to `float()` to allow decimal calculations for monetary amounts and interest rates.
