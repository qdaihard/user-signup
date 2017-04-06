#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
    <style type="text/css">
        .error {
            color: red;
        }
        .warning {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Signup</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

# submission form template
table = """
<form method="post" action="/">
    <table>
        <tr>
            <td align="right">Username</td>
            <td><input type="text" name="username" value="%(username)s"><p>%(error)s</p></td>

        </tr>
        <tr>
            <td align="right">Password</td>
            <td><input type="password" name="password"></td>
        </tr>
        <tr>
            <td align="right">Verify Password</td>
            <td><input type="password" name="verpass"></td>
        </tr>
        <tr>
            <td align="right">Email (optional)</td>
            <td><input type="text" name="email" value=""></td>
        </tr>
    </table>
    <input type="submit">
</form>
"""

#validation methods for each entry
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PASSWORD_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_verpass(verpass):
    if verpass==password:
        return True

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)

class Index(webapp2.RequestHandler):
    def createForm(self, username, username_error="", password_error="", passwordVerify_error="", email, email_error=""):
        self.response.write(page_header + table + page_footer)

    def get(self):
        self.createForm()

    def post(self):
        username = self.request.get("username")
        username_correct = valid_username(username)
        if not username_correct:
            self.response.write(page_header + table%{"username":username, "error":"something wrong"} + page_footer)
        else:
            self.redirect("/welcome")


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        welcome_msg = "<h2>Welcome, {0}!</h2>".format(username)
        self.response.write(welcome_msg)



app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', WelcomeHandler)
], debug=True)
