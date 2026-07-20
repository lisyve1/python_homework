print("hello!") # this is my code in python.
##########################################################################
def greet(name):
    return f"Hello!, {name}!" 
print(greet("Lissette"))

def hello(): ## This function returns a greeting message.
    return "Hello!"
############################################################################

def calc(x, y, operation="multiply"):
    try:
        match operation:
            case "add": return x + y
            case "subtract": return x - y
            case "multiply": return x * y
            case "divide": return x / y
            case "modulo": return x % y
            case "int_divide": return x // y
            case "power": return x ** y
            case _: return "Invalid operation"

    except ZeroDivisionError:
        return "cant divide by 0!"
    except TypeError:
        return "can't multiply those values!"

print(calc(5, 0, "add"))
print(calc(5, 0, "subtract"))
print(calc(5, 0, "multiply"))
print(calc(5, 0, "modulo"))
print(calc(5, 0, "int_divide"))
print(calc(5, 0, "divide"))
print(calc(5, 0, "power"))
print(calc(5, 0, "invalid"))
#############################################################################

def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return value  # For unsupported types, return the original value
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."


print(data_type_conversion("123", "int"))
print(data_type_conversion("123.45", "float"))
print(data_type_conversion("True", "str"))
print(data_type_conversion("abc", "int"))
print(data_type_conversion("123", "list"))


################################################################################################



######################################################################################################




def grade(*args):
    try:
        average = sum(args) / len(args)
        grades = {90: "A", 80: "B", 70: "C", 60: "D", 0: "F"}
        for cutoff, letter in grades.items():
            if average >= cutoff:
                return letter
    except:
        return "Invalid data was provided."

    # Test
print(grade(95, 88, 92))        # A
print(grade(85, 82, 88))        # B
print(grade(75, 72, 78))        # C
print(grade(65, 62, 68))        # D
print(grade(50, 55, 45))        # F
print(grade(95, "A", 88))       # Invalid data was provided.
print(grade())                  # Invalid data was provided.


############################################################################################################

def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
        print(f"Step {i + 5}: {result}")
    return result

# Test the repeat function directly (no input needed):
repeat("Code The Dream", 5)


##############################################################################################################
def student_scores(option, **kwargs):
    if option == "best":
        return max(kwargs, key=kwargs.get)
    elif option == "mean":
        return sum(kwargs.values()) / len(kwargs) if kwargs else 0

print(student_scores("best", Elsa=85, Divante=92, Charles=78))  # divante has the best score

################################################################################################################

def titleize(string):
    little = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words)-1 or word.lower() not in little:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()
    return " ".join(words)

# Test
print(titleize("the lord is my shepard"))   # The Lord is My Shepard
print(titleize("a  promise of hope"))       # A Promise of Hope
print(titleize("the story of creation"))    # The Story of Creation


#########################################################################################################################

def hangman(secret, guess):
    print(f"Secret word: {secret}")
    print(f"Guessed letters: {guess}")

    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
            print(f"  '{letter}' is in guess → keep it")
        else:
            result += "_"
            print(f"  '{letter}' is NOT in guess → replace with _")

    print(f"Result: {result}")
    return result

# Test
hangman("alphabet", "ab")

##########################################################################################################################################

def pig_latin(text):
    words = text.split()
    pig_latin_words = []
    for word in words:
        if word[0].lower() in "aeiou":
            pig_latin_word = word + "way"
        else:
            pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)
    return " ".join(pig_latin_words)

# Test
print(pig_latin("apple")) 
print(pig_latin("banana")) 
print(pig_latin("cherry")) 