import webbrowser;

url = 'https://www.youtube.com/watch?v=Lzqlp1iOBMQ';
path = r'C:\Program Files\Google\Chrome\chrome.exe';

webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(path));
webbrowser.get("chrome").open_new_tab(url);