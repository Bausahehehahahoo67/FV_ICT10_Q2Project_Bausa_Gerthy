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