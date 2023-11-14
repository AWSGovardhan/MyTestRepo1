def calculate_product(**kwargs):
    # Check if 'numbers' key is present in kwargs
    if 'numbers' in kwargs:
        numbers = kwargs['numbers']
        product = 1

        # Calculate the product of the numbers
        for num in numbers:
            product *= num

        print(f"The product of the numbers is: {product}")
    else:
        print("No 'numbers' key found in kwargs.")

# Example calls to the function
calculate_product(numbers=[2, 3, 4])
calculate_product(numbers=[5, 6, 7, 8])
calculate_product()
