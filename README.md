# crew_assignments
crew_assignments is an app that is part of the MagisAir project.
The app is contained in the "crew_assignments" folder.
In order to install this app to a project,
1. Copy and paste the folder "crew_assignments" into the project directory.
2. In "settings.py" -> INSTALLED_APPS, add the string `'crew_assignments'`.
3. In "urls.py" (project URLs), add the line `path('crew_assignments/', include('crew_assignments.urls')),`.
