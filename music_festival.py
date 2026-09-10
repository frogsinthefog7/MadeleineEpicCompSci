
musicians = {}

def new_musician(musician):
    global musicians

    musicians[musician] = 1

    return 

def new_count(musician):
    global musicians

    if musician == "Done":
        return

    
    musician_votes = musicians.get(musician)
    if musician_votes == None:
        new_musician(musician)
    else:
        musician_votes = musician_votes + 1
        musicians[musician] = musician_votes

    return 
 
def main():

    print("Enter all musicians voted for until done.\nTo compile all votes, type \"done\" into votes bar.")

    user_input = input("Enter a musician: ")
    user_input = user_input.lower()
    user_input = user_input.title()
    new_count(user_input)

    while user_input != "Done":
        user_input = input("Enter a musician: ")
        user_input = user_input.lower()
        user_input = user_input.title()
        new_count(user_input)


    print("Votes")
    print("--------------")

    for i in musicians:
        print(f"{i}: {musicians[i]}")

main()