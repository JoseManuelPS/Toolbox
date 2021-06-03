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



## templates - v1.1

Base templates for creating scripts on Python and Shell.


