# Inventory Management System Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Components](#key-components)
3. [Project Structure](#project-structure)
4. [Setup and Installation](#setup-and-installation)
5. [Usage Guide](#usage-guide)
6. [Technical Details](#technical-details)
7. [Future Enhancements](#future-enhancements)

## Project Overview

The Inventory Management System is designed for efficient product tracking and business operations management.

## Key Components

### main.py

#### Function: `main()`

No description available

### __init__.py

### streamlit_inventory.py

#### Function: `scrape_product_details()`

Scrapes product details using Selenium to handle dynamic content.

#### Function: `save_inventory()`

No description available

#### Function: `load_inventory()`

No description available

#### Function: `format_price()`

No description available

#### Function: `main()`

No description available

### script.py

### generate_project_doc.py

#### Class: `ProjectScanner`

No description available

- Method `__init__()`
  - No description available
- Method `scan_directory()`
  - No description available
- Method `extract_classes_and_functions()`
  - No description available
- Method `generate_doc()`
  - No description available
### inventory/inventory_manager.py

#### Class: `InventoryManager`

No description available

- Method `__init__()`
  - No description available
- Method `add_product()`
  - No description available
- Method `remove_product()`
  - No description available
- Method `remove_product()`
  - No description available
- Method `update_product_quantity()`
  - No description available
- Method `get_product_info()`
  - No description available
- Method `get_total_inventory_value()`
  - No description available
### inventory/user_manager.py

#### Class: `UserManager`

No description available

- Method `__init__()`
  - Initializes the user manager with a default admin user.
- Method `register_user()`
  - Registers a new user if the username is not already taken.
- Method `authenticate_user()`
  - Authenticates the user and returns the User object if valid.
- Method `get_all_users()`
  - Returns the list of existing users as a dictionary.
### inventory/__init__.py

### inventory/product.py

#### Class: `Product`

No description available

- Method `__init__()`
  - No description available
- Method `update_quantity()`
  - No description available
- Method `get_product_info()`
  - No description available
### inventory/user.py

#### Class: `UserRole`

No description available

#### Class: `User`

No description available

- Method `__init__()`
  - No description available
- Method `__repr__()`
  - No description available
- Method `check_password()`
  - Verifică dacă parola introdusă este corectă (momentan fără hashing).
### inventory/cart.py

#### Class: `Cart`

No description available

- Method `__init__()`
  - No description available
- Method `add_to_cart()`
  - No description available
- Method `remove_from_cart()`
  - No description available
- Method `view_cart()`
  - No description available
- Method `calculate_cart_total()`
  - No description available
### inventory/export_manager.py

#### Class: `InventoryExporter`

No description available

- Method `to_excel()`
  - Exports the product list to an Excel file and returns the buffer.
- Method `to_pdf()`
  - Exports the product list to a PDF file and returns the buffer.
### tests/__init__.py

### tests/test_cart.py

#### Class: `TestCart`

No description available

- Method `setUp()`
  - No description available
- Method `test_add_to_cart()`
  - No description available
- Method `test_remove_from_cart()`
  - No description available
- Method `test_view_cart()`
  - No description available
- Method `test_calculate_cart_total()`
  - No description available
### tests/test_inventory_manager.py

#### Class: `TestInventoryManager`

No description available

- Method `setUp()`
  - No description available
- Method `test_add_product()`
  - No description available
- Method `test_remove_product()`
  - No description available
- Method `test_update_product_quantity()`
  - No description available
- Method `test_get_product_info()`
  - No description available
- Method `test_get_total_inventory_value()`
  - No description available
### tests/test_app.py

#### Function: `main()`

No description available

## Project Structure

```plaintext
InventoryManagementSystem/
    main.py
    __init__.py
    streamlit_inventory.py
    script.py
    generate_project_doc.py
    .git/
        info/
        branches/
        refs/
            remotes/
                George/
            heads/
            tags/
        logs/
            refs/
                remotes/
                    George/
                heads/
        objects/
            97/
            b4/
            89/
            ac/
            cc/
            9c/
            bc/
            f4/
            77/
            74/
            80/
            65/
            91/
            48/
            f2/
            a1/
            7b/
            info/
            96/
            06/
            88/
            d6/
            f3/
            32/
            b2/
            01/
            b1/
            3b/
            d2/
            58/
            38/
            81/
            a8/
            df/
            70/
            76/
            75/
            3c/
            46/
            ef/
            e8/
            8d/
            8f/
            53/
            c0/
            98/
            db/
            33/
            26/
            pack/
            da/
            92/
            99/
            fe/
            2f/
            47/
            8c/
            1b/
            28/
            11/
            20/
            1a/
            e5/
            5e/
            ae/
            71/
            5f/
            bf/
            54/
            c4/
            c6/
            1c/
            5b/
            4f/
            7f/
            23/
            85/
            9d/
            0d/
            63/
            6e/
            21/
            f5/
            fb/
            b0/
            f8/
            f0/
            45/
            f7/
            6f/
            fc/
            aa/
            3e/
            0f/
            3f/
            4e/
            73/
            ea/
            30/
            3d/
            dc/
            05/
            d1/
            4a/
            a0/
            44/
            19/
            00/
            fa/
            09/
            13/
            e6/
            66/
            49/
            27/
            2c/
            4c/
            61/
            be/
            a6/
            57/
            b8/
            0c/
            b5/
            a2/
            eb/
            a3/
            bd/
            1d/
            29/
            1e/
            2a/
            6c/
            51/
            1f/
            d0/
            94/
            5c/
            04/
            31/
            ca/
            43/
            56/
            6b/
            ad/
            e3/
            d4/
            d7/
            e7/
            17/
            cf/
            a4/
            2d/
            12/
            b6/
            62/
            84/
            39/
            c2/
            36/
            ee/
            25/
            a7/
            40/
            f9/
            ed/
            b7/
            3a/
            2b/
            d5/
            64/
            6d/
            a9/
            83/
            5a/
            87/
            9a/
            7e/
            24/
            41/
            a5/
            0e/
            cb/
            d9/
            c1/
            ce/
            ab/
            c3/
            72/
            c5/
            69/
            55/
            f6/
            c9/
            c7/
            ba/
            07/
            22/
            18/
            d3/
            16/
            c8/
            d8/
            8e/
            7d/
            6a/
            ec/
            af/
            9f/
            e2/
            82/
            e0/
            0a/
            90/
            8a/
            68/
            fd/
            4b/
            ff/
            bb/
            42/
            7c/
            9e/
            02/
            5d/
            34/
            dd/
            b9/
            4d/
            b3/
            2e/
            de/
            8b/
            35/
            93/
            60/
            08/
            e1/
            37/
            15/
            59/
            9b/
            03/
            f1/
            cd/
            14/
            50/
            95/
            e4/
            67/
            e9/
            52/
            78/
            7a/
            10/
            0b/
            79/
            86/
        hooks/
    inventory/
        inventory_manager.py
        user_manager.py
        __init__.py
        product.py
        user.py
        cart.py
        export_manager.py
    tests/
        __init__.py
        test_cart.py
        test_inventory_manager.py
        test_app.py
```

## Setup and Installation

### Prerequisites

- Python 3.11 or higher
- PostgreSQL database

### Installation Steps

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
```bash
python init_db.py
```

## Usage Guide

Run the application:
```bash
python -m streamlit run streamlit_app.py
```

Access the app at `http://localhost:8501`

## Technical Details

- Uses PostgreSQL for data persistence
- Integrates RESTful APIs for external product synchronization
- Implements role-based access control

## Future Enhancements

- Add analytics dashboard
- Implement real-time alerts
- Enhance caching for performance

