
special_characters = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_",'=','+','{','}',"[","]","|",':',";",'"',"'",".","?","/"]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def main():
    plate = list(input("Plate: ").lower())

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):

    plate_len = len(plate)
    if plate_len < 2 or plate_len > 6:
        return False

    for i in plate:
        i_index = plate.index(i)
        if plate[i_index] in special_characters:
            return False

    if plate[0] == "0":
        return False

    if plate[0] in numbers or plate[1] in numbers:
        return False


    for i in range(plate_len):

        current_index = i
        previous_index = i - 1

        if current_index == 0:
            pass
        elif plate[previous_index] in numbers and plate[current_index] in letters:
            return False
        else:
            pass

    return True

main() 