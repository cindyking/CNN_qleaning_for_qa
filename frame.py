#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import wx as wx
import os
import locale
import sys


def get_encoding():
    """Return system encoding. """
    try:
        encoding = locale.getpreferredencoding()
        'TEST'.encode(encoding)
    except:
        encoding = 'UTF-8'

    return encoding


def absolute_path(filename):
    """Return absolute path to the given file. """
    return os_path_dirname(os_path_realpath(os_path_abspath(filename)))


def convert_item(item, to_unicode=False):
    """Convert item between 'unicode' and 'str'.

    Args:
        item (-): Can be any python item.

        to_unicode (boolean): When True it will convert all the 'str' types
            to 'unicode'. When False it will convert all the 'unicode'
            types back to 'str'.

    """
    if to_unicode and isinstance(item, str):
        # Convert str to unicode
        return item.decode(get_encoding(), 'ignore')

    if not to_unicode and isinstance(item, str):
        # Convert unicode to str
        return item.encode(get_encoding(), 'ignore')

    if hasattr(item, '__iter__'):
        # Handle iterables
        temp_list = []

        for sub_item in item:
            if isinstance(item, dict):
                temp_list.append((convert_item(sub_item, to_unicode), convert_item(item[sub_item], to_unicode)))
            else:
                temp_list.append(convert_item(sub_item, to_unicode))

        return type(item)(temp_list)

    return item


def convert_on_bounds(func):
    """Decorator to convert string inputs & outputs.
    Covert string inputs & outputs between 'str' and 'unicode' at the
    application bounds using the preferred system encoding. It will convert
    all the string params (args, kwargs) to 'str' type and all the
    returned strings values back to 'unicode'.
    """

    def wrapper(*args, **kwargs):
        returned_value = func(*convert_item(args), **convert_item(kwargs))

        return convert_item(returned_value, True)

    return wrapper


def get_icon_file():
    """Search for youtube-dlg app icon.

    Returns:
        The path to youtube-dlg icon file if exists, else returns None.

    """
    ICON_NAME = "youtube-dl-gui.png"

    pixmaps_dir = get_pixmaps_dir()

    if pixmaps_dir is not None:
        icon_file = os.path.join(pixmaps_dir, ICON_NAME)

        if os_path_exists(icon_file):
            return icon_file

    return None


os_getenv = convert_on_bounds(os.getenv)
os_makedirs = convert_on_bounds(os.makedirs)
os_path_isdir = convert_on_bounds(os.path.isdir)
os_path_exists = convert_on_bounds(os.path.exists)
os_path_dirname = convert_on_bounds(os.path.dirname)
os_path_abspath = convert_on_bounds(os.path.abspath)
os_path_realpath = convert_on_bounds(os.path.realpath)
os_path_expanduser = convert_on_bounds(os.path.expanduser)

options = {
    'save_path_dirs': [
        os.path.join(os_path_expanduser('~').decode('utf-8'), "Downloads"),
        os.path.join(os_path_expanduser('~').decode('utf-8'), "Desktop"),
        os.path.join(os_path_expanduser('~').decode('utf-8'), "Videos"),
        os.path.join(os_path_expanduser('~').decode('utf-8'), "Music"),
    ],
    'video_format': '0',
    'second_video_format': '0',
    'to_audio': False,
    'keep_video': False,
    'audio_format': '',
    'audio_quality': '5',
    'restrict_filenames': False,
    'output_format': 1,
    'output_template': os.path.join('%(uploader)s', '%(title)s.%(ext)s'),
    'playlist_start': 1,
    'playlist_end': 0,
    'max_downloads': 0,
    'min_filesize': 0,
    'max_filesize': 0,
    'min_filesize_unit': '',
    'max_filesize_unit': '',
    'write_subs': False,
    'write_all_subs': False,
    'write_auto_subs': False,
    'embed_subs': False,
    'subs_lang': 'en',
    'ignore_errors': True,
    'open_dl_dir': False,
    'write_description': False,
    'write_info': False,
    'write_thumbnail': False,
    'retries': 10,
    'user_agent': '',
    'referer': '',
    'proxy': '',
    'shutdown': False,
    'sudo_password': '',
    'username': '',
    'password': '',
    'video_password': '',
    'cmd_args': '',
    'enable_log': True,
    'log_time': True,
    'workers_number': 3,
    'main_win_size': (740, 490),
    'opts_win_size': (640, 490),
    'selected_video_formats': ['webm', 'mp4'],
    'selected_audio_formats': ['mp3', 'm4a', 'vorbis'],
    'selected_format': '0',
    'youtube_dl_debug': False,
    'ignore_config': True,
    'confirm_exit': True,
    'native_hls': True,
    'show_completion_popup': True,
    'confirm_deletion': True,
    'nomtime': False,
    'embed_thumbnail': False,
    'add_metadata': False,
    'disable_update': False
}


def get_pixmaps_dir():
    """Return absolute path to the pixmaps icons folder.

    Note:
        Paths we search: __main__ dir, library dir

    """
    search_dirs = [
        os.path.join(absolute_path(sys.argv[0]).decode('utf-8'), "data/"),
        os.path.join(os_path_dirname(__file__).decode('utf-8'), "data/")
    ]

    for directory in search_dirs:
        pixmaps_dir = os.path.join(directory, "pixmaps/")

        if os_path_exists(pixmaps_dir):
            return pixmaps_dir
    print(1)
    return None


class Main_Frame(wx.Frame):
    """Main Window Class"""

    FRAMES_MIN_SIZE = (560, 360)
    # Labels area
    URLS_LABEL = "运行日志显示"
    MODEL_LABEL = "选择数据集"
    Next_PAGE = '下一页'
    From_PAGE = '上一页'
    UPDATE_LABEL = "Update"
    RESTART_LABEL = '重新训练'
    OPTIONS_LABEL = "Options"
    STOP_LABEL = "Stop"
    INFO_LABEL = "Info"
    WELCOME_MSG = "Welcome"
    WARNING_LABEL = "Warning"

    ADD_LABEL = "Add"
    DOWNLOAD_LIST_LABEL = "Download list"
    CLEAR_LOG = '清空日志'
    DELETE_LABEL = "Delete"
    PLAY_LABEL = "Play"
    UP_LABEL = "Up"
    DOWN_LABEL = "Down"
    RELOAD_LABEL = "Reload"
    PAUSE_LABEL = "暂停训练"
    SAVE_LABEL = "存储参数"
    CHANGE_LABEL = "超参数调整"
    START_LABEL = "开始训练"
    ABOUT_LABEL = "About"
    VIEWLOG_LABEL = "View Log"

    CLOSING_MSG = "Stopping downloads"
    CLOSED_MSG = "Downloads stopped"
    PROVIDE_URL_MSG = "You need to provide at least one URL"
    DOWNLOAD_STARTED = "Downloads started"
    CHOOSE_DIRECTORY = "Choose Directory"

    DOWNLOAD_ACTIVE = "Download in progress. Please wait for all downloads to complete"
    UPDATE_ACTIVE = "Update already in progress"

    UPDATING_MSG = "Downloading latest youtube-dl. Please wait..."
    UPDATE_ERR_MSG = "Youtube-dl download failed [{0}]"
    UPDATE_SUCC_MSG = "Successfully downloaded youtube-dl"

    SHUTDOWN_ERR = "Error while shutting down. Make sure you typed the correct password"
    SHUTDOWN_MSG = "Shutting down system"

    VIDEO_LABEL = "Title"
    EXTENSION_LABEL = "Extension"
    SIZE_LABEL = "Size"
    PERCENT_LABEL = "Percent"
    ETA_LABEL = "ETA"
    SPEED_LABEL = "Speed"
    STATUS_LABEL = "Status"
    CHECK_LABEL = '验证模型'
    TEST_LABEL = '测试模型'

    #################################

    # STATUSLIST_COLUMNS
    #
    # Dictionary which contains the columns for the wxListCtrl widget.
    # Each key represents a column and holds informations about itself.
    # Structure informations:
    #  column_key: (column_number, column_label, minimum_width, is_resizable)
    #
    STATUSLIST_COLUMNS = {
        'filename': (0, VIDEO_LABEL, 150, True),
        'extension': (1, EXTENSION_LABEL, 60, False),
        'filesize': (2, SIZE_LABEL, 80, False),
        'percent': (3, PERCENT_LABEL, 65, False),
        'eta': (4, ETA_LABEL, 45, False),
        'speed': (5, SPEED_LABEL, 90, False),
        'status': (6, STATUS_LABEL, 160, False)
    }

    def __init__(self, opt_manager, log_manager, parent=None):
        super(Main_Frame, self).__init__(parent, wx.ID_ANY, str('模型训练'), size=options["main_win_size"])
        self.download_manager = None
        self.update_thread = None
        self.app_icon = None  # REFACTOR Get and set on __init__.py

        # Get the pixmaps directory
        self._pixmaps_path = get_pixmaps_dir()

        # Set the app icon
        app_icon_path = get_icon_file()
        if app_icon_path is not None:
            self.app_icon = wx.Icon(app_icon_path, wx.BITMAP_TYPE_PNG)
            self.SetIcon(self.app_icon)

        bitmap_data = (
            ("down", "arrow_down_32px.png"),
            ("up", "arrow_up_32px.png"),
            ("play", "play_32px.png"),
            ("start", "cloud_download_32px.png"),
            ("delete", "delete_32px.png"),
            ("folder", "folder_32px.png"),
            ("pause", "pause_32px.png"),
            ("resume", "play_32px.png"),
            ("reload", "reload_32px.png"),
            ("settings", "settings_20px.png"),
            ("stop", "stop_32px.png"),
            ("start2", 'start_32px.png'),
            ("check", 'check_32px.png'),
            ("test", 'test_32px.png')
        )

        ## 按钮图片
        self._bitmaps = {}

        for item in bitmap_data:
            target, name = item
            self._bitmaps[target] = wx.Bitmap(os.path.join(self._pixmaps_path, name))

        # Set the data for all the wx.Button items
        # name, label, size, event_handler
        buttons_data = (
            ("delete", self.DELETE_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("start2", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("test", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("check", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("play", self.PLAY_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            # ("up", self.UP_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            # ("down", self.DOWN_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("reload", self.RELOAD_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("pause", self.PAUSE_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("start", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton)
            #("savepath", "...", (35, -1), self._on_update, wx.Button)
        )

        # Set the data for the settings menu item
        # label, event_handler
        settings_menu_data = (
            (self.OPTIONS_LABEL, self._on_update),
            (self.UPDATE_LABEL, self._on_update),
            (self.VIEWLOG_LABEL, self._on_update),
            (self.ABOUT_LABEL, self._on_update)
        )

        statuslist_menu_data = (
            ("Get URL", self._on_update),
            ("Get command", self._on_update),
            ("Open destination", self._on_update),
            ("Re-enter", self._on_update)
        )

        # Create options frame
        # self._options_frame = OptionsFrame(self)

        # Create frame components
        self._panel = wx.Panel(self)

        self._url_text = self._create_statictext(self.URLS_LABEL)

       # self._model_text = self._create_statictext(self.MODEL_LABEL)

       # self._clear_text = self._create_statictext(self.CLEAR_LOG)

        self._pause_text = self._create_statictext(self.PAUSE_LABEL)

        self._restart_text = self._create_statictext(self.RESTART_LABEL)

        self._start_text= self._create_statictext(self.START_LABEL)

       # self._next_page = self._create_statictext(self.Next_PAGE)

       # self._from_page= self._create_statictext(self.From_PAGE)

        self._save_label = self._create_statictext(self.SAVE_LABEL)

        self._change_label = self._create_statictext(self.CHANGE_LABEL)

        self._check_label = self._create_statictext(self.CHECK_LABEL)

        self._test_label = self._create_statictext(self.TEST_LABEL)

        # REFACTOR Move to buttons_data
        self._settings_button = self._create_bitmap_button(self._bitmaps["settings"], (30, 30), self._on_update)

        self._url_list = self._create_textctrl(wx.TE_MULTILINE | wx.TE_DONTWRAP, self._on_update)

        # self._folder_icon = self._create_static_bitmap(self._bitmaps["folder"], self._on_update)

        # self._path_combobox = ExtComboBox(self._panel, 5, style=wx.CB_READONLY)
        # self._videoformat_combobox = CustomComboBox(self._panel, style=wx.CB_READONLY)

        # self._download_text = self._create_statictext(self.DOWNLOAD_LIST_LABEL)
        # self._status_list = ListCtrl(self.STATUSLIST_COLUMNS,
        #                              parent=self._panel,
        #                              style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)

        # Dictionary to store all the buttons
        self._buttons = {}

        for item in buttons_data:
            name, label, size, evt_handler, parent = item

            button = parent(self._panel, size=size)

            if parent == wx.Button:
                button.SetLabel(label)
            elif parent == wx.BitmapButton:
                button.SetToolTip(wx.ToolTip(label))

            if name in self._bitmaps:
                button.SetBitmap(self._bitmaps[name], wx.TOP)

            if evt_handler is not None:
                button.Bind(wx.EVT_BUTTON, evt_handler)

            self._buttons[name] = button

        self._status_bar = self.CreateStatusBar()

        # Create extra components
        # self._settings_menu = self._create_menu_item(settings_menu_data)
        # self._statuslist_menu = self._create_menu_item(statuslist_menu_data)

        # Overwrite the menu hover event to avoid changing the statusbar
        # self.Bind(wx.EVT_MENU_HIGHLIGHT, lambda event: None)

        # # Bind extra events
        # self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self._on_statuslist_right_click, self._status_list)
        # self.Bind(wx.EVT_TEXT, self._update_savepath, self._path_combobox)
        # self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._update_pause_button, self._status_list)
        # self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self._update_pause_button, self._status_list)
        # self.Bind(wx.EVT_CLOSE, self._on_close)
        # self.Bind(wx.EVT_TIMER, self._on_timer, self._app_timer)

        # self._videoformat_combobox.Bind(wx.EVT_COMBOBOX, self._update_videoformat)

        # # Set threads wxCallAfter handlers
        # self._set_publisher(self._update_handler, UPDATE_PUB_TOPIC)
        # self._set_publisher(self._download_worker_handler, WORKER_PUB_TOPIC)
        # self._set_publisher(self._download_manager_handler, MANAGER_PUB_TOPIC)

        # Set up extra stuff
        self.Center()
        self.SetMinSize(self.FRAMES_MIN_SIZE)

        self._status_bar_write(self.WELCOME_MSG)

        # self._update_videoformat_combobox()
        # self._path_combobox.LoadMultiple(self.opt_manager.options["save_path_dirs"])
        # self._path_combobox.SetValue(self.opt_manager.options["save_path"])

        self._set_layout()

    def _on_options(self):
        pass

    def _on_update(self):
        pass

    def _create_menu_item(self, items):
        menu = wx.Menu()

        for item in items:
            label, evt_handler = item
            menu_item = menu.Append(-1, label)
        return menu

    def _status_bar_write(self, msg):
        """Display msg in the status bar. """
        self._status_bar.SetStatusText(msg)

    def _create_statictext(self, label):
        return wx.StaticText(self._panel, label=label)

    def _create_bitmap_button(self, icon, size=(-1, -1), handler=None):
        button = wx.BitmapButton(self._panel, bitmap=icon, size=size, style=wx.NO_BORDER)

        if handler is not None:
            button.Bind(wx.EVT_BUTTON, handler)

        return button

    def _create_static_bitmap(self, icon, event_handler=None):
        static_bitmap = wx.StaticBitmap(self._panel, bitmap=icon)

        if event_handler is not None:
            static_bitmap.Bind(wx.EVT_LEFT_DCLICK, event_handler)

        return static_bitmap

    def _create_textctrl(self, style=None, event_handler=None):
        if style is None:
            textctrl = wx.TextCtrl(self._panel)
        else:
            textctrl = wx.TextCtrl(self._panel, style=style)

        textctrl.AppendText("""
2019-02-23T15:07:00.016934: step 45,  loss 3.09304
2019-02-23T15:07:01.416972: step 46,  loss 2.83289
2019-02-23T15:07:02.681005: step 47,  loss 2.732
2019-02-23T15:07:04.016052: step 48,  loss 2.86763
2019-02-23T15:07:05.454088: step 49,  loss 2.88685
2019-02-23T15:07:06.831133: step 50,  loss 2.70065
2019-02-23T15:07:08.215178: step 51,  loss 2.75914
2019-02-23T15:07:09.627214: step 52,  loss 2.94328
2019-02-23T15:07:11.039283: step 53,  loss 2.67097
2019-02-23T15:07:12.397347: step 54,  loss 2.71534
2019-02-23T15:07:13.784412: step 55,  loss 2.8525
2019-02-23T15:07:15.224469: step 56,  loss 2.75389
2019-02-23T15:07:16.535524: step 57,  loss 2.74363
2019-02-23T15:07:17.814559: step 58,  loss 2.76741
2019-02-23T15:07:19.149597: step 59,  loss 2.76995
2019-02-23T15:07:20.540673: step 60,  loss 2.66857
2019-02-23T15:07:21.912722: step 61,  loss 2.6794
2019-02-23T15:07:23.242765: step 62,  loss 2.76718
2019-02-23T15:07:24.622807: step 63,  loss 2.62352
2019-02-23T15:07:26.014856: step 64,  loss 2.64142
2019-02-23T15:07:27.408930: step 65,  loss 2.51963

        """)
        if event_handler is not None:
            textctrl.Bind(wx.EVT_TEXT_PASTE, event_handler)
            textctrl.Bind(wx.EVT_MIDDLE_DOWN, event_handler)

        if os.name == 'nt':
            # Enable CTRL+A on Windows
            def win_ctrla_eventhandler(event):
                if event.GetKeyCode() == wx.WXK_CONTROL_A:
                    event.GetEventObject().SelectAll()

                event.Skip()

            # textctrl.Bind(wx.EVT_CHAR, win_ctrla_eventhandler)

        return textctrl

    def _create_popup(self, text, title, style):
        wx.MessageBox(text, title, style)

    def _set_layout(self):
        """Sets the layout of the main window. """
        main_sizer = wx.BoxSizer()
        panel_sizer = wx.BoxSizer(wx.VERTICAL)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        top_sizer.Add(self._url_text, 0, wx.ALIGN_BOTTOM | wx.BOTTOM, 5)
        # top_sizer.AddSpacer((-1, -1), 1)
        top_sizer.Add(self._settings_button)
        top_sizer.Add(self._change_label,flag=wx.ALIGN_CENTER)
        panel_sizer.Add(top_sizer, 0, wx.EXPAND)

        panel_sizer.Add(self._url_list, 1, wx.EXPAND)

        # mid_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # mid_sizer.Add(self._folder_icon,wx.ALIGN_CENTER)
        # mid_sizer.Add(self._model_text, flag=wx.ALIGN_CENTER)
        # mid_sizer.Add(self._path_combobox, 2, wx.ALIGN_CENTER_VERTICAL)
        # mid_sizer.AddSpacer((5, -1))
        # mid_sizer.AddSpacer((10, -1), 1)
        # mid_sizer.Add(self._videoformat_combobox, 1, wx.ALIGN_CENTER_VERTICAL)
        # mid_sizer.AddSpacer((5, -1))
        # mid_sizer.Add(self._buttons["add"], flag=wx.ALIGN_CENTER_VERTICAL)
        # panel_sizer.Add(mid_sizer, 0, wx.EXPAND | wx.ALL, 10)

        # panel_sizer.Add(self._download_text, 0, wx.BOTTOM, 5)
        # panel_sizer.Add(self._status_list, 2, wx.EXPAND)

        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        bottom_sizer.Add(self._buttons["start2"])
        bottom_sizer.Add(self._start_text, flag=wx.ALIGN_CENTER_VERTICAL)
        # bottom_sizer.AddSpacer((5, -1))
        # bottom_sizer.AddSpacer((5, -1))
        # bottom_sizer.Add(self._buttons["up"])
        # bottom_sizer.Add(self._from_page, flag=wx.ALIGN_CENTER_VERTICAL)
        # bottom_sizer.AddSpacer((5, -1))
        # bottom_sizer.Add(self._buttons["down"])
        # bottom_sizer.Add(self._next_page, flag=wx.ALIGN_CENTER_VERTICAL)
        # bottom_sizer.AddSpacer((5, -1))
        bottom_sizer.Add(self._buttons["reload"])
        bottom_sizer.Add(self._restart_text, flag=wx.ALIGN_CENTER_VERTICAL)
        # bottom_sizer.AddSpacer((5, -1))
        bottom_sizer.Add(self._buttons["pause"])
        bottom_sizer.Add(self._pause_text,flag=wx.ALIGN_CENTER_VERTICAL)
        # bottom_sizer.AddSpacer((10, -1), 1)
        bottom_sizer.Add(self._buttons["start"])
        bottom_sizer.Add(self._save_label, flag=wx.ALIGN_CENTER_VERTICAL)
        bottom_sizer.Add(self._buttons["check"])
        bottom_sizer.Add(self._check_label, flag=wx.ALIGN_CENTER_VERTICAL)
        bottom_sizer.Add(self._buttons["test"])
        bottom_sizer.Add(self._test_label, flag=wx.ALIGN_CENTER_VERTICAL)
        panel_sizer.Add(bottom_sizer, 0, wx.EXPAND | wx.TOP, 5)

        main_sizer.Add(panel_sizer, 1, wx.ALL | wx.EXPAND, 10)
        self._panel.SetSizer(main_sizer)

        self._panel.Layout()
        self.Show(True)

class my_frame(wx.Frame):
    """We simple derive a new class of Frame"""

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title=title, size=(550, 500))

        bitmap_data = (
            ("down", "arrow_down_32px.png"),
            ("up", "arrow_up_32px.png"),
            ("play", "play_32px.png"),
            ("start", "cloud_download_32px.png"),
            ("delete", "delete_32px.png"),
            ("folder", "folder_32px.png"),
            ("pause", "pause_32px.png"),
            ("resume", "play_32px.png"),
            ("reload", "reload_32px.png"),
            ("settings", "settings_20px.png"),
            ("stop", "stop_32px.png"),
            ("start2", 'start_32px.png'),
            ("check", 'check_32px.png'),
            ("test", 'test_32px.png'))

        buttons_data = (
            ("delete", self.DELETE_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("start2", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("test", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("check", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("play", self.PLAY_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("up", self.UP_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("down", self.DOWN_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("reload", self.RELOAD_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("pause", self.PAUSE_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("start", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("savepath", "...", (35, -1), self._on_update, wx.Button),
        )

        self._buttons = {}

        for item in buttons_data:
            name, label, size, evt_handler, parent = item

            button = parent(self._panel, size=size)

            if parent == wx.Button:
                button.SetLabel(label)
            elif parent == wx.BitmapButton:
                button.SetToolTip(wx.ToolTip(label))

            if name in self._bitmaps:
                button.SetBitmap(self._bitmaps[name], wx.TOP)

            if evt_handler is not None:
                button.Bind(wx.EVT_BUTTON, evt_handler)

            self._buttons[name] = button

        self._pixmaps_path = get_pixmaps_dir()

        self._bitmaps = {}

        for item in bitmap_data:
            target, name = item
            self._bitmaps[target] = wx.Bitmap(os.path.join(self._pixmaps_path, name))

        p = wx.Panel(self)
        panelBox = wx.BoxSizer()
        main = wx.BoxSizer(wx.VERTICAL)
        panelBox.Add(main)
        topbox = wx.BoxSizer(wx.HORIZONTAL)
        top_text = wx.StaticText(p, label="数据导入", style=wx.ALIGN_CENTRE)
        topbox.Add(top_text, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 10)
        main.Add(topbox,0,wx.EXPAND,2)

        vbox = wx.BoxSizer(wx.HORIZONTAL)
        l1 = wx.StaticText(p, label="选择数据集合", style=wx.ALIGN_CENTRE)
        vbox.Add(l1, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 13)
        text = wx.TextCtrl(p,10)
        vbox.Add(text,0,wx.ALIGN_CENTER_VERTICAL,10)
        vbox.AddSpacer(2)
        b1 = wx.Button(self._buttons['folder'])
        vbox.Add(b1, 1, wx.EXPAND)
        main.Add(vbox,0,wx.EXPAND,2)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(p, label="Label2", style=wx.ALIGN_CENTER_VERTICAL)
        hbox.Add(l2, 0, wx.SHAPED,2)
        b3 = wx.Button(p, label="Btn3")
        hbox.Add(b3, 0, wx.ALIGN_CENTER_VERTICAL,3)
        main.Add(hbox, 0, wx.ALL | wx.EXPAND,1)

        p.SetSizer(panelBox)
        self.Show(True)

    def _on_update(self):
        pass

    def _create_textctrl(self, style=None, event_handler=None):
        if style is None:
            textctrl = wx.TextCtrl(self.panel)
        else:
            textctrl = wx.TextCtrl(self.panel, style=style)

        return textctrl


class Main_Frame2(wx.Frame):
    """Main Window Class"""

    FRAMES_MIN_SIZE = (560, 360)
    # Labels area
    URLS_LABEL = "运行日志显示"
    MODEL_LABEL = "选择数据集"
    Next_PAGE = '下一页'
    From_PAGE = '上一页'
    UPDATE_LABEL = "Update"
    RESTART_LABEL = '重新训练'
    OPTIONS_LABEL = "Options"
    STOP_LABEL = "Stop"
    INFO_LABEL = "Info"
    WELCOME_MSG = "Welcome"
    WARNING_LABEL = "Warning"

    ADD_LABEL = "Add"
    DOWNLOAD_LIST_LABEL = "Download list"
    CLEAR_LOG = '清空日志'
    DELETE_LABEL = "Delete"
    PLAY_LABEL = "Play"
    UP_LABEL = "Up"
    DOWN_LABEL = "Down"
    RELOAD_LABEL = "Reload"
    PAUSE_LABEL = "暂停训练"
    SAVE_LABEL = "存储参数"
    CHANGE_LABEL = "超参数调整"
    START_LABEL = "开始训练"
    ABOUT_LABEL = "About"
    VIEWLOG_LABEL = "View Log"

    CLOSING_MSG = "Stopping downloads"
    CLOSED_MSG = "Downloads stopped"
    PROVIDE_URL_MSG = "You need to provide at least one URL"
    DOWNLOAD_STARTED = "Downloads started"
    CHOOSE_DIRECTORY = "Choose Directory"

    DOWNLOAD_ACTIVE = "Download in progress. Please wait for all downloads to complete"
    UPDATE_ACTIVE = "Update already in progress"

    UPDATING_MSG = "Downloading latest youtube-dl. Please wait..."
    UPDATE_ERR_MSG = "Youtube-dl download failed [{0}]"
    UPDATE_SUCC_MSG = "Successfully downloaded youtube-dl"

    SHUTDOWN_ERR = "Error while shutting down. Make sure you typed the correct password"
    SHUTDOWN_MSG = "Shutting down system"

    VIDEO_LABEL = "Title"
    EXTENSION_LABEL = "Extension"
    SIZE_LABEL = "Size"
    PERCENT_LABEL = "Percent"
    ETA_LABEL = "ETA"
    SPEED_LABEL = "Speed"
    STATUS_LABEL = "Status"
    CHECK_LABEL = '验证模型'
    TEST_LABEL = '测试模型'

    #################################

    # STATUSLIST_COLUMNS
    #
    # Dictionary which contains the columns for the wxListCtrl widget.
    # Each key represents a column and holds informations about itself.
    # Structure informations:
    #  column_key: (column_number, column_label, minimum_width, is_resizable)
    #
    STATUSLIST_COLUMNS = {
        'filename': (0, VIDEO_LABEL, 150, True),
        'extension': (1, EXTENSION_LABEL, 60, False),
        'filesize': (2, SIZE_LABEL, 80, False),
        'percent': (3, PERCENT_LABEL, 65, False),
        'eta': (4, ETA_LABEL, 45, False),
        'speed': (5, SPEED_LABEL, 90, False),
        'status': (6, STATUS_LABEL, 160, False)
    }

    def __init__(self, parent=None):

        super(Main_Frame2, self).__init__(parent, wx.ID_ANY, str('模型训练'), size=(630, 460))
        self.download_manager = None
        self.update_thread = None
        self.app_icon = None  # REFACTOR Get and set on __init__.py

        # Get the pixmaps directory
        self._pixmaps_path = get_pixmaps_dir()

        # Set the app icon
        app_icon_path = get_icon_file()

        bitmap_data = (
            ("down", "arrow_down_32px.png"),
            ("up", "arrow_up_32px.png"),
            ("play", "play_32px.png"),
            ("start", "cloud_download_32px.png"),
            ("delete", "delete_32px.png"),
            ("folder", "folder_32px.png"),
            ("pause", "pause_32px.png"),
            ("resume", "play_32px.png"),
            ("reload", "reload_32px.png"),
            ("settings", "settings_20px.png"),
            ("stop", "stop_32px.png"),
            ("start2", 'start_32px.png'),
            ("check", 'check_32px.png'),
            ("test", 'test_32px.png')
        )

        ## 按钮图片
        self._bitmaps = {}

        for item in bitmap_data:
            target, name = item
            self._bitmaps[target] = wx.Bitmap(os.path.join(self._pixmaps_path, name))

        # Set the data for all the wx.Button items
        # name, label, size, event_handler
        buttons_data = (
            ("delete", self.DELETE_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("start2", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("test", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("check", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("play", self.PLAY_LABEL, (-1, -1), self._on_update2, wx.BitmapButton),
            ("up", self.UP_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("down", self.DOWN_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("reload", self.RELOAD_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("pause", self.PAUSE_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("start", self.START_LABEL, (-1, -1), self._on_update, wx.BitmapButton),
            ("savepath", "...", (35, -1), self._on_update, wx.Button),
            ("savepath2", "...", (35, -1), self._on_update, wx.Button),
            ("savepath3", "...", (35, -1), self._on_update, wx.Button),
        )

        # Set the data for the settings menu item
        # label, event_handler
        settings_menu_data = (
            (self.OPTIONS_LABEL, self._on_update),
            (self.UPDATE_LABEL, self._on_update),
            (self.VIEWLOG_LABEL, self._on_update),
            (self.ABOUT_LABEL, self._on_update)
        )

        statuslist_menu_data = (
            ("Get URL", self._on_update),
            ("Get command", self._on_update),
            ("Open destination", self._on_update),
            ("Re-enter", self._on_update)
        )

        # Create options frame
        # self._options_frame = OptionsFrame(self)

        # Create frame components
        self._panel = wx.Panel(self)

       #  self._url_text = self._create_statictext(self.URLS_LABEL)
       #
       #  self._model_text = self._create_statictext(self.MODEL_LABEL)
       #
       # # self._clear_text = self._create_statictext(self.CLEAR_LOG)
       #
       #  self._pause_text = self._create_statictext(self.PAUSE_LABEL)
       #
       #  self._restart_text = self._create_statictext(self.RESTART_LABEL)
       #
       #  self._start_text= self._create_statictext(self.START_LABEL)
       #
       # # self._next_page = self._create_statictext(self.Next_PAGE)
       #
       # # self._from_page= self._create_statictext(self.From_PAGE)
       #
       #  self._save_label = self._create_statictext(self.SAVE_LABEL)
       #
       #  self._change_label = self._create_statictext(self.CHANGE_LABEL)
       #
       #  self._check_label = self._create_statictext(self.CHECK_LABEL)
       #
       #  self._test_label = self._create_statictext(self.TEST_LABEL)
       #
       #  # REFACTOR Move to buttons_data
       #  self._settings_button = self._create_bitmap_button(self._bitmaps["settings"], (30, 30), self._on_update)
       #
       #  # self._url_list = self._create_textctrl(wx.TE_MULTILINE | wx.TE_DONTWRAP, self._on_update)

        self._folder_icon = self._create_static_bitmap(self._bitmaps["folder"], self._on_update)

        self._folder_icon2= self._create_static_bitmap(self._bitmaps["folder"], self._on_update)

        self._folder_icon3 = self._create_static_bitmap(self._bitmaps["folder"], self._on_update)

        # self._path_combobox = ExtComboBox(self._panel, 5, style=wx.CB_READONLY)
        # self._videoformat_combobox = CustomComboBox(self._panel, style=wx.CB_READONLY)

        # self._download_text = self._create_statictext(self.DOWNLOAD_LIST_LABEL)
        # self._status_list = ListCtrl(self.STATUSLIST_COLUMNS,
        #                              parent=self._panel,
        #                              style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)

        # Dictionary to store all the buttons
        self._buttons = {}

        for item in buttons_data:
            name, label, size, evt_handler, parent = item

            button = parent(self._panel, size=size)

            if parent == wx.Button:
                button.SetLabel(label)
            elif parent == wx.BitmapButton:
                button.SetToolTip(wx.ToolTip(label))

            if name in self._bitmaps:
                button.SetBitmap(self._bitmaps[name], wx.TOP)

            if evt_handler is not None:
                button.Bind(wx.EVT_BUTTON, evt_handler)

            self._buttons[name] = button

        self._status_bar = self.CreateStatusBar()

        # Create extra components

        # Overwrite the menu hover event to avoid changing the statusbar
        # self.Bind(wx.EVT_MENU_HIGHLIGHT, lambda event: None)

        # # Bind extra events
        # self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self._on_statuslist_right_click, self._status_list)
        # self.Bind(wx.EVT_TEXT, self._update_savepath, self._path_combobox)
        # self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._update_pause_button, self._status_list)
        # self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self._update_pause_button, self._status_list)
        # self.Bind(wx.EVT_CLOSE, self._on_close)
        # self.Bind(wx.EVT_TIMER, self._on_timer, self._app_timer)

        # self._videoformat_combobox.Bind(wx.EVT_COMBOBOX, self._update_videoformat)

        # # Set threads wxCallAfter handlers
        # self._set_publisher(self._update_handler, UPDATE_PUB_TOPIC)
        # self._set_publisher(self._download_worker_handler, WORKER_PUB_TOPIC)
        # self._set_publisher(self._download_manager_handler, MANAGER_PUB_TOPIC)

        # Set up extra stuff
        self.Center()
        self.SetMinSize(self.FRAMES_MIN_SIZE)

        self._status_bar_write(self.WELCOME_MSG)

        # self._update_videoformat_combobox()
        # self._path_combobox.LoadMultiple(self.opt_manager.options["save_path_dirs"])
        # self._path_combobox.SetValue(self.opt_manager.options["save_path"])

        self._set_layout()

    def _on_options(self):
        pass

    def _on_update(self):
        pass

    def _create_menu_item(self, items):
        menu = wx.Menu()

        for item in items:
            label, evt_handler = item
            menu_item = menu.Append(-1, label)
        return menu

    def _status_bar_write(self, msg):
        """Display msg in the status bar. """
        self._status_bar.SetStatusText(msg)

    def _create_statictext(self, label):
        return wx.StaticText(self._panel, label=label)

    def _create_bitmap_button(self, icon, size=(-1, -1), handler=None):
        button = wx.BitmapButton(self._panel, bitmap=icon, size=size, style=wx.NO_BORDER)

        if handler is not None:
            button.Bind(wx.EVT_BUTTON, handler)

        return button

    def _create_static_bitmap(self, icon, event_handler=None):
        static_bitmap = wx.StaticBitmap(self._panel, bitmap=icon)

        if event_handler is not None:
            static_bitmap.Bind(wx.EVT_LEFT_DCLICK, event_handler)

        return static_bitmap

    def _create_textctrl(self, style=None, event_handler=None):
        if style is None:
            textctrl = wx.TextCtrl(self._panel)
        else:
            textctrl = wx.TextCtrl(self._panel, style=style)

        textctrl.AppendText("""
2019-02-23T15:07:00.016934: step 45,  loss 3.09304
2019-02-23T15:07:01.416972: step 46,  loss 2.83289
2019-02-23T15:07:02.681005: step 47,  loss 2.732
2019-02-23T15:07:04.016052: step 48,  loss 2.86763
2019-02-23T15:07:05.454088: step 49,  loss 2.88685
2019-02-23T15:07:06.831133: step 50,  loss 2.70065
2019-02-23T15:07:08.215178: step 51,  loss 2.75914
2019-02-23T15:07:09.627214: step 52,  loss 2.94328
2019-02-23T15:07:11.039283: step 53,  loss 2.67097
2019-02-23T15:07:12.397347: step 54,  loss 2.71534
2019-02-23T15:07:13.784412: step 55,  loss 2.8525
2019-02-23T15:07:15.224469: step 56,  loss 2.75389
2019-02-23T15:07:16.535524: step 57,  loss 2.74363
2019-02-23T15:07:17.814559: step 58,  loss 2.76741
2019-02-23T15:07:19.149597: step 59,  loss 2.76995
2019-02-23T15:07:20.540673: step 60,  loss 2.66857
2019-02-23T15:07:21.912722: step 61,  loss 2.6794
2019-02-23T15:07:23.242765: step 62,  loss 2.76718
2019-02-23T15:07:24.622807: step 63,  loss 2.62352
2019-02-23T15:07:26.014856: step 64,  loss 2.64142
2019-02-23T15:07:27.408930: step 65,  loss 2.51963

        """)
        if event_handler is not None:
            textctrl.Bind(wx.EVT_TEXT_PASTE, event_handler)
            textctrl.Bind(wx.EVT_MIDDLE_DOWN, event_handler)

        if os.name == 'nt':
            # Enable CTRL+A on Windows
            def win_ctrla_eventhandler(event):
                if event.GetKeyCode() == wx.WXK_CONTROL_A:
                    event.GetEventObject().SelectAll()

                event.Skip()

            # textctrl.Bind(wx.EVT_CHAR, win_ctrla_eventhandler)

        return textctrl

    def _create_popup(self, text, title, style):
        wx.MessageBox(text, title, style)

    def one(self,text1,text2,sboxSizer):
        sbox5 = wx.BoxSizer(wx.HORIZONTAL)
        fx5_1 = wx.StaticText(self._panel, -1, text1)
        t5_1 = wx.TextCtrl(self._panel, -1, size=(100, 20))
        sbox5.Add(t5_1, 0, wx.ALL | wx.ALIGN_CENTER, 1)

        sbox5.Add(fx5_1, 0, wx.ALL | wx.ALIGN_CENTER, 1)
        fx5_2 = wx.StaticText(self._panel, -1, text2)
        t5_2 = wx.TextCtrl(self._panel, -1, size=(100, 20))
        sbox5.Add(t5_2, 0, wx.ALL | wx.ALIGN_CENTER, 1)
        sbox5.Add(fx5_2, 0, wx.ALL | wx.ALIGN_CENTER, 1)
        sboxSizer.Add(sbox5, 0, wx.ALL | wx.CENTER, 1)

    def _on_update2(self,hello):

        print("true")
        frame = Main_Frame(None,None)
        self.Show(False)
        frame.Show(True)



    def _set_layout(self):
        """Sets the layout of the main window. """

        topbox = wx.BoxSizer(wx.HORIZONTAL)


        nm = wx.StaticBox(self._panel, -1, '数据导入')
        nm.SetMinSize((500,40))
        nmSizer = wx.StaticBoxSizer(nm, wx.VERTICAL)

        nmbox = wx.BoxSizer(wx.HORIZONTAL)
        fn1 = wx.StaticText(self._panel, -1, "数据集")
        txt1 = wx.TextCtrl(self._panel, -1,size =  (100,20))
        nmbox.Add(fn1, 0, wx.ALL | wx.CENTER, 5)
        nmbox.Add(txt1, 0, wx.ALL | wx.CENTER, 5)
        nmbox.Add(self._buttons["savepath"],wx.ALL | wx.CENTER, 5)
        nmbox.Add(self._folder_icon,wx.ALL | wx.CENTER, 1)
        nmSizer.Add(nmbox, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        nmbox2 = wx.BoxSizer(wx.HORIZONTAL)
        fn2 = wx.StaticText(self._panel, -1, "验证集")
        txt2 = wx.TextCtrl(self._panel, -1, size=(100, 20))
        nmbox2.Add(fn2, 0, wx.ALL | wx.CENTER, 5)
        nmbox2.Add(txt2, 0, wx.ALL | wx.CENTER, 5)
        nmbox2.Add(self._buttons["savepath2"], wx.ALL | wx.CENTER, 5)
        nmbox2.Add(self._folder_icon2, wx.ALL | wx.CENTER, 5)
        nmSizer.Add(nmbox2, 0, wx.ALL | wx.CENTER, 5)

        nmbox3 = wx.BoxSizer(wx.HORIZONTAL)
        fn3 = wx.StaticText(self._panel, -1, "测试集")
        txt3 = wx.TextCtrl(self._panel, -1, size=(100, 20))
        nmbox3.Add(fn3, 0, wx.ALL | wx.CENTER, 5)
        nmbox3.Add(txt3, 0, wx.ALL | wx.CENTER, 5)
        nmbox3.Add(self._buttons["savepath3"], wx.ALL | wx.CENTER, 5)
        nmbox3.Add(self._folder_icon3, wx.ALL | wx.CENTER, 5)
        nmSizer.Add(nmbox3, 0, wx.ALL | wx.CENTER, 5)



        sbox = wx.StaticBox(self._panel, -1, '参数设置')
        sbox.SetMinSize((500, 200))
        sboxSizer = wx.StaticBoxSizer(sbox, wx.VERTICAL)

        sbox1 = wx.BoxSizer(wx.HORIZONTAL)
        fx2_1 = wx.StaticText(self._panel, -1, "学习率")
        t2_1 = wx.TextCtrl(self._panel, -1, size=(100, 20))
        sbox1.Add(t2_1, 0, wx.ALL | wx.ALIGN_CENTER, 1)
        sbox1.AddSpacer(13)
        sbox1.Add(fx2_1, 0, wx.ALL | wx.ALIGN_CENTER, 1)

        sboxSizer.Add(sbox1, 0, wx.ALL | wx.CENTER, 1)

        fx3_1 = wx.StaticText(self._panel, -1, "迭代次数")
        t3_1 = wx.TextCtrl(self._panel, -1, size=(100, 20))
        sbox1.Add(t3_1, 0, wx.ALL | wx.ALIGN_CENTER, 1)
        sbox1.Add(fx3_1, 0, wx.ALL | wx.ALIGN_CENTER, 1)

        self.one('卷积窗口','卷积核数',sboxSizer)

        self.one('池化窗口','正则系数',sboxSizer)

        abox = wx.StaticBox(self._panel, -1, '算法设置')
        abox.SetMinSize((500, 20))
        asboxSizer = wx.StaticBoxSizer(abox, wx.VERTICAL)

        sbox2 = wx.BoxSizer(wx.HORIZONTAL)
        fx2_2 = wx.StaticText(self._panel, -1, "优化方法")
        combBox = wx.ComboBox(self._panel, -1, u'Adam算法',)


        fx2_3 = wx.StaticText(self._panel, -1, "模型选择")
        combBox2 = wx.ComboBox(self._panel, -1, u'LSTM',)

        sbox2.Add(fx2_3, 0, wx.ALL | wx.ALIGN_CENTER, 1)
        sbox2.Add(combBox2, 0,wx.ALL | wx.ALIGN_CENTER, 1)

        sbox2.Add(fx2_2, 0, wx.ALL | wx.ALIGN_CENTER, 1)
        sbox2.Add(combBox, 0,wx.ALL | wx.ALIGN_CENTER, 1)
        asboxSizer.Add(sbox2, 0,wx.ALL | wx.CENTER, 3)

        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(topbox, 0, wx.ALL | wx.CENTER, 10)
        vbox.Add(nmSizer, 0, wx.ALL | wx.CENTER, 5)
        vbox.Add(asboxSizer, 0, wx.ALL | wx.CENTER, 5)
        vbox.Add(sboxSizer, 0, wx.ALL | wx.CENTER, 5)
        vbox.Add(self._buttons['play'],0,wx.ALL | wx.CENTER, 5)

        # box = wx.BoxSizer(wx.HORIZONTAL)
        # fx2_2 = wx.StaticText(self._panel, -1, "程序正在执行中：当前进度70%")
        # box.Add(fx2_2,0,wx.ALL | wx.ALIGN_CENTER, 10)
        # slide = wx.Gauge(self._panel, -1, range = 100,size= (600,100),style = wx.GA_HORIZONTAL)
        # slide.SetValue(70)
        # box.Add(slide, 1, wx.ALL | wx.ALIGN_CENTER, 1)
        # vbox.Add(box)
        self._panel.SetSizer(vbox)


        self._panel.Layout()
        self.Show(True)


app = wx.App(False)
frame = Main_Frame2(None)
app.MainLoop()