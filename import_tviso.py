from import_trakt import _trakt, api_auth, read_config, _headers, api_add_to_list, cleanup_list
import datetime
import os
import sys
import json

def auth(options, config):
    ## Trakt auth
    if not _trakt['access_token'] and not _trakt['refresh_token'] and \
            _trakt['client_id'] and _trakt['client_secret']:
        print("Trakt, no token found in config file, requesting authorization_code")
        api_auth(options, config, False)
    elif _trakt['access_token'] and _trakt['refresh_token'] and \
            _trakt['client_id'] and _trakt['client_secret']:
        ## Check token validity
        ## Trakt access_token is valid for 3 months before it needs to be refreshed again.
        today = datetime.datetime.today()
        modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(options.config))
        duration = today - modified_date
        if duration and duration.seconds < 2592000:
            # 30*24*60*60 = 2592000
            print("Trakt, skipped access token refresh, token is less than 30 days, only %s" % duration)
            _headers['Authorization'] = 'Bearer ' + _trakt["access_token"]
            _headers['trakt-api-key'] = _trakt['client_id']
        else:
            ## Exchange refresh_token for access_token
            print("Trakt, access token refresh, token is more than 30 days, token is %s old" % duration)
            api_auth(options, config, True)
    else:
        print("No valid authentication parameters found in config file")
        sys.exit(1)

    if not _headers['Authorization'] and not _headers['trakt-api-key']:
        print("No valid Authorization header")
        sys.exit(1)

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

def main():
    options = {
        'config': 'config.ini'
    }

    options = dotdict(options)

    config = read_config(options)

    auth(options, config)

    with open('tviso-collection.json') as f:
        collection = json.load(f)

    # Type pending or following: tviso_${movie/show}_watchlist.csv
    # Type watched: tviso_${movie/show}_watched.csv
    movies = [x for x in collection if x['type'] == 2]

    movies_watched = [{ 'ids': { 'imdb': x['imdb'] }, 'watched_at': x['checkedDate'] } for x in movies if x['status'] == 'watched']
    movies_watchlist = [{ 'ids': { 'imdb': x['imdb'] }} for x in movies if x['status'] == 'pending']

    shows = [x for x in collection if x['type'] == 1]
    shows_watched = [{ 'ids': { 'imdb': x['imdb'] }, 'watched_at': x['checkedDate'] } for x in shows if x['status'] == 'watched']
    shows_watchlist = [{ 'ids': { 'imdb': x['imdb'] }} for x in shows if x['status'] == 'pending' or x['status'] == 'following']

    movies_watched_options = dotdict({
        'type': 'movies',
        'list': 'history'
    })
    movies_watchlist_options = dotdict({
        'type': 'movies',
        'list': 'watchlist'
    })
    shows_watchlist_options = dotdict({
        'type': 'shows',
        'list': 'watchlist'
    })
    shows_watched_options = dotdict({
        'type': 'shows',
        'list': 'history'
    })

    cleanup_list(movies_watched_options)
    cleanup_list(shows_watched_options)

    print(api_add_to_list(shows_watchlist_options, shows_watchlist))
    print(api_add_to_list(shows_watched_options, shows_watched))
    print(api_add_to_list(movies_watchlist_options, movies_watchlist))
    print(api_add_to_list(movies_watched_options, movies_watched))

if __name__ == '__main__':
        main()