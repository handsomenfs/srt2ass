![image](https://github.com/user-attachments/assets/be9294cc-f39c-437e-90f1-2728317d53b6)


# SRT2ASS  / SRT转ASS字幕转换工具

A powerful and user-friendly GUI application for converting SRT subtitle files to ASS format with advanced animation effects and multilingual support.

一个功能强大且用户友好的图形界面应用程序，用于将SRT字幕文件转换为ASS格式，支持高级动画效果和多语言界面。

## Features / 功能特性

### Core Functions / 核心功能
- **SRT to ASS Conversion** / **SRT转ASS转换**: Convert subtitle files from SRT format to Advanced SubStation Alpha (ASS) format
- **Batch Processing** / **批量处理**: Process multiple files or entire folders at once
- **Dual Mode Support** / **双模式支持**: Switch between single file and folder processing modes
- **Flexible Output Options** / **灵活输出选项**: Save converted files to custom directory or same location as source files

### Animation Effects / 动画效果
The application supports a wide variety of subtitle animation effects:

本应用支持多种字幕动画效果：

#### In Animations / 入场动画
- **Fade In** / **淡入**: Smooth opacity transition
- **Scale In** / **缩放进入**: Gradual size increase
- **Slide In** / **滑入**: From left, right, top, or bottom
- **Typewriter** / **逐字显示**: Character-by-character appearance
- **Dissolve** / **溶解**: Gradual materialization
- **Bounce In** / **弹跳进入**: Elastic entrance effect
- **Rotate In** / **旋转进入**: Spinning entrance
- **Blink In** / **闪烁进入**: Flashing appearance
- **Wave In** / **波浪进入**: Wavy entrance motion
- **Flip In** / **翻转进入**: 3D flip effect
- **Diagonal In** / **对角滑入**: Diagonal sliding entrance
- **Elastic In** / **弹性进入**: Elastic bounce effect

#### Out Animations / 退场动画
- **Fade Out** / **淡出**: Smooth opacity transition
- **Scale Out** / **缩放退出**: Gradual size decrease
- **Slide Out** / **滑出**: To left, right, top, or bottom
- **Dissolve Out** / **溶解退出**: Gradual dematerialization
- **Bounce Out** / **弹跳退出**: Elastic exit effect
- **Rotate Out** / **旋转退出**: Spinning exit
- **Instant Disappear** / **瞬间消失**: Immediate removal
- **Wave Out** / **波浪退出**: Wavy exit motion
- **Flip Out** / **翻转退出**: 3D flip exit effect
- **Diagonal Out** / **对角滑出**: Diagonal sliding exit
- **Elastic Out** / **弹性退出**: Elastic exit effect

### Multilingual Support / 多语言支持
- **Simplified Chinese** / **简体中文**: Full interface localization
- **Traditional Chinese** / **繁体中文**: Complete traditional Chinese support
- **English**: Full English interface

### Advanced Features / 高级功能
- **Random Animation Selection** / **随机动画选择**: Automatically applies random animations from selected options to each subtitle
- **Settings Persistence** / **设置持久化**: Automatically saves and restores user preferences
- **Intuitive Interface** / **直观界面**: Clean and easy-to-use PyQt5-based GUI
- **Progress Feedback** / **进度反馈**: Real-time processing status and completion notifications

## Technical Architecture / 技术架构

The application is built with a modular architecture consisting of three main components:

应用程序采用模块化架构，包含三个主要组件：

### Main Files / 主要文件
- srt2ass_gui.py: Main application logic and GUI implementation
- main_window.py: Window management and event handling
- ui_main_window.py: User interface layout and components

### Key Components / 关键组件
- **Srt2AssGUI Class** / **Srt2AssGUI类**: Main application window with conversion logic
- **AnimationSettingsDialog Class** / **AnimationSettingsDialog类**: Advanced animation configuration dialog
- **Language Management** / **语言管理**: Comprehensive multilingual text dictionary system
- **Settings Management** / **设置管理**: QSettings-based preference storage

## Installation / 安装

### Requirements / 系统要求
```
Python 3.6+
PyQt5
srt (Python library)
```

### Setup / 安装步骤
```bash
pip install PyQt5 srt
python srt2ass_gui.py
```

## Usage / 使用方法

1. **Launch the Application** / **启动应用程序**: Run the main script to open the GUI
2. **Select Input Mode** / **选择输入模式**: Choose between file or folder processing mode
3. **Choose Source** / **选择源文件**: Select SRT file(s) or folder containing SRT files
4. **Set Output Location** / **设置输出位置**: Choose output directory or use same directory option
5. **Configure Animations** / **配置动画**: Open animation settings to select desired effects
6. **Start Conversion** / **开始转换**: Click the start button to begin processing

## Animation Configuration / 动画配置

The animation settings dialog allows you to:

动画设置对话框允许您：

- **Select Multiple Effects** / **选择多种效果**: Choose from various in and out animations
- **Random Application** / **随机应用**: Each subtitle gets randomly assigned animations from your selection
- **Persistent Settings** / **持久设置**: Your animation preferences are automatically saved

## Output Format / 输出格式

The generated ASS files include:

生成的ASS文件包含：

- **Standard ASS Headers** / **标准ASS头部**: Script info and style definitions
- **Optimized Styling** / **优化样式**: Pre-configured styles for best compatibility
- **Advanced Animation Tags** / **高级动画标签**: Complex ASS animation commands for smooth effects
- **UTF-8 Encoding** / **UTF-8编码**: Proper encoding for international character support

## Contributing / 贡献

We welcome contributions to improve this tool! Feel free to:

我们欢迎为改进此工具做出贡献！您可以：

- Report bugs / 报告错误
- Suggest new features / 建议新功能
- Submit pull requests / 提交拉取请求
- Improve translations / 改进翻译

## License / 许可证

This project is open source and available under the MIT License.

此项目为开源项目，采用MIT许可证。

---

**Note**: This tool is designed for subtitle enthusiasts and video creators who need professional-quality animated subtitles for their content.

**注意**：此工具专为需要为其内容制作专业质量动画字幕的字幕爱好者和视频创作者设计。
