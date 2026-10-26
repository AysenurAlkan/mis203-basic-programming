# Week 5 Lab - Reusable Shipping Quote

## Test Run
- Input: `unit_price = 30.0`, `quantity = 4` (Subtotal = $120.00)
- Output: Discount Rate = 10%, Shipping Fee = $0.00, Final Total = $108.00

## Change After Testing
- Fixed `get_discount_rate` condition from `subtotal > 100.0` to `subtotal >= 100.0` so boundary orders of exactly $100 receive the 10% discount.

## Difference Between `print` and `return`
- `return` passes a value back to the code to be used in calculations or `assert` checks.
- `print()` only displays text on the screen and returns `None`.
