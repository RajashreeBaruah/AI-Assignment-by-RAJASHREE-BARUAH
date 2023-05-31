from langdetect import detect

input_lang = input("Enter text: ")
output_lang = detect(input_lang)

print("The language is ", output_lang)