# Design

## Media files

CoderDojo mobile uses media files a lot. Project tutorials, images, etc are all media files. Remember, media files must be served, in production, directly by the web server

Media files are uploaded by the user (example: tutorials), they are then unzipped and single files are saved to the db.

They are also saved to the `DEFAULT_FILE_STORAGE` 

## Event management

The toolkit can display a list of registered events, ordered by date. Clicking on an event leads to a web page showing the participant lists, for each participant the toolkit shows whether it has checked-in or not. The toolkit allows selecting a participant in the list and toggling the checked-in property. It also allows to check-in by participant or ticket id.

