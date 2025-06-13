import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import srt
import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox,
    QPushButton, QLabel, QLineEdit, QHBoxLayout, QWidget,
    QVBoxLayout, QToolButton, QMenu, QCheckBox, QDialog, QGroupBox,
    QMenuBar, QAction
)
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtGui import QIcon
import random

# 多语言文本字典 / Multilingual text dictionary
LANGUAGES = {
    'zh_CN': {
        'window_title': 'SRT转ASS工具',
        'select_subtitle_file': '选择字幕文件',
        'select_subtitle_folder': '选择字幕文件夹',
        'select_output_folder': '选择输出文件夹',
        'same_directory': '生成在同一目录',
        'animation_settings': '字幕动画设置',
        'start_processing': '开始处理',
        'file_mode': '文件',
        'folder_mode': '文件夹',
        'error': '错误',
        'warning': '警告',
        'info': '提示',
        'please_select_subtitle': '请选择字幕文件',
        'please_select_output': '请选择输出文件夹',
        'no_valid_srt': '未找到有效的SRT文件',
        'conversion_complete': '转换完成！共处理 {} 个文件',
        'processing_file': '处理第 {}/{} 个文件: {}',
        'conversion_error': '转换文件 {} 时出错：{}',
        'language': '语言',
        'simplified_chinese': '简体中文',
        'traditional_chinese': '繁体中文',
        'english': 'English',
        'in_animations': '入场动画',
        'out_animations': '退场动画',
        'select_all': '全选',
        'fade_in': '淡入',
        'scale_in': '缩放进入',
        'slide_in_left': '滑入(自左)',
        'slide_in_right': '滑入(自右)',
        'slide_in_top': '滑入(自上)',
        'slide_in_bottom': '滑入(自下)',
        'typewriter': '逐字显示',
        'dissolve_in': '溶解',
        'bounce_in': '弹跳进入',
        'rotate_in': '旋转进入',
        'blink_in': '闪烁进入',
        'gradient_scale': '渐变缩放',
        'wave_in': '波浪进入',
        'flip_in': '翻转进入',
        'diagonal_in': '对角滑入',
        'elastic_in': '弹性进入',
        'fade_out': '淡出',
        'scale_out': '缩放退出',
        'slide_out_left': '滑出(向左)',
        'slide_out_right': '滑出(向右)',
        'slide_out_top': '滑出(向上)',
        'slide_out_bottom': '滑出(向下)',
        'dissolve_out': '溶解退出',
        'bounce_out': '弹跳退出',
        'rotate_out': '旋转退出',
        'blink_out': '闪烁退出',
        'gradient_scale_out': '渐变缩放退出',
        'instant_disappear': '瞬间消失',
        'wave_out': '波浪退出',
        'flip_out': '翻转退出',
        'diagonal_out': '对角滑出',
        'elastic_out': '弹性退出',
        'confirm': '确定'
    },
    'zh_TW': {
        'window_title': 'SRT轉ASS工具',
        'select_subtitle_file': '選擇字幕文件',
        'select_subtitle_folder': '選擇字幕文件夾',
        'select_output_folder': '選擇輸出文件夾',
        'same_directory': '生成在同一目錄',
        'animation_settings': '字幕動畫設置',
        'start_processing': '開始處理',
        'file_mode': '文件',
        'folder_mode': '文件夾',
        'error': '錯誤',
        'warning': '警告',
        'info': '提示',
        'please_select_subtitle': '請選擇字幕文件',
        'please_select_output': '請選擇輸出文件夾',
        'no_valid_srt': '未找到有效的SRT文件',
        'conversion_complete': '轉換完成！共處理 {} 個文件',
        'processing_file': '處理第 {}/{} 個文件: {}',
        'conversion_error': '轉換文件 {} 時出錯：{}',
        'language': '語言',
        'simplified_chinese': '簡體中文',
        'traditional_chinese': '繁體中文',
        'english': 'English',
        'in_animations': '入場動畫',
        'out_animations': '退場動畫',
        'select_all': '全選',
        'fade_in': '淡入',
        'scale_in': '縮放進入',
        'slide_in_left': '滑入(自左)',
        'slide_in_right': '滑入(自右)',
        'slide_in_top': '滑入(自上)',
        'slide_in_bottom': '滑入(自下)',
        'typewriter': '逐字顯示',
        'dissolve_in': '溶解',
        'bounce_in': '彈跳進入',
        'rotate_in': '旋轉進入',
        'blink_in': '閃爍進入',
        'gradient_scale': '漸變縮放',
        'wave_in': '波浪進入',
        'flip_in': '翻轉進入',
        'diagonal_in': '對角滑入',
        'elastic_in': '彈性進入',
        'fade_out': '淡出',
        'scale_out': '縮放退出',
        'slide_out_left': '滑出(向左)',
        'slide_out_right': '滑出(向右)',
        'slide_out_top': '滑出(向上)',
        'slide_out_bottom': '滑出(向下)',
        'dissolve_out': '溶解退出',
        'bounce_out': '彈跳退出',
        'rotate_out': '旋轉退出',
        'blink_out': '閃爍退出',
        'gradient_scale_out': '漸變縮放退出',
        'instant_disappear': '瞬間消失',
        'wave_out': '波浪退出',
        'flip_out': '翻轉退出',
        'diagonal_out': '對角滑出',
        'elastic_out': '彈性退出',
        'confirm': '確定'
    },
    'en': {
        'window_title': 'SRT to ASS Converter',
        'select_subtitle_file': 'Select Subtitle File',
        'select_subtitle_folder': 'Select Subtitle Folder',
        'select_output_folder': 'Select Output Folder',
        'same_directory': 'Save in Same Directory',
        'animation_settings': 'Subtitle Animation Settings',
        'start_processing': 'Start Processing',
        'file_mode': 'File',
        'folder_mode': 'Folder',
        'error': 'Error',
        'warning': 'Warning',
        'info': 'Info',
        'please_select_subtitle': 'Please select subtitle file',
        'please_select_output': 'Please select output folder',
        'no_valid_srt': 'No valid SRT files found',
        'conversion_complete': 'Conversion complete! Processed {} files',
        'processing_file': 'Processing file {}/{}: {}',
        'conversion_error': 'Error converting file {}: {}',
        'language': 'Language',
        'simplified_chinese': '简体中文',
        'traditional_chinese': '繁體中文',
        'english': 'English',
        'in_animations': 'In Animations',
        'out_animations': 'Out Animations',
        'select_all': 'Select All',
        'fade_in': 'Fade In',
        'scale_in': 'Scale In',
        'slide_in_left': 'Slide In (Left)',
        'slide_in_right': 'Slide In (Right)',
        'slide_in_top': 'Slide In (Top)',
        'slide_in_bottom': 'Slide In (Bottom)',
        'typewriter': 'Typewriter',
        'dissolve_in': 'Dissolve In',
        'bounce_in': 'Bounce In',
        'rotate_in': 'Rotate In',
        'blink_in': 'Blink In',
        'gradient_scale': 'Gradient Scale',
        'wave_in': 'Wave In',
        'flip_in': 'Flip In',
        'diagonal_in': 'Diagonal In',
        'elastic_in': 'Elastic In',
        'fade_out': 'Fade Out',
        'scale_out': 'Scale Out',
        'slide_out_left': 'Slide Out (Left)',
        'slide_out_right': 'Slide Out (Right)',
        'slide_out_top': 'Slide Out (Top)',
        'slide_out_bottom': 'Slide Out (Bottom)',
        'dissolve_out': 'Dissolve Out',
        'bounce_out': 'Bounce Out',
        'rotate_out': 'Rotate Out',
        'blink_out': 'Blink Out',
        'gradient_scale_out': 'Gradient Scale Out',
        'instant_disappear': 'Instant Disappear',
        'wave_out': 'Wave Out',
        'flip_out': 'Flip Out',
        'diagonal_out': 'Diagonal Out',
        'elastic_out': 'Elastic Out',
        'confirm': 'OK'
    }
}

