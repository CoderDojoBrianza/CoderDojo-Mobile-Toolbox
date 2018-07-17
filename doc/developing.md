# Developing

CoderDojo mobile's development is managed via [GitHub](https://github.com/CoderDojoBrianza/CoderDojo-Mobile-Toolbox)

## Tools

Some tools you might want to use:

- Code editing (text editor): [Notepad++](https://notepad-plus-plus.org/download/v7.5.7.html)
- Viewing markdown files: [Markdown Viewer extension for Chrome](https://chrome.google.com/webstore/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk)
- Working with GitHub in Windows: [TortoiseGit](https://tortoisegit.org/)
- Working with the database: [DB Browser for sqlite](https://sqlitebrowser.org/)
- To work with translations, use [Gettex for windows](https://mlocati.github.io/articles/gettext-iconv-windows.html)

## Localization

To generate locale files, run the `django-admin makemessages` command with the desired language:

```
django-admin makemessages -l en -e py,html
django-admin makemessages -l it -e py,html
```

or, for all languages:

```
django-admin makemessages -a -e py,html
```

after providing actual translations, you have to compile message files:

```
django-admin compilemessages
```

## Documentation 

For correctly managing Markdown lists / code blocks, see [This Gist](https://gist.github.com/clintel/1155906#file-gistfile1-md)