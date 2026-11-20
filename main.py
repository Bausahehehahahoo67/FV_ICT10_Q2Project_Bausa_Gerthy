from pyscript import document, display
#SW1
member_pairs = (
    ("gerthy", "bausa"),
    ("jericho", "magsalin"),
    ("joaquin", "castor"),
    ("eran", "diaz"),
    ("louie", "lee"),
    ("carlos", "borromeo"),
    ("philip", "ponce"),
    ("jarvis", "joven"),
)

def checkers_membershippers(e):
    members_f = document.getElementById("first").value.strip()
    members_l = document.getElementById("last").value.strip()
    result = document.getElementById("result")

    is_member = member_pairs.count((members_f.casefold(), members_l.casefold()))
    messages = (
        f"Sorry {members_f} {members_l}, your name is not on the list.",
        f"Welcome {members_f} {members_l}, you are on the list.",
    )
    result.innerText = messages[is_member]

#DRILL2
original_members = {"Gerthy Bruces Bausa", "Jericho Tuvieron Magsalin", "Joaquin Gabriel Mallari Castor", "Eran James Sangayab Diaz V", "Louie Vonn Medrana Lee", "Carlos Ezequiel Barja Borromeo", "Philip Joaquin Ponce"} #the original team

def add_club_member(e):
    First = document.getElementById("first").value #gets user input on firstname field
    Last = document.getElementById("last").value #gets user input on lastname field
    Full_name =  Full_name = First + " " + Last #combines values of "First" and "Last" to create fullname. a space is used to create a proper space between the two names
    original_members.add(Full_name) #combines the original set of members + user's name, also if i used "+" it wont work because two different types
    members_list = f"Total Members: {len(original_members)}<br>{'<br>'.join(sorted(original_members))}"
    document.getElementById("result").innerHTML = members_list #displays via "result" div id. if i used display it would just bunch up like a paragraph, but now it displays like a proper vertical list

#SKILLSTEST
nonmets = {
    "Hydrogen": ("H", 1, 1.008),
    "Helium": ("He", 2, 4.0026),
    "Carbon": ("C", 6, 12.011),
    "Nitrogen": ("N", 7, 14.007),
    "Oxygen": ("O", 8, 15.999),
    "Fluorine": ("F", 9, 18.998),
    "Neon": ("Ne", 10, 20.180),
    "Phosphorus": ("P", 15, 30.974),
    "Sulfur": ("S", 16, 32.06),
    "Chlorine": ("Cl", 17, 35.45),
    "Argon": ("Ar", 18, 39.948),
    "Selenium": ("Se", 34, 78.971),
    "Bromine": ("Br", 35, 79.904),
    "Krypton": ("Kr", 36, 83.798),
    "Iodine": ("I", 53, 126.90),
    "Xenon": ("Xe", 54, 131.29),
    "Radon": ("Rn", 86, 222.0)
}
# The full names represent Keys, the tuples are values describing (symbols index 0, atomic numbers index 1, atomic weight index 2)

def locate_element(e): #defining my own function, which is to locate elements
    Element = document.getElementById("nonmets").value #collects user input
    result = nonmets.get(Element, ("Element not found", "-","-")) #validates user input if it matches anything in "nonmets" databse, other wise results to fallback
    document.getElementById("data_name").innerText = Element #gets name
    document.getElementById("data_symbol").innerText = result[0] #gets index 0
    document.getElementById("data_number").innerText = result[1] #gets index 1
    document.getElementById("data_weight").innerText = result[2] #gets index 2