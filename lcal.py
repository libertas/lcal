#! /usr/bin/env python3


from PyQt4 import QtGui,QtCore

from math import *
import sys

import ui

class MainWindow(QtGui.QWidget,ui.Ui_Window):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
		
	def insert0(self):
		self.expression.setText(self.expression.text()+"0")
		
	def insert1(self):
		self.expression.setText(self.expression.text()+"1")
	
	def insert2(self):
		self.expression.setText(self.expression.text()+"2")
	
	def insert3(self):
		self.expression.setText(self.expression.text()+"3")
	
	def insert4(self):
		self.expression.setText(self.expression.text()+"4")
	
	def insert5(self):
		self.expression.setText(self.expression.text()+"5")
	
	def insert6(self):
		self.expression.setText(self.expression.text()+"6")
	
	def insert7(self):
		self.expression.setText(self.expression.text()+"7")
	
	def insert8(self):
		self.expression.setText(self.expression.text()+"8")
	
	def insert9(self):
		self.expression.setText(self.expression.text()+"9")
		
	def add(self):
		self.expression.setText(self.expression.text()+"+")
	
	def sub(self):
		self.expression.setText(self.expression.text()+"-")
	
	def mul(self):
		self.expression.setText(self.expression.text()+"*")
	
	def div(self):
		self.expression.setText(self.expression.text()+"/")
		
	def point(self):
		self.expression.setText(self.expression.text()+".")
		
	def bracket_l(self):
		self.expression.setText(self.expression.text()+"(")
		
	def bracket_r(self):
		self.expression.setText(self.expression.text()+")")
		
	def getresult(self):
		ex=self.expression.text()
		try:
			ans=eval(ex)
			self.expression.setText(str(ans))
		except:
			self.expression.setText("Error")
	
	
	
if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	main=MainWindow()
	main.show()
	sys.exit(app.exec_())
