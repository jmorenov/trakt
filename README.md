# Trakt.tv tools

- [Trakt.tv tools](#trakttv-tools)
  * [Purpose](#purpose)
  * [Usage](#usage)
  * [Configuration](#configuration)
    + [Configuration sample](#configuration-sample)
    + [Configuration details](#configuration-details)
  * [Developer documentation](#developer-documentation)
  * [Howto](#howto)
    + [Import](#import)
  * [Support](#support)
  * [Contribution](#contribution)
  * [Licence](#licence)

## Purpose

 * Import Movies or TVShows IDs from CSV file format into Trakt.tv.
 * Import Ratings of Movies or TVShows IDs from CSV file format into Trakt.tv.

## Requirements

You must use Python 3.x.

## Usage

* Create an [Trakt.tv application](https://trakt.tv/oauth/applications) to have your own ``client_id`` and ``client_secret``, https://trakt.tv/oauth/applications.
You only need to fill up the ``Name`` with a ``Description`` and ``Redirect uri`` to `urn:ietf:wg:oauth:2.0:oob`, leave the rest empty and click on ``SAVE APP``.

* Run the script to create a default config file ``config.ini``

* Edit the config file ``config.ini`` and specify the ``client_id`` and ``client_secret`` as well as any other settings appropriate to your enviromenent, eg: URL, proxy, etc...
Refer to [Configuration details](#configuration) section for more information.

```
$ vim config.ini
```

## Configuration

### Configuration sample

```text
[TRAKT]
client_id = xxxxxxxxxxxxxxxxxxxxxxxxx
client_secret = xxxxxxxxxxxxxxxxxxxxxx
access_token =
refresh_token =
baseurl = https://api-v2launch.trakt.tv
[SETTINGS]
proxy = False
proxy_host = https://127.0.0.1
proxy_port = 3128
```

### Configuration details

 * ``client_id``: Uniq ID to identify your application, https://trakt.tv/oauth/applications
 * ``client_secret``: Uniq ID to identify your application, https://trakt.tv/oauth/applications
 * ``access_token``: Uniq ID to identify yourself against your application, manage by the script
 * ``refresh_token``: Uniq ID to identify yourself against your application, manage by the script
 * ``baseurl``: API base URL, depends on the platfrom, eg: Production (https://api-v2launch.trakt.tv) or Staging (https://api-staging.trakt.tv)
 * ``proxy``: True/False setting to enable proxy support
 * ``proxy_host``: Full URI of the proxy
 * ``proxy_port``: Port of the proxy to connect to

## Developer documentation

```bash
$ pydoc `pwd`/import_trakt.py
$ pydoc `pwd`/export_trakt.py
$ pydoc `pwd`/sync_tmdb_trakt.py
```

## Howto

### Import 

[Import CSV into trakt.tv](import.md)

## Support

To get support, please create new [issue](https://github.com/xbgmsharp/trakt/issues)

## Contribution
I'm happy to accept Pull Requests! 

## License

This script is free software:  you can redistribute it and/or  modify  it under  the  terms  of the  GNU  General  Public License  as published by the Free Software Foundation.

This program is distributed in the hope  that it will be  useful, but WITHOUT ANY WARRANTY; without even the  implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

See <http://www.gnu.org/licenses/gpl.html>.
