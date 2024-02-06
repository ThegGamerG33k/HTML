import tornado.web
import json
import base64
import Profile

class Handler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path.split("/")
        uname = p[2]
        info = Profile.D[uname]
        self.render("updateprofile.html", fname = info["fname"], lname = info["lname"],
                        birthDate = info["birthDate"], ppic = info["ppic"])
    
    def post(self):
        J=json.loads(self.request.body)
        firstName = J["firstName"]
        lastName = J["lastName"]
        dob = J["birthDate"]
        p = self.request.path.split("/")
        uname = p[2]
        info = Profile.D[uname]
        info["fname"] = firstName
        info["lname"] = lastName
        info["birthDate"] = dob
        if (not J["pic"]):
            pass
        else:
            ppic = J["pic"]
            info["ppic"] = "data:image/png;base64," + ppic
        print("WE GOT:",firstName,lastName,dob,ppic[:20])
        resp={"ok": True}
        self.write( json.dumps(resp) )
    
