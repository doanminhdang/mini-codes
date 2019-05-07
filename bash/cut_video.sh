if [ "$#" -ne 4 ]; then
    echo "This command needs 4 parameters: input_video_name start_time_to_cut end_time_to_cut output_video_name"
else
    vid_length=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $1)
    echo $vid_length
    ./trim_video.sh $1 0:0 $2 temp_video1.mp4
    ./trim_video.sh $1 $3 $vid_length temp_video2.mp4
    echo "file 'temp_video1.mp4'" > joinlist.txt
    echo "file 'temp_video2.mp4'" >> joinlist.txt
    ./join_videos.sh joinlist.txt $4
    echo "remove temporary videos"
    rm temp_video1.mp4
    rm temp_video2.mp4
fi
