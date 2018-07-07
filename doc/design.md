# Design

# Media files

CoderDojo mobile uses media files a lot. Project tutorials, images, etc are all media files. Remember, media files must be served, in production, directly by the web server

Media files are uploaded by the user (example: tutorials), they are then unzipped and single files are saved to the db.

They are also saved to the `DEFAULT_FILE_STORAGE` 
