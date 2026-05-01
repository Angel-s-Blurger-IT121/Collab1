#Create-Deve

#Append-Jackie
def append_entry():
    try:
        date = input("Enter date: ")
        entry = input("Write your diary entry: ")

        file = open("diary.txt", "a")
        file.write(f"[{date}] {entry}\n")
        file.close()

        print("Entry added!")

    except Exception as e:
        print("Error:", e)

#Read-Sam

#Update-Sam

#Search-Jackie
def search_entry():
    try:
        keyword = input("Enter keyword/date to search: ")

        file = open("diary.txt", "r")
        found = False

        for line in file:
            if keyword.lower() in line.lower():
                print("Found:", line.strip())
                found = True

        if not found:
            print("No entry found.")

        file.close()

    except FileNotFoundError:
        print("Diary file not found.")
    except Exception as e:
        print("Error:", e)

#Delete-Jackie
def delete_entry():
    try:
        date_to_delete = input("Enter date to delete: ")

        file = open("diary.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("diary.txt", "w")

        found = False
        for line in lines:
            if date_to_delete not in line:
                file.write(line)
            else:
                found = True

        file.close()

        if found:
            print("Entry deleted!")
        else:
            print("Date not found.")

    except FileNotFoundError:
        print("Diary file not found.")
    except Exception as e:
        print("Error:", e)

#Main Menu-Devw
