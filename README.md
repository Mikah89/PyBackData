PyBackData
==========

PyBackData is a python util tool that allows users to backup their data on Dropbox. Soon some more services will
be added to this tool (waiting on your contribution!!).

**Why?**

Simply put, in my case I needed something that simply pushed the files I wanted to dropbox but not the way back.
Well for that we have the dropbox client. This tool is supposed to mimic a "copy/paste" of the file with no sync back.

**What you need to do?**

Check out the repo and simply run pybackdata.py with the specific service. Do not forget to install the needed dependencies to run each
service. These instructions should be added on each service subsection. Also if a configuration file exists each necessary 
key should be explained.

**Contributions**

More online services or improvements to the existing ones are always welcome! "Backup" should always be the public API
of any eventual new service.

**Usage**
```
./pybackdata.py <service> # where <service> is the supported online service of your choosing.
```

Dropbox
==========
**Configuration File**

The configuration file follows an [INI](https://docs.python.org/3.4/library/configparser.html?highlight=configparser#supported-ini-file-structure) like file structure. For now it supports the following keys:

```INI
[dropbox]
appkey = #use your own
appsecret = #use your own
token = #access_token to service
data = #list of local files to be backed up separated by ';'
backupfolder = #location where it will be saved in the online service (e.g. '/' is the first level of files on db)
```

To obtain an app key and app secret, you just have to create an app ou your dropbox developer console. For the time
being I'm not providing my own keys.

After that just run pybackdata (dropbox service) and it should request both app key and secret on the console. After this step the app key, app secret and token keys should have values assigned.

What's left for you to configure is the *data* and *backupfolder* keys. And that is it!

**SDK Client**

For this version  you have to install the Dropbox SDK on your machine so python can find it. Find the
package [here!](https://www.dropbox.com/developers/core/sdks/python)

**REST Client**

N/A
