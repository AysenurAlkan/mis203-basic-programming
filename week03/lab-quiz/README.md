## Boundary Test Cases

| Test Case | Order Amount | Available Stock | Requested Quantity | Is Member? | Expected Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Just Below (499.99 TRY)** | 499.99 | 10 | 2 | yes | **Approved** - Stock sufficient. No discount applied. Final Price: **499.99 TRY** |
| **Exactly At (500.00 TRY)** | 500.00 | 10 | 2 | yes | **Approved** - Stock sufficient. 10% discount applied. Final Price: **450.00 TRY** |
| **Above (500.01 TRY)** | 500.01 | 10 | 2 | yes | **Approved** - Stock sufficient. 10% discount applied. Final Price: **450.01 TRY** |
| **Boundary: Non-Member** | 500.00 | 10 | 2 | no | **Approved** - Stock sufficient. No discount applied. Final Price: **500.00 TRY** |
| **Reject: Insufficient Stock** | 600.00 | 3 | 5 | yes | **Rejected** - Insufficient stock. No final price shown. |
| **Reject: Invalid Quantity** | 600.00 | 10 | 0 | yes | **Rejected** - Invalid quantity. No final price shown. |
