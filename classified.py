
target_words = ["james", "london", "mi6", "classified", "paris", "midnight", "nuclear", "asset"]

def remove_target_words(Classifier):

    Classifier = Classifier.split()

    for i in Classifier:
        if i in target_words:
            index = Classifier.index(i)
            Classifier[index] = "[REDACTED]"

    Classifier = " ".join(Classifier)
    Classifier += "."
    Classifier = Classifier.capitalize()

    
    return Classifier


def main():
    Classifier = input("What is the report? ").lower()
    Classifier = Classifier.replace(".", " ")

    Classified = remove_target_words(Classifier) 

    print("Here is your classified report: " + Classified)

main()