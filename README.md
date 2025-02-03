# Audio files converter
Script to convert audio files using ffmpeg. Tested with Windows 10 with flac to mp3 conversion.

Can be called with arguments:
| Position | Suggested type | Description |
| --- | --- | --- |
| 1 | String | Path to folder with audio files
| 2 | String | Path to output folder
| 3 | String | Target (output) bitrate

:exclamation: Variables set in the script have priority over script arguments

Script return codes:
| Code | Description |
| --- | --- |
| 0 | Successful execution
| 1 | Specified target folder parg does bor exist
| 2 | String specifying target folder path not rpvided
| 3 | Specified output folder path does not exist
| 4 | String specifying output folder path not provided
| 5 | Specified output folder path does not exist
| 6 | Incorrect bitrate specified
| 7 | Incorrect string specifying bitrate
| 8 | Incorrect bitrate value
| 9 | ffmpeg binary file not found
| 10 | Could not get target file list
