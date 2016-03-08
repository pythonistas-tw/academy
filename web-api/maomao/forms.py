class LoginForm():
    account = ""
    password = ""

    def __init__(self, account="", password=""):
        self.account = account
        self.password = password

    def is_valid(self):
        if self.account and "@" in self.account and self.password:
            return True
        return False

    def as_html(self):
        return """
        Username: <input id="account" type="text" name="account" maxlength="100" value="{}"></br>
        Password: <input id="password" type="password" name="password" maxlength="100"></br>""".format(self.account)