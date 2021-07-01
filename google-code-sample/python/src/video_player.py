"""A video player class."""

from os import truncate
from .video_library import VideoLibrary
from .video_playlist import Playlist

import random

class VideoPlayer:
    """A class used to represent a Video Player."""
    playlists = []
    curr_video = ""
    paused = False

    def __init__(self):
        self._video_library = VideoLibrary()

        self.curr_video = ""
        self.paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        video_list = self._video_library.get_all_videos()
        video_list.sort(key=lambda video: video.title) #https://docs.python.org/3/howto/sorting.html
        print("Here's a list of all available videos:")
        for video in video_list:
            print(video.title + " (" + video.video_id + ") [" + ' '.join(map(str, video.tags)) + "]")

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        self.paused = False
        video = self._video_library.get_video(video_id)

        if not video:
            print("Cannot play video: Video does not exist")
        else:
            if self.curr_video:
                print("Stopping video: " + self.curr_video.title)
            self.curr_video = video
            print("Playing video: " + video.title)

    def stop_video(self):
        """Stops the current video."""
        if not self.curr_video:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: " + self.curr_video.title)
            self.curr_video = ""
            self.paused = False  

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_list = self._video_library.get_all_videos()
        rand_video = random.choice(video_list)
        video = rand_video.video_id
        self.play_video(video)

    def pause_video(self):
        """Pauses the current video."""
        if self.paused == True:
            print("Video already paused: " + self.curr_video.title)
        elif self.curr_video != "":
            print("Pausing video: " + self.curr_video.title)
            self.paused = True
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        
        if self.paused == False and not self.curr_video:
            print("Cannot continue video: No video is currently playing")
        elif self.paused == False and self.curr_video:
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video: " + self.curr_video.title)
            self.paused = False

    def show_playing(self):
        """Displays video currently playing."""
        if not self.curr_video:
            print("No video is currently playing")
        else:
            if self.paused == False:
                print("Currently playing: " + self.curr_video.title + " (" + self.curr_video.video_id + ") [" + ' '.join(map(str, self.curr_video.tags)) + "]")
            else:
                print("Currently playing: " + self.curr_video.title + " (" + self.curr_video.video_id + ") [" + ' '.join(map(str, self.curr_video.tags)) + "]" + " - PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        for x in VideoPlayer.playlists:
            if x.lower() == playlist_name.lower():
                print("Cannot create playlist: A playlist with the same name already exists")
                return
        self._video_playlist = Playlist(playlist_name)
        VideoPlayer.playlists.append(playlist_name)
        print("Successfully created new playlist: " + playlist_name)


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        print("Added video to " + playlist_name + " : " )

        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search.
        """
        video_list = self._video_library.get_all_videos()
        video_list.sort(key=lambda video: video.title)
        n = 0
        results = []
        for video in video_list:
            if search_term.lower() in video.title.lower():
                n += 1
                if n == 1:
                    print("Here are the results for " + search_term + ":")
                print(str(n) + ") " + video.title + " (" + video.video_id + ") [" + ' '.join(map(str, video.tags)) + "]")
                results.append(video.video_id)         

        if n < 1:
            print("No search results for " + search_term)
        else:
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            try:
                choice = int(input())
                if choice > 0 and choice <= n:
                    vid_id = results[choice-1]
                    self.play_video(vid_id)
            except:
                pass

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.
        Args:
            video_tag: The video tag to be used in search.
        """
        video_list = self._video_library.get_all_videos()
        video_list.sort(key=lambda video: video.title)
        n = 0
        results = []
        for video in video_list:
            if video_tag.lower() in ' '.join(map(str, video.tags)):
                n += 1
                if n == 1:
                    print("Here are the results for " + video_tag  + ":")
                print(str(n) + ") " + video.title + " (" + video.video_id + ") [" + ' '.join(map(str, video.tags)) + "]")
                results.append(video.video_id)         

        if n < 1:
            print("No search results for " + video_tag)
        else:
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            try:
                choice = int(input())
                if choice > 0 and choice <= n:  
                    #player = VideoPlayer()
                    vid_id = results[choice-1]
                    self.play_video(vid_id)
            except:
                pass

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
