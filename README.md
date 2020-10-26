# crew_assignments
crew_assignments is an app that is part of the MagisAir project.

The app is contained in the "crew_assignments" folder.

The MagisAir project files here are outdated. It may be better to install the app to a newer version of the MagisAir project.

In order to install this app to another project,
1. In the "src" folder, copy and paste the folder "crew_assignments" into the project directory.
2. In "settings.py" (project settings) -> INSTALLED_APPS, add the string `'crew_assignments'`.
3. In "urls.py" (project URLs), add the line `path('crew_assignments/', include('crew_assignments.urls')),`.

The URL for the app's main page is http://localhost:8000/crew_assignments/.
