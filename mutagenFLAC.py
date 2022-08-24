import os
import sys
from mutagen.flac import Picture, FLAC

def main():

    '''
    Tagging script for FLAC files using the python module 'Mutagen'.
    '''

    inputFLAC = sys.argv[1]
    taggerFLAC = FLAC(os.path.abspath(inputFLAC))
    tagMode = input(
        f'\nmutagenFLAC\
        \n|\
        \n|-- 1 : Add tags\
        \n|-- 2 : Remove tags\
        \n|\
        \n|--tagMode: [1/2] '
    )

    if tagMode == '2':
        taggerFLAC.delete()
        print(f'\nAll tags are successfully removed, but Covers/Albumarts are still remain.')
        removeCovers = input(f'Do you want to remove all Covers/Albumarts? [y/n] ')
        if (removeCovers.lower() == "y") or (removeCovers.lower() == "yes"):
            taggerFLAC.clear_pictures()
            print(f'Covers/Albumarts are successfully removed.')
        elif (removeCovers.lower() == "") or (removeCovers.lower() == "n") or (removeCovers.lower() == "no"):
            print(f'Covers/Albumarts are still available.')

    elif tagMode == '1':
        print('\n' + os.path.basename(os.path.abspath(inputFLAC)), '\n|')
        Title = input(f'|--Title: ')
        Album = input(f'|--Album: ')
        Artist = input(f'|--Artist: ')
        albumArtist = input(f'|--Album Artist: ')
        releaseDate = input(f'|--Release Date: ')
        Composer = input(f'|--Composer: ')
        Lyricist = input(f'|--Lyricist: ')
        Genre = input(f'|--Genre: ')
        discNumber = input(f'|--Disc No.: ')
        discTotal = input(f'|--Disc Total: ')
        trackNumber = input(f'|--Track No.: ')
        trackTotal = input(f'|--Track Total: ')
        Copyright = input(f'|--Copyright: ')
        isrc = input(f'|--ISRC: ')
        
        taggerFLAC['title'] = Title.split(', ')
        taggerFLAC['album'] = Album.split(', ')
        taggerFLAC['artist'] = Artist.split(', ')
        taggerFLAC['albumartist'] = albumArtist.split(', ')    
        taggerFLAC['date'] = releaseDate.split(', ')   
        taggerFLAC['composer'] = Composer.split(', ')
        taggerFLAC['Lyricist'] = Lyricist.split(', ')
        taggerFLAC['genre'] = Genre.split(', ')
        taggerFLAC['discnumber'] = discNumber.split(', ')
        taggerFLAC['totaldiscs'] = discTotal.split(', ')
        taggerFLAC['tracknumber'] = trackNumber.split(', ')
        taggerFLAC['totaltracks'] = trackTotal.split(', ')
        taggerFLAC['copyright'] = Copyright.split(', ')
        taggerFLAC['isrc'] = isrc.split(', ')
        
        Rating = input(
            f'|\
            \n|-- 1 : None\
            \n|-- 2 : Clean\
            \n|-- 3 : Explicit\
            \n|\
            \n|--Rating: [1/2/3] '
        )
        if Rating == '3':
            taggerFLAC['rating'] = ['Explicit']
        elif Rating == '2':
            taggerFLAC['rating'] = ['Clean']
        elif Rating == '1':
            taggerFLAC['rating'] = []
        else:
            print("|--Invalid input is detected. So, Ignoring the Rating tag.")

        addLyrics = input(f"|\n|--Do you want to add 'Lyrics'? [y/n] ")
        if (addLyrics.lower() == 'y') or (addLyrics.lower() == 'yes'):
            lrcDoc = input(f"|--Save lyrics in a text document and enter it's path\n|--Text document's path: ")
            if lrcDoc.startswith('"') and lrcDoc.endswith('"'):
                lrcDoc = lrcDoc[1:-1]
            Lyrics = open(lrcDoc, 'r').read()
            taggerFLAC["lyrics"] = Lyrics
        else:
            print("|--No 'Lyrics' added!")

        addCustomTags = input(f"|\n|--Do you want to add more 'Custom Tags'? [y/n] ")
        if (addCustomTags.lower() == 'y') or (addCustomTags.lower() == 'yes'):
            addTextDoc = input(f'|--Do you want to add tags from a text document? [y/n] ')
            if (addTextDoc.lower() == '') or (addTextDoc.lower() == 'n') or (addTextDoc.lower() == 'no'):
                print(f'|\n|--Type [tag name] first and [tag value] second')
                print(f"|--When finished, Type 'done' in [tag name]\n|")
                while True:
                    tagName = input(f'|--Tag name: ')
                    if tagName.lower() == "done":
                        break
                    tagValue = input(f'|--{tagName}: ')
                    taggerFLAC[tagName] = tagValue.split(', ')
            elif (addTextDoc.lower() == 'y') or (addTextDoc.lower() == 'yes'):
                textDoc = input(f"|--Text document's path: ")
                if textDoc.startswith('"') and textDoc.endswith('"'):
                    textDoc = textDoc[1:-1]
                print(f'|')
                with open(textDoc) as textTags:
                    for customTags in textTags:
                        customTags = customTags.strip()
                        print(f'|--{customTags}')
                        tagName = customTags.split(': ')
                        tagValue = tagName[1].split(', ')
                        taggerFLAC[tagName[0]] = [value for value in tagValue]
        else:
            print(f"|--No 'Custom Tags' added!")

        addCover = input(f"|\n|--Do you want to add a 'Cover'? [y/n] ")
        if (addCover.lower() == 'y') or (addCover.lower() == 'yes'):
            albumart = input(f"|--Cover's file path: ")
            if albumart.startswith('"') and albumart.endswith('"'):
                albumart = albumart[1:-1]
            image = Picture()
            image.type = 3
            if os.path.splitext(albumart)[1] == '.png':
                image.mime = 'image/png'
            elif (os.path.splitext(albumart)[1] == '.jpg') or (os.path.splitext(albumart)[1] == '.jpeg'):
                image.mime = 'image/jpeg'
            with open(albumart, 'rb') as coverFile:
                image.data = coverFile.read()
            taggerFLAC.add_picture(image)
        else:
            print(f"|--No 'Cover' added!")
        taggerFLAC.pprint()
        taggerFLAC.save()
        print(f'|\n|--Successfully Tagged')
    else:
        print(f'|--Invalid response, Try again....')

if __name__ == '__main__':
    main()
