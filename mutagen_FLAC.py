import os
import sys
from mutagen.flac import Picture, FLAC

input_file = sys.argv[1]
tagger = FLAC(input_file)

print("Mutagen FLAC tags")
print("1 : Add Tags")
print("2 : Remove Tags")
add_or_delete = input("Type number: ")

if add_or_delete == "2":
    tagger.delete()
    tagger.pprint()
    tagger.save()
    print("|")
    print("|--All Tags are Successfully Removed.")
    print("|")
    print("|--Remove all Covers/Albumarts")
    remove_covers = input("|--Type 'Yes' or 'No': ")
    if remove_covers.lower() == "yes":
        tagger.clear_pictures()
        tagger.pprint()
        tagger.save()
        print("|--Covers/Albumarts are Successfully Removed.")
    else:
        print("|--Covers/Albumarts still available.")

elif add_or_delete == "1":
    print("|")
    
    title = input("|--Title: ")
    tagger['title'] = title.split(', ')

    album = input("|--Album: ")
    tagger['album'] = album.split(', ')

    artist = input("|--Artist: ")
    tagger['artist'] = artist.split(', ')

    albumartist = input("|--Album Artist: ")
    tagger['albumartist'] = albumartist.split(', ')

    releasedate = input("|--Release date: ")
    tagger['date'] = releasedate.split(', ')

    composer = input("|--Composer: ")
    tagger['composer'] = composer.split(', ')

    lyricist = input("|--Lyricist: ")
    tagger['Lyricist'] = lyricist.split(', ')
    
    print("|")
    print("|-- 1 : Explicit")
    print("|-- 2 : Clean")
    print("|-- 3 : None")
    add_rating = input("|--Rating: ")
    if add_rating == "1":
        tagger['rating'] = ['Explicit']
    elif add_rating == "2":
        tagger['rating'] = ['Clean']
    elif add_rating == "3":
        tagger['rating'] = []
    elif add_rating == "":
        tagger['rating'] = []
    else:
        print("|--Enter a vaild number")
        add_rating = int(input("|--Rating: "))
        if add_rating == "1":
            tagger['rating'] = ['Explicit']
        elif add_rating == "2":
            tagger['rating'] = ['Clean']
        elif add_rating == "3":
            tagger['rating'] = []
        elif add_rating == "":
            tagger['rating'] = []
        else:
            print("|--Try again...")

    print("|")
    genre = input("|--Genre: ")
    tagger['genre'] = genre.split(', ')

    discnumber = input("|--Disc No.: ")
    tagger['discnumber'] = discnumber.split(', ')

    totaldiscs = input("|--Total Discs: ")
    tagger['totaldiscs'] = totaldiscs.split(', ')

    tracknumber = input("|--Track No.: ")
    tagger['tracknumber'] = tracknumber.split(', ')

    totaltracks = input("|--Total Tracks: ")
    tagger['totaltracks'] = totaltracks.split(', ')

    copyright = input("|--Copyright: ")
    tagger['copyright'] = copyright.split(', ')

    isrc = input("|--ISRC: ")
    tagger['isrc'] = isrc.split(', ')

    print("|")
    print("|--Add Lyrics")
    add_lyrices = input("|--Type 'Yes' or 'No': ")
    if add_lyrices.lower() == "yes":
        print("|--NOTE: To Add Lyrics Save Lyrics in a Text file and Add Text file's Path.")
        lyrics_txt = input("|--Enter Text file's Path: ")
        txt_folder = os.path.dirname(lyrics_txt)
        txt_folder = txt_folder.split('"')
        txt_file = lyrics_txt.split("\\")
        txt_file = txt_file[-1].split('"')
        os.chdir(txt_folder[-1])
        load_lyrics = open(txt_file[0], "r").read()
        tagger["lyrics"] = load_lyrics
    else:
        print("|--No Lyrics Added!")

    print("|")
    print("|--Add more Custom Tags")
    add_custom_tags = input("|--Type 'Yes' or 'No': ")
    if add_custom_tags.lower() == "yes":
        print("|--Add Custom Tags from a Text file")
        add_custom_tags_text = input("|--Type 'Yes' or 'No': ")
        if add_custom_tags_text.lower() == "yes":
            print("|")
            print("|--Text file's content format must be as below.")
            print("|-----------------------------------------")
            print("|-- Tag_Name_1: Tag_Value_1, Tag_Value_2")
            print("|-- Tag_Name_2: Tag_Value_1, Tag_Value_2")
            print("|-----------------------------------------")
            custom_tags_text = input("|--Enter Text file's Path: ")
            print("|")
            custags_txt_folder = os.path.dirname(custom_tags_text)
            custags_txt_folder = custags_txt_folder.split('"')
            custags_txt_file = custom_tags_text.split("\\")
            custags_txt_file = custags_txt_file[-1].split('"')
            os.chdir(custags_txt_folder[-1])
            with open(custags_txt_file[0]) as txt_tags:
                for custags in txt_tags:
                    custags = custags.strip()
                    print("|--" + custags)
                    tag_name_add = custags.split(': ')
                    tag_value_add = tag_name_add[-1].split(', ')
                    tagger[tag_name_add[0]] = [con for con in tag_value_add]
        else:
            print("|--Enter Tag Name first and Enter Tag Value second.")
            print("|--When finished, Type 'done' in Tag Name.")
            while True:
                enter_tag_name = input("|--Enter Tag Name: ")
                if enter_tag_name.lower() == "done":
                    break
                tag_value = input("|--" + enter_tag_name + ": ")
                tagger[enter_tag_name] = tag_value.split(', ')
    else:
        print("|--No Additional Tags Added.")

    print("|")
    print("|--Add a Cover/Albumart")
    add_cover = input("|--Type 'Yes' or 'No': ")
    if add_cover == "yes":
        albumart = input("|--Enter Cover's/Albumart's file Path: ")
        albumart_folder = os.path.dirname(albumart)
        albumart_folder = albumart_folder.split('"')
        albumart_file = albumart.split("\\")
        albumart_file = albumart_file[-1].split('"')
        os.chdir(albumart_folder[-1])
        image = Picture()
        image.type = 3
        if albumart.endswith('png'):
            image.mime = 'image/png'
        elif albumart.endswith('png"'):
            image.mime = 'image/png'
        elif albumart.endswith('jpg') or albumart.endswith('jpeg'):
            image.mime = 'image/jpeg'
        elif albumart.endswith('jpg"') or albumart.endswith('jpeg"'):
            image.mime = 'image/jpeg'
        with open(albumart_file[0], 'rb') as f:
            image.data = f.read()
        tagger.add_picture(image)
    else:
        print("|--No Cover/Albumart Added.")
    tagger.pprint()
    tagger.save()
    print("|")
    print("|--Successfully Tagged.")
else:
    print("|")
    print("|--Enter a valid number and Try again....")