# # task 1 Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова,
# # що складаються не менше ніж з семи літер.
# import re
#
# with open('input.txt', 'w') as file:
#     file.write("In late summer, the hibiscus bloomed freely."
#                "But as I left the house one day, something caught my eye."
#                "In the middle of all those pristine white blooms was a solitary purple flower.")
#
# with open('input.txt', 'r') as file:
#     text = file.read()
#     word_pattern = r'\b[a-zA-Z-]{7,}\b'
#     filtered_words = re.findall(word_pattern, text)
#
# get_words = [word for word in filtered_words if len(word) >= 7]
#
# with open('output.txt', 'w') as file:
#     file.write("\n".join(get_words))
#
# task 2 Даний текстовий файл. Підрахувати кількість слів у ньому.
#
# user_input = input("Please enter a text: ")
#
# with open('user_input.txt', 'w') as file:
#     file.write(user_input)
#
# with open('user_input.txt', 'r') as file:
#     text = file.read()
#     word_count = len(text.split())
#
# print(f"The number of words in the text is: {word_count}")
#
