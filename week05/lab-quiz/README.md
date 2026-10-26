# Week 5 Lab - Reusable Shipping Quote

## Test Run
- Input: unit_price = 30.0, quantity = 4 (Subtotal = 120.0)
- Output: Discount Rate = 10%, Shipping Fee = 0.0, Final Total = 108.0

## Change After Testing
- Initially, `get_discount_rate` checked `subtotal > 100.0`. During threshold testing (`subtotal = 100.0`), it returned 0% instead of 10%. Changed the condition to `subtotal >= 100.0` so boundary values receive the discount properly.
