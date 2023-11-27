import emoji

emoji_input = input("Input: ")
emojized_input = emoji.emojize(emoji_input)
print(f"Output: {emojized_input}")