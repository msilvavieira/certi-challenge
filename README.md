# Integer to Portuguese converter

## How to run it

1. First off, set up and activate a Python virtual environment, or at least
install the requirements:

``` bash
pip install -r requirements.txt
```

2. Run the server like this:
``` bash
python server.py
```

**By defaul the server listens to port 3000.** To make it listen to
a different port (say, 8888), pass it on to the --port argument
like this:

``` bash
python server.py --port=8888
```


3. Another easy way to run the app is by building up the Docker image,
which by itself takes care of the above steps. Suppose we're gonna call
it "tagname":

```bash
docker build [-t tagname] .
```
(do NOT forget the dot, its important!)


Done that, just run it. The following example assumes you the reader
wants to use port 3000, but it could be anything:

``` bash
docker run -p 3000:80 tagname
```



4. Optionally, there's a very special Docker image published in the
public registry set up with everything included. And I do mean EVERYTHING.
Run it like so:

``` bash
docker run -p 3000:80 85ms/int-por-extenso:challenge
```

(of course, pass any port of yout choice to the -p argument! Just remember
that the Dockerfile exposes port 80.)


## What it does

This little app was coded in a effort to enroll myself
into a software developer position at CERTI. Its purpose
is to translate an integer (in the range -99999 to 99999)
to its numeral form in portuguese, with a little twist:
there is a extra " e " connective between every thousand
to hundred places.

The integer input must be specified in the URI, as in
```
http://localhost:3000/1
```
Every valid input generates a JSON, with a single key named
"extenso" - its value is the string corresponding to the
portuguese numeral value for the integer (in portuguese, verbal
written forms of numbers are called "números por extenso").

For example, the above URI would give out
``` JSON
{ "extenso": "um" }
```


## How it works

The server is built in Tornado, and it is a very basic
implementation. The core router is based on a simple regular
expression form:

``` regexp
r"/[-]?(\d)+"
```

which matches any Unicode decimal digit preceded or not by
the minus sign in the URI. The MainHandler class get() method
filters out any integer outside the specified range, giving
those a status 404 response. 


Now, about the "int_to_numeral" algorithm... it must be seen
to be believed! Get to the code! :)



## What about the tests?

Just Pytest the deuce out of them!

``` python
pytest test_int_to_numeral.py
```
