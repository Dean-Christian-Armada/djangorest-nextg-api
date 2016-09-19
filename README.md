# Technology stack #

### Language: Python 2.7 ###

### Database: Postgres ###

Currently runs on an RDS instance

### Major Libraries: Django 1.10, Django REST Framework ###

### Continuous Integration: Bitbucket Pipelines ###

Currently supports running unit tests and flake8 checking for Pep 8.

TODO: add jmeter tests

TODO: add code coverage

### Authentication ###

Possible options:

-   Oauth2
-   jwt

### Push notifications ###

Text goes here

### Asynchonous jobs ###

Text goes here

### Caching: ###

Do we want a standalone server?

Pros:
-   If we horizontally scale application servers then we will want a standalone redis server to easily invalidate the cache

Possibile Options:

-   Redis
    -   Pros:
        -   Development Team has most experience with this
            Persistence to disk, by default [Source](http://stackoverflow.com/questions/10558465/memcached-vs-redis)
    -   CONS:
        -   Limited to one core as it is based on an event loop [Source](http://stackoverflow.com/questions/10558465/memcached-vs-redis)
-   Memcache
    -   Pros:
        -   Multithreaded and fast [Source](<http://stackoverflow.com/questions/10558465/memcached-vs-redis>)
-   Vagrant



### Load Balancer: ###

Possible Options:

-   AWS
-   nginx


### Real Time ###

Possible Options: 

-   Django-channels
-   Socket.io

### Web Accelerator: ###

Possible Options:

-   Apache
-   Nginx

### WSGI Interface: ###

Possible options:

-   uWSGI
-   gunicorn

### Searching ###

Possible Options:

-   Elastic Search
-   Cloud Search
-   Django ORM

### DNS ###

AWS

TODO: Add DNS details

### SSL Implementation ###

ACM (Amazon Certificate Manager)

### Monitoring ###

Text goes here

##### Logging #####

Text goes here

##### Alerts #####

Text goes here

### Email ###

Text goes here


# Backups #

Text goes here

# Coding Standards #

### Python ###

[PEP 8](https://www.python.org/dev/peps/pep-0008/)

[Django 1.10 Coding Style](https://docs.djangoproject.com/el/1.10/internals/contributing/writing-code/coding-style/)

[PEP 20](https://www.python.org/dev/peps/pep-0020/)

What max line length do we want to use? I think 79 is too small. How about we relax the hard limit to 99 characters and keep comments and docstrings to 72? (recommended by PEP 8)

avoid wildcard importsto avoid import conflicts and improve code introspection tools functionality

use explicity relative imports instead of absolute imports to keep apps easily movable

    

### Patterns ###

Test Driven Development

TODO: add more detail about how strict TDD

Fat models [source](http://django-best-practices.readthedocs.io/en/latest/applications.html)

A common pattern in MVC-style programming is to build thick/fat models and thin controllers. For Django this translates to building models with lots of small methods attached to them and views which use those methods to keep their logic as minimal as possible. There are lots of benefits to this approach.

Reasons:

-   DRY: Rather than repeating the same logic in multiple views, it is defined once on the model.
-   Testable: Breaking up logic into small methods on the model makes your code easier to unit test.
-   Readable: By giving your methods friendly names, you can abstract ugly logic into something that is easily readable and understandable.

[Example](https://github.com/django/django/blob/ff6ee5f06c2850f098863d4a747069e10727293e/django/contrib/auth/models.py#L225-404)

### Directory Structure ###

Each app should be named the same as it is in the url e.g. an app called users maps to http://nextg.com.au/users

### URL conventions ###

Router from Django Rest Framework [source](http://www.django-rest-framework.org/api-guide/routers/)

### Admin Frontend ###

Do we want JS / CS / HTML style guide?


### To Keep In Mind ###

-   ALWAYS be concern of scalability, performance, availability, and security of the application

-   COMPLICATED or UNFAMILIAR codes must be commented

-   PRAGMATICALLY segregate anything for easier scanning of codes and don't over segregate

### Database ###

How do we want to handle transactions? Do we want to user ATOMIC_REQUESTS so database tranactions contain the entire HTTP request?

-   PROS:
    -   safer and easier to develop
-   CONS:
    -   slower performance

### Database Migrations ###

Always manually review migrations and test rollback functionality 

Always backup the database before applying a migration

Once project is deployed, test migration time on similar dataset with similar size to live database


### Git Commit Message Standards / Git Workflow ###

##### Branches #####

master (production):
kept production ready

develop (staging):
almost all commits should branch from here


Each issue / feature / bug fix should be in its own topic branch.

Almost all changes should be branched from develop. If it is instead a hotfix, the branch should be named "hotfix-*"

To avoid integration problems, all topic branches should be short lived. If not possible, parent branch should be merged back into the topic branch frequently.

###### Before merging into develop: ######

1) All Continuous Integration tests should pass

2) Commits messages should only be about one thing and all changes should be related to the commit message. If they aren't, break them into a separate commit for each type of change, or possibly split into two branches if the changes aren't related at all.

3) All code should conform to the coding standards set.

4) Changes must be manually tested locally while with all commits from develop

###### How to Merge into develop: #####


Do we want to use merges with accurate history or rebase to keep a neat linear history? my (Ben's) proposal:

Rebase should be used to keep the history clean. 

All commits being pulled should be squashed into one commit to remove noise from the git log but kept unsquashed in the topic branch to preserve development history. The squashed commit should have all the other commit messages in the commit description, it should also reference the ticket number used by our project management software.

##### Merging to master: ######

Due to CI and large test coverage, develop should be kept to an almost production ready state in terms of stability. 

Should be tagged with a version number.

Ensure everything is documented, and has all the functionality required for a release.


# Coding Reviews #

possibile options:
-   Bitbucket pull requests
-   Gerrit
-   Phabricator

Make sure code is easy to read, meets business requirements, follows coding standards

Do we want to divide who is primarily responsible for the code reviews by tools?
e.g. developer X ensure caching works, developer Y ensures 

# Deployment #

Text goes here

### Configuration management ###

Possible Options:

-   Chef
-   Puppet
-   Ansible
-   SaltStack
-   Docker

### Scaling Plan ###

Text goes here

# Settings #

Possibly:
    Turn off features with flags e.g. python manage.py runserver --no-cache

### Application Settings ###

local development settings => settings.local

continuous integration settings => settings.test

production server settings => settings.production

All these will extend settings.base

### Dependencies ###

-   requirements/
    -   base.txt
    -   local.txt
    -   test.txt
    -   production.txt
    
### Secret Keys ###

Text goes here
