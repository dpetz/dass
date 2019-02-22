# DASS as a Service

Implement [DASS] Digital Advertising System Simulation as a RESTful Python microservice.

## Project Log


### Feb 22:
- Do to  limited app scope and simplicity prefer [Flask over Django](https://www.codementor.io/garethdwyer/flask-vs-django-why-flask-might-be-better-4xs7mdf8v)
- Create [PyCharm] [Flask] project
  - As template language choose [Ninja2 over Mako](https://www.quora.com/Python-Web-Frameworks-What-are-the-advantages-and-disadvantages-of-using-Mako-vs-Jinja2) as it's the one mentioned all over the [flask docs]
  - Download Python 3.7 to [base a virtualenv](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) on it
- Create https://github.com/dpetz/dass
  - from PyCharm via ``Personal access tokens`` of sufficient rights
- Add [this](https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore) ``.gitignore``. Add ``.idea`` to it.
- Refresh [python decorators](https://realpython.com/primer-on-python-decorators/) which Flask uses to bind functions to URLs.
-  ["Flask Web Development"](https://learning.oreilly.com/library/view/flask-web-development/9781491991725/) is the best reated book
- Start implementing activity stream model.
- Add ``numpy`` package to [PyCharm project interpreter](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)
- [attr] supports [class immutability](https://opensource.com/article/18/10/functional-programming-python-immutable-data-structures) and [much more](https://glyph.twistedmatrix.com/2016/08/attrs.html).


[DASS]: https://ai.google/research/pubs/pub45331
[PyCharm]: https://www.jetbrains.com/pycharm/
[Flask]: http://flask.pocoo.org/
[flask docs]: http://flask.pocoo.org/docs/1.0/
[flask-restful]: https://flask-restful.readthedocs.io/en/latest/
[attr]: https://www.attrs.org/en/stable/