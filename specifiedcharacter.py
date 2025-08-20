char_list = ["a", "b", "c"]
string = "abcd"
matched_list = [characters in char_list for characters in string]
print(matched_list)

[True, True, True, False]
string_contains_char = all(matched_list)
print(string_contains_char)