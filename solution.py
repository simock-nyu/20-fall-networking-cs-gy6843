import hashlib

### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

hash = hashlib.md5(b'NYU Computer Networking').hexdigest()

items = {
    "Are encoding and encryption the same? - Yes/No": "No",
    "Is it possible to decrypt a message without a key? - Yes/No": "No",
    "Is it possible to decode a message without a key? - Yes/No": "Yes",
    "Is a hashed message supposed to be un-hashed? - Yes/No": "No",
    "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code": hash,
    "Is MD5 a secured hashing algorithm? - Yes/No": "No",
    "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number": 5,
    "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number": 3
}


def welcome_assignment_answers(question):
    #The student doesn't have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    try:
        return items[question]
    except:
        return "Invalid question"
    



if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))

    for key in items:
        print(welcome_assignment_answers(key))

    
    print(welcome_assignment_answers("bad quest"))
