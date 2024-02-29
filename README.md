# Timezone clock Vue component and Flask server


## Flask server setup and launch
After downloading this repo, navigate to `/server` directory to install python dependencies. Run the following commands
to create a virtual env (assuming you have `virtualenv` and `pip` installed on your system):
```console
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

To run the dev server, launch Flask as such:
```console
FLASK_APP=server.py FLASK_DEBUG=1 flask run
```

Server should now be running at `localhost:5000`. If you configure Flask to run on a different host/port, make sure to
update the client config file accordingly (see below).


## Vue client setup and launch
On a different terminal, navigate into the `/client` directory. A basic Vue project is already setup. Assuming `npm` is
installed on your system, you may run `npm install` to fetch all needed packages.

Once that's done, launch the server by running `npm run serve`. You can open the client on your browser by navigating
to `localhost:8080`.

> Note: The client will access the Flask API via the url located in `/client/config/index.js`. So make sure to update
> this file if you launch Flask on a different host/port.


## Rationale
I've included two endpoints on `server/server.py`. First one (`/zones`) serves a list of available timezones as
outputted by `pytz.common_timezones`. Second endpoint (`/time-at/<path:zone>`) expects a single parameter, which
*should* be an element of the previous list (otherwise a `404` is returned). Note I take advantage of the fact that
`common_timezones` have a path-like syntax (e.g. `America/Argentina/Buenos_Aires`) by using the `path:` prefix on the
decorator.

A basic Vue project was set up with vue-cli. The important part is the `ZonePicker` component located in
`/client/src/components/ZonePicker.vue`. After mount, the component fetches a list of timezones, and populates a
`select` element with the returned zones. After the user selects a timezone, the `Get time` button becomes enabled and
we can fetch the current time at that zone.

Form inputs are also disabled while fetching the zones list (right after mount) and while waiting for a requested time
(after clicking the button) so that only one request can be done at a time. We can uncomment the `time.sleep()`
statements on the endpoint methods to simulate slow connection speeds, making this effect more noticeable.
