### Week 02 Lab Notes

- **Test Run:** Tested with 2 × 50 TRY and 1 × 80 TRY, shipping 20 TRY, and 10% tax. The output matched the expected total of 218.00 TRY (Subtotal: 180.00 TRY, Tax: 18.00 TRY, Shipping: 20.00 TRY).
- **Change After Testing:** Initially, the output had extra spacing inside the f-string format specifiers (`: .2f`). Corrected them to `:.2f` to ensure standard, error-free formatting for two decimal places.
- **Input Types:** `input()` returns a string by default, so inputs were converted using `int()` for quantities and `float()` for prices to perform arithmetic calculations.
