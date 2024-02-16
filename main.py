def calculate_accuracy(ground_truth_answers, predicted_answers):
    """Calculates exact-match accuracy for a question-answering task"""
    num_correct = 0
    for gt_answer, pred_answer in zip(ground_truth_answers, predicted_answers):
        if gt_answer == pred_answer:
            num_correct += 1
    accuracy = num_correct / len(ground_truth_answers)
    return accuracy


if __name__ == '__main__':
    # Sample PopQA Data (Adapt this to your actual dataset loading)
    questions = ["What color is the sky?", "Who is the current US president?"]
    ground_truth_answers = ["blue", "Joe Biden"]

    # Replace with your model's prediction logic
    predicted_answers = ["blue", "Donald Trump"]

    # Calculate test accuracy
    accuracy = calculate_accuracy(ground_truth_answers, predicted_answers)
    print("Test Accuracy:", accuracy)