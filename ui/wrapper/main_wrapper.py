from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QHeaderView, QMenu, QAbstractItemView, QMessageBox

from config import load_config, write_config
from ui.source.main import Ui_Dialog
from ui.wrapper.dialog_rule_add_wrapper import DialogRuleAddWrapper
from ui.wrapper.dialog_rule_edit_wrapper import DialogRuleEditWrapper


class MainWrapper(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.config = None
        self.config_map = {}
        self.column_folder = 0
        self.column_app = 1

        self.draw_ui()
        self.connect()

    def draw_ui(self):
        self.config = load_config()
        model = QStandardItemModel(len(self.config['rules']), 2)
        model.setHorizontalHeaderLabels(['Folder', 'Application'])
        for row, rule in enumerate(self.config['rules']):
            folder_item = QStandardItem(rule['folder'])
            folder_item.setEditable(False)
            folder_item.setToolTip(rule['folder'])

            app_item = QStandardItem(rule['app'])
            app_item.setEditable(False)
            app_item.setToolTip(rule['app'])

            model.setItem(row, self.column_folder, folder_item)
            model.setItem(row, self.column_app, app_item)
            self.config_map[row] = rule
        self.tableView.setModel(model)
        self.tableView.verticalHeader().hide()
        self.tableView.horizontalHeader().setSectionResizeMode(self.column_folder, QHeaderView.ResizeToContents)
        self.tableView.horizontalHeader().setSectionResizeMode(self.column_app, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setSectionsClickable(False)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setFocusPolicy(Qt.NoFocus)
        self.tableView.setSelectionMode(QAbstractItemView.NoSelection)

    def connect(self):
        self.tableView.doubleClicked.connect(self.slot_tableView_doubleClicked)
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.slot_tableView_customContextMenuRequested)

    """
    @pyqtSlot()
    def slot_tableView_doubleClicked(self):
        self.slot_table_menu_view_action_triggered()
        if self.tableView.currentIndex().column() == self.column_app:
            rule_tmp = self.config_map[self.tableView.currentIndex().row()]
            app = QFileDialog.getOpenFileName(self, f'Choose an app to open the videos under {rule_tmp["folder"]}')[0]
            if not app:
                return
            res = QMessageBox.question(self, 'Confirm',
                                       f'Are you sure for using \n'
                                       f'[{app}]\n'
                                       f'to open videos under\n'
                                       f'[{rule_tmp["folder"]}]?')
            if res == QMessageBox.Yes:
                for rule_config in self.config['rules']:
                    if rule_config['folder'] == rule_tmp['folder']:
                        rule_config['app'] = str(PureWindowsPath(app))
                write_config(self.config)
                QMessageBox.information(self, 'Notify', f'Successfully update the app connect to {rule_tmp["folder"]}')
        """

    def slot_tableView_customContextMenuRequested(self):
        menu_top = QMenu(self)
        menu_main = menu_top.addMenu('Menu')

        menu_add_action = menu_main.addAction('Add')
        menu_add_action.triggered.connect(self.slot_table_menu_add_action_triggered)
        menu_edit_action = menu_main.addAction('Edit')
        menu_edit_action.triggered.connect(self.slot_table_menu_edit_action_triggered)
        menu_del_action = menu_main.addAction('Del')
        menu_del_action.triggered.connect(self.slot_table_menu_del_action_triggered)
        menu_index_action = menu_main.addAction('Change Index')
        menu_index_action.triggered.connect(self.slot_table_menu_index_action_triggered)
        menu_main.exec_(QtGui.QCursor.pos())

    @pyqtSlot()
    def slot_tableView_doubleClicked(self):
        rule = self.current_rule()
        self.dialog = DialogRuleEditWrapper(rule['folder'], rule['app'])
        self.dialog.closed.connect(self.slot_dialog_closed)
        self.dialog.show()

    @pyqtSlot()
    def slot_dialog_closed(self):
        self.draw_ui()

    @pyqtSlot()
    def slot_table_menu_add_action_triggered(self):
        self.dialog = DialogRuleAddWrapper()
        self.dialog.closed.connect(self.slot_dialog_closed)
        self.dialog.show()

    @pyqtSlot()
    def slot_table_menu_edit_action_triggered(self):
        self.slot_tableView_doubleClicked()

    @pyqtSlot()
    def slot_table_menu_del_action_triggered(self):
        self.config.get('rules').remove(self.current_rule())
        write_config(self.config)
        self.draw_ui()
        QMessageBox.information(self, 'Rule Delete', 'Successfully delete a rule!')

    @pyqtSlot()
    def slot_table_menu_index_action_triggered(self):
        pass

    def current_rule(self):
        return self.config_map[self.tableView.currentIndex().row()]