import os
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from interface import Ui_MainWindow
from settings_window import Ui_Settings_window
from zipfile import ZipFile
from rarfile import RarFile
import xmltodict
import rarfile
import patoolib


class Settings_window(QtWidgets.QWidget):
    # class for Settings window
    def __init__(self):
        super(Settings_window, self).__init__()
        self.sw = Ui_Settings_window()
        self.sw.setupUi(self)
        self.sw.toolButton_unrar.clicked.connect(self.toolButton_unrar_Clicked)
        self.sw.pushButton.clicked.connect(self.ok_Clicked)
        self.sw.pushButton_2.clicked.connect(self.cancel_Clicked)
        self.str_unrarfile_path = ''
        self.sett_content = sett_content
        self.sett_content_inner = ''
        self.sw.label_2.setText(self.sett_content)
        # reading settings from file and display them on widget
        try:
            with open('settings.txt', 'r') as sett_file:
                self.sett_content_inner = sett_file.read()
            self.sw.label_2.setText(self.sett_content_inner)
        except Exception:
            pass

    def toolButton_unrar_Clicked(self):
        # clicking on '...' button shows FileDialog to choose Unrar.exe
        self.unrarfile_path = QFileDialog.getOpenFileName(self, 'Specify Unrar.exe path', '/home')
        self.str_unrarfile_path = str(self.unrarfile_path[0])
        self.sw.label_2.setText(self.str_unrarfile_path)

    def ok_Clicked(self):
        # if Unrar.exe was chosen clicking on OK button saves the path to a txt-file
        if self.str_unrarfile_path != '':
            with open('settings.txt', 'w') as settings_file:
                settings_file.write(self.str_unrarfile_path)
            self.close()
        else:
            self.close()

    def cancel_Clicked(self):
        self.close()




