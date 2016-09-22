# fixture used in core/tests.py
python manage.py dumpdata core.FeatureToggle --indent=4 > core/fixtures/feature_toggle.json
# fixture used in core/tests.py
python manage.py dumpdata oauth2_provider.application --indent=4 > core/fixtures/applications.json
# fixture used in core/tests.py
python manage.py dumpdata auth.User --indent=4 > core/fixtures/users.json