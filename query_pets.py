import sqlite3

def query_person_pets():

    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()

    while True:
        person_id = input("Enter a person's ID (or '-1' to exit): ")
        if person_id == '-1':
            print("Exiting program.")
            break

        # Query person
        cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
        person = cursor.fetchone()

        if person:
            first_name, last_name, age = person
            print(f"{first_name} {last_name}, {age} years old")

            # Query person's pets
            cursor.execute("""
                SELECT pet.name, pet.breed, pet.age, pet.dead
                FROM pet
                JOIN person_pet ON pet.id = person_pet.pet_id
                WHERE person_pet.person_id = ?
            """, (person_id,))
            pets = cursor.fetchall()

            if pets:
                for pet_name, breed, age, dead in pets:
                    status = "that is no longer alive" if dead else "that is alive"
                    print(f"  - {first_name} owned {pet_name}, a {breed}, that was {age} years old {status}.")
            else:
                print("  This person does not own any pets.")
        else:
            print("Error: Person not found.")

    connection.close()

if __name__ == "__main__":
    print("Running query_pets.py")
    query_person_pets()