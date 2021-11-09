Please make notes here to clarify any decisions taken that you wish to communicate, and capture any URLs you used in solving the problems at hand.

I split the core of the project into 3 modules:
* Seen_Strings.py - the data class. Just a dict that contains strings and counts, and implements the 'add' and 'stats' methods.
* app.py - a web application that allows use of a Seen_Strings object through the /add and /stats endpoints.
* cli.py - runs the application via the command line.

Decisions
* I expanded the original seen_strings dict and stringinate methods into the Seen_Strings class. This makes the functionality of the class much easier to understand than looking at it via the [command line loop](https://github.com/ryanhassing/comcast-coding-exercise-11-8/commit/0d2d0bc0c8ceaffbedbe7a24172381bf221b558d#diff-568470d013cd12e4f388206520da39ab9a4e4c3c6b95846cbc281abc1ba3c959R4-R19). It also makes it much easier to add/modify functionality to the data object when in a separate class.
* I separated the web application from the CLI runner. That way, the web application could potentially serve different clients. A separate web application module also makes it easier to look at and understand the endpoints, and add/modify endpoints if necessary.
* I added options to load a Seen_Strings object to/from a csv file. This allows data to be stored after the application stops running.

Sources consulted - I really just consulted library documentation
* https://docs.python.org/3/library/csv.html
* https://docs.python-requests.org/en/latest/
* https://flask.palletsprojects.com/en/2.0.x/quickstart/