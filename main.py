from PyQt5 import QtCore, QtGui, QtWidgets
from mainui import Ui_Form as main_ui_form
from QtTitleBarManager import title_bar_handler
from rpcs3_handle import rpcs3_mem
from S3RecipeHandler.Recipe import Recipe
import json


class maiuUi(QtWidgets.QWidget,main_ui_form):
    def setupUi(self,form):
        super().setupUi(form)
        title_bar_handler(form,self.titlebar, self.close_but, self.mini_but)

        try:
            self.rpcs3 = rpcs3_mem()
            self.extract_but.setEnabled(True)
            self.inject_but.setEnabled(True)
        except:
            self.msg_box = QtWidgets.QMessageBox()
            self.msg_box.setText("failed to hook RPCS3")
            self.msg_box.exec()

        self.events()

    def events(self):
        self.inject_but.clicked.connect(self.inject)
        self.extract_but.clicked.connect(self.extract)

    def inject(self):
        try:
            selected_files = QtWidgets.QFileDialog.getOpenFileName(filter="RSON files (*.json *.rson)")
            if len(selected_files) != 0:
                filepath = selected_files[0]
            
            with open(filepath, "r+") as file:
                recipe_json = json.loads(file.read())
            
            gameRecipe = Recipe(Recipe_Json=recipe_json)
            game_bytes = gameRecipe.get_bytes()
            self.rpcs3.write_recipe(game_bytes)
            self.msg_box = QtWidgets.QMessageBox()
            self.msg_box.setText("loaded recipe")
            self.msg_box.exec()
        except Exception as e:
            print(e)
            self.msg_box = QtWidgets.QMessageBox()
            self.msg_box.setText("failed to load recipe")
            self.msg_box.exec()

    def extract(self):
        try:
            recipe_bytes = self.rpcs3.read_recipe()
            gameRecipe = Recipe(recipe_bytes=recipe_bytes)


            rson = json.dumps(gameRecipe.to_json(), indent=4)

            with open("output.json","w+") as file:
                file.write(rson)

            self.msg_box = QtWidgets.QMessageBox()
            self.msg_box.setText("outputed recipe to output.json")
            self.msg_box.exec()
        except Exception as e:
            print(e)
            self.msg_box = QtWidgets.QMessageBox()
            self.msg_box.setText("failed to extract recipe")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = maiuUi()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
