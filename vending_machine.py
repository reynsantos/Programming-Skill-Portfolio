import sqlite3
import pygame
import requests
from io import BytesIO
import tempfile

# Initialize pygame mixer for music
pygame.mixer.init()

# URL of royalty-free vending machine-style music
music_url = 'https://filesamples.com/samples/audio/mp3/sample2.mp3'

# Function to play music from a URL
def play_music_from_url(url):
    try:
        # Download the audio file
        print("Downloading music...")
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Create a temporary file to store the audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
            temp_audio_file.write(response.content)
            temp_audio_path = temp_audio_file.name

        # Load and play the audio
        pygame.mixer.music.load(temp_audio_path)
        pygame.mixer.music.play(-1)  # Loop the music indefinitely

        print("Music is now playing...")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the music: {e}")
    except pygame.error as e:
        print(f"Error playing the music: {e}")

# Play music from URL
play_music_from_url(music_url)


# Function to connect to the database and fetch products
def load_products_from_db():
    conn = sqlite3.connect('vending_machine.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    
    products = {}
    for row in cursor.fetchall():
        product_id, name, price, category, stock = row
        products[product_id] = {"name": name, "price": price, "category": category, "stock": stock}
    
    conn.close()
    return products

# Function to update product stock in the database
def update_stock_in_db(product_id, new_stock):
    conn = sqlite3.connect('vending_machine.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Products SET stock = ? WHERE id = ?", (new_stock, product_id))
    conn.commit()
    conn.close()

# Function to display all products
def display_products(products):
    print("\n--- Available Products ---")
    for product_id, product_info in products.items():
        print(f"{product_id}. {product_info['name']} - ${product_info['price']} (Category: {product_info['category']}) - Stock: {product_info['stock']}")

def suggest_products(products, category, exclude_product_id):
    print("\n--- Suggested Products ---")
    # Filter products: same category, not the purchased product, and in stock
    suggestions = [
        product
        for product_id, product in products.items()
        if product['category'] == category and str(product_id) != str(exclude_product_id) and product['stock'] > 0
    ]

    # Display suggestions
    if suggestions:
        for product in suggestions:
            print(f"{product['name']} - ${product['price']} (Stock: {product['stock']})")
    else:
        print("No suggestions available.")



# Function to handle purchasing
def purchase_item(products):
    display_products(products)

    try:
        product_id = int(input("\nEnter the number of the product you want to buy: "))

        if product_id in products:
            product = products[product_id]
            print(f"\nYou selected: {product['name']} - ${product['price']}")
            price = product['price']
            stock = product['stock']

            if stock > 0:
                # Ask how many items the user wants to buy
                quantity = int(input(f"How many {product['name']} do you want to buy? "))

                # Ensure quantity does not exceed stock
                if quantity > stock:
                    print(f"\nSorry, only {stock} items are available in stock.")
                else:
                    total_price = quantity * price
                    money_inserted = float(input(f"\nEnter the amount of money you're inserting: $"))

                    if money_inserted >= total_price:
                        change = money_inserted - total_price
                        print(f"\n{quantity} {product['name']} dispensed.")
                        print(f"Your change: ${change:.2f}")

                        # Update stock in the dictionary and database
                        product['stock'] -= quantity
                        update_stock_in_db(product_id, product['stock'])

                        # Suggest products from the same category
                        suggest_products(products, product['category'], product_id)

                    else:
                        print("\nYou do not have enough money for this item.")
            else:
                print("\nSorry, this item is out of stock.")
        else:
            print("\nInvalid product number.")

    except ValueError:
        print("\nInvalid input. Please enter a valid number.")


# Main function to run the vending machine
def main():
    # Load products from the database into a dictionary
    products = load_products_from_db()
    
    while True:
        print("\n--- Welcome to the Mars Vending Machine ---")
        print("1. Purchase Item")
        print("2. Exit")

        try:
            choice = int(input("\nPlease select an option (1 or 2): "))

            if choice == 1:
                purchase_item(products)
            elif choice == 2:
                print("\nThank you for using the Mars Vending Machine! Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid option.")

# Run the vending machine
if __name__ == "__main__":
    main()
