# Inventory Management System

A Python-based command-line Inventory Management System developed to practice Object-Oriented Programming, JSON file handling, exception handling, logging, and automated testing.

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON File Handling
- Python Logging
- Pytest

## Features

- Manage product inventory
- Store product information using JSON
- Calculate inventory values
- Record application activity using logging
- Test inventory functionality using Pytest

## Project Structure

- `main.py` — Application entry point
- `inventory.py` — Inventory management logic
- `product.py` — Product-related functionality
- `products.json` — Inventory data
- `test_inventory.py` — Automated tests
- `requirements.txt` — Python dependencies

## Installation

1. Download or clone the repository.
2. Open a terminal in the project directory.
3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate it on Windows:

   ```powershell
   .venv\Scripts\activate
   ```

5. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## How to Run

```bash
python main.py
```

## Run Automated Tests

```bash
python -m pytest -v
```

## Future Improvements

- Django web interface
- PostgreSQL database integration
- User authentication