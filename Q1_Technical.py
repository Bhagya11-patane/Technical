def get_search_suggestions(search_history, partial_query):
    # Using list comprehension to filter suggestions
    return [item for item in search_history if item.startswith(partial_query)]

def main():
    search_history = [
        "apple",
        "banana",
        "carrot",
        "pear",
        "pineapple",
        "potato",
        "strawberry"
    ]
    
    # Get user input for partial search query
    partial_query = input("Enter your partial search query: ").lower()
    
    # Get suggestions based on the search history
    suggestions = get_search_suggestions(search_history, partial_query)
    
    # Output suggestions
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)

if __name__ == "__main__":
    main()
