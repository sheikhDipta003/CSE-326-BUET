# CSE-326-BUET
Information System Design Sessional codes.

*Harpy* is a blog-post web app built with django. After registering, users can create new post,delete any post,change their credentials or view others posts. The admin(s) can add new user and delete any existing user. The 'blog' app is used as the homepage.

This project has the following apps [In django, an app is an independent module]:

**Harpy** *a folder with the same name as our project*
|  File Name  |                                             Description                                             | Needs to be manually modified / not |
|:-----------:|:---------------------------------------------------------------------------------------------------:|-------------------------------------|
| settings.py |                      Contains a list of all the installed apps for the project                      | yes                                 |
|   urls.py   | URL configuration for Harpy project. The 'urlpatterns' list routes a url to its appropriate 'view'. | yes                                 |

**blog** *an app/module in our project that handles the homepage/blogpage*
|     Subfolder/File Name    |                                                                          Description                                                                          | Needs to be manually modified / not |
|:--------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------:|-------------------------------------|
| migrations/0001_initial.py | Contains the backend database codes, for creating 'Post' table, that get executed when we run 'python manage.py migrate'.                                     | no                                  |
| static/blog                | All 'static', that is, css/js files needed for blog page.                                                                                                     | yes                                 |
| templates/blog             | All html files for blog-page. All of them extend 'base.html'.                                                                                                 | yes                                 |
| admin.py                   | Used for registering all relevant ORM models so that they show up in the localhost/admin page.                                                                | yes                                 |
| apps.py                    | Contains the class instance of the 'blog' app. This class-name must be included in the  INSTALLED list in settings.py.                                        | no                                  |
| models.py                  | Create all necessary Object Relational Models, that is, 'tables' with proper field names and types.                                                           | yes                                 |
| urls.py                    | Contains 'urlpatterns' list that routes a url to its appropriate 'view' in blog app.                                                                          | yes                                 |
| views.py                   | For each action in blog-page, that is, navigating to 'home'/'about' section, create a view that receives an HttpRequest and renders corresponding Html files. | yes                                 |

**users** *an app/module in our project that handles the users page for register,login,logout etc*
|     Subfolder/File Name    |                                                                      Description                                                                     | Needs to be manually modified / not |
|:--------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------:|
|        static/users        | All 'static', that is, css/js files needed for users page.                                              												|                 yes                 |
|       templates/users      | All html files for users-page. All of them extend 'base.html' from 'blog' app.                                    									|                 yes                 |
|          admin.py          | Used for registering all relevant ORM models so that they show up in the localhost/users/admin page.                         						|                 yes                 |
|           apps.py          | Contains the class instance of the 'users' app. This class-name must be included in the  INSTALLED list in settings.py.               				|                  no                 |
|          forms.py          | This class serves to create our customized form by overriding the 'UserCreationForm' class that  django provides us with.              				|                 yes                 |
|          models.py         | Create all necessary Object Relational Models, that is, 'tables' with proper field names and types.                         							|                 yes                 |
|          views.py          | Each time a new user registers, collect all the data from the form and save the user in database. After successful registration, return to homepage. |                 yes                 |

