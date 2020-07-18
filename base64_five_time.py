#  Peyton Thomas 18 JUL 2020

"""
This program encode the string 5 times in base64 format, each encode after the first uses the string from the
previous encoding to do the job.
"""


import base64


def base5tencode(data):
    # first encode
    # put the desired message as an argument for the function
    encoded_text1 = base64.b64encode(data.encode("utf-8"))
    encoded_data1 = str(encoded_text1, "utf-8")
    # second encode
    encoded_text2 = base64.b64encode(encoded_data1.encode("utf-8"))
    encoded_data2 = str(encoded_text2, "utf-8")
    # third encode
    encoded_text3 = base64.b64encode(encoded_data2.encode("utf-8"))
    encoded_data3 = str(encoded_text3, "utf-8")
    # fourth encode
    encoded_text4 = base64.b64encode(encoded_data3.encode("utf-8"))
    encoded_data4 = str(encoded_text4, "utf-8")
    # fifth encode
    encoded_text5 = base64.b64encode(encoded_data4.encode("utf-8"))
    encoded_data5 = str(encoded_text5, "utf-8")
    # output
    print("This is the encoded data after five cycles: ", encoded_data5)  # should be long
    return encoded_data5


def base5tdecode(data_encoded):
    # going from 5-1 for decoding
    # first decode
    decode_text5 = base64.b64decode(data_encoded)
    decoded_data5 = str(decode_text5, "utf-8")
    # second decode
    decode_text4 = base64.b64decode(decoded_data5)
    decoded_data4 = str(decode_text4, "utf-8")
    # third decode
    decode_text3 = base64.b64decode(decoded_data4)
    decoded_data3 = str(decode_text3, "utf-8")
    # fourth decode
    decode_text2 = base64.b64decode(decoded_data3)
    decoded_data2 = str(decode_text2, "utf-8")
    # fifth decode
    decode_text1 = base64.b64decode(decoded_data2)
    decoded_data1 = str(decode_text1, "utf-8")
    # output
    print("This is the original message: ", decoded_data1)
    return decoded_data5


# Main function
def main():
    input_message = input(str("Enter the phrase you would like encoded: "))  # string value
    base5tencode(input_message)
    decode_input_message = input(str("Enter the phrase you would like decoded: "))  # long b64 value
    base5tdecode(decode_input_message)


#  Executes main function
if __name__ == '__main__':
    main()
