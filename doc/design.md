# Design

## Media files

CoderDojo mobile uses media files a lot. Project tutorials, images, etc are all media files. Remember, media files must be served, in production, directly by the web server

Media files are uploaded by the user (example: tutorials), they are then unzipped and single files are saved to the db.

They are also saved to the `DEFAULT_FILE_STORAGE` 

## Event management

The toolkit can display a list of registered events, ordered by date. Clicking on an event leads to a web page showing the participant lists, for each participant the toolkit shows whether it has checked-in or not. The toolkit allows selecting a participant in the list and toggling the checked-in property. It also allows to check-in by participant or ticket id.

## Learning Material Rating 

Participants can rate learning material. Since Ninjas are not authenticated, they are identified by their ip address / day of participation. This allows the toolkit to distinguish between a new rating and a rating editing. Rating consists in a rate (1-5 stars), an optional comment, and the name of the rating author. 
The average rating is shown besides the learning material in the list of learning materials. The average rating, the single ratings and comments are shown in the detailed view of the learning material