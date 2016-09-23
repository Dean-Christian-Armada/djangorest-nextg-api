#!/bin/bash

# fixture used in core/tests.py
python manage.py dumpdata core.FeatureToggle --indent=4 > core/fixtures/feature_toggle.json
# fixture used in core/tests.py
python manage.py dumpdata oauth2_provider.application --indent=4 > core/fixtures/applications.json
# fixture used in core/tests.py
python manage.py dumpdata auth.User --indent=4 > core/fixtures/users.json
# fixture used in core/tests.py
python manage.py dumpdata accounts.UserType --indent=4 > core/accounts/fixtures/user_types.json
# fixture used in core/tests.py
python manage.py dumpdata accounts.UserAccount --indent=4 > core/accounts/fixtures/user_accounts.json
# fixture used in core/tests.py
python manage.py dumpdata core.School --indent=4 > core/fixtures/schools.json
# fixture used in core/tests.py
python manage.py dumpdata core.AUState --indent=4 > core/fixtures/au_states.json
# fixture used in core/tests.py
python manage.py dumpdata core.Course --indent=4 > core/fixtures/courses.json
# fixture used in core/tests.py
python manage.py dumpdata core.SchoolsAndCourses --indent=4 > core/fixtures/schools_and_courses.json
# fixture used in core/tests.py
python manage.py dumpdata accounts.UsersAndCourses --indent=4 > core/accounts/fixtures/users_and_courses.json
# fixture used in students/tests.py
python manage.py dumpdata core.Unit --indent=4 > core/fixtures/units.json
# fixture used in students/tests.py
python manage.py dumpdata accounts.UsersAndUnits --indent=4 > core/accounts/fixtures/users_and_units.json
# fixture used in students/tests.py
python manage.py dumpdata core.CoursesAndUnits --indent=4 > core/fixtures/courses_and_units.json
# fixture used in core/accounts/tests.py
python manage.py dumpdata oauth2_provider.AccessToken --indent=4 > core/fixtures/access_tokens.json