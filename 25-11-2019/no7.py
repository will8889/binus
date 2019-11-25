def sentance_palindrome(text:str):
    text_no_space:str = ""
    for t in text.split(' '):
        text_no_space+=t
    return text_no_space == text_no_space[::-1]

print(sentance_palindrome('Rise to vote sir'))