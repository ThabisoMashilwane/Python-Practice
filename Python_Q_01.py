"""
Python Practice (Medium) — Inputs, Types, Casting, Lists, Dicts, Conditionals

Goal:
- Practice: print(), type(), input(), casting (int/float/str), lists, dictionaries, if/elif/else
- Get comfortable researching built-in functions and methods like you would in real programming.

How to use:
1) Open this file in VS Code (or any editor).
2) Work through the tasks in order.
3) Run the file:
   python python_exercise_medium.py

Research tips (try these in Python):
- help(str), help(list), help(dict)
- dir(str), dir(list), dir(dict)
- Search online for: "python strip", "python split", "python isdigit", "python dict get", "python round"
"""

# -------------------------------------------------------------------
# IMPORTANT RULES (for the student)
# -------------------------------------------------------------------
# - You may use: print, type, input, int, float, str, lists, dicts, if/elif/else
# - You are ENCOURAGED to research functions/methods when you get stuck.
# - Stretch section includes loops (optional). If you haven't learned loops yet,
#   treat it as a "research challenge".
# -------------------------------------------------------------------


def pause():
    """Small pause between tasks so the output is easier to read."""
    input("\nPress Enter to continue...")


# -------------------------------------------------------------------
# TASK 1 — Inputs + types + string cleaning (medium)
# -------------------------------------------------------------------
def task_1_name_cleaning():
    """
    Ask the user for their full name, but handle messy input.

    Requirements:
    - Ask: "Enter your full name: "
    - Clean the input:
      * Remove leading/trailing spaces
      * Replace multiple spaces between names with a single space (research!)
    - Print:
      1) The cleaned name
      2) The type of the cleaned name
      3) A greeting using the cleaned name in Title Case (research .title())
      4) The user's initials (example: "Ada Lovelace" -> "A.L.")
         Hint: split the name into parts (research: str.split)

    Notes:
    - You may assume the user enters at least a first name and last name.
    - Use only what you've learned + research.
    """
    print("\n--- Task 1: Name cleaning ---")

    # TODO: get raw input
    # raw_name = input("Enter your full name: ")

    # TODO: clean name (strip, fix multiple spaces)
    # cleaned = ...

    # TODO: print cleaned name and type
    # print("Cleaned name:", cleaned)
    # print("Type:", type(cleaned))

    # TODO: greeting in Title Case
    # print("Greeting:", ...)

    # TODO: initials
    # print("Initials:", ...)


# -------------------------------------------------------------------
# TASK 2 — Safe casting (medium-hard)
# -------------------------------------------------------------------
def task_2_safe_age():
    """
    Ask for age and handle bad input without crashing.

    Requirements:
    - Ask: "Enter your age (whole number): "
    - If the input is made of digits only:
        * Convert to int
        * Print: "Next year you will be X"
        * Print the type of the converted age
      Else:
        * Print: "That doesn't look like a whole number."

    Research:
    - str.isdigit()

    Extra:
    - If age is < 0 or > 120, print "Age out of range."
    """
    print("\n--- Task 2: Safe age casting ---")

    # TODO: get age_str = input(...)
    # TODO: if age_str.isdigit(): convert and validate range
    # TODO: else: message


# -------------------------------------------------------------------
# TASK 3 — If/elif/else decision tree (medium)
# -------------------------------------------------------------------
def task_3_membership_gate():
    """
    Simple decision logic based on age.

    Rules:
    - Ask the user for their age again (reuse Task 2 ideas).
    - If age is invalid, print an error and return.

    If valid:
    - age < 18  -> "You qualify for the youth plan."
    - 18–59     -> "You qualify for the standard plan."
    - 60+       -> "You qualify for the senior plan."

    Extra:
    - Print a different message if age is exactly 18.
    """
    print("\n--- Task 3: Membership gate ---")

    # TODO: input and safe cast
    # TODO: apply if/elif/else rules


# -------------------------------------------------------------------
# TASK 4 — Lists from user input (medium-hard)
# -------------------------------------------------------------------
def task_4_language_list():
    """
    Create a list from user input and do checks.

    Requirements:
    - Ask: "Enter 3 programming languages separated by commas: "
      Example input:  python, JavaScript,  SQL
    - Convert that into a list of 3 cleaned strings:
      * remove extra spaces around each item (research: strip)
    - If the user did NOT enter 3 items, print an error.
    - Otherwise:
      1) Print the list
      2) Print the first and last items
      3) Print whether "python" is in the list (case-insensitive)

    Research ideas:
    - str.split(",")
    - str.strip()
    - case-insensitive comparison (e.g., .lower())

    Hint:
    - You can clean three items one-by-one, OR research list comprehensions.
    """
    print("\n--- Task 4: Language list ---")

    # TODO: raw = input(...)
    # TODO: parts = raw.split(",")
    # TODO: clean parts
    # TODO: validate length == 3
    # TODO: do outputs/checks


# -------------------------------------------------------------------
# TASK 5 — Dictionaries + conditionals (medium-hard)
# -------------------------------------------------------------------
def task_5_simple_shop():
    """
    Build a tiny shop using a dictionary.

    Starter catalog (you may add more):
    - "chips": 15.0
    - "juice": 12.0
    - "water": 10.0
    - "chocolate": 18.5

    Requirements:
    - Create a dict called catalog mapping item -> price (float).
    - Ask: "What item do you want? "
      * Clean the input (strip + lower recommended).
    - If the item exists in catalog:
        * Ask for quantity (whole number)
        * Compute line total = price * quantity
        * Print line total rounded to 2 decimals (research: round)
      Else:
        * Print: "Item not found."
        * Print the available items (hint: catalog keys)

    Extra:
    - If quantity is invalid, print an error (reuse Task 2).
    - If quantity is 0, print "Quantity must be at least 1."
    """
    print("\n--- Task 5: Simple shop ---")

    # TODO: create catalog dict
    # catalog = {...}

    # TODO: get item input and clean it
    # TODO: check if in catalog, then ask quantity, validate, compute totals
    # TODO: else: print available items


# -------------------------------------------------------------------
# TASK 6 — Combine list + dict into a "cart" (hard)
# -------------------------------------------------------------------
def task_6_cart_receipt():
    """
    Make a mini checkout that stores multiple items.

    Requirements:
    - Use the same catalog idea as Task 5.
    - Create an empty list called cart.
    - Collect exactly TWO items from the user:
        Item 1: name + quantity
        Item 2: name + quantity

    For each item (only if it exists in catalog and quantity is valid):
    - Append a dictionary into cart with keys:
        "name", "qty", "unit_price", "line_total"

    After collecting two items:
    - If cart has no items, print "Cart is empty" and return.
    - Otherwise compute:
        subtotal = sum of line_total for the items in cart
      (Research: sum, or add them manually if you want.)
    - Apply discount rules (if/elif/else):
        * If subtotal >= 200 -> discount = 0.10 * subtotal
        * Elif subtotal >= 100 -> discount = 0.05 * subtotal
        * Else -> discount = 0
    - total = subtotal - discount

    Print a simple receipt:
    - Each line: "name x qty = line_total"
    - Subtotal, Discount, Total (rounded to 2 decimals)

    Research ideas (choose any):
    - f-strings: f"Hello {name}"
    - round(number, 2)
    - dict.get
    """
    print("\n--- Task 6: Cart + receipt ---")

    # TODO: build catalog dict
    # TODO: cart = []
    # TODO: collect item 1 (name + qty) and validate, add to cart if valid
    # TODO: collect item 2 (name + qty) and validate, add to cart if valid
    # TODO: compute subtotal, discount, total
    # TODO: print receipt


# -------------------------------------------------------------------
# TASK 7 — Decision-only "shipping" calculator (medium-hard)
# -------------------------------------------------------------------
def task_7_shipping():
    """
    Shipping cost depends on the order total.

    Requirements:
    - Ask user for an order total (decimal is allowed), cast to float safely.
      (Research: try/except for float conversion, or keep it simple with one attempt.)
    - Shipping rules:
        * total >= 250 -> shipping = 0
        * elif total >= 150 -> shipping = 25
        * elif total >= 50 -> shipping = 40
        * else -> shipping = 60
    - Print "Shipping cost: Rxx"

    Extra:
    - If total is negative, print "Invalid total".
    """
    print("\n--- Task 7: Shipping calculator ---")

    # TODO: get total_str = input(...)
    # TODO: convert to float (research try/except)
    # TODO: apply if/elif/else shipping rules
    # TODO: print shipping cost


# -------------------------------------------------------------------
# STRETCH — Loops (optional research challenge)
# -------------------------------------------------------------------
def stretch_loop_cart():
    """
    OPTIONAL (research challenge):

    Upgrade Task 6 to allow unlimited items until the user types 'done'.

    Hints to research:
    - while loop
    - break
    - continue
    - stripping/lowering user input
    - validating input inside a loop

    If you haven't learned loops yet, skip this section.
    """
    print("\n--- Stretch: Loop-based cart (optional) ---")
    # TODO (optional): implement an unlimited cart using a while loop


def main():
    print("Python Practice (Medium) — Start\n")

    # Do tasks in order. Uncomment as you complete them.
    task_1_name_cleaning()
    pause()

    task_2_safe_age()
    pause()

    task_3_membership_gate()
    pause()

    task_4_language_list()
    pause()

    task_5_simple_shop()
    pause()

    task_6_cart_receipt()
    pause()

    task_7_shipping()
    pause()

    # Optional:
    # stretch_loop_cart()

    print("\nDone! If you finished early, attempt the Stretch task or improve your error handling.")


if __name__ == "__main__":
    main()
