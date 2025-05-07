print("Mohd Jawwad Ali Farooqui,USN:1AY24AI070,SEC:O")
def list_to_string(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f'{items[0]} and {items[1]}'
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]
spam = ['apples', 'bananas', 'tofu', 'cats']
print(list_to_string(spam)) 
