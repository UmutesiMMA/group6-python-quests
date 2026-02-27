# Level 5 - Quest 24
# ask age function
def ask_for_age():
    age=int(input("What is your age? "))
    return age
# can they vote function
def can_they_vote(age):
    if age>=18:
        print("You are old enough to vote")
    else:
        print("You are not old enough to vote")

can_they_vote(ask_for_age())