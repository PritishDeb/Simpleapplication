from flask import jsonify

class viewdata():
    def viewdata(self):
        try:
            with open("C:\\Users\\pdebnath\\PycharmProjects\\SimpleApplication\\datafile.txt", 'r') as f:
                return [{i:j for i,j in zip(['Name', 'Age', 'Place'],[line.rstrip() for line in f])}]
        except Exception as e:
            print(e)

