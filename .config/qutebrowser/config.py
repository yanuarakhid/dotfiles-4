# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# load plugin
import sys
import os
from xresources import read_xresources

xresources = read_xresources("*")

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {
    "q": "close",
    "qa": "quit",
    "w": "session-save",
    "wq": "quit --save",
    "wqa": "quit --save",
}

# Enable JavaScript.
# Type: Bool
config.set("content.javascript.enabled", True, "file://*")

# Enable JavaScript.
# Type: Bool
config.set("content.javascript.enabled", True, "chrome://*/*")

# Enable JavaScript.
# Type: Bool
config.set("content.javascript.enabled", True, "qute://*/*")

# Editor (and arguments) to use for the `open-editor` command. The
# following placeholders are defined: * `{file}`: Filename of the file
# to be edited. * `{line}`: Line in which the caret is found in the
# text. * `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ["st", "-e", "nvim", "{file}"]

# Open new tabs (middleclick/ctrl+click) in the background.
# Type: Bool
c.tabs.background = True

# Padding (in pixels) around text for tabs.
# Type: Padding
c.tabs.padding = {"bottom": 2, "left": 5, "right": 5, "top": 3}

# Position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = "bottom"

# Alignment of the text inside of tabs.
# Type: TextAlignment
# Valid values:
#   - left
#   - right
#   - center
c.tabs.title.alignment = "center"

# Format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: Percentage as a string like `[10%]`. *
# `{perc_raw}`: Raw percentage, e.g. `10`. * `{current_title}`: Title of the
# current web page. * `{title_sep}`: The string ` - ` if a title is set,
# empty otherwise. * `{index}`: Index of this tab. * `{id}`: Internal
# tab ID of this tab. * `{scroll_pos}`: Page scroll position. *
# `{host}`: Host of the current web page. * `{backend}`: Either
# ''webkit'' or ''webengine'' * `{private}`: Indicates when private mode
# is enabled. * `{current_url}`: URL of the current web page. *
# `{protocol}`: Protocol (http/https/...) of the current web page. *
# `{audio}`: Indicator for audio/mute status.
# Type: FormatString
c.tabs.title.format = "{audio}{index}: {current_title}"

# Padding (in pixels) for tab indicators.
# Type: Padding
c.tabs.indicator.padding = {"bottom": 2, "left": 0, "right": 4, "top": 2}

# When to show favicons in the tab bar.
# Type: String
c.tabs.favicons.show = "pinned"

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
# for a blank page.
# Type: FuzzyUrl
c.url.default_page = "about:blank"

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "ag": "http://anigrab.herokuapp.com/?keyword={}",
    "au": "https://aur.archlinux.org/packages/?O=0&K={}",
    "aw": "https://wiki.archlinux.org/?search={}",
    "da": "http://www.deviantart.com/?q={}",
    "dz": "https://www.deezer.com/search/{}",
    "g": "https://www.google.com/search?hl=en&q={}",
    "gh": "https://github.com/search?q={}",
    "gl": "https://gitlab.com/search?search={}",
    "gt": "https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text={}",
    "mal": "https://myanimelist.net/search/all?q={}",
    "py": "https://pypi.org/search/?q={}",
    "wp": "https://id.wikipedia.org/w/index.php?search={}",
    "yp": "https://yarnpkg.com/en/packages?q={}&p=1",
    "yt": "https://www.youtube.com/results?search_query={}",
}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = "about:blank"

# Text color of the completion widget. May be a single color to use for all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = [
    xresources["*color15"],
    xresources["*color7"],
    xresources["*color15"],
]

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = xresources["*color0"]

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = xresources["*color0"]

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = xresources["*color15"]

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = xresources["*color0"]

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = xresources["*color0"]

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = xresources["*color0"]

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = xresources["*color0"]

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = xresources["*color3"]

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.item.selected.border.top = xresources["*color3"]

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = xresources["*color3"]

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = xresources["*color3"]

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = xresources["*color3"]

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = xresources["*color0"]

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = xresources["*color0"]

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = xresources["*color0"]

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = xresources["*color0"]

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = xresources["*color11"]

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = xresources["*color15"]

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = xresources["*color0"]

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = "1px solid {}".format(xresources["*color0"])

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = xresources["*color3"]

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = xresources["*color0"]

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = xresources["*color15"]

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = xresources["*color0"]

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = xresources["*color0"]

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = xresources["*color11"]

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = xresources["*color0"]

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = xresources["*color11"]

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = xresources["*color0"]

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = xresources["*color2"]

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = xresources["*color0"]

# Background color of the tab bar.
# Type: QtColor
c.colors.tabs.bar.bg = xresources["*color0"]

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = xresources["*color15"]

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = xresources["*color0"]

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = xresources["*color15"]

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = xresources["*color0"]

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = xresources["*color0"]

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = xresources["*color3"]

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = xresources["*color0"]

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = xresources["*color3"]

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = xresources["*color1"]

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = xresources["*color4"]

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = xresources["*color2"]

# Background color for webpages if unset (or empty to use the theme’s color).
# Type: QtColor
c.colors.webpage.bg = xresources["*color0"]

# Width (in pixels) of the scrollbar in the completion window.
# Type: Int
c.completion.scrollbar.width = 8

# Automatically start playing <video> elements.
# Type: Bool
c.content.autoplay = False

# Allow JavaScript to read from or write to the clipboard.
# Type: Bool
c.content.javascript.can_access_clipboard = True

# Allow JavaScript to open new tabs without user interaction.
# Type: Bool
c.content.javascript.can_open_tabs_automatically = True

# Use the standard JavaScript modal dialog for alert() and confirm().
# Type: Bool
c.content.javascript.modal_dialog = True

# Allow pdf.js to view PDF files in the browser.
# Type: Bool
c.content.pdfjs = False

# Open new windows in private browsing mode which does not record visited pages.
# Type: Bool
c.content.private_browsing = False

# Try to pre-fetch DNS entries to speed up browsing.
# Type: Bool
c.content.dns_prefetch = True

# List of URLs of lists which contain hosts to block.
# it’s also possible to add a local file or directory via a file:// URL. In case of a directory, all files in the directory are read as adblock lists.
# The file ~/.config/qutebrowser/blocked-hosts is always read if it exists.
c.content.host_blocking.lists = [
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=1&mimetype=plaintext",
    "https://www.malwaredomainlist.com/hostslist/hosts.txt",
]
# Enable host blocking.
# This setting supports URL patterns.
# Type: Bool
c.content.host_blocking.enabled = True

# Default monospace fonts. Whenever "monospace" is used in a font setting, it’s replaced with the fonts listed here.
c.fonts.monospace = '"Iosevka","xos4 Terminus", "Terminus", "Monospace", "DejaVu Sans Mono", "Monaco", "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", "Courier", "Liberation Mono", "monospace", "Fixed", "Consolas", "Terminal"'

# Font used for prompts.
# Type: Font
c.fonts.prompts = "10pt monospace"

# Rounding radius (in pixels) for the edges of prompts.
# Type: int
c.prompt.radius = 0

# Custom headers for qutebrowser HTTP requests.
# This setting supports URL patterns.
# Type: Dict
c.content.headers.custom = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "DNT": "1",
}

#
# Keybinding
#
config.bind("gh", "home", "normal")
config.bind("<Ctrl-Shift-J>", "tab-move +", "normal")
config.bind("<Ctrl-Shift-K>", "tab-move -", "normal")
