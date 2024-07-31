    # Extract features from the input invoice
    input_features = extractFeatures(inputInvoiceText)
    print("\nInput Invoice Features:")
    for key, value in input_features.items():
        if value:
            print(f"{key}: {value.group(1)}")  # Print the extracted feature if found
        else:
            print(f"{key}: Not found")  # Print 'Not found' if the feature was not extracted
