import tornado.web

D = {
    "alice": {
        "name": ("Alice Smith"),
        "dob": ("Jan. 1"),
        "email": ("alice@example.com"),
        "image": ("/static/assets/alice.png")
    },
    "bob": {
        "name": ("Bob Jones"),
        "dob": ("Dec. 31"),
        "email": ("bob@bob.xyz"),
        "image": ("/static/assets/bob.png")
    },
    "carol": {
        "name": ("Carol Ling"),
        "dob": ("Jul. 17"),
        "email": ("carol@example.com"),
        "image": ("/static/assets/carol.png")
    },
    "dave": {
        "name": ("Dave N. Port"),
        "dob": ("Mar. 14"),
        "email": ("dave@dave.dave"),
        "image": ("/static/assets/dave.png")
    }
}

class ProfileHandler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path.split("/")
        uname = p[2]
        info = D[uname]
        self.render("Profile.html", name = info["name"], 
                    dateOfBirth = info["dob"], email = info["email"], image = info["image"])