def convert_to_snake_case(pascal_or_camel_string):
    snake_cased_char_list = ['_'+char.lower() if char.isupper() else char for char in pascal_or_camel_string]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    choice = input("Enter a pascal or camel string: ")
    print (convert_to_snake_case(choice))
    
main()