class CustomError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)

def process_data(data):
    """Example function that may raise a custom exception."""
    if not data:
        raise CustomError("Empty data: Cannot process an empty dataset")
    
    # Processing logic goes here
    processed_data = data.upper()
    
    return processed_data

def main():
    try:
        input_data = ""  # Simulating an empty dataset
        result = process_data(input_data)
        print(f"Processed data: {result}")
    except CustomError as e:
        print(f"CustomError caught: {e}")
        # Handle the custom exception (log, notify, etc.)
    except Exception as e:
        print(f"Unexpected error: {e}")
        # Handle other exceptions

if __name__ == "__main__":
    main()
