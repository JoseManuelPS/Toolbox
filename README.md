# Toolbox

Multiple scripts for all kinds of problems.



## 3n1gm4 - v1.1

Create a secret box to store a key. 

Usage:
```
3n1gm4.py [-h] ROWS COLUMNS
```

- **ROWS**: Type number of rows.
- **COLUMNS**: Type number of columns.
- **-h**: Show information about help.

Example of use:
```
3n1gm4.py 100 100
```

---

_Last test info:_

- _Date: 30/05/2021_
- _Python versión: alpine:3.8.5_

---



## custom_youtube-dl - v1.1

Assistant to use the youtube-dl tool.

Usage:
```
custom_youtube-dl.py [-h] [--name NAME] PATH
```

- **PATH**: Set the path to the directory where the download is saved.
- **-h**: Show information about help.
- **--name NAME**: Set the name under which the download is saved.

Example of use - 1:
```
custom_youtube.py ~/Downloads/
```

Example of use - 2:
```
custom_youtube.py --name List ~/Downloads/
```

---

_Last test info:_

- _Date: 02/06/2021_
- _Python versión: alpine:3.8.5_

---



## oh-my-cfg/zsh - v1.1

Script to install a custom zsh shell.

Usage:
```
oh-my-custom-zsh.sh
```

---

_Last test info:_

- _Date: 07/05/2022_
- _ZSH: zsh:5.8_
- _p10k: v1.16.1_

---



## random_wallpaper - v1.0

Sets a wallpaper randomly, choosing from all the existing images in a directory and its subdirectories.

Usage:
```
random_wallpaper.py [-h] [--time TIME] [--verbose] PATH
```

- **PATH**: Path to the images directory.
- **-h**: Show information about help.
- **--time TIME**: Set the time (in seconds) of each screen background. Default 60s.
- **--verbose**: Show more information during execution.

Example of use - 1:
```
random_wallpaper.py ~/Pictures/wallpapers/
```

Example of use - 2:
```
random_wallpaper.py --time 60 --verbose ~/Pictures/wallpapers/
```

---

_Last test info:_

- _Date: 30/05/2021_
- _Python versión: alpine:3.8.5_

---



## templates - v1.3

Base templates for creating scripts for Python, Shell and Linux Services.



## text_utils/rebuild_line - v1.0

The program reads one by one each of the lines of a file, if in any line it finds a match with the text entered as **old**, it replaces it with the text entered as **new**.

Usage:
```
rebuild_line.py [-h] [--new NEW] [--old OLD] [--replace] [--verbose] PATH
```

- **PATH**: Path to the folder or the file to process.
- **-h**: Show information about help.
- **--new**: The NEW text that you want to replace.
- **--old**: The OLD text that you want to replace.
- **--replace**: Replace the original file with the new content.
- **--verbose**: Show more information during execution.      

Example of use - 1:
```
rebuild_line.py ~/tmp/file.sh
```

Example of use - 2:
```
rebuild_line.py --verbose --replace --new something_new --old something_old ~/tmp/app
```

---

_Last test info:_

- _Date: 05/06/2021_
- _Python versión: alpine:3.8.5_

---


## text_utils/scripts_processor - v1.0

Simple application for code processing in shell scripts.

Usage:
```
scripts_processor.py [-h] [--advanced_on] [--advanced_off] [--verbose_on] [--verbose_off] [--verbose] PATH
```

- **PATH**: Path to shell script.
- **-h**: Show information about help.
- **--advanced_on**: Turn on advanced mode.
- **--advanced_off**: Turn off advanced mode.
- **--verbose_on**: Turn on verbose mode.
- **--verbose_off**: Turn off verbose mode.
- **--verbose**: Show more information during execution.      

Example of use - 1:
```
scripts_processor.py --verbose_on ~/tmp/file.sh
```

Example of use - 2:
```
scripts_processor.py --verbose_on --advanced_off ~/tmp/file.sh
```

---

_Last test info:_

- _Date: 03/06/2021_
- _Python versión: alpine:3.8.5_

---


