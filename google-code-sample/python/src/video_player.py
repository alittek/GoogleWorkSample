"""A video player class."""

from os import truncate
from .video_library import VideoLibrary
from .video_playlist import Playlist

import random

#curr_playing = ""
#paused = False

class VideoPlayer:
    """A class used to represent a Video Player."""
    playlists = []
    curr_playing = ""
    paused = False

    def __init__(self):
        self._video_library = VideoLibrary()

        VideoPlayer.curr_playing = ""
        VideoPlayer.paused = False

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
        VideoPlayer.paused = False
        video = self._video_library.get_video(video_id)
        curr_video = self._video_library.get_video(VideoPlayer.curr_playing)

        if not video:
            print("Cannot play video: Video does not exist")
        else:
            if curr_video:
                print("Stopping video: " + curr_video.title)
            VideoPlayer.curr_playing = video.video_id
            print("Playing video: " + video.title)

    def stop_video(self):
        """Stops the current video."""
        video = self._video_library.get_video(VideoPlayer.curr_playing)
        if not video:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: " + video.title)
            VideoPlayer.curr_playing = ""
            VideoPlayer.paused = False  

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_list = self._video_library.get_all_videos()
        rand_video = random.choice(video_list)
        video = rand_video.video_id
        self.play_video(video)

    def pause_video(self):
        """Pauses the current video."""
        video = self._video_library.get_video(VideoPlayer.curr_playing)
        if VideoPlayer.paused == True:
            print("Video already paused: " + video.title)
        elif VideoPlayer.curr_playing != "":
            print("Pausing video: " + video.title)
            VideoPlayer.paused = True
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        video = self._video_library.get_video(VideoPlayer.curr_playing)
        if VideoPlayer.paused == False and not video:
            print("Cannot continue video: No video is currently playing")
        elif VideoPlayer.paused == False and video:
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video: " + video.title)
            VideoPlayer.paused = False

    def show_playing(self):
        """Displays video currently playing."""
        video = self._video_library.get_video(VideoPlayer.curr_playing)

        video_list = self._video_library.get_all_videos()
        video_title = VideoPlayer.curr_playing                

        if not video:
            print("No video is currently playing")
        else:
            if VideoPlayer.paused == False:
                print("Currently playing: " + video.title + " (" + video.video_id + ") [" + ' '.join(map(str, video.tags)) + "]")
            else:
                print("Currently playing: " + video.title + " (" + video.video_id + ") [" + ' '.join(map(str, video.tags)) + "]" + " - PAUSED")

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
