from pyscript import document, display

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