def srt_to_ass(srt_content):
    subs = list(srt.parse(srt_content))
    ass_header = """[Script Info]
ScriptType: v4.00+
Collisions: Normal
PlayResY: 600
PlayResX: 800
Timer: 100.0000

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,36,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,2,2,2,10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ass_events = ""
    for sub in subs:
        def to_ass_time(t):
            total = datetime.timedelta(seconds=t.total_seconds())
            h, remainder = divmod(total.seconds, 3600)
            m, s = divmod(remainder, 60)
            cs = int(t.microseconds / 10000)
            return f"{h:d}:{m:02d}:{s:02d}.{cs:02d}"
        text = sub.content.replace('\n', '\\N')
        ass_events += f"Dialogue: 0,{to_ass_time(sub.start)},{to_ass_time(sub.end)},Default,,0,0,0,,{text}\n"
    return ass_header + ass_events

def batch_convert_srt_to_ass(files, output_dir):
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            srt_content = f.read()
        ass_content = srt_to_ass(srt_content)
        base = os.path.splitext(os.path.basename(file))[0]
        ass_path = os.path.join(output_dir, base + '.ass')
        with open(ass_path, 'w', encoding='utf-8') as f:
            f.write(ass_content)

class Srt2AssGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        print("初始化SRT转ASS工具... / Initializing SRT to ASS converter...")
        self.settings = QSettings("srt2ass", "srt2ass_gui")
        self.current_language = self.settings.value("language", "zh_CN")
        self.setWindowTitle(self.tr('window_title'))
        self.setGeometry(100, 100, 600, 400)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        # 初始化随机动画变量 / Initialize random animation variables
        self.current_in_animation = None
        self.current_out_animation = None
        self.init_ui()
        self.load_settings()

    def tr(self, key):
        """翻译函数 / Translation function"""
        return LANGUAGES.get(self.current_language, LANGUAGES['zh_CN']).get(key, key)

    def change_language(self, lang_code):
        """切换语言 / Switch language"""
        self.current_language = lang_code
        self.settings.setValue("language", lang_code)
        self.update_ui_text()
        print(f"切换语言到: {lang_code} / Switched language to: {lang_code}")

    def update_ui_text(self):
        """更新界面文本 / Update UI text"""
        self.setWindowTitle(self.tr('window_title'))
        self.btn_select_subtitle.setText(self.tr('select_subtitle_file'))
        self.btn_select_output.setText(self.tr('select_output_folder'))
        self.checkbox_same_dir.setText(self.tr('same_directory'))
        self.btn_animation_settings.setText(self.tr('animation_settings'))
        self.btn_start.setText(self.tr('start_processing'))
        
        # 更新模式菜单 / Update mode menu
        if hasattr(self, 'mode_menu'):
            self.mode_menu.clear()
            self.mode_menu.addAction(self.tr('file_mode'), lambda: self.set_file_mode("文件"))
            self.mode_menu.addAction(self.tr('folder_mode'), lambda: self.set_file_mode("文件夹"))
        
        # 更新动画设置对话框（如果存在） / Update animation settings dialog (if exists)
        if hasattr(self, 'animation_settings_dialog'):
            self.animation_settings_dialog.update_ui_text()

    def closeEvent(self, event):
        print("正在保存设置并关闭应用... / Saving settings and closing application...")
        self.save_settings()
        super().closeEvent(event)

    def save_settings(self):
        print("保存设置到注册表... / Saving settings to registry...")
        # 路径 / Paths
        self.settings.setValue("subtitle_lineedit", self.subtitle_lineedit.text())
        self.settings.setValue("output_lineedit", self.output_lineedit.text())
        self.settings.setValue("file_mode", getattr(self, "file_mode", "文件"))
        self.settings.setValue("same_dir", self.checkbox_same_dir.isChecked())
        self.settings.setValue("language", self.current_language)
        # 动画设置窗口 / Animation settings window
        if hasattr(self, "animation_settings_dialog"):
            dlg = self.animation_settings_dialog
            # 出场动画 / In animations
            self.settings.setValue("in_animations", [cb.isChecked() for cb in dlg.in_checks])
            # 退场动画 / Out animations
            self.settings.setValue("out_animations", [cb.isChecked() for cb in dlg.out_checks])

    def load_settings(self):
        print("从注册表加载设置... / Loading settings from registry...")
        # 检查控件是否存在再加载设置 / Check if controls exist before loading settings
        if hasattr(self, 'subtitle_lineedit'):
            self.subtitle_lineedit.setText(self.settings.value("subtitle_lineedit", ""))
        if hasattr(self, 'output_lineedit'):
            self.output_lineedit.setText(self.settings.value("output_lineedit", ""))
        if hasattr(self, 'file_mode'):
            self.file_mode = self.settings.value("file_mode", "文件")
        if hasattr(self, 'checkbox_same_dir'):
            self.checkbox_same_dir.setChecked(self.settings.value("same_dir", False, type=bool))
        self.current_language = self.settings.value("language", "zh_CN")
        # 动画设置窗口（如果已创建） / Animation settings window (if created)
        if hasattr(self, "animation_settings_dialog"):
            dlg = self.animation_settings_dialog
            in_states = self.settings.value("in_animations", [])
            out_states = self.settings.value("out_animations", [])
            for cb, state in zip(dlg.in_checks, in_states):
                cb.setChecked(state == 'true' or state is True)
            for cb, state in zip(dlg.out_checks, out_states):
                cb.setChecked(state == 'true' or state is True)
        print("设置加载完成 / Settings loaded successfully")

    def set_file_mode(self, mode):
        print(f"切换文件模式: {mode} / Switching file mode: {mode}")
        self.file_mode = mode
        self.btn_mode_menu.setToolTip(f"当前模式: {mode} / Current mode: {mode}")
        if mode == "文件":
            self.btn_select_subtitle.setText(self.tr('select_subtitle_file'))
        else:
            self.btn_select_subtitle.setText(self.tr('select_subtitle_folder'))

    def on_same_dir_checked(self, state):
        checked = self.checkbox_same_dir.isChecked()
        print(f"生成在同一目录复选框状态变更: {checked} / Same directory checkbox state changed: {checked}")
        self.output_lineedit.setEnabled(not checked)
        self.btn_select_output.setEnabled(not checked)

    def select_subtitle_file(self):
        mode = getattr(self, "file_mode", "文件")
        print(f"选择字幕文件，当前模式: {mode} / Selecting subtitle file, current mode: {mode}")
        if mode == "文件":
            file_paths, _ = QFileDialog.getOpenFileNames(
                self,
                "选择字幕文件",
                "",
                "SRT字幕文件 (*.srt)"
            )
            if file_paths:
                print(f"选择了 {len(file_paths)} 个文件: {file_paths} / Selected {len(file_paths)} files: {file_paths}")
                self.subtitle_lineedit.setText(";".join(file_paths))
                self.srt_files_in_folder = file_paths  # 统一用此变量保存待处理文件 / Use this variable to store files to be processed
        else:
            folder_path = QFileDialog.getExistingDirectory(self, "选择字幕文件夹", "")
            if folder_path:
                print(f"选择文件夹: {folder_path} / Selected folder: {folder_path}")
                self.subtitle_lineedit.setText(folder_path)
                import os
                srt_files = []
                for root, dirs, files in os.walk(folder_path):
                    for f in files:
                        if f.lower().endswith('.srt'):
                            srt_files.append(os.path.join(root, f))
                self.srt_files_in_folder = srt_files
                print(f"在文件夹中找到 {len(srt_files)} 个SRT文件 / Found {len(srt_files)} SRT files in folder")

    def select_output_folder(self):
        print("选择输出文件夹... / Selecting output folder...")
        dir_path = QFileDialog.getExistingDirectory(self, "选择输出文件夹", "")
        if dir_path:
            print(f"选择的输出文件夹: {dir_path} / Selected output folder: {dir_path}")
            self.output_lineedit.setText(dir_path)

    def convert(self):
        files = getattr(app, 'selected_files', [])
        output_dir = getattr(app, 'output_dir', '')
        if not files or (not output_dir and not self.checkbox_same_dir.isChecked()):
            QMessageBox.critical(self, "错误", "请选择字幕文件和输出文件夹")
            return
        try:
            batch_convert_srt_to_ass(files, output_dir)
            QMessageBox.information(self, "完成", "批量转换完成！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"转换失败: {e}")

    def get_output_path(self, srt_path):
        # 只根据复选框决定输出路径，不再检查输出目录
        if hasattr(self, "checkbox_same_dir") and self.checkbox_same_dir.isChecked():
            import os
            folder = os.path.dirname(srt_path)
            base = os.path.splitext(os.path.basename(srt_path))[0]
            return os.path.join(folder, base + ".ass")
        else:
            # ...existing code...
            pass

    def open_animation_settings(self):
        print("打开动画设置窗口...")
        self.animation_settings_dialog = AnimationSettingsDialog(self)
        # 加载动画设置
        in_states = self.settings.value("in_animations", [])
        out_states = self.settings.value("out_animations", [])
        for cb, state in zip(self.animation_settings_dialog.in_checks, in_states):
            cb.setChecked(state == 'true' or state is True)
        for cb, state in zip(self.animation_settings_dialog.out_checks, out_states):
            cb.setChecked(state == 'true' or state is True)
        self.animation_settings_dialog.exec_()
        # 关闭窗口时自动保存
        self.save_settings()
        print("动画设置窗口已关闭")

    def init_ui(self):
        # 创建菜单栏 / Create menu bar
        menubar = self.menuBar()
        
        # 语言菜单 / Language menu
        language_menu = menubar.addMenu(self.tr('language'))
        
        # 简体中文 / Simplified Chinese
        zh_cn_action = QAction(self.tr('simplified_chinese'), self)
        zh_cn_action.triggered.connect(lambda: self.change_language('zh_CN'))
        language_menu.addAction(zh_cn_action)
        
        # 繁体中文 / Traditional Chinese
        zh_tw_action = QAction(self.tr('traditional_chinese'), self)
        zh_tw_action.triggered.connect(lambda: self.change_language('zh_TW'))
        language_menu.addAction(zh_tw_action)
        
        # English
        en_action = QAction(self.tr('english'), self)
        en_action.triggered.connect(lambda: self.change_language('en'))
        language_menu.addAction(en_action)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # 字幕文件选择行 / Subtitle file selection row
        subtitle_layout = QHBoxLayout()
        self.subtitle_lineedit = QLineEdit(self)
        self.btn_select_subtitle = QPushButton(self.tr('select_subtitle_file'), self)
        self.btn_mode_menu = QToolButton(self)
        self.btn_mode_menu.setText("▼")
        self.btn_mode_menu.setPopupMode(QToolButton.InstantPopup)
        self.mode_menu = QMenu(self)
        self.mode_menu.addAction(self.tr('file_mode'), lambda: self.set_file_mode("文件"))
        self.mode_menu.addAction(self.tr('folder_mode'), lambda: self.set_file_mode("文件夹"))
        self.btn_mode_menu.setMenu(self.mode_menu)
        self.file_mode = "文件"
        
        subtitle_layout.addWidget(self.subtitle_lineedit)
        subtitle_layout.addWidget(self.btn_select_subtitle)
        subtitle_layout.addWidget(self.btn_mode_menu)
        main_layout.addLayout(subtitle_layout)

        # 输出文件夹选择行 / Output folder selection row
        output_layout = QHBoxLayout()
        self.output_lineedit = QLineEdit(self)
        self.btn_select_output = QPushButton(self.tr('select_output_folder'), self)
        self.checkbox_same_dir = QCheckBox(self.tr('same_directory'), self)
        output_layout.addWidget(self.output_lineedit)
        output_layout.addWidget(self.btn_select_output)
        output_layout.addWidget(self.checkbox_same_dir)
        main_layout.addLayout(output_layout)

        # 字幕动画设置按钮 / Subtitle animation settings button
        self.btn_animation_settings = QPushButton(self.tr('animation_settings'), self)
        main_layout.addWidget(self.btn_animation_settings)

        # 开始处理按钮 / Start processing button
        self.btn_start = QPushButton(self.tr('start_processing'), self)
        main_layout.addWidget(self.btn_start)

        # 连接信号 / Connect signals
        self.btn_select_subtitle.clicked.connect(self.select_subtitle_file)
        self.btn_select_output.clicked.connect(self.select_output_folder)
        self.btn_animation_settings.clicked.connect(self.open_animation_settings)
        self.checkbox_same_dir.stateChanged.connect(self.on_same_dir_checked)
        self.btn_start.clicked.connect(self.start_convert)

    def start_convert(self):
        print("开始转换处理... / Starting conversion process...")
        subtitle = self.subtitle_lineedit.text().strip()
        same_dir = self.checkbox_same_dir.isChecked()
        output_dir = self.output_lineedit.text().strip()
        
        print(f"字幕路径: {subtitle} / Subtitle path: {subtitle}")
        print(f"生成在同一目录: {same_dir} / Generate in same directory: {same_dir}")
        print(f"输出目录: {output_dir} / Output directory: {output_dir}")

        if not subtitle:
            QMessageBox.critical(self, self.tr('error'), self.tr('please_select_subtitle'))
            return

        if not same_dir and not output_dir:
            QMessageBox.critical(self, self.tr('error'), self.tr('please_select_output'))
            return

        # 获取要处理的SRT文件列表 / Get list of SRT files to process
        srt_files = []
        if hasattr(self, 'srt_files_in_folder') and self.srt_files_in_folder:
            srt_files = self.srt_files_in_folder
            print(f"使用已加载的文件列表，共 {len(srt_files)} 个文件 / Using loaded file list, {len(srt_files)} files total")
        elif ";" in subtitle:  # 多文件选择 / Multiple file selection
            srt_files = subtitle.split(";")
            print(f"多文件选择，共 {len(srt_files)} 个文件 / Multiple file selection, {len(srt_files)} files total")
        elif subtitle.endswith('.srt'):  # 单文件 / Single file
            srt_files = [subtitle]
            print("单文件模式 / Single file mode")
        
        if not srt_files:
            print("错误: 未找到有效的SRT文件 / Error: No valid SRT files found")
            QMessageBox.critical(self, self.tr('error'), self.tr('no_valid_srt'))
            return

        # 转换每个SRT文件 / Convert each SRT file
        import os
        converted_count = 0
        for i, srt_file in enumerate(srt_files, 1):
            print(self.tr('processing_file').format(i, len(srt_files), srt_file))
            
            # 为每个文件随机选择动画 / Randomly select animations for each file
            self.select_random_animations()
            
            try:
                # 确定输出路径 / Determine output path
                if same_dir:
                    output_path = os.path.splitext(srt_file)[0] + ".ass"
                else:
                    filename = os.path.splitext(os.path.basename(srt_file))[0] + ".ass"
                    output_path = os.path.join(output_dir, filename)
                
                print(f"输出路径: {output_path} / Output path: {output_path}")
                
                # 实际转换SRT到ASS / Actual SRT to ASS conversion
                self.convert_srt_to_ass(srt_file, output_path)
                converted_count += 1
                print(f"文件 {srt_file} 转换成功 / File {srt_file} converted successfully")
            except Exception as e:
                print(f"转换文件 {srt_file} 时出错: {str(e)} / Error converting file {srt_file}: {str(e)}")
                QMessageBox.warning(self, self.tr('warning'), self.tr('conversion_error').format(srt_file, str(e)))

        print(f"转换完成！共处理 {converted_count} 个文件 / Conversion complete! Processed {converted_count} files")
        QMessageBox.information(self, self.tr('info'), self.tr('conversion_complete').format(converted_count))

    def select_random_animations(self):
        """为当前文件随机选择入场和出场动画 / Randomly select in and out animations for current file"""
        # 检查是否有动画设置对话框 / Check if animation settings dialog exists
        if not hasattr(self, 'animation_settings_dialog'):
            print("未找到动画设置对话框，使用默认动画 / Animation settings dialog not found, using default animations")
            self.current_in_animation = '淡入'
            self.current_out_animation = '淡出'
            return
            
        dlg = self.animation_settings_dialog
        
        # 获取选中的入场动画（排除全选） / Get selected in animations (excluding select all)
        selected_in_animations = []
        in_options = ['淡入', '缩放进入', '滑入(自左)', '滑入(自右)', '滑入(自上)', '滑入(自下)', 
                     '逐字显示', '溶解', '弹跳进入', '旋转进入', '闪烁进入', '渐变缩放',
                     '波浪进入', '翻转进入', '对角滑入', '弹性进入']
        
        for i, option in enumerate(in_options):
            if i + 1 < len(dlg.in_checks) and dlg.in_checks[i + 1].isChecked():
                selected_in_animations.append(option)
        
        # 获取选中的出场动画（排除全选） / Get selected out animations (excluding select all)
        selected_out_animations = []
        out_options = ['淡出', '缩放退出', '滑出(向左)', '滑出(向右)', '滑出(向上)', '滑出(向下)',
                      '溶解退出', '弹跳退出', '旋转退出', '闪烁退出', '渐变缩放退出', '瞬间消失',
                      '波浪退出', '翻转退出', '对角滑出', '弹性退出']
        
        for i, option in enumerate(out_options):
            if i + 1 < len(dlg.out_checks) and dlg.out_checks[i + 1].isChecked():
                selected_out_animations.append(option)
        
        # 如果没有选中任何动画，使用默认动画 / If no animations selected, use default animations
        if not selected_in_animations:
            selected_in_animations = ['淡入']
            print("未选择入场动画，使用默认淡入 / No in animation selected, using default fade in")
        if not selected_out_animations:
            selected_out_animations = ['淡出']
            print("未选择出场动画，使用默认淡出 / No out animation selected, using default fade out")
        
        # 从选中的动画中随机选择 / Randomly select from chosen animations
        self.current_in_animation = random.choice(selected_in_animations)
        self.current_out_animation = random.choice(selected_out_animations)
        
        print(f"从选中动画中随机选择: 入场-{self.current_in_animation}, 出场-{self.current_out_animation} / Randomly selected from chosen animations: in-{self.current_in_animation}, out-{self.current_out_animation}")
        print(f"可选入场动画: {selected_in_animations} / Available in animations: {selected_in_animations}")
        print(f"可选出场动画: {selected_out_animations} / Available out animations: {selected_out_animations}")

    def convert_srt_to_ass(self, srt_path, ass_path):
        print(f"开始转换SRT到ASS: {srt_path} -> {ass_path} / Starting SRT to ASS conversion: {srt_path} -> {ass_path}")
        
        with open(srt_path, 'r', encoding='utf-8') as f:
            srt_content = f.read()
        
        print(f"SRT文件大小: {len(srt_content)} 字符 / SRT file size: {len(srt_content)} characters")
        
        # 使用srt库解析SRT文件 / Parse SRT file using srt library
        try:
            subs = list(srt.parse(srt_content))
            print(f"成功解析 {len(subs)} 条字幕 / Successfully parsed {len(subs)} subtitles")
        except Exception as e:
            print(f"SRT解析失败: {e} / SRT parsing failed: {e}")
            return
        
        # ASS文件头 - 标准ASS格式，字幕位置设置在底部 / ASS file header - standard ASS format, subtitle position set at bottom
        ass_content = """[Script Info]
