import tornado.web

D = {
    "alice": {
        "fname": ("Alice"),
        "lname": ("Smith"),
        "birthDate": ("1980-01-01"),
        "email": ("alice@example.com"),
        "ppic": ("/static/assets/alice.png")
    },
    "bob": {
        "fname": ("Bob"),
        "lname": ("Jones"),
        "birthDate": ("1976-12-31"),
        "email": ("bob@bob.xyz"),
        "ppic": ("/static/assets/bob.png")
    },
    "carol": {
        "fname": ("Carol"),
        "lname": ("Ling"),
        "birthDate": ("1989-07-17"),
        "email": ("carol@example.com"),
        "ppic": ("/static/assets/carol.png")
    },
    "dave": {
        "fname": ("Dave"),
        "lname": ("Port"),
        "birthDate": ("1992-03-14"),
        "email": ("dave@dave.dave"),
        "ppic": ("/static/assets/dave.png")
    }
}

class ProfileHandler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path.split("/")
        uname = p[2]
        info = D[uname]
        self.render("Profile.html", name = info["fname"], 
                    dateOfBirth = info["birthdate"], email = info["email"], image = info["image"])