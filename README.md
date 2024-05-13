# CITS3403 Project: PetroPulse

## Overview and Design

This project PetroPulse is inspired by the application FuelWatch on the idea that users are able to search for the fuel stations with the prices and other information displayed. PetroPulse allows users to both search and upload information on different fuel stations making it a potentially powerful de-centralised design and can be scale up easily.

## Contributors

|UWA ID | Name | Github user name |
|----------|----------|----------|
| 23478401| Lingwan Peng | lingwan-peng |
| 23620426 | Leon Thomas | ElTee2k4 |
| 23976415 | Daniyal Qureshi | daniyalq114 |
| 23380159 | Amir Husain | husaia123 |

## Architecture

PetroPulse contains five main front end pages:

- __Map and stations (home page):__ This is where the information of stations uploaded by users is displayed as a list.
- __Station info collection:__ Users can upload details of a fuel station on this page by filling out related information or clicking a button to choose between different categories.
- __Leaderboard:__ Ranks users based on the number of posts they have contributed.
- __Login page:__ Users are required to login with their stored credentials to access their profile page.
- __User profile:__ Displays all the information relevant to an authenticated user such as their username, biography and recent posts. Users are free to edit their profile as they like.

Users have read previledge of the information presented by the website as well as write privelidge to update fuel station details, but they are requied to log in to have their own user profile page or to entre the leaderboard.

As the input from users are submitted, it will be sent to the back end server to either create, read, update or delete the corresponding fields in the database.

## How to launch application

To launch this application, make sure you have the following conditions satisfied:

- A reliable internet connection.
- ...

If on a computer, use the command line `flask run` and follow the link provided in the flask description such as `http://127.0.0.1:5000`.

If on a mobile device: to be implemented.

## How to run application

Unit tests to be implemented.

## Refrences

Bootstrap: <https://getbootstrap.com/docs/5.0/components/dropdowns/>

General style inspiration: <https://themewagon.com/themes/free-bootstrap-5-admin-dashboard-template-darkpan/>

General set up of server and architecture: <https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world>

Helpful documentation and tutorial: <https://www.w3schools.com>
