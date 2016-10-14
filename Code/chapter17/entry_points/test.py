from pkg_resources import load_entry_point
entry_point = load_entry_point('SimpleSite', 'paste.app_install', 'main')

print entry_point
