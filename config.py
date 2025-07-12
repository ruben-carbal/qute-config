import rosepine

rosepine.setup(c, 'rose-pine', True)

c.url.start_pages = ["https://www.google.com/"]

# c.colors.statusbar.normal.bg = "#00000000"
# c.colors.statusbar.command.bg = "#00000000"
# c.colors.tabs.even.bg = "#00000000"
# c.colors.tabs.odd.bg = "#00000000"
# c.colors.tabs.bar.bg = "#00000000"

c.tabs.title.format = "{audio}{current_title}"
c.fonts.web.size.default = 20
config.set('fonts.web.family.serif', 'Cascadia Code')

c.url.searchengines = {
    'DEFAULT': 'https://www.duckduckgo.com/?q={}',
    '!aw': 'https://wiki.archlinux.org/?search={}',
    '!yt': 'https://www.youtube.com/results?search_query={}',
}

c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

config.load_autoconfig()
c.auto_save.session = True

# dark mode
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'never'

c.content.blocking.enabled = True

