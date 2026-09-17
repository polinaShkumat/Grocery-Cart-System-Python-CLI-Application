# 🛒 Grocery Cart System — Python CLI Application

An interactive command-line shopping cart simulator. Users add products to
a cart (checked against live stock), can remove items back into stock, undo
their last action, and check out with an automatic 10% discount on orders
over 30€.

## Features

- **Stock-aware cart** — every product has a fixed stock quantity that
  decreases as items are added to the cart and is restored on removal
- **Input validation** — rejects unknown products or quantities exceeding
  available stock
- **Undo support** — reverses the single most recent add/remove action
- **Automatic discount** — 10% off orders over 30€ at checkout
- **Itemized receipt** — shows quantity, unit price, and line total per item

## Tech Stack

- Python 3 (standard library only)

## How to Run

```bash
python grocery_cart.py
```

Products available in the demo catalog: `apple`, `banana`, `milk`, `bread`.

## Example Session

```
1: Add (or type 'done' to end): apple
Type amount for apple: 5
Added 5 apple to our cart. There is 195 left
1: Add (or type 'done' to end): done
...
--- RECEIPT ---
apple : 5 x 2€ = 10€
Initial sum: 10€
Total price: 10€
```

## Possible Extensions

- Support multi-step undo (a full action history stack)
- Persist stock/cart state to a JSON file or database
- Add a proper checkout flow with payment simulation
- Wrap the core logic in a `Cart` class for reuse in a web app

## License

MIT
