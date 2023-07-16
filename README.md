# VMNF, Var-MagNiFier
No auto variable watcher in debugging when composing Python? Try this library to show them into the console!

## How to use it
1. Download it [here](https://github.com/KobeArthurScofield/var-magnifier-py/releases/latest).
1. Put the ```vmnf``` folder into the ```lib``` folder or beside your project file.
1. Import it.
   ``` python
   import vmnf
   ```
1. Use the functions inside the package, such as ```ConLogVar()```, ```ConLogMsg()```, ```FilLogVar()``` and ```FilLogMsg()```.

## Functions

### ```ConLogVar()```
``` python
ConLogVar(*variables)
```
Put any variables as the function's paramaters, and it will print the types and values of variables in the ```stdout```.

### ```ConLogMsg()```
``` python
ConLogMsg(*messages)
```
Put any elements as the function's paramaters, and it will compose them as a message and print message texts in the ```stdout```.

### ```FilLogVar()```
``` python
FilLogVar(path, *variables)
```
Put any variables as the function's paramaters, and it will put the types and values of variables in the file that written in ```path```.

```path``` could be a string or a string tuple. When it is a string tuple, it will write them to several files that given in the tuple.

### ```FilLogMsg()```
``` python
FilLogMsg(path, *messages)
```
Put any elements as the function's paramaters, and it will compose them as a message and put the message text in the file that written in ```path```.

```path``` could be a string or a string tuple. When it is a string tuple, it will write them to several files that given in the tuple.
