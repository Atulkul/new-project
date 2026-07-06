import re

def mail_addr_validator(mailid):
    """ Validate the mail address by checking the pattern [a-z,A-Z,0-9]+@+[a-z,A-Z]+.+[a-z,A-Z]
    """
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]+$'
    return re.match(pattern, mailid) is not None

if __name__ == "__main__":
    input_mailid = input("Enter the mail address to validate: \n")
    result = mail_addr_validator(input_mailid)
    print(f"The mail address '{input_mailid}' is {'valid' if result else 'invalid'}.")