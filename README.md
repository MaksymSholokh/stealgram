Stealgram — Django social network

Stealgram is a social network developed on Django with support for Google login, creating posts, likes, real-time chats via WebSocket, and saving message history in the database.

Main functionality

-  User registration and login
-  Google authorization (OAuth)
-  Profile creation and editing
-  Post creation, viewing, deleting
-  Likes to posts
-  Real-time messaging (WebSocket, Django Channels)
-  Saving message history 
-  Loading old messages 


Project structure 

stealgram/
├── chat/ # WebSocket
├── fixtures/ # fixtures in Postgres
├── media/ # User`s content
├── post/ # Module post
├── static/ # CSS / JS 
├── stealgram/ # settings
├── templates/ # HTML
├── users/ # Module user
├── manage.py
└── venv/ # virtuale environment  

Technology

Python 3.10
Django
Django Channels
Redis
WebSocket
Google OAuth (social-auth-app-django)
HTML / CSS / JavaScript