class Mywindow(QtWidgets.QMainWindow):
    # class for main window of program
    def __init__(self):
        super(Mywindow, self).__init__()
        self.files_to_save_list = []
        self.input_path = ''
        self.output_path = ''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Input_dir_toolButton.clicked.connect(self.input_dir_toolButton_Clicked)
        self.ui.Output_dir_toolButton.clicked.connect(self.output_dir_toolButton_Clicked)
        self.ui.F01X.stateChanged.connect(self.chooseF01X)
        self.ui.F02X.stateChanged.connect(self.chooseF02X)
        self.ui.F6DX.stateChanged.connect(self.chooseF6DX)
        self.ui.FC5X.stateChanged.connect(self.chooseFC5X)
        self.ui.F20X.stateChanged.connect(self.chooseF20X)
        self.ui.FA7X.stateChanged.connect(self.chooseFA7X)
        self.ui.F6BX.stateChanged.connect(self.chooseF6BX)
        self.ui.Start.clicked.connect(self.start_Clicked)
        self.ui.analysis_date.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.analysis_date.setCalendarPopup(True)
        self.ui.analysis_date.dateChanged.connect(self.update_date)
        self.analysis_date = None
        self.ui.actionSettings.triggered.connect(self.show_settings_window)
        self.sett_content = sett_content


    def show_settings_window(self):
        # clicking on file -> settings shows Settings window
        self.settdWin = Settings_window()
        self.settdWin.show()


    def update_date(self, user_date):
        self.analysis_date = user_date.toString("dd.MM.yyyy")


    def input_dir_toolButton_Clicked(self):
        # clicking '...' button near input dir. shows FileDialog. After choosing the dir it
        # handles in input_path variable
        self.input_path = QFileDialog.getExistingDirectory(self, 'Setup Input Folder', '/home')
        self.ui.Input_directory_label.setText(self.input_path)

    def output_dir_toolButton_Clicked(self):
        # clicking '...' button near output dir. shows FileDialog. After choosing the dir it
        # handles in output_path variable
        self.output_path = QFileDialog.getExistingDirectory(self, 'Setup Output Folder', '/home')
        self.ui.Output_directory_label.setText(self.output_path)

    def chooseF01X(self, state):
        # checked check-box adds name of statfile to list
        # uchecked check-box removes name of statfile from list
        if state == Qt.Checked:
            self.files_to_save_list.append('F01X')
        else:
            try:
                self.files_to_save_list.remove('F01X')
            except Exception:
                pass

    def chooseF02X(self, state):
        if state == Qt.Checked:
            self.files_to_save_list.append('F02X')
        else:
            try:
                self.files_to_save_list.remove('F02X')
            except Exception:
                pass

    def chooseF6DX(self, state):
        if state == Qt.Checked:
            self.files_to_save_list.append('F6DX')
        else:
            try:
                self.files_to_save_list.remove('F6DX')
            except Exception:
                pass

    def chooseFC5X(self, state):
        if state == Qt.Checked:
            self.files_to_save_list.append('FC5X')
        else:
            try:
                self.files_to_save_list.remove('FC5X')
            except Exception:
                pass

    def chooseF20X(self, state):
        if state == Qt.Checked:
            self.files_to_save_list.append('F20X')
        else:
            try:
                self.files_to_save_list.remove('F20X')
            except Exception:
                pass

    def chooseFA7X(self, state):
        if state == Qt.Checked:
            self.files_to_save_list.append('FA7X')
        else:
            try:
                self.files_to_save_list.remove('FA7X')
            except Exception:
                pass

    def chooseF6BX(self, state):
        if state == Qt.Checked:
            self.files_to_save_list.append('F6BX')
        else:
            try:
                self.files_to_save_list.remove('F6BX')
            except Exception:
                pass

    def message_box(self, text):
        # displays message box with specified text when error arise
        msg = QMessageBox()
        msg.setWindowTitle('Error!')
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def start_Clicked(self):
        # what happens when Start is clicked
        # truing to read settings.txt with path to unrar.exe and configurating RarFile module
        try:
            with open('settings.txt', 'r') as sett_file:
                self.sett_content = sett_file.read()
                rarfile.UNRAR_TOOL = self.sett_content
        except Exception:
            pass
        # checking if all needed options is defined
        # if not colling message_box method to display the error
        if self.sett_content == '':
            self.message_box('Specify Unrar.exe path on File Menu -> Settings')
        elif self.input_path == '':
            self.message_box('Specify Input Directory')
        elif self.output_path == '':
            self.message_box('Specify Output Directory')
        elif self.files_to_save_list == []:
            self.message_box('Choose Files')
        # if all is good, clear the text browser and print 'Start' and begin the program
        else:
            self.ui.textBrowser.clear()
            self.ui.textBrowser.append("<span style=\" font-size:9pt; font-weight:600;"
                                       "color:#0000ff;\" >---Start!---</span>")
            self.if_7z()  # if file is 7z then repack it to zip an delete 7z
            count = 0
            number_of_files = len(os.listdir(self.input_path))
            for file in os.listdir(self.input_path):
                self.ui.textBrowser.append(file)  # print the name of file in the text browser
                QtWidgets.QApplication.processEvents()  # refresh window to show new text in the text browser
                file_read = self.input_path + '/' + file  # choosing the method of processing of file
                if self.what_file_is(file_read) == 'Zip':
                    self.Zip_archive(file_read)
                elif self.what_file_is(file_read) == 'Rar':
                    self.Rar_archive(file_read)
                else:
                    pass
                count += 1
                value = (count*100) // number_of_files
                self.ui.progressBar.setValue(value)  # updating progressBar
            self.ui.textBrowser.append("<span style=\" font-size:9pt; font-weight:600;"
                                       "color:#0000ff;\" >---Finished!---</span>")
            QtWidgets.QApplication.processEvents()  # at the end print Finished! and refresh window


    def what_file_is(self, file_read):
        # defines file's type
        type_dict = {'PK': 'Zip', 'Ra': 'Rar', '7z': '7z', '<?': 'Xml_file'}
        with open(file_read, 'rb') as file_to_identify:
            current_type = file_to_identify.read(2).decode()
        return type_dict[current_type]

    def if_7z(self):
        # if file is 7z repack to zip and delete 7z
        for file in os.listdir(self.input_path):
            file_read = self.input_path + '/' + file
            if self.what_file_is(file_read) == '7z':
                patoolib.repack_archive(file_read, file_read + '.zip')
                os.remove(file_read)

    def Zip_archive(self, file_read):
        # method for zip archive processing
        done_set = set()
        try:
            with ZipFile(file_read) as my_archive:
                for i in my_archive.namelist():  # taking list of all files and reading files
                    with my_archive.open(i) as myfile:
                        try:
                            xmlDict = xmltodict.parse(myfile)  # parse xml
                            context = my_archive.read(i)
                            statform = xmlDict['NBUSTATREPORT']['HEAD']['STATFORM']
                            kod = xmlDict['NBUSTATREPORT']['HEAD']['EDRPOU']
                            report_date = xmlDict['NBUSTATREPORT']['HEAD']['REPORTDATE']
                            # taking a name of statfile and checking if it was selected to save
                            if statform in self.files_to_save_list and report_date == self.analysis_date:
                                with open(self.output_path + '/' + statform + '_' + kod + '.xml', 'wb') as output_file:
                                    output_file.write(context)
                                done_set.add(statform)
                        except Exception:
                            # if file in archive is archive, then do this staff:
                            try:
                                with ZipFile(myfile) as inner_archive:
                                    for i in inner_archive.namelist():
                                        with inner_archive.open(i) as myfile:
                                            try:
                                                xmlDict = xmltodict.parse(myfile)
                                                context = my_archive.read(i)
                                                statform = xmlDict['NBUSTATREPORT']['HEAD']['STATFORM']
                                                kod = xmlDict['NBUSTATREPORT']['HEAD']['EDRPOU']
                                                report_date = xmlDict['NBUSTATREPORT']['HEAD']['REPORTDATE']
                                                if statform in self.files_to_save_list \
                                                        and report_date == self.analysis_date:
                                                    with open(self.output_path + '/' + statform + kod + '.xml',
                                                              'wb') as output_file:
                                                        output_file.write(context)
                                                    done_set.add(statform)
                                            except Exception:
                                                pass
                            except Exception:
                                pass
        except Exception:
            pass
        # define what selected files was processed (print name of the statfile + OK)
        # and what didn't (print name of the statfile + Error)
        for x in self.files_to_save_list:
            if x in done_set:
                self.ui.textBrowser.append(x + '- OK')
                QtWidgets.QApplication.processEvents()
            else:
                self.ui.textBrowser.append(x + '-' + "<span style=\" font-size:8pt;"
                                                     "font-weight:600; color:#ff0000;\" >ERROR!</span>")  # red colour
                QtWidgets.QApplication.processEvents()

    def Rar_archive(self, file_read):
        # method for rar archive processing
        # the same principle as in zip archive method
        done_set = set()
        try:
            with RarFile(file_read) as my_archive:
                for i in my_archive.namelist():
                    with my_archive.open(i) as myfile:
                        try:
                            xmlDict = xmltodict.parse(myfile)
                            context = my_archive.read(i)
                            statform = xmlDict['NBUSTATREPORT']['HEAD']['STATFORM']
                            kod = xmlDict['NBUSTATREPORT']['HEAD']['EDRPOU']
                            report_date = xmlDict['NBUSTATREPORT']['HEAD']['REPORTDATE']
                            if statform in self.files_to_save_list and report_date == self.analysis_date:
                                with open(self.output_path + '/' + statform + '_' + kod + '.xml', 'wb') as output_file:
                                    output_file.write(context)
                                done_set.add(statform)
                        except Exception:
                            try:
                                with ZipFile(myfile) as inner_archive:
                                    for i in inner_archive.namelist():
                                        with inner_archive.open(i) as myfile:
                                            try:
                                                xmlDict = xmltodict.parse(myfile)
                                                context = my_archive.read(i)
                                                statform = xmlDict['NBUSTATREPORT']['HEAD']['STATFORM']
                                                kod = xmlDict['NBUSTATREPORT']['HEAD']['EDRPOU']
                                                report_date = xmlDict['NBUSTATREPORT']['HEAD']['REPORTDATE']
                                                if statform in self.files_to_save_list \
                                                        and report_date == self.analysis_date:
                                                    with open(self.output_path + '/' + statform + kod + '.xml',
                                                              'wb') as output_file:
                                                        output_file.write(context)
                                                    done_set.add(statform)
                                            except Exception:
                                                pass
                            except Exception:
                                pass
        except Exception:
            pass
        for x in self.files_to_save_list:
            if x in done_set:
                self.ui.textBrowser.append(x + '- OK')
                QtWidgets.QApplication.processEvents()

            else:
                self.ui.textBrowser.append(x + '-' + "<span style=\" font-size:8pt; font-weight:600;"
                                                     "color:#ff0000;\" >ERROR!</span>")
                QtWidgets.QApplication.processEvents()


if __name__ == '__main__':
    # first truing to read settings file to understand if unrar.exe path was defined before
    sett_content = ''
    try:
        with open('settings.txt', 'r') as sett_file:
            sett_content = sett_file.read()
            rarfile.UNRAR_TOOL = sett_content

    except Exception:
        pass

    app = QtWidgets.QApplication(sys.argv)
    application = Mywindow()
    application.show()

    sys.exit(app.exec())
