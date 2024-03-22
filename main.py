# This is the main function to identify sentence types - it follows a very strict detection process - so it may make mistakes. 
def classify_sentence(sentence):
    
    # Lists of common coordinating and subordinating conjunctions - not finite
    coordinating_conjunctions = {"for", "and", "nor", "but", "or", "yet", "so"}
    subordinating_conjunctions = {"because", "since", "as", "although", "though", "while", "if", "unless", "until", "provided", "assuming", "even though", "in case"}
    
    # Split the sentence into words
    words = sentence.lower().split()
    
    # Flags for detecting conjunctions
    has_coordinating_conjunction = any(cc in words for cc in coordinating_conjunctions)
    has_subordinating_conjunction = any(sc in words for sc in subordinating_conjunctions)
    
    # Basic classification based on the presence of conjunctions
    if has_coordinating_conjunction and has_subordinating_conjunction:
        return "compound-complex"
    elif has_coordinating_conjunction:
        return "compound"
    elif has_subordinating_conjunction:
        return "complex"
    else:
        return "simple"

# This is a functions you can use to integrate the above anywhere seamlessly into your program.
def main():
    sentence = input("Enter a sentence: ")
    classification = classify_sentence(sentence)
    print(f"The sentence is likely {classification}.")
