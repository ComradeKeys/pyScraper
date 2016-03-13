###pyScraper

This application runs python 3 and the scripts are intended to run on Fedora 23. On your system you should have an instance of MongoDB running on the local host. You can run

To start the daemon that pulls the posts invoke:
```{r, engine='bash', count_lines}
AutoPyReddit.py
```
It will run as a daemon automatically. However, if you want a little more control over when the application starts and stops you can invoke:
```{r, engine='bash', count_lines}
python3 PyReddit.py start/stop/restart
```
Stopping the daemon will be a bit easier this way.

Then to view the posts in your web browser invoke:
```{r, engine='bash', count_lines}
FrontEnd.py
```

Using a command line parameter would probably be a better way of going about this; but this is only for proof of concept.

If all goes well your shell should report
```{r, engine='bash', count_lines}
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```

Just paste http://127.0.0.1:5000/ into your web browser to view the posts