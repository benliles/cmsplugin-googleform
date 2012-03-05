README.txt
Texas A&M University - College of Architecture
Information Technology Services
Created By: Corbin Fanning
Created: 3/5/2012
Last Updated: 3/5/2012
================================================================================
List of apps dumped to googleform.json

================================================================================

googleform.json v.1.0

Apps
---------------
googleform

Commands Used
----------------
-To dump data from database to the googleform.json file:

bin/django dumpdata cms cmsplugin_googleform --format=json --indent=4 > src/app.googleform/cmsplugin_googleform/fixtures/googleform.json

-To reset an applications data (delete all content in the table's attribute):

bin/django reset [app name]
bin/django reset cms cmsplugin_googleform

-To load the data from googleform.json (this overwrites that exists in ALL
 applications for the data that is in googleform.json):

bin/django loaddata cmsplugin_googleform
