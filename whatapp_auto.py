import pywhatkit as wa

# Send a message to an individual
# wa.sendwhatmsg("+919444488330", "Hello", 20, 38, 15)

# Send a message to a group
# wa.sendwhatmsg_to_group("EMDcq9rcXpR0bW9aEZMLgj", "Hi", 20, 53, 10, True, 5)

# Send a message instantly (Mobile number, Message, Wait time, Close the browser, Wait time to close the browser)
wa.sendwhatmsg_instantly("+919444488330", "Hello", 10, True, 5)