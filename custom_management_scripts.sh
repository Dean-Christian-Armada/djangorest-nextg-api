#!/bin/bash

# To fill up the 6 AU states in the db
# core.management.commands.predefined_au_states.py
python manage.py predefined_au_states
# To fill up sample units in the db for testing
# core.management.commands.sample_units.py
python manage.py sample_units
# To fill up the 3 User Types of NextG
# core.accounts.management.commands.predefined_user_types.py
python manage.py predefined_user_types
# To fill up a sample user account in the db for testing
# core.accounts.management.commands.sample_user_accounts.py
python manage.py sample_user_accounts
# To fill up a sample user with course in the db for testing
# core.accounts.management.commands.sample_user_accounts_courses.py
python manage.py sample_user_accounts_courses
# To fill up a sample user with units in the db for testing
# core.accounts.management.commands.sample_user_accounts_units.py
python manage.py sample_user_accounts_units
# To fill up a sample groups in the db for testing
# core.accounts.management.commands.sample_groups.py
python manage.py sample_groups