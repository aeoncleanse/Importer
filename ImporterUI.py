# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImporterUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(702, 316)
        self.inputLayerField = QtGui.QLineEdit(Dialog)
        self.inputLayerField.setGeometry(QtCore.QRect(130, 80, 416, 21))
        self.inputLayerField.setText(_fromUtf8(""))
        self.inputLayerField.setObjectName(_fromUtf8("inputLayerField"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 80, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(610, 80, 46, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.inputLayerCount = QtGui.QLineEdit(Dialog)
        self.inputLayerCount.setEnabled(False)
        self.inputLayerCount.setGeometry(QtCore.QRect(555, 80, 46, 20))
        self.inputLayerCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputLayerCount.setText(_fromUtf8(""))
        self.inputLayerCount.setMaxLength(6)
        self.inputLayerCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.inputLayerCount.setReadOnly(True)
        self.inputLayerCount.setObjectName(_fromUtf8("inputLayerCount"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 5, 236, 46))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButtonsedimentary = QtGui.QRadioButton(self.groupBox)
        self.radioButtonsedimentary.setEnabled(False)
        self.radioButtonsedimentary.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButtonsedimentary.setObjectName(_fromUtf8("radioButtonsedimentary"))
        self.ignSedButtonGroup = QtGui.QButtonGroup(Dialog)
        self.ignSedButtonGroup.setObjectName(_fromUtf8("ignSedButtonGroup"))
        self.ignSedButtonGroup.addButton(self.radioButtonsedimentary)
        self.radioButtonigneous = QtGui.QRadioButton(self.groupBox)
        self.radioButtonigneous.setEnabled(False)
        self.radioButtonigneous.setGeometry(QtCore.QRect(100, 20, 141, 17))
        self.radioButtonigneous.setObjectName(_fromUtf8("radioButtonigneous"))
        self.ignSedButtonGroup.addButton(self.radioButtonigneous)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(55, 180, 66, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 125, 91, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(15, 50, 106, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 111, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.destinationLayerField = QtGui.QLineEdit(Dialog)
        self.destinationLayerField.setGeometry(QtCore.QRect(130, 105, 416, 20))
        self.destinationLayerField.setObjectName(_fromUtf8("destinationLayerField"))
        self.destinationPathField = QtGui.QLineEdit(Dialog)
        self.destinationPathField.setEnabled(False)
        self.destinationPathField.setGeometry(QtCore.QRect(130, 130, 416, 20))
        self.destinationPathField.setReadOnly(True)
        self.destinationPathField.setObjectName(_fromUtf8("destinationPathField"))
        self.projectPathField = QtGui.QLineEdit(Dialog)
        self.projectPathField.setEnabled(False)
        self.projectPathField.setGeometry(QtCore.QRect(130, 55, 506, 20))
        self.projectPathField.setReadOnly(True)
        self.projectPathField.setObjectName(_fromUtf8("projectPathField"))
        self.destinationPreviewField = QtGui.QLineEdit(Dialog)
        self.destinationPreviewField.setGeometry(QtCore.QRect(130, 155, 416, 20))
        self.destinationPreviewField.setObjectName(_fromUtf8("destinationPreviewField"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(35, 100, 86, 21))
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.masterLayerField = QtGui.QLineEdit(Dialog)
        self.masterLayerField.setGeometry(QtCore.QRect(130, 180, 416, 20))
        self.masterLayerField.setObjectName(_fromUtf8("masterLayerField"))
        self.masterPreviewField = QtGui.QLineEdit(Dialog)
        self.masterPreviewField.setGeometry(QtCore.QRect(130, 205, 416, 20))
        self.masterPreviewField.setObjectName(_fromUtf8("masterPreviewField"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(645, 129, 46, 22))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(295, 5, 396, 46))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.radioButtonSamples = QtGui.QRadioButton(self.groupBox_3)
        self.radioButtonSamples.setEnabled(False)
        self.radioButtonSamples.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButtonSamples.setObjectName(_fromUtf8("radioButtonSamples"))
        self.dataButtonGroup = QtGui.QButtonGroup(Dialog)
        self.dataButtonGroup.setObjectName(_fromUtf8("dataButtonGroup"))
        self.dataButtonGroup.addButton(self.radioButtonSamples)
        self.radioButtonSummaryAges = QtGui.QRadioButton(self.groupBox_3)
        self.radioButtonSummaryAges.setEnabled(False)
        self.radioButtonSummaryAges.setGeometry(QtCore.QRect(80, 20, 96, 17))
        self.radioButtonSummaryAges.setObjectName(_fromUtf8("radioButtonSummaryAges"))
        self.dataButtonGroup.addButton(self.radioButtonSummaryAges)
        self.radioButtonSampleAnalyses = QtGui.QRadioButton(self.groupBox_3)
        self.radioButtonSampleAnalyses.setEnabled(False)
        self.radioButtonSampleAnalyses.setGeometry(QtCore.QRect(180, 20, 106, 17))
        self.radioButtonSampleAnalyses.setObjectName(_fromUtf8("radioButtonSampleAnalyses"))
        self.dataButtonGroup.addButton(self.radioButtonSampleAnalyses)
        self.radioButtonRawExcel = QtGui.QRadioButton(self.groupBox_3)
        self.radioButtonRawExcel.setEnabled(False)
        self.radioButtonRawExcel.setGeometry(QtCore.QRect(290, 20, 106, 17))
        self.radioButtonRawExcel.setObjectName(_fromUtf8("radioButtonRawExcel"))
        self.dataButtonGroup.addButton(self.radioButtonRawExcel)
        self.label_21 = QtGui.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(45, 200, 76, 21))
        self.label_21.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.destinationLayerCount = QtGui.QLineEdit(Dialog)
        self.destinationLayerCount.setEnabled(False)
        self.destinationLayerCount.setGeometry(QtCore.QRect(555, 105, 46, 20))
        self.destinationLayerCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.destinationLayerCount.setText(_fromUtf8(""))
        self.destinationLayerCount.setMaxLength(6)
        self.destinationLayerCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.destinationLayerCount.setReadOnly(True)
        self.destinationLayerCount.setObjectName(_fromUtf8("destinationLayerCount"))
        self.destinationPreviewCount = QtGui.QLineEdit(Dialog)
        self.destinationPreviewCount.setEnabled(False)
        self.destinationPreviewCount.setGeometry(QtCore.QRect(555, 155, 46, 20))
        self.destinationPreviewCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.destinationPreviewCount.setText(_fromUtf8(""))
        self.destinationPreviewCount.setMaxLength(6)
        self.destinationPreviewCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.destinationPreviewCount.setReadOnly(True)
        self.destinationPreviewCount.setObjectName(_fromUtf8("destinationPreviewCount"))
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(610, 105, 46, 16))
        self.label_18.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_22 = QtGui.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(610, 155, 46, 16))
        self.label_22.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.masterLayerCount = QtGui.QLineEdit(Dialog)
        self.masterLayerCount.setEnabled(False)
        self.masterLayerCount.setGeometry(QtCore.QRect(555, 180, 46, 20))
        self.masterLayerCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.masterLayerCount.setText(_fromUtf8(""))
        self.masterLayerCount.setMaxLength(6)
        self.masterLayerCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.masterLayerCount.setReadOnly(True)
        self.masterLayerCount.setObjectName(_fromUtf8("masterLayerCount"))
        self.label_23 = QtGui.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(610, 180, 46, 16))
        self.label_23.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.masterPreviewCount = QtGui.QLineEdit(Dialog)
        self.masterPreviewCount.setEnabled(False)
        self.masterPreviewCount.setGeometry(QtCore.QRect(555, 205, 46, 20))
        self.masterPreviewCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.masterPreviewCount.setText(_fromUtf8(""))
        self.masterPreviewCount.setMaxLength(6)
        self.masterPreviewCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.masterPreviewCount.setReadOnly(True)
        self.masterPreviewCount.setObjectName(_fromUtf8("masterPreviewCount"))
        self.label_24 = QtGui.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(610, 205, 46, 16))
        self.label_24.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 235, 601, 71))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(545, 14, 46, 22))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(15, 11, 96, 21))
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.destinationBackupPathField = QtGui.QLineEdit(self.groupBox_4)
        self.destinationBackupPathField.setEnabled(False)
        self.destinationBackupPathField.setGeometry(QtCore.QRect(120, 15, 416, 20))
        self.destinationBackupPathField.setReadOnly(True)
        self.destinationBackupPathField.setObjectName(_fromUtf8("destinationBackupPathField"))
        self.pushButton_10 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_10.setGeometry(QtCore.QRect(545, 39, 46, 22))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.masterBackupPathField = QtGui.QLineEdit(self.groupBox_4)
        self.masterBackupPathField.setEnabled(False)
        self.masterBackupPathField.setGeometry(QtCore.QRect(120, 40, 416, 20))
        self.masterBackupPathField.setReadOnly(True)
        self.masterBackupPathField.setObjectName(_fromUtf8("masterBackupPathField"))
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(35, 35, 76, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.pushButton_11 = QtGui.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(645, 179, 46, 22))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(645, 154, 46, 22))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_13 = QtGui.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(645, 104, 46, 22))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14 = QtGui.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(645, 204, 46, 22))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_15 = QtGui.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(645, 79, 46, 22))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_16 = QtGui.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(645, 54, 46, 22))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.groupBox.raise_()
        self.inputLayerField.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.inputLayerCount.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.destinationLayerField.raise_()
        self.destinationPathField.raise_()
        self.projectPathField.raise_()
        self.destinationPreviewField.raise_()
        self.label_14.raise_()
        self.masterLayerField.raise_()
        self.masterPreviewField.raise_()
        self.pushButton.raise_()
        self.groupBox_3.raise_()
        self.label_21.raise_()
        self.destinationLayerCount.raise_()
        self.destinationPreviewCount.raise_()
        self.label_18.raise_()
        self.label_22.raise_()
        self.masterLayerCount.raise_()
        self.label_23.raise_()
        self.masterPreviewCount.raise_()
        self.label_24.raise_()
        self.groupBox_4.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_16.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Input Layer", None))
        self.label_5.setText(_translate("Dialog", "Lines", None))
        self.groupBox.setTitle(_translate("Dialog", "Sedimentary or Igneous/Metamorphic", None))
        self.radioButtonsedimentary.setText(_translate("Dialog", "Sedimentary", None))
        self.radioButtonigneous.setText(_translate("Dialog", "Igneous/Metamorphic", None))
        self.label_2.setText(_translate("Dialog", "Master Layer", None))
        self.label_7.setText(_translate("Dialog", "Destination Path", None))
        self.label_8.setText(_translate("Dialog", "Project Save Path", None))
        self.label_10.setText(_translate("Dialog", "Destination Preview", None))
        self.label_14.setText(_translate("Dialog", "Destination Layer", None))
        self.pushButton.setText(_translate("Dialog", "Open", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Data Type", None))
        self.radioButtonSamples.setText(_translate("Dialog", "Samples", None))
        self.radioButtonSummaryAges.setText(_translate("Dialog", "Summary Ages", None))
        self.radioButtonSampleAnalyses.setText(_translate("Dialog", "Sample Analyses", None))
        self.radioButtonRawExcel.setText(_translate("Dialog", "Raw Excel Data", None))
        self.label_21.setText(_translate("Dialog", "Master Preview", None))
        self.label_18.setText(_translate("Dialog", "Lines", None))
        self.label_22.setText(_translate("Dialog", "Lines", None))
        self.label_23.setText(_translate("Dialog", "Lines", None))
        self.label_24.setText(_translate("Dialog", "Lines", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Backups", None))
        self.pushButton_9.setText(_translate("Dialog", "Open", None))
        self.label_13.setText(_translate("Dialog", "Destination Backup", None))
        self.pushButton_10.setText(_translate("Dialog", "Open", None))
        self.label_9.setText(_translate("Dialog", "Master Backup", None))
        self.pushButton_11.setText(_translate("Dialog", "Open", None))
        self.pushButton_12.setText(_translate("Dialog", "Open", None))
        self.pushButton_13.setText(_translate("Dialog", "Open", None))
        self.pushButton_14.setText(_translate("Dialog", "Open", None))
        self.pushButton_15.setText(_translate("Dialog", "Open", None))
        self.pushButton_16.setText(_translate("Dialog", "Open", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

