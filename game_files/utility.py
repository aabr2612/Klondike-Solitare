# Movement check for the tableaus, foundations and waste and their indexes
def validate_movement(source,destination,source_index,destination_index):
    # If the source or destination is not tableaum foundation or waste
    if (source not in ["T", "F", "W"] or destination not in ["T", "F"]) or (source=="F" and destination=="F"):
        return False

    # If indexes are not in numbers
    if not (str(source_index).isnumeric() and str(destination_index).isnumeric()):
        return False
    
    source_index = int(source_index)
    destination_index = int(destination_index)
    
    # If tableau index not in range of tableaus
    if source == "T":
        if source_index < 1 or source_index > 7:
            return False

    # If foundation index not in range of foundations
    elif source == "F":
        if source_index < 1 or source_index > 4:
            return False

    # If tableau index not in range of tableaus
    if destination == "T":
        if destination_index < 1 or destination_index > 7:
            return False
    # If foundation index not in range of foundations
    elif destination == "F":
        if destination_index < 1 or destination_index > 4:
            return False
    
    # If both have same indexes and same destination and source
    if source==destination and destination_index==source_index:
        return False

    return True

# Validation movements for multiple card movements
def valid_move(source_index,destination_index):
    # If indexes are not in numbers
    if not (str(source_index).isnumeric() and str(destination_index).isnumeric()):
        return False
    
    source_index = int(source_index)
    destination_index = int(destination_index)

    # If tableau index not in range of tableaus
    if source_index < 1 or source_index > 7:
            return False
    if destination_index < 1 or destination_index > 7:
            return False
    
    # If both have same indexes
    if destination_index==source_index:
        return False
    
    return True

# Function to capitalize the card name alphabets
def capitalize_card_name(card_name):
    return card_name[:-1] + card_name[-1].upper()