import npyscreen

class SplashFormClass(npyscreen.FormWithMenus):
    def create(self):

        value_list = ["HDP Text User Interface",
                      "César Rodríguez Moreno",
                      ""]

        self.add(npyscreen.MultiLine, name="Presentation", max_height=5,
                 footer = "Press Ctrl-X to select service.",
                 values=value_list)

    def afterEditing(self):
        self.parentApp.setNextForm(None)