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

class Index(webapp2.RequestHandler):
    def get(self):
        page_content = ""

        table = """
        <form>
            <table>
                <tr>
                    <td align="right">Username</td>
                    <td><input></td>
                </tr>
                <tr>
                    <td align="right">Password</td>
                    <td><input></td>
                </tr>
                <tr>
                    <td align="right">Verify Password</td>
                    <td><input></td>
                </tr>
                <tr>
                    <td align="right">Email (optional)</td>
                    <td><input></td>
                </tr>
            </table>
            <input type="submit">
        </form>

        """

        page_content = table

        self.response.write(page_header + page_content + page_footer)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