Title: Converted from SRT
ScriptType: v4.00+
WrapStyle: 0
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,48,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,2,2,2,54,54,160,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
        
        # 转换每个字幕 / Convert each subtitle
        for sub in subs:
            def to_ass_time(t):
                total_seconds = int(t.total_seconds())
                hours = total_seconds // 3600
                minutes = (total_seconds % 3600) // 60
                seconds = total_seconds % 60
                microseconds = t.microseconds
                centiseconds = microseconds // 10000
                return f"{hours}:{minutes:02d}:{seconds:02d}.{centiseconds:02d}"
            
            start_time = to_ass_time(sub.start)
            end_time = to_ass_time(sub.end)
            text = sub.content.replace('\n', '\\N')
            
            # 添加动画效果 / Add animation effects
            animated_text = self.apply_animations(text)
            
            ass_content += f"Dialogue: 0,{start_time},{end_time},Default,,0,0,0,,{animated_text}\n"
        
        with open(ass_path, 'w', encoding='utf-8-sig') as f:
            f.write(ass_content)
        
        print(f"ASS文件已保存: {ass_path} / ASS file saved: {ass_path}")

    def apply_animations(self, text):
        if not hasattr(self, 'current_in_animation') or not hasattr(self, 'current_out_animation'):
            print("未选择随机动画，跳过动画应用 / No random animations selected, skipping animation application")
            return text
            
        animated_text = text
        animation_tags = []
        
        print(f"为文本应用动画: '{text[:20]}...', 入场: {self.current_in_animation}, 出场: {self.current_out_animation} / Applying animations to text: '{text[:20]}...', in: {self.current_in_animation}, out: {self.current_out_animation}")
        
        # 应用入场动画 / Apply in animations
        if self.current_in_animation == '淡入':
            animation_tags.append("\\fad(250,0)")
        elif self.current_in_animation == '缩放进入':
            animation_tags.append("\\fscx0\\fscy0\\t(0,250,\\fscx100\\fscy100)")
        elif self.current_in_animation == '滑入(自左)':
            animation_tags.append("\\move(-200,1600,540,1600,0,250)")
        elif self.current_in_animation == '滑入(自右)':
            animation_tags.append("\\move(1280,1600,540,1600,0,250)")
        elif self.current_in_animation == '滑入(自上)':
            animation_tags.append("\\move(540,-100,540,1600,0,250)")
        elif self.current_in_animation == '滑入(自下)':
            animation_tags.append("\\move(540,2000,540,1600,0,250)")
        elif self.current_in_animation == '逐字显示':
            animated_text = "{\\k15}" + animated_text.replace(" ", "{\\k15} ")
        elif self.current_in_animation == '溶解':
            animation_tags.append("\\fad(400,0)")
        elif self.current_in_animation == '弹跳进入':
            animation_tags.append("\\fscx120\\fscy120\\t(0,100,\\fscx90\\fscy90)\\t(100,200,\\fscx110\\fscy110)\\t(200,300,\\fscx100\\fscy100)")
        elif self.current_in_animation == '旋转进入':
            animation_tags.append("\\frz360\\t(0,400,\\frz0)")
        elif self.current_in_animation == '闪烁进入':
            animation_tags.append("\\alpha&HFF&\\t(0,50,\\alpha&H00&)\\t(50,100,\\alpha&HFF&)\\t(100,150,\\alpha&H00&)\\t(150,200,\\alpha&HFF&)\\t(200,250,\\alpha&H00&)")
        elif self.current_in_animation == '渐变缩放':
            animation_tags.append("\\fscx50\\fscy50\\alpha&H80&\\t(0,300,\\fscx100\\fscy100\\alpha&H00&)")
        elif self.current_in_animation == '波浪进入':
            animation_tags.append("\\t(0,400,\\frx20\\fry20)\\t(200,600,\\frx0\\fry0)")
        elif self.current_in_animation == '翻转进入':
            animation_tags.append("\\fry180\\t(0,300,\\fry0)")
        elif self.current_in_animation == '对角滑入':
            animation_tags.append("\\move(-200,-200,540,1600,0,300)")
        elif self.current_in_animation == '弹性进入':
            animation_tags.append("\\fscx0\\fscy0\\t(0,150,\\fscx150\\fscy150)\\t(150,250,\\fscx80\\fscy80)\\t(250,350,\\fscx110\\fscy110)\\t(350,400,\\fscx100\\fscy100)")
        
        # 应用出场动画 / Apply out animations
        if self.current_out_animation == '淡出':
            if "\\fad(" not in "".join(animation_tags):
                animation_tags.append("\\fad(0,250)")
        elif self.current_out_animation == '缩放退出':
            animation_tags.append("\\t(\\*,\\*,\\fscx0\\fscy0)")
        elif self.current_out_animation == '滑出(向左)':
            animation_tags.append("\\move(540,1600,-200,1600)")
        elif self.current_out_animation == '滑出(向右)':
            animation_tags.append("\\move(540,1600,1280,1600)")
        elif self.current_out_animation == '滑出(向上)':
            animation_tags.append("\\move(540,1600,540,-100)")
        elif self.current_out_animation == '滑出(向下)':
            animation_tags.append("\\move(540,1600,540,2000)")
        elif self.current_out_animation == '溶解退出':
            if "\\fad(" not in "".join(animation_tags):
                animation_tags.append("\\fad(0,800)")
        elif self.current_out_animation == '弹跳退出':
            animation_tags.append("\\t(\\*,\\*,\\fscx120\\fscy120)\\t(\\*,\\*,\\fscx0\\fscy0)")
        elif self.current_out_animation == '旋转退出':
            animation_tags.append("\\t(\\*,\\*,\\frz360)")
        elif self.current_out_animation == '闪烁退出':
            animation_tags.append("\\t(\\*,\\*,\\alpha&HFF&)")
        elif self.current_out_animation == '渐变缩放退出':
            animation_tags.append("\\t(\\*,\\*,\\fscx50\\fscy50\\alpha&H80&)")
        elif self.current_out_animation == '瞬间消失':
            animation_tags.append("\\t(\\*,\\*,\\alpha&HFF&)")
        elif self.current_out_animation == '波浪退出':
            animation_tags.append("\\t(\\*,\\*,\\frx30\\fry30)")
        elif self.current_out_animation == '翻转退出':
            animation_tags.append("\\t(\\*,\\*,\\fry180)")
        elif self.current_out_animation == '对角滑出':
            animation_tags.append("\\move(540,1600,1280,2000)")
        elif self.current_out_animation == '弹性退出':
            animation_tags.append("\\t(\\*,\\*,\\fscx120\\fscy120)\\t(\\*,\\*,\\fscx0\\fscy0)")
            
        # 组合动画标签 / Combine animation tags
        if animation_tags:
            animated_text = "{" + "".join(animation_tags) + "}" + animated_text
            print(f"应用了 {len(animation_tags)} 个动画标签 / Applied {len(animation_tags)} animation tags")
        else:
            print("未应用任何动画 / No animations applied")
            
        return animated_text

class AnimationSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        print("创建动画设置对话框... / Creating animation settings dialog...")
        self.setWindowTitle(self.tr('animation_settings'))
        self.setFixedSize(800, 600)
        self.init_ui()

    def tr(self, key):
        """翻译函数 / Translation function"""
        if hasattr(self.parent, 'tr'):
            return self.parent.tr(key)
        return LANGUAGES.get('zh_CN', {}).get(key, key)

    def toggle_all_checks(self, checks, state):
        print(f"全选状态变更: {state == 2} / Select all state changed: {state == 2}")
        # 跳过第一个（全选），其余全部设置 / Skip first (select all), set all others
        for cb in checks[1:]:
            cb.setChecked(state == 2)

print("启动应用程序... / Starting application...")
app = QApplication([])
window = Srt2AssGUI()
window.show()
print("应用程序启动完成 / Application startup complete")
app.exec_()