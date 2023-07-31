import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load the pre-trained model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(
    model_name, num_labels=2
)  # Assuming 2 classes (positive, negative)


# Function to perform sentiment analysis
def predict_sentiment(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        predicted_label = torch.argmax(probabilities, dim=1).item()
        if predicted_label == 1:
            return "Positive"
        else:
            return "Negative"


if __name__ == "__main__":
    # Get user input and perform sentiment analysis
    while True:
        user_input = input("Enter a sentence (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting the program...")
            break
        else:
            sentiment = predict_sentiment(user_input)
            print(f"Sentiment: {sentiment}")
