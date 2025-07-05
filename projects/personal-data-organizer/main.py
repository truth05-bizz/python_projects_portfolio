class User:
    def __init__(self, first_name, last_name, age, dob, contact, interests):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dob = dob
        self.contact = contact
        self.interests = interests

class PersonalDataOrganizer:
    def __init__(self):
        self.users = []

    def add_user(self, first_name, last_name, age, dob, contact, *interests):
        interest_set = set(i.strip().lower().capitalize() for i in interests)
        user = User(first_name, last_name, age, dob, contact, interest_set)
        self.users.append(user)

    def search_user(self, name):
        matches = [x for x in self.users if x.first_name.lower() == name.lower()]

        if not matches:
            print(f"No user found with first name '{name}'.")
            return

        if len(matches) == 1:
            user = matches[0]
            print("User Found............")
            print(f"User Name: {user.first_name} {user.last_name}")
            print(f"  Age: {user.age}")
            print(f"  DOB: {user.dob}")
            print(f"  Contact: {user.contact}")
            print(f"  Interests: {user.interests}")
            return

        print(f"There are {len(matches)} users with the first name '{name}'.")
        choice = input("Would you like to search by last name? (yes/no): ").lower()

        if choice == "yes":
            last_name_input = input("Enter the user's last name: ").lower()
            for user in matches:
                if user.last_name.lower() == last_name_input:
                    print("User Found............")
                    print(f"User Name: {user.first_name} {user.last_name}")
                    print(f"  Age: {user.age}")
                    print(f"  DOB: {user.dob}")
                    print(f"  Contact: {user.contact}")
                    print(f"  Interests: {user.interests}")
                    return
            print(f"No user found with first name '{name}' and last name '{last_name_input}'.")
        else:
            print("Here are the matched users:")
            for user in matches:
                print(f"User Name: {user.first_name} {user.last_name}")
                print(f"  Age: {user.age}")
                print(f"  DOB: {user.dob}")
                print(f"  Contact: {user.contact}")
                print(f"  Interests: {user.interests}")
                print("-" * 30)


    def show_users(self):
        for x in self.users:
            print(f"User Name: {x.first_name} {x.last_name}")
            print(f"  Age: {x.age}")
            print(f"  DOB: {x.dob}")
            print(f"  Contact: {x.contact}")
            print(f"  Interests: {x.interests}")


li = PersonalDataOrganizer()
li.add_user("Divine", "Okacha", 19, "09-03-2006", "08143208048", "Coding", "learning", "coding")
li.add_user("Truth", "bizz", 20, "09-03-2005", "08109600233", "Coding", "dancing", "singing")
li.add_user("Divine", "Domain", 14, "07-04-2012", "08061653094", "Playing Games")
li.search_user("Divine")

