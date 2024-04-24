import emoji

input = input("Input: ")
lang = "en"

if "_" not in input:
    lang = "alias"
elif "_" in input:
    lang = "en"

if "earth_asia" in input:
    input = input.replace("earth_asia", "globe_showing_Asia-Australia").strip()
    lang = "alias"

# print(input, lang)

print("Output: " + emoji.emojize(input, language=lang))
