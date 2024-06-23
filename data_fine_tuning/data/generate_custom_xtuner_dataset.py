import json
import random


def generate_simple_text():
    texts = [
        "Machine learning is a subset of artificial intelligence.",
        "Natural language processing deals with human-computer interaction.",
        "Deep learning uses artificial neural networks for complex tasks.",
        "Artificial intelligence has applications in various fields.",
        "Data science combines statistics, mathematics, and computer science."
    ]
    return random.choice(texts)


def create_dataset(num_samples=5):
    dataset = []
    for _ in range(num_samples):
        sample = {
            "conversation": [
                {
                    "input": "",
                    "output": generate_simple_text()
                }
            ]
        }
        dataset.append(sample)
    return dataset


def main():
    dataset = create_dataset()
    with open('custom_xtuner_dataset_v0.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
    print("Dataset generated and saved as 'custom_xtuner_dataset_v0.json'")


if __name__ == "__main__":
    main()
